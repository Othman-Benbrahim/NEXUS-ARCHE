# NEXUS-ARCHÊ — Journal des modifications

---

## v0.3.1 — Antagonismes structurels

**Objectif** : fournir la relation supposée par les configurations pathologiques 3 et 4 du Mode 3, absente depuis v0.2.

### Nouveaux fichiers

| Fichier | Contenu |
|---|---|
| `references/antagonismes.md` | Table des 9 paires de cartes structurellement incompatibles, chacune fondée sur une citation de `cards.md` ; définitions opératoires des 4 configurations pathologiques ; condition du même objet ; journal |

### Modifications de fichiers existants

- `references/protocol.md` : les 4 configurations pathologiques reçoivent une condition vérifiable ; renvoi vers `antagonismes.md` ; la configuration signalée est requalifiée en hypothèse à vérifier
- `references/calibration.md` : note liminaire distinguant confusion et antagonisme
- `SKILL.md` : version portée à 0.3.1, renvoi depuis le mécanisme de tirage, tableau des fichiers de référence mis à jour
- `README.md` : version, tableau des dépendances internes, arborescence et roadmap mis à jour

### Décisions

- La configuration 4 est calculée sur **deux** paires antagonistes et non trois : la table ne contient aucun triangle, et l'exiger rendrait la configuration inatteignable par construction.
- Aucune partition des 16 cartes en « registres » n'a été introduite. Elle aurait dû être inventée, et aurait servi de fondement à un diagnostic. L'antagonisme est défini paire à paire, à partir des définitions déjà écrites dans `cards.md`.
- Aucun antagonisme n'est dérivé du « ou » d'un critère discriminant : ce « ou » désigne la carte à retenir pour une lecture, pas une exclusion entre structures. Appliqué mécaniquement, il ferait de HIÉRARCHIE et RÉSEAU des antagonistes.
- La définition du voisinage documenté (configuration 2) réutilise une relation écrite pour un autre usage. Elle est signalée comme la plus fragile du fichier et à réviser sur données réelles.

### Limitation connue

- Les 24 citations de `cards.md` et `protocol.md` reprises dans `antagonismes.md` ont été vérifiées mot pour mot contre la v0.3. Toute modification ultérieure de `cards.md` impose de refaire cette vérification : une citation devenue fausse invalide la ligne de table qu'elle fonde.

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

