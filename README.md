# NEXUS-ARCHÊ

**Système de lecture résonante des structures invariantes**

NEXUS-ARCHÊ est un outil d'analyse structurelle à double registre, conçu pour identifier les patterns qui organisent une situation en les faisant résonner simultanément dans deux langages : les mathématiques des systèmes et les universaux comportementaux humains documentés par Donald Brown.

---

## Ce que c'est

16 cartes structurelles, chacune portant :
- Une structure mathématique précise (attracteur, réseau, bifurcation...) avec sa branche mathématique explicite
- Un universel comportemental documenté (Brown, *The Universal People*, 1991)
- Un glyphe STÈLE primaire pour la compression symbolique
- Une Question IRIS pour activer la lecture
- Des critères de distinction avec les cartes proches (À ne pas confondre avec)

Le mécanisme est **résonant, non narratif** : les cartes décrivent simultanément les structures actives d'une situation, sans raconter une histoire.

---

## Démarrage rapide

### Prompt d'activation (pour LLM)

```
Activez NEXUS-ARCHÊ. Situation : [décrire la situation en 3 à 5 phrases].
Mode demandé : [1 / 2 / 3]. Modalité : [aléatoire / délibératif].
```

### Exemple minimal (Mode 1, délibératif)

```
Activez NEXUS-ARCHÊ. Situation : Un projet a démarré sans plan directeur.
Des rôles émergent naturellement. Personne ne coordonne vraiment mais ça
fonctionne. Mode 1. Modalité délibérative.

→ Carte : ÉMERGENCE · ⊙ SOURCE
→ Ancrage : les rôles se sont constitués spontanément sans désignation.
→ Anti-résonance : un initiateur a posé le cadre de départ — l'émergence
   est partielle.
→ Chaîne STÈLE : ⊙ → SOURCE
→ Statut : Descriptif
```

### Questions IRIS directes (sans tirage formel)

Si la situation est déjà claire, poser directement la Question IRIS de la carte suspectée :

- *Quelle structure tient tout en place ici — et est-ce qu'elle tient encore ?* → HIÉRARCHIE
- *Qu'est-ce qui est en train d'apparaître sans qu'on l'ait décidé ?* → ÉMERGENCE
- *Quel cycle se rejoue — et à quel point du cycle es-tu ?* → PÉRIODICITÉ

---

## Positionnement dans l'écosystème IRIS

| Skill | Ce qu'il fait |
|---|---|
| Fractales du Destin | Lecture oraculaire symbolique |
| Miroir-Trans-Échelle | Pont entre FdD et registre analytique |
| **NEXUS-ARCHÊ** | Identification des structures invariantes — registre propre, autonome |
| STÈLE | Compression glyphique des sorties |
| OSINT-Intel | Analyse stratégique — NEXUS-ARCHÊ identifie la structure avant l'analyse |
| Superforecasting | Prédiction — NEXUS-ARCHÊ nomme le type de situation avant de projeter |

---

## Dépendances

### Dépendances internes à ce dépôt (autonomes)

| Fichier | Rôle |
|---|---|
| `references/stele_rules.md` | Règles syntaxiques STÈLE minimales — autonomes, utilisables sans le skill STÈLE |
| `references/cards.md` | Les 16 fiches complètes |
| `references/protocol.md` | Protocole de tirage complet |
| `references/examples.md` | Exemples annotés |

### Dépendances externes (écosystème IRIS)

| Skill | Nature de la dépendance | Requis ? |
|---|---|---|
| **STÈLE** | Grammaire STÈLE complète (modales avancées, règles de composition étendues) | Non — `stele_rules.md` couvre l'usage de base |
| Fractales du Destin | Complémentarité oraculaire | Non — optionnel |
| OSINT-Intel | Analyse prédictive post-structurelle | Non — optionnel |

> NEXUS-ARCHÊ est utilisable de façon entièrement autonome à partir de ce dépôt seul.

---

## Contenu du dépôt

```
SKILL.md                      — Fichier principal : architecture, cartes, protocole résumé
README.md                     — Ce fichier
references/
  cards.md                    — Les 16 fiches complètes (+ branche mathématique + distinctions)
  protocol.md                 — Protocole de tirage complet (modes 1-4, configurations pathologiques)
  stele_rules.md              — Règles syntaxiques STÈLE autonomes pour NEXUS-ARCHÊ
  examples.md                 — Tirages annotés : Mode 1, Mode 2, Mode 3 + tirage rejeté
```

---

## Fondements

- **Mathématiques** : systèmes dynamiques, topologie, théorie des graphes, probabilité, algèbre des transformations, physique des oscillateurs couplés — voir tableau détaillé dans `SKILL.md`
- **Anthropologie** : Donald Brown (*The Universal People*, 1991) — universaux comportementaux documentés
- **Symbolique** : Alphabet STÈLE (écosystème IRIS) — règles autonomes dans `references/stele_rules.md`

---

## Statut et roadmap

**Version actuelle** : v0.2

### Changements v0.1 → v0.2
- Branche mathématique ajoutée à chaque carte
- Sections "À ne pas confondre avec" sur toutes les paires proches
- Modalités de tirage explicites (aléatoire / délibératif / activation LLM)
- Configurations pathologiques du Mode 3 documentées
- Mode 4 (Tirage de résolution) ajouté
- `references/stele_rules.md` — règles STÈLE autonomes, glyphes ▲ ⟶ ✶ confirmés définitifs
- `references/examples.md` — 3 tirages annotés complets + 1 tirage rejeté

### Roadmap v0.3

- Tests sur 10 situations réelles documentées
- Calibration des distinctions inter-cartes sur corpus de lectures
- CHANGELOG.md
- Éventuellement : interface de tirage guidé (prompt structuré pour LLM)

---

*Projet IRIS — Dépôt public, usage libre.*
