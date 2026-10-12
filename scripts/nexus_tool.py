#!/usr/bin/env python3
"""NEXUS-ARCHÊ — outil de tirage, de validation et de contrôle.

Lit ses données dans les références (source unique) :
  references/notation.md    §1  table canonique des 16 cartes
  references/antagonismes.md §3  table des incompatibilités

Commandes
  draw [-n 1..3] [--seed TEXTE] [--exclude "A,B"]
                                  tirage sans remise, avec ligne de journal ;
                                  --exclude retire les cartes déjà sorties (retirage)
  validate "SIGNATURE"            valide une signature (noms, ids ou glyphes)
  stats                           fréquences des configurations en tirage uniforme
  lint                            cohérence croisée des références
"""
import argparse
import datetime as dt
import hashlib
import itertools
import random
import re
import secrets
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "references"


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def key(s):
    return re.sub(r"[^A-Z0-9]", "", strip_accents(s).upper())


def load_cards():
    text = (REF / "notation.md").read_text(encoding="utf-8")
    sect = text.split("## 1.")[1].split("\n## ")[0]
    cards = []
    for line in sect.splitlines():
        m = re.match(r"\|\s*(\d{2})\s*\|\s*([^|]+?)\s*\|\s*(\S+)\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            cards.append({"id": m[1], "name": m[2], "glyph": m[3], "code": m[4]})
    if len(cards) != 16:
        sys.exit(f"notation.md §1 : 16 cartes attendues, {len(cards)} lues")
    return cards


def build_index(cards):
    idx = {}
    for c in cards:
        for alias in (c["name"], c["id"], str(int(c["id"])), c["glyph"]):
            idx[key(alias) or alias] = c["name"]
        if c["name"].startswith("TRACE"):
            idx[key("TRACE")] = c["name"]
    return idx


def resolve(token, idx):
    t = token.strip()
    return idx.get(key(t) or t) or idx.get(t)


def load_incompat(cards):
    text = (REF / "antagonismes.md").read_text(encoding="utf-8")
    sect = text.split("## 3.")[1].split("\n## ")[0]
    idx = build_index(cards)
    pairs = []
    for line in sect.splitlines():
        m = re.match(r"\|\s*([^|↮]+?)\s*↮\s*([^|]+?)\s*\|", line)
        if m:
            a, b = resolve(m[1], idx), resolve(m[2], idx)
            if not a or not b:
                sys.exit(f"antagonismes.md : carte inconnue dans « {line[:60]} »")
            pairs.append(frozenset((a, b)))
    return pairs


def load_qualifiers():
    """Qualificatifs = table de R13 (protocol.md) : | `{nom}` | `code` | marqueur |"""
    text = (REF / "protocol.md").read_text(encoding="utf-8")
    sect = text.split("## R13")[1] if "## R13" in text else ""
    out = {}
    for m in re.finditer(r"^\| `\{([^}]+)\}` \| `([^`]+)` \|", sect, re.M):
        out[m[1]] = m[2]
    return out


def split_quals(token, quals, errors):
    """'POLARITÉ {multi-échelle}' -> ('POLARITÉ', ['multi-échelle'])"""
    m = re.match(r"^(.*?)((?: \{[^{}]+\})*)$", token)
    head, tail = m[1], m[2]
    if "{" in head or "}" in head:
        errors.append(f"qualificatif mal formé dans « {token} » (une espace avant chaque « {{ », notation.md §3 règle 6)")
        return head, []
    names = re.findall(r"\{([^{}]+)\}", tail)
    by_code = {v: k for k, v in quals.items()}
    out = []
    for q in names:
        qn = q if q in quals else by_code.get(q)
        if not qn:
            errors.append(f"« {{{q}}} » n'est pas un qualificatif (R13 : {', '.join(quals)})")
            continue
        out.append(qn)
    if len(out) > 2:
        errors.append(f"plus de deux qualificatifs sur « {head} » (R13 règle 3)")
    if len(set(out)) != len(out):
        errors.append(f"qualificatif répété sur « {head} »")
    return head.strip(), out


REQUIRED_REFS = ["protocol", "cards", "notation", "antagonismes", "calibration",
                 "examples", "test_log", "prompt_guide"]


def load_neighbors(cards):
    """Voisines documentées = puces *NOM* de la rubrique « À ne pas confondre avec »."""
    idx = build_index(cards)
    text = (REF / "cards.md").read_text(encoding="utf-8")
    out = {}
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        head = block.split("\n", 1)[0]
        name = resolve(head, idx)
        if not name:
            continue
        part = block.split("**À ne pas confondre avec**")[1].split("**Question d'exploration**")[0]
        out[name] = {resolve(x, idx) for x in re.findall(r"^- \*([^*]+)\*", part, re.M)}
    return out


def check_r3(path, neigh, cards, bad):
    """Chaque carte de niveau final Fort doit avoir, dans sa section, une ligne
    « R3 · CARTE : V1 → (…) ; V2 + (…) » couvrant toutes ses voisines, sans « ? »."""
    idx = build_index(cards)
    text = path.read_text(encoding="utf-8")
    checked = 0
    for sec in re.split(r"^#{2,3} ", text, flags=re.M)[1:]:
        title = sec.split("\n", 1)[0][:40]
        r3 = {}
        for m in re.finditer(r"R3 · ([^:]+?) : (.+)$", sec, re.M):
            card = resolve(m[1], idx)
            if not card:
                bad(f"{path.name} « {title} » : R3 sur une carte inconnue « {m[1]} »")
                continue
            items = {}
            for it in re.split(r" ; (?=[A-ZÀ-Ý·]+(?: [A-ZÀ-Ý·]+)* [→+?←] \()", m[2]):
                mm = re.match(r"\s*([^→+?←(]+?)\s*([→+?←])\s*\((.+)\)\s*\.?$", it)
                if not mm or not mm[3].strip():
                    bad(f"{path.name} « {title} » : R3 {card}, élément mal formé « {it.strip()[:40]} »")
                    continue
                items[resolve(mm[1], idx)] = mm[2]
            r3[card] = items
        for row in re.finditer(r"^\| ([^|]+?) \|.*\| \**(Fort)\** \|\s*$", sec, re.M):
            first = re.split(r" \(| —", row[1])[0].strip()
            card = resolve(first, idx)
            if not card:
                continue
            checked += 1
            if card not in r3:
                bad(f"{path.name} « {title} » : {card} Fort sans ligne R3")
                continue
            missing = neigh[card] - set(r3[card])
            if missing:
                bad(f"{path.name} « {title} » : R3 {card} omet {', '.join(sorted(missing))}")
            extra = set(r3[card]) - neigh[card]
            if extra:
                bad(f"{path.name} « {title} » : R3 {card} cite des non-voisines {', '.join(sorted(x or '?' for x in extra))}")
            for v in ("?", "←"):
                if v in r3[card].values():
                    bad(f"{path.name} « {title} » : {card} Fort alors qu'une voisine est « {v} »")
    return checked


def cmd_draw(args, cards):
    n = args.n
    if not 1 <= n <= 3:
        sys.exit("n doit être 1, 2 ou 3")
    pool = list(cards)
    excluded = []
    if args.exclude:
        idx = build_index(cards)
        for tok in args.exclude.split(","):
            r = resolve(tok, idx)
            if not r:
                sys.exit(f"--exclude : « {tok.strip()} » n'est pas une carte")
            excluded.append(r)
        pool = [c for c in pool if c["name"] not in excluded]
    if n > len(pool):
        sys.exit("plus assez de cartes à tirer")
    if args.seed:
        seed = hashlib.sha256(args.seed.encode("utf-8")).hexdigest()
        rng = random.Random(int(seed, 16))
        picks = rng.sample(pool, n)
        source = f"seed=sha256:{seed[:12]}"
    else:
        picks = []
        for _ in range(n):  # sans remise
            picks.append(pool.pop(secrets.randbelow(len(pool))))
        source = "secrets"
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    names = [c["name"] for c in picks]
    excl = f" · exclues : {', '.join(excluded)}" if excluded else ""
    print(f"TIRAGE {now} · {source} · sans remise{excl} · " + " | ".join(names))
    if n == 3:
        print("Note : l'ordre de sortie ne vaut pas position ; les positions se fixent après ancrage (R1, R7).")


def cmd_validate(sig, cards):
    idx = build_index(cards)
    glyph = {c["name"]: c["glyph"] for c in cards}
    s = sig.strip()
    errors = []
    if s in ("∅", "0", "NUL", "nul"):
        print("VALIDE · résultat nul · ∅")
        return 0
    canon_spacing = re.sub(r"\s*([+/⇒])\s*", r" \1 ", s).strip()
    if canon_spacing != s:
        print(f"INVALIDE · espacement non canonique (notation.md §3, règle 1) ; forme attendue : « {canon_spacing} »")
        return 1
    res = None
    if "⇒" in s:
        base, _, res = s.partition("⇒")
        if "⇒" in res:
            errors.append("un seul ⇒ autorisé")
        res = res.strip()
        s = base.strip()
    if "/" in s and "+" in s:
        errors.append("mélange de « / » et « + » : une signature a une seule syntaxe")
    if "/" in s:
        parts, mode = [p.strip() for p in s.split("/")], 3
        if len(parts) != 3:
            errors.append(f"Mode 3 : 3 positions attendues, {len(parts)} trouvées")
    elif "+" in s:
        parts, mode = [p.strip() for p in s.split("+")], 2
        if len(parts) != 2:
            errors.append(f"Mode 2 : 2 cartes attendues, {len(parts)} trouvées")
    else:
        parts, mode = [s], 1
    if res is not None and mode == 1:
        errors.append("⇒ s'applique à une signature de Mode 2 ou 3")
    quals = load_qualifiers()
    names, qlists = [], []
    for p in parts + ([res] if res is not None else []):
        head, ql = split_quals(p, quals, errors)
        r = resolve(head, idx)
        if not r:
            errors.append(f"« {head} » n'est pas une carte (noms : notation.md §1)")
        names.append(r)
        qlists.append(ql)
    if not errors:
        base_names = names[: len(parts)]
        if len(set(base_names)) != len(base_names):
            if mode == 3 and base_names[0] == base_names[2] and base_names[0] != base_names[1]:
                print("NOTE · configuration Scission (R8) : la lecture doit nommer deux objets distincts")
            else:
                errors.append("carte répétée")
        if res is not None and names[-1] in base_names:
            errors.append("la carte de tenue doit différer des cartes tenues")
    if errors:
        for e in errors:
            print("INVALIDE ·", e)
        return 1
    sep = {1: "", 2: " + ", 3: " / "}[mode]
    cn = lambda i: names[i] + "".join(f" {{{q}}}" for q in qlists[i])
    gn = lambda i: glyph[names[i]] + "".join(f"{{{quals[q]}}}" for q in qlists[i])
    canon = sep.join(cn(i) for i in range(len(parts)))
    gl = sep.join(gn(i) for i in range(len(parts)))
    if res is not None:
        canon += " ⇒ " + cn(len(names) - 1)
        gl += " ⇒ " + gn(len(names) - 1)
    label = f"Mode {4 if res is not None else mode}"
    print(f"VALIDE · {label}\n  {canon}\n  {gl}")
    if any(qlists):
        print("NOTE · chaque qualificatif doit avoir sa ligne « Q · CARTE {qualificatif} : fait ; contre-observation » (R13)")
    inc = {tuple(sorted(p)) for p in load_incompat(cards)}
    if mode == 3:
        t_, m_ = names[0], names[2]
        if tuple(sorted((t_, m_))) in inc:
            print(f"SIGNAL · Lacune contradictoire possible ({t_} ↮ {m_}) : vérifier le même objet (R8)")
    if mode == 2:
        a_, b_ = names[0], names[1]
        if tuple(sorted((a_, b_))) in inc:
            print(f"SIGNAL · paire incompatible ({a_} ↮ {b_}) : seule la relation « indépendance » est admise, objets distincts nommés ; sinon un ancrage est erroné (R6)")
    return 0


def cmd_stats(cards):
    names = [c["name"] for c in cards]
    inc = set(load_incompat(cards))
    ant = lambda a, b: frozenset((a, b)) in inc
    perms = list(itertools.permutations(names, 3))
    combos = list(itertools.combinations(names, 3))
    c3 = sum(1 for t, b, m in perms if ant(t, m))
    c2p = [s for s in combos if sum(ant(x, y) for x, y in itertools.combinations(s, 2)) >= 2]
    print(f"Incompatibilités lues : {len(inc)}")
    for p in sorted(tuple(sorted(p)) for p in inc):
        print("  ", " ↮ ".join(p))
    print(f"Configuration 3 (tient ↮ manque) : {c3} / {len(perms)} = {100*c3/len(perms):.2f} %")
    print(f"Constellations avec ≥ 2 paires incompatibles : {len(c2p)} / {len(combos)}")
    for s in c2p:
        print("  ", " + ".join(s))


def cmd_lint(cards):
    ok = True
    def bad(msg):
        nonlocal ok
        ok = False
        print("ERREUR ·", msg)
    cards_md = (REF / "cards.md").read_text(encoding="utf-8")
    heads = re.findall(r"^## (.+)$", cards_md, re.M)
    heads = [h.strip() for h in heads if h.strip() != "Références"]
    canon = [c["name"] for c in cards]
    hk = [key(h) for h in heads]
    blocks = {key(b.split("\n", 1)[0]): b for b in re.split(r"^## ", cards_md, flags=re.M)[1:]}
    for c in cards:
        block = blocks.get(key(c["name"]))
        if block is None:
            bad(f"cards.md : pas de fiche pour {c['name']}")
        else:
            for field in ("**Définition**", "**Structure mathématique**", "**Marqueurs observables**",
                          "**Registre anthropologique**", "**À ne pas confondre avec**",
                          "**Question d'exploration**", "**Signature**"):
                if field not in block:
                    bad(f"cards.md {c['name']} : champ {field} manquant")
            if f"`{c['glyph']}` {c['code']}" not in block:
                bad(f"cards.md {c['name']} : signature ≠ notation.md ({c['glyph']} {c['code']})")
    if len(heads) != 16:
        bad(f"cards.md : 16 fiches attendues, {len(heads)} trouvées")
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    desc = re.search(r"description: >\n(.*?)\nmetadata:", skill, re.S)
    if desc:
        d = " ".join(l.strip() for l in desc[1].splitlines())
        if len(d) > 1024:
            bad(f"SKILL.md : description de {len(d)} caractères (> 1024)")
        else:
            print(f"OK · description SKILL.md : {len(d)} caractères")
    for c in cards:
        if f"| {c['name']} | {c['glyph']} |" not in skill:
            bad(f"SKILL.md : ligne de table pour {c['name']} absente ou glyphe divergent")
    for f in sorted(REF.glob("*.md")):
        t = f.read_text(encoding="utf-8")
        for bad_term in ("pathologique", "Performatif", "stele_rules.md"):
            for m in re.finditer(bad_term, t):
                ctx = t[max(0, m.start()-80):m.end()+20]
                if "v0.3.1" not in ctx and "supprim" not in ctx and "remplace" not in ctx.lower() and "Remplace" not in ctx:
                    bad(f"{f.name} : terme retiré « {bad_term} » hors mention historique")
    # --- fichiers requis et versions (N2) ---
    required = ["SKILL.md", "README.md", "CHANGELOG.md", "scripts/nexus_tool.py"] + [
        f"references/{f}.md" for f in REQUIRED_REFS]
    for f in required:
        if not (ROOT / f).exists():
            bad(f"fichier requis absent : {f}")
    m = re.search(r"^\s*version:\s*([\d.]+)", skill, re.M)
    version = m[1] if m else None
    if not version:
        bad("SKILL.md : metadata.version absente")
    for f in REQUIRED_REFS:
        pth = REF / f"{f}.md"
        if pth.exists():
            mv = re.search(r"^> Version : ([\d.]+)", pth.read_text(encoding="utf-8"), re.M)
            if not mv or mv[1] != version:
                bad(f"references/{f}.md : version {mv[1] if mv else 'absente'} ≠ SKILL.md {version}")
    ch = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    mc = re.search(r"^## v([\d.]+)", ch, re.M)
    if not mc or mc[1] != version:
        bad(f"CHANGELOG.md : première entrée v{mc[1] if mc else '?'} ≠ {version}")
    if f"v{version}" not in (ROOT / "README.md").read_text(encoding="utf-8"):
        bad(f"README.md : v{version} non mentionnée")
    print(f"OK · version {version} cohérente" if ok else "")
    # --- voisines documentées : symétrie ---
    neigh = load_neighbors(cards)
    for a, ns in neigh.items():
        for b in ns:
            if a not in neigh.get(b, set()):
                bad(f"cards.md : {a} cite {b} comme voisine, mais {b} ne cite pas {a}")
    npairs = {frozenset((a, b)) for a, ns in neigh.items() for b in ns}
    print(f"OK · graphe des voisines : {len(npairs)} paires, symétrique" if ok else "")
    # --- R3 appliqué dans le corpus ---
    for fname in ("examples.md", "test_log.md"):
        n_checked = check_r3(REF / fname, neigh, cards, bad)
        print(f"OK · {fname} : {n_checked} cartes Fort, lignes R3 complètes" if ok else "")
    # --- qualificatifs : chaque {q} d'une signature du corpus a sa ligne Q ---
    quals = load_qualifiers()
    if len(quals) != 4:
        bad(f"protocol.md R13 : 4 qualificatifs attendus, {len(quals)} lus")
    idxq = build_index(cards)
    nq = 0
    for fname in ("examples.md", "test_log.md"):
        text = (REF / fname).read_text(encoding="utf-8")
        for sec in re.split(r"^#{2,3} ", text, flags=re.M)[1:]:
            title = sec.split("\n", 1)[0][:40]
            for sig in re.findall(r"\*\*Signature\*\* :? ?`([^`]+)`", sec):
                for card, qs in re.findall(r"([A-ZÀ-Ý·]+)((?: \{[^{}]+\})+)", sig):
                    for q in re.findall(r"\{([^{}]+)\}", qs):
                        nq += 1
                        c = resolve(card, idxq)
                        if q not in quals:
                            bad(f"{fname} « {title} » : qualificatif inconnu {{{q}}}")
                        pat = rf"^Q · {re.escape(card)} \{{{re.escape(q)}\}} : .+ ; contre-observation : .+\((marginale|aucune trouvée)\)"
                        if not re.search(pat, sec, re.M):
                            bad(f"{fname} « {title} » : {c} {{{q}}} sans ligne Q ancrée (fait ; contre-observation (portée))")
    print(f"OK · {nq} qualificatif(s) dans les signatures du corpus, tous ancrés" if ok else "")
    # --- citations ↔ bibliographie ---
    refs_part = cards_md.split("## Références")[1]
    body = cards_md.split("## Références")[0]
    for name, year in set(re.findall(r"\b([A-Z][a-zà-ÿ]+)(?:, [A-Z][a-zà-ÿ]+)*(?: & [A-Z][a-zà-ÿ]+| et al\.)?,? (1[6-9]\d\d|20\d\d)\b", body)):
        if not re.search(rf"^- {name}\b.*\({year}\)", refs_part, re.M):
            bad(f"cards.md : citation « {name} {year} » absente des Références")
    print("LINT OK" if ok else "LINT : erreurs ci-dessus")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("draw"); d.add_argument("-n", type=int, default=1); d.add_argument("--seed"); d.add_argument("--exclude")
    v = sub.add_parser("validate"); v.add_argument("signature")
    sub.add_parser("stats"); sub.add_parser("lint")
    a = ap.parse_args()
    cards = load_cards()
    if a.cmd == "draw":
        cmd_draw(a, cards)
    elif a.cmd == "validate":
        sys.exit(cmd_validate(a.signature, cards))
    elif a.cmd == "stats":
        cmd_stats(cards)
    else:
        sys.exit(cmd_lint(cards))


if __name__ == "__main__":
    main()
