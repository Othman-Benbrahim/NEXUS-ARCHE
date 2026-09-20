---
name: nexus-arche
version: 0.3.1
description: >
  NEXUS-ARCHÊ est un système de lecture résonante à double registre.
  Il identifie les structures invariantes qui apparaissent simultanément
  dans les mathématiques (systèmes dynamiques, topologie, théorie des réseaux)
  et dans les universaux comportementaux documentés par Donald Brown.
  16 cartes structurelles, un mécanisme de tirage résonant (non narratif),
  un protocole de rigueur à 4 niveaux, une compression STÈLE par carte.
  Activer quand : analyser la structure cachée d'une situation complexe,
  travailler à l'interface rationnel/symbolique, identifier des patterns
  qui traversent les deux registres, ou réaliser un tirage structurel.
---

# NEXUS-ARCHÊ
### Système de lecture résonante des structures invariantes

---

## POSITION DANS L'ÉCOSYSTÈME IRIS

NEXUS-ARCHÊ est un outil d'analyse structurelle autonome.

Il se distingue de **Miroir-Trans-Échelle** qui orchestre une lecture croisée
entre deux skills existants (Fractales du Destin / Signaux du Futur).
NEXUS-ARCHÊ possède son propre corpus de 16 structures et son propre mécanisme.

Articulations possibles :
- **STÈLE** : chaque carte porte un glyphe STÈLE primaire. Les tirages produisent des chaînes compressibles. Les règles syntaxiques minimales nécessaires à NEXUS-ARCHÊ sont disponibles dans `references/stele_rules.md`.
- **Fractales du Destin** : peut compléter un tirage FdD en nommant la structure sous-jacente.
- **OSINT / Superforecasting** : NEXUS-ARCHÊ identifie la structure d'une situation avant l'analyse prédictive.

---

## LES 16 CARTES

Chaque carte = une structure invariante documentée en deux registres.
Les fiches complètes (rationnel / symbolique / branche mathématique / STÈLE / Question IRIS / À ne pas confondre avec) se trouvent dans `references/cards.md`.

| Carte | Glyphe STÈLE | Mot-code | Branche mathématique |
|---|---|---|---|
| SEUIL | ⊥ | LIMITE | Systèmes dynamiques |
| RÉCIPROCITÉ | ⊗ | LIER | Théorie des jeux coopératifs |
| PÉRIODICITÉ | ↻ | CYCLE | Systèmes dynamiques — oscillateurs |
| RÉCURSIVITÉ | ↺ | RÉFLEXIVITÉ | Théorie de la computation / fractals |
| ÉMERGENCE | ⊙ | SOURCE | Systèmes complexes |
| HIÉRARCHIE | ✦ | AXE | Théorie des graphes / lois de puissance |
| RÉSEAU | ⊛ | NOEUD | Théorie des graphes / topologie |
| POLARITÉ | ⥀ | INVERSER | Algèbre / topologie différentielle |
| INCERTITUDE | Ø | VIDE | Théorie des probabilités / entropie |
| CONTRAINTE | ⊘ | NÉGATION | Théorie des systèmes / optimisation |
| PROPORTION | ◯ | FORME | Géométrie / algèbre |
| TRANSFORMATION | ∿ | MOUVEMENT | Algèbre des transformations / topologie |
| TRACE · MÉMOIRE | ◊ | TRACE | Théorie de l'information |
| CROISSANCE | ▲ | INTENSITÉ | Analyse mathématique / équations différentielles |
| COMMUNAUTÉ | ⟶ | TRANSMETTRE | Théorie des jeux coopératifs / auto-organisation |
| RÉSONANCE | ✶ | RÉVÉLER | Physique des oscillateurs couplés |

---

## MÉCANISME DE TIRAGE

**Principe** : tirage résonant, non narratif.
Les cartes décrivent simultanément les structures actives d'une situation.
La question de base : *Quelles structures organisent ce qui est en train de se passer ?*

Voir `references/protocol.md` pour les trois modes, les modalités de tirage et le protocole de rigueur complet.
Les configurations pathologiques du Mode 3 reposent sur la relation d'antagonisme définie dans `references/antagonismes.md`.

### Deux modalités de tirage

**Tirage aléatoire** : sélection d'une ou plusieurs cartes parmi les 16 par simulation numérique ou procédé aléatoire physique. Usage recommandé pour provoquer la surprise structurelle — faire apparaître une structure qu'on n'aurait pas spontanément identifiée.

**Tirage délibératif** : identification directe de la ou des cartes qui résonnent le plus avec la situation après lecture du corpus. Usage recommandé pour confirmer une intuition structurelle ou approfondir une analyse en cours.

**Activation par LLM** : le modèle lit la situation, identifie 2 à 3 cartes candidates, applique le test d'ancrage observable à chacune, et retient uniquement celles disposant d'un ancrage vérifiable. Voir `references/protocol.md` section *Activation par LLM*.

### Les trois modes

**Mode 1 — Tirage simple (1 carte)**
Une structure dominante. La Question IRIS comme point d'entrée.

**Mode 2 — Tirage de tension (2 cartes)**
Lecture simultanée des deux cartes. Question : quelle relation structurelle ?

**Mode 3 — Tirage de constellation (3 cartes)**
Ce qui tient / Ce qui bouge / Ce qui manque.
Produit une chaîne STÈLE à 3 glyphes.

---

## PROTOCOLE DE RIGUEUR

4 exigences applicables à tout tirage :

1. **Ancrage observable** — nommer une observation concrète dans la situation réelle qui correspond à la structure. Sans ancrage, la carte n'est pas active dans cette lecture.

2. **Test d'anti-résonance** — pour chaque carte : qu'est-ce qui, dans la situation, contredit cette structure ? Force la vérification du biais de confirmation.

3. **Énoncé structurel de tension** — si plusieurs cartes : formuler la relation entre elles en termes structurels précis, pas en métaphore.

4. **Chaîne STÈLE syntaxiquement valide** — la compression finale suit les règles grammaticales de STÈLE. Toujours fournir la transcription verbale. Voir `references/stele_rules.md` pour les règles de composition autonomes.

---

## FICHIERS DE RÉFÉRENCE

| Fichier | Contenu |
|---|---|
| `references/cards.md` | Les 16 fiches complètes : rationnel / symbolique / branche mathématique / STÈLE / Question IRIS / À ne pas confondre avec |
| `references/protocol.md` | Mécanisme de tirage détaillé + modalités aléatoire/délibératif + protocole de rigueur + configurations pathologiques Mode 3 |
| `references/stele_rules.md` | Règles syntaxiques STÈLE minimales autonomes : classification des 16 glyphes, grammaire des chaînes, validation |
| `references/examples.md` | 3 tirages annotés complets (Mode 1, Mode 2, Mode 3) + 1 tirage rejeté commenté |
| `references/test_log.md` | 10 situations documentées couvrant les 16 cartes — validations d'ancrage, rejets commentés, observations transversales |
| `references/calibration.md` | Matrice de risque de confusion inter-cartes, faux positifs documentés, protocole de suivi et journal de calibration |
| `references/antagonismes.md` | Table des incompatibilités structurelles entre cartes, conditions opératoires des 4 configurations pathologiques du Mode 3, journal |
| `references/prompt_guide.md` | 7 templates d'activation LLM pour différents contextes : Mode 1/2/3, STÈLE, OSINT, Fractales du Destin |

---

## FONDEMENTS

**Mathématiques** : voir tableau des cartes pour la branche par carte. Domaines couverts : systèmes dynamiques, topologie, théorie des réseaux, probabilité, algèbre des transformations, fonctions de croissance, théorie des jeux coopératifs, physique des oscillateurs couplés.

**Anthropologie** : universaux comportementaux documentés par Donald Brown (*The Universal People*, 1991), via Steven Pinker (*The Blank Slate*). Pour RÉSONANCE : ancrage complémentaire dans la biologie évolutive (synchronisation collective, entraînement).

**Symbolique** : alphabet STÈLE — compression glyphique en registre performatif. Règles minimales autonomes dans `references/stele_rules.md`.

**Positionnement** : outil structurel empirique. Ni ésotérisme naïf, ni réductionnisme scientifique. Langage de structures qui traversent les deux régimes.

