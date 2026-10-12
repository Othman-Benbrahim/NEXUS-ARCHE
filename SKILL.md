---
name: nexus-arche
description: >
  NEXUS-ARCHÊ — lecture structurelle d'une situation par 16 cartes (SEUIL, RÉSEAU, HIÉRARCHIE,
  ÉMERGENCE, PÉRIODICITÉ, CONTRAINTE…), chacune définie par une structure mathématique nommée et,
  quand il existe, un universel humain de Donald Brown. Chaque carte doit être ancrée dans des
  faits observables et passer un test d'anti-résonance qui peut la rejeter ; la lecture peut
  conclure qu'aucune structure n'est active. Modes 1 à 4, tirage délibératif ou aléatoire
  journalisé, signature compacte, statut calculé.
  Activer pour : nommer la structure d'une situation complexe, un « tirage NEXUS-ARCHÊ »,
  cadrer une situation avant une analyse OSINT ou prédictive, ajouter un plan structurel à un
  tirage Fractales du Destin. Ne pas activer pour : une demande de solution ou de conseil, une
  prévision chiffrée (prediction-engine), un soutien émotionnel, une situation décrite seulement
  par des ressentis sans faits (demander des faits d'abord), ou une phrase STÈLE (skill stele).
metadata:
  version: 0.4.1
---

# NEXUS-ARCHÊ

Lecture des structures invariantes d'une situation. Ce fichier donne **l'ordre des étapes** ;
les règles R1–R12 sont définies une seule fois dans `references/protocol.md`.

## Contrôle d'intégrité (avant toute lecture)

Cette version (0.4.1) exige les fichiers `references/protocol.md`, `cards.md`, `notation.md`,
`antagonismes.md`, et chaque fichier de référence porte en tête `> Version : 0.4.1`.
Si un fichier requis manque, ou si sa version diffère de celle-ci, **le dire à l'utilisateur**
(« installation incomplète ou mélangée : la v0.4.1 de NEXUS-ARCHÊ exige … ») et ne pas appliquer
de règle dont la source manque. Une copie en v0.3 ne contient ni `notation.md` ni les règles R1–R12.
Avec un shell : `python3 scripts/nexus_tool.py lint` vérifie fichiers, versions et cohérence.

## Ce qu'il faut charger

| Situation | Fichiers |
|---|---|
| Toute lecture | ce fichier + `references/protocol.md` + `references/cards.md` + `references/notation.md` |
| Mode 3, ou une configuration à vérifier | + `references/antagonismes.md` |
| Doute entre deux cartes | + `references/calibration.md` (matrice de confusion) |
| L'utilisateur veut voir des exemples, ou une lecture ambiguë | + `references/examples.md` |
| Template d'activation, intégration OSINT / Fractales du Destin | + `references/prompt_guide.md` |
| Audit, évaluation du skill | + `references/test_log.md` |

## Les 16 cartes

| Carte | Glyphe | Structure mathématique nommée | Registre Brown |
|---|---|---|---|
| SEUIL | ⊥ | hystérésis, état absorbant | documenté |
| RÉCIPROCITÉ | ⊗ | jeux répétés, stratégies conditionnelles | documenté |
| PÉRIODICITÉ | ↻ | orbites périodiques, cycles limites | documenté |
| RÉCURSIVITÉ | ↺ | auto-référence, points fixes, réflexivité | partiel |
| ÉMERGENCE | ⊙ | auto-organisation, criticité auto-organisée | à établir |
| HIÉRARCHIE | ✦ | ordres partiels, arborescences, dominance | documenté |
| RÉSEAU | ⊛ | graphes, centralité, ponts, trous structuraux | documenté |
| POLARITÉ | ⥀ | involution (Z₂) | documenté |
| INCERTITUDE | Ø | distribution sur un espace d'états non réduit | documenté |
| CONTRAINTE | ⊘ | ensemble admissible, contraintes actives | documenté |
| PROPORTION | ◯ | ratios, similitudes, allométrie | partiel |
| TRANSFORMATION | ∿ | déformations continues à invariant | à établir |
| TRACE·MÉMOIRE | ◊ | dépendance au chemin, processus à mémoire | documenté |
| CROISSANCE | ▲ | croissance logistique, saturation | partiel |
| COMMUNAUTÉ | ⟶ | biens publics, coalitions, communs | documenté |
| RÉSONANCE | ✶ | oscillateurs couplés (Kuramoto) | documenté |

Définitions, marqueurs observables, voisines documentées et questions discriminantes :
`references/cards.md`. Les 16 cartes ne couvrent pas toutes les structures possibles (R9).
Le nom de carte fait foi ; le glyphe n'est qu'une projection (`references/notation.md`).

## Procédure

**0. Recevabilité.** Si la description ne contient aucun fait (seulement des ressentis), ne pas
tirer : demander 2 ou 3 faits précis (qui, quoi, quand, quel comportement). Si l'utilisateur
demande une solution, dire que NEXUS-ARCHÊ nomme des structures et proposer la lecture.

**1. Modalité (R1).** Délibérative par défaut. Aléatoire seulement avec un générateur réel —
`python3 scripts/nexus_tool.py draw -n 3` — et sa ligne de journal recopiée. Jamais de « hasard »
simulé de tête. Tirage sans remise ; il choisit les cartes, pas les positions. Au plus deux retirages
d'une carte (`--exclude` les cartes déjà sorties).

**2. Candidates.** En délibératif : 2 à 4 cartes, dont au moins une **contre-candidate** prise dans
les « À ne pas confondre avec » de la favorite. Si l'utilisateur impose une carte, la tester comme
une candidate parmi d'autres.

**3. Ancrage (R2, R3).** Pour chaque candidate : citer le fait qui remplit un marqueur observable,
puis attribuer un niveau Fort / Faible / Nul. Le niveau Fort exige une ligne
`R3 · CARTE : VOISINE → (raison) ; …` qui passe **toutes** les voisines documentées de la carte
(verdicts `→`, `+`, `?`, `←`). Ressenti, ignorance déclarée et coïncidence lexicale ne comptent pas.
Carte Nul = inactive, listée comme telle.

**4. Anti-résonance (R4).** Pour chaque carte restante : la contre-observation la plus forte, sa
portée (marginale / substantielle / dominante / aucune trouvée) et son effet sur le niveau.
Ce test **peut rejeter**.

**5. Mode (R5).** Déterminé par les cartes encore ancrées : 0 → résultat nul (R9) ; 1 → Mode 1 ;
2 → Mode 2 ; 3 ou plus → Mode 3 **seulement si** trois d'entre elles remplissent les positions de R7
(*tient* présente et Fort, *bouge* présente, *manque* absente aux effets observables), sinon Mode 2
sur les deux plus fortes ; les autres sont listées « ancrées non retenues ». Ne jamais compléter avec
une carte non ancrée.

**6. Lecture.**
- Mode 1 : la question d'exploration de la carte, posée à la situation.
- Mode 2 (R6) : énoncé en termes structurels + une relation parmi renforcement mutuel, conflit,
  inclusion, appui, reproduction, indépendance, tension documentée. Une paire incompatible n'admet
  que l'indépendance.
- Mode 3 (R7, R8) : positions *tient / bouge / manque* (tient exige Fort ; manque s'ancre par un
  effet de l'absence) ; vérifier les configurations Scission, Reproduction, Lacune contradictoire,
  chacune avec ce qu'elle signale et sa question à l'auteur.
- Mode 4 (R10) : seulement après une configuration ou une reproduction confirmée, ou sur demande ;
  la carte de tenue s'ancre comme les autres.
- Structure hors corpus (R9) : la nommer en clair plutôt que la rabattre sur une carte.

**7. Signature (notation.md).** Noms canoniques : `A` · `A + B` · `tient / bouge / manque` ·
`… ⇒ R` · `∅`. Glyphes en seconde ligne, facultatifs. Vérifiable par
`python3 scripts/nexus_tool.py validate "<signature>"`.

**8. Statut (R11).** Calculé : Descriptif si toutes les cartes sont Fort, chacune avec une
contre-observation classée, et toute configuration confirmée ; sinon Spéculatif ; Nul si ∅.

## Format de sortie

```
NEXUS-ARCHÊ · Mode [0–4] · Modalité [délibérative | aléatoire : <ligne de journal>]

Cartes examinées
| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
R3 · [carte Fort] : [voisine] → (raison) ; …

Cartes inactives : [carte — raison]

Lecture : [question d'exploration / énoncé de tension / constellation + configurations]

Signature : [noms canoniques]
            [glyphes]
Statut : [Descriptif | Spéculatif | Nul] — [raison en une ligne]
À vérifier auprès de vous : [questions de même objet, configurations, faits manquants]
```

## Limites (R12)

Ne prescrit pas, ne diagnostique pas, ne prévoit pas. Les hypothèses sur l'avenir se confient à
`prediction-engine` ou `osint-intel`. Une phrase STÈLE se demande au skill `stele` (la signature
NEXUS-ARCHÊ n'est pas une chaîne STÈLE). Autonome pour la lecture structurelle ; l'export STÈLE
et les intégrations dépendent des skills concernés.

## Articulations

| Skill | Relation |
|---|---|
| `stele` | compresse une signature en phrase STÈLE légale (protocole P1) |
| `fractales-du-destin` | NEXUS-ARCHÊ nomme la structure sous un tirage symbolique, sans le remplacer |
| `miroir-trans-echelle` | lit croisé symbolique / analytique ; NEXUS-ARCHÊ peut fournir le plan structurel |
| `osint-intel`, `prediction-engine` | reçoivent la structure identifiée comme cadre d'hypothèses |
| `zetetique-broch` | peut auditer une lecture comme n'importe quel raisonnement |
