# NEXUS-ARCHÊ — Journal des modifications

---

## v0.3 — Phase Publication

**Objectif** : complétion du corpus de référence, calibration des distinctions, guide d'activation LLM.

### Nouveaux fichiers

| Fichier | Contenu |
|---|---|
| `CHANGELOG.md` | Ce fichier — historique des versions |
| `references/test_log.md` | 10 situations documentées couvrant les 16 cartes : validation des ancrages, rejets commentés, chaînes STÈLE produites |
| `references/calibration.md` | Matrice de risque de confusion inter-cartes, protocole de suivi des erreurs, journal de calibration (template) |
| `references/prompt_guide.md` | 7 templates d'activation LLM pour différents contextes et modes, avec exemples d'échanges complets |

### Modifications de fichiers existants

- `SKILL.md` : version portée à 0.3, tableau des fichiers de référence mis à jour
- `README.md` : structure de fichiers mise à jour, section CHANGELOG ajoutée, roadmap v0.4 esquissée

---

## v0.2 — Phase Complétion structurelle

**Objectif** : résoudre les dépendances non résolues, documenter les distinctions inter-cartes, clarifier le mécanisme de tirage.

### Nouveaux fichiers

| Fichier | Contenu |
|---|---|
| `references/stele_rules.md` | Règles syntaxiques STÈLE autonomes — 3 classes, 4 syntaxes valides, tableau de validation |
| `references/examples.md` | 3 tirages annotés complets (Mode 1, 2, 3) + 1 tirage rejeté commenté |

### Modifications de fichiers existants

- `SKILL.md` : glyphes ▲ ⟶ ✶ confirmés définitifs (suppression de la note d'incertitude) ; colonne *Branche mathématique* ajoutée au tableau des 16 cartes ; section Mécanisme de tirage étendue (aléatoire / délibératif / activation LLM) ; tableau des fichiers de référence mis à jour
- `references/cards.md` : champ *Branche mathématique* ajouté à chaque carte ; sections *À ne pas confondre avec* ajoutées sur toutes les paires à risque de confusion
- `references/protocol.md` : section *Modalité du tirage* ajoutée ; 4 configurations pathologiques du Mode 3 documentées ; Mode 4 optionnel (Tirage de résolution) ajouté avec sa syntaxe STÈLE propre ; section *Activation par LLM* ajoutée

---

## v0.1 — Mise en place initiale

**Objectif** : architecture de base, 16 cartes, protocole de rigueur, compression STÈLE.

### Fichiers fondateurs

| Fichier | Contenu |
|---|---|
| `SKILL.md` | Architecture principale, tableau des 16 cartes, mécanisme de tirage, protocole de rigueur |
| `references/cards.md` | Les 16 fiches (rationnel / symbolique / STÈLE / Question IRIS) |
| `references/protocol.md` | 3 modes de tirage, protocole de rigueur en 4 étapes, statut épistémique |
| `README.md` | Présentation générale, positionnement écosystème IRIS |

### Limitations connues au moment de la publication

- 3 glyphes STÈLE marqués comme incertains (▲ CROISSANCE, ⟶ COMMUNAUTÉ, ✶ RÉSONANCE) → résolus en v0.2
- Absence de règles syntaxiques STÈLE autonomes → résolues en v0.2
- Absence d'exemples de tirages concrets → résolue en v0.2
- Absence de distinctions inter-cartes → résolue en v0.2
- Mécanisme de tirage non précisé → résolu en v0.2
