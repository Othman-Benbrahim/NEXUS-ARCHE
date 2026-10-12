# NEXUS-ARCHÊ

**Lecture structurelle d'une situation par 16 structures invariantes** — v0.4.1

NEXUS-ARCHÊ est un skill Claude de l'écosystème IRIS. Il identifie, dans une situation décrite par
des faits, les structures qui l'organisent : SEUIL, RÉSEAU, HIÉRARCHIE, ÉMERGENCE, PÉRIODICITÉ…
Chaque structure est définie par une **structure mathématique nommée** et, lorsqu'il existe, par un
**universel humain** de la liste de Donald Brown.

## Ce qui le distingue d'un système projectif

| Garde-fou | Où |
|---|---|
| Une carte n'est active que si un **fait** observable remplit l'un de ses marqueurs ; un ressenti ne suffit jamais | `protocol.md` R2–R3 |
| L'**anti-résonance** peut rétrograder ou rejeter une carte, selon la portée de la contre-observation | R4 |
| La lecture peut conclure : **aucune structure du corpus n'est active** | R9 |
| Le tirage aléatoire passe par un **vrai générateur**, journalisé ; pas de hasard simulé | R1, `scripts/nexus_tool.py draw` |
| Le **statut** (Descriptif / Spéculatif / Nul) se **calcule** à partir des ancrages | R11 |
| Le double registre est **vérifiable** : items exacts de Brown, statut par carte | `cards.md` |

Le skill ne prescrit pas, ne diagnostique pas, ne prévoit pas.

**« 16 structures » n'est pas une revendication de complétude.** Le corpus est volontairement plus
étroit qu'en v0.3.1 (RÉCURSIVITÉ réduite à l'auto-référence, par exemple) ; deux lacunes sont déjà
connues (rétroaction simple, auto-similarité). Quand un motif clair n'est décrit par aucune carte, la
lecture le nomme en clair (R9) au lieu de le rabattre sur la carte la plus proche.

## Démarrage

```
NEXUS-ARCHÊ. Situation : [4 à 8 phrases factuelles : qui, quoi, quand, combien].
```

Sortie type :

```
NEXUS-ARCHÊ · Mode 1 · Modalité délibérative
| ÉMERGENCE | format de compte rendu adopté par imitation, sans consigne | Fort | la fondatrice a recruté les 10 premiers (marginale) | Fort |
R3 · ÉMERGENCE : TRANSFORMATION → (rien ne préexistait) ; RÉCURSIVITÉ → (…) ; CROISSANCE → (…) ; INCERTITUDE → (…)
Cartes inactives : TRANSFORMATION — aucune entité préexistante
Signature : ÉMERGENCE
            ⊙
Statut : Descriptif
```

Plus de templates : `references/prompt_guide.md`. Exemples complets : `references/examples.md`.

## Contenu

```
SKILL.md                    procédure (ordre des étapes) et politique de chargement
README.md                   ce fichier
CHANGELOG.md                historique ; v0.4.0 et v0.4.1 = réponses point par point aux deux audits
VERIFICATION_AUDIT.md       contrôle de l'audit v0.3.1 avant réécriture
LICENSE
references/
  protocol.md               règles R1–R12 (source unique)
  cards.md                  16 fiches : définition, structure, marqueurs, items Brown, distinctions
  notation.md               noms canoniques, glyphes, syntaxe des signatures, relation à STÈLE
  antagonismes.md           2 incompatibilités, 7 tensions documentées, fréquences
  calibration.md            matrice de confusion a priori, faux positifs, lacunes, indicateurs
  examples.md               6 lectures annotées (dont rejet, ∅, hors corpus, tirage réel)
  test_log.md               10 démonstrations relues + protocole de test réel (journal vide)
  prompt_guide.md           8 templates
scripts/
  nexus_tool.py             draw · validate · stats · lint (lit ses données dans references/)
```

## Outil

```
python3 scripts/nexus_tool.py draw -n 3                 # tirage sans remise, ligne de journal
python3 scripts/nexus_tool.py draw -n 2 --seed "texte"  # tirage rejouable
python3 scripts/nexus_tool.py draw -n 1 --exclude "SEUIL,RÉSEAU"   # retirage parmi les cartes non sorties
python3 scripts/nexus_tool.py validate "RÉCIPROCITÉ / POLARITÉ / RÉSEAU"
python3 scripts/nexus_tool.py stats                     # fréquences des configurations
python3 scripts/nexus_tool.py lint                      # fichiers, versions, voisines, R3 du corpus, citations
```

## Déploiement

La v0.4.1 forme un tout : `SKILL.md` + les 8 fichiers de `references/` + `scripts/nexus_tool.py`.
Une installation partielle ou mélangée (par exemple un `SKILL.md` récent avec des références v0.3,
qui n'ont ni `notation.md` ni les règles R1–R12) produit des renvois vers des règles inexistantes.

1. Remplacer **tout** le dossier du skill installé, pas fichier par fichier.
2. Vérifier : `python3 scripts/nexus_tool.py lint` doit afficher `LINT OK` et
   `version 0.4.1 cohérente` (il contrôle la présence des fichiers requis et l'en-tête
   `> Version :` de chaque référence).
3. Sans shell, le skill fait lui-même ce contrôle (section « Contrôle d'intégrité » de `SKILL.md`)
   et signale toute version divergente avant de lire.
4. Publier le dépôt et l'installation **en même temps** : la copie installée sur claude.ai était
   restée en v0.3 quand le dépôt passait en v0.3.1.

## Dépendances

Autonome pour la lecture structurelle. Le script demande Python 3.8+ sans bibliothèque externe.
Dépendant de skills tiers pour : la phrase STÈLE (`stele`), la prévision (`prediction-engine`,
`osint-intel`), le dialogue avec un tirage symbolique (`fractales-du-destin`).

## Statut empirique

Aucune donnée d'usage n'est encore collectée : les journaux de `calibration.md`,
`antagonismes.md` et `test_log.md` sont vides. Les exemples et démonstrations sont des cas
construits. La v0.5 doit exécuter le protocole de `test_log.md` §3 avant toute revendication de
fiabilité.

## Fondements

- **Mathématiques** : une structure nommée par carte (`cards.md`), avec références.
- **Anthropologie** : Brown, D. E. (1991), *Human Universals*, McGraw-Hill ; liste citée dans la
  compilation reprise par Pinker (2002), *The Blank Slate*. 11 cartes documentées, 3 partielles,
  2 à établir.
- **Symbolique** : glyphes empruntés à l'alphabet STÈLE, comme projection d'affichage.

*Projet IRIS — Othman Benbrahim. Dépôt public, usage libre selon LICENSE.*
