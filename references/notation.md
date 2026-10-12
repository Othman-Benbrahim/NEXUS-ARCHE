# NEXUS-ARCHÊ — Notation des signatures

> Version : 0.4.2

> Remplace `stele_rules.md` (v0.3.1). Source de vérité des **identifiants**, **glyphes** et de la
> **syntaxe des signatures**. Le script `scripts/nexus_tool.py` lit la table du §1.

---

## 0. Ce qu'est une signature — et ce qu'elle n'est pas

Une signature NEXUS-ARCHÊ est une **notation positionnelle propre au skill** : elle dit quelles
cartes ont été retenues et à quelle position. Elle n'est **pas** une phrase STÈLE.

Raison : dans l'alphabet STÈLE, seules 8 primitives sont des substances. Huit glyphes de carte y
sont des opératives (strate II) ou des modales (strate III) ; les placer en tête de chaîne est
illégal en STÈLE (voir §5). La v0.3.1 revendiquait une « validité syntaxique STÈLE » qu'elle ne
respectait pas. La v0.4 sépare les deux : NEXUS-ARCHÊ produit une signature ; qui veut une phrase
STÈLE confie la signature au skill STÈLE.

**L'identifiant canonique est le nom de carte.** Le glyphe est une projection d'affichage.
La validation porte sur les noms, jamais sur les glyphes.

---

## 1. Table canonique

| Id | Nom canonique | Glyphe | Mot-code STÈLE | Strate STÈLE du glyphe |
|---|---|---|---|---|
| 01 | SEUIL | ⊥ | LIMITE | I — substance |
| 02 | RÉCIPROCITÉ | ⊗ | LIER | II — opérative |
| 03 | PÉRIODICITÉ | ↻ | CYCLE | III — modale |
| 04 | RÉCURSIVITÉ | ↺ | RÉFLEXIVITÉ | III — modale |
| 05 | ÉMERGENCE | ⊙ | SOURCE | I — substance |
| 06 | HIÉRARCHIE | ✦ | AXE | I — substance |
| 07 | RÉSEAU | ⊛ | NOEUD | I — substance |
| 08 | POLARITÉ | ⥀ | INVERSER | II — opérative |
| 09 | INCERTITUDE | Ø | VIDE | I — substance |
| 10 | CONTRAINTE | ⊘ | NÉGATION | III — modale |
| 11 | PROPORTION | ◯ | FORME | I — substance |
| 12 | TRANSFORMATION | ∿ | MOUVEMENT | I — substance |
| 13 | TRACE·MÉMOIRE | ◊ | TRACE | I — substance |
| 14 | CROISSANCE | ▲ | INTENSITÉ | III — modale |
| 15 | COMMUNAUTÉ | ⟶ | TRANSMETTRE | II — opérative |
| 16 | RÉSONANCE | ✶ | RÉVÉLER | II — opérative |

Formes d'entrée acceptées par le validateur : nom avec ou sans accents, casse indifférente,
`TRACE` pour `TRACE·MÉMOIRE`, numéro d'id. La forme de **sortie** est toujours le nom canonique.

---

## 2. Syntaxe

| Mode | Forme | Exemple (noms) | Projection glyphique |
|---|---|---|---|
| 1 | `A` | `SEUIL` | `⊥` |
| 2 | `A + B` (non ordonnée) | `HIÉRARCHIE + CONTRAINTE` | `✦ + ⊘` |
| 3 | `tient / bouge / manque` (ordonnée) | `RÉCIPROCITÉ / POLARITÉ / RÉSEAU` | `⊗ / ⥀ / ⊛` |
| 4 | `<signature mode 2 ou 3> ⇒ R` | `PÉRIODICITÉ / CONTRAINTE / ÉMERGENCE ⇒ SEUIL` | `↻ / ⊘ / ⊙ ⇒ ⊥` |
| nul | `∅` | `∅` | `∅` |
| qualificatif (R13) | `A {qualificatif}` à la place de `A`, dans tout mode | `POLARITÉ {multi-échelle}` · `CROISSANCE {rétroaction amplifiante} + CONTRAINTE` | `⥀{×N}` · `▲{R↑} + ⊘` |

Chaque séparateur a un seul sens : `+` tension non ordonnée, `/` positions du Mode 3, `⇒` carte de
tenue (Mode 4), `{…}` qualificatif de la carte qui le précède. Les qualificatifs sont écrits par
leur **nom canonique** (`{rétroaction amplifiante}`, `{rétroaction stabilisante}`,
`{multi-échelle}`, `{délai}`) ; le code court (`R↑`, `R↓`, `×N`, `Δt`) n'apparaît que dans la ligne
glyphique. Aucun nom ni code ne contient `+`, `/` ou `⇒`. Il n'y a plus d'opérative ni de modale dans une signature : la chaîne condensée
`S+O+M` de la v0.3.1 est supprimée (elle introduisait des glyphes de cartes non ancrées).

---

## 3. Règles de validation

Une signature est valide si et seulement si :

1. **Forme** — elle suit exactement une ligne du §2, avec **une espace de chaque côté** de chaque
   séparateur (`A + B`, pas `A+B`) ; 1 à 4 cartes. Le validateur rejette une forme mal espacée et
   indique la forme canonique.
2. **Identité** — chaque élément se résout en un nom canonique du §1.
3. **Ancrage** — chaque carte de la signature a un ancrage de niveau Fort ou Faible dans la lecture
   (Fort obligatoire pour la position *tient*). Le validateur ne peut pas vérifier ce point ; la
   lecture doit le montrer.
4. **Distinction** — pas de carte répétée, sauf la configuration *Scission* (même carte en *tient* et
   *manque*, avec les deux objets nommés ; R8). La carte `⇒ R` est distincte des cartes qu'elle tient.
5. **Double écriture** — en sortie, toujours la ligne des noms ; la ligne glyphique est facultative
   et ne remplace jamais les noms.
6. **Qualificatifs** — au plus deux par carte, sans répétition, pris dans la liste de R13 ; une
   espace entre la carte et `{`, une espace entre deux qualificatifs. Chaque qualificatif d'une
   signature a sa ligne `Q ·` dans la lecture (R13, règle 1 ; contrôlé par `lint` dans le corpus).

Vérification mécanique : `python3 scripts/nexus_tool.py validate "<signature>"`. Le validateur
signale aussi une paire incompatible : en *tient* / *manque* (configuration Lacune contradictoire
possible) et en Mode 2 (relation obligatoirement « indépendance », R6).

---

## 4. Glyphes confondables

Ces paires sont presque identiques à l'écran, et elles recouvrent des paires que la lecture doit
précisément séparer. D'où la règle 5 : le nom fait foi.

| Glyphes | Cartes | Enjeu |
|---|---|---|
| `⊘` / `Ø` | CONTRAINTE / INCERTITUDE | paire **incompatible** (voir `antagonismes.md`) |
| `↻` / `↺` | PÉRIODICITÉ / RÉCURSIVITÉ | confusion de risque élevé |
| `⊙` / `⊛` / `⊗` | ÉMERGENCE / RÉSEAU / RÉCIPROCITÉ | cluster de confusion RÉSEAU–RÉCIPROCITÉ |
| `✦` / `✶` | HIÉRARCHIE / RÉSONANCE | lisibilité |

Les codes de qualificatifs ont été choisis hors de l'alphabet des cartes : la v0.4.1 envisageait
`↻±` pour la rétroaction, glyphe de PÉRIODICITÉ, et `+`, séparateur du Mode 2. Les deux sont exclus.

---

## 5. Relation avec STÈLE

Les glyphes et mots-codes sont **empruntés** à l'alphabet STÈLE ; la correspondance carte ↔ glyphe
est une convention mnémonique, pas un isomorphisme (`✶` RÉVÉLER ne dit rien du modèle de Kuramoto).

| Fait | Conséquence |
|---|---|
| 8 glyphes de carte sont des substances STÈLE | lisibles comme substances dans une phrase STÈLE |
| 4 sont des opératives (`⊗ ⥀ ⟶ ✶`) | exigent un sujet en STÈLE |
| 4 sont des modales (`↻ ↺ ⊘ ▲`) | ne peuvent pas ouvrir une chaîne STÈLE |
| STÈLE n'a pas les séparateurs `+ / ⇒` | une signature n'est pas une chaîne STÈLE |

**Export vers STÈLE** (facultatif) : transmettre la signature et l'énoncé structurel au skill STÈLE,
protocole P1 (Compression). Sa sortie suit la grammaire STÈLE et peut ne pas reprendre les glyphes
de carte tels quels. NEXUS-ARCHÊ ne valide pas cette sortie ; STÈLE la valide selon ses règles.
