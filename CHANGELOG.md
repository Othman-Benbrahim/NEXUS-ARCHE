# NEXUS-ARCHÊ — Journal des modifications

---

## v0.4.2 — Qualificatifs et procédure d'admission

**Objet** : répondre à la question « comment pallier l'étroitesse du corpus ? » sans recréer les
confusions supprimées en v0.4. Les deux lacunes connues (rétroaction, auto-similarité) ne sont pas
des structures de même nature que les 16 cartes : ce sont des **mécanismes** ou des **modes de
déploiement**. Elles deviennent des qualificatifs, pas des cartes.

### Ajouts

| Fichier | Changement |
|---|---|
| `references/protocol.md` | **R13 — Qualificatifs** : `{rétroaction amplifiante}` (R↑), `{rétroaction stabilisante}` (R↓), `{multi-échelle}` (×N), `{délai}` (Δt), chacun avec son marqueur observable ; ancrage par une ligne `Q ·`, anti-résonance qui peut le retirer, deux au plus par carte, aucun effet sur le mode, les voisines ou les incompatibilités. R9 : tester les qualificatifs avant de conclure « hors corpus ». R11 : Descriptif exige une contre-observation classée pour chaque qualificatif |
| `references/notation.md` | syntaxe `A {qualificatif}` dans tout mode ; règle de validation 6 ; codes choisis hors de l'alphabet des cartes |
| `references/calibration.md` | §4 : statut des lacunes connues, entrées réelles seulement ; **§6 Procédure d'admission** en quatre étapes (seuil de 3 cas réels indépendants, test de non-réduction contre cartes et qualificatifs, fiche complète, régression) + déclencheur global (> 15 % hors corpus sur 20 lectures) ; deux indicateurs ajoutés |
| `references/examples.md` | exemple 6 relu : `POLARITÉ {multi-échelle}` au lieu de « hors corpus » ; variante honnête d'un hors-corpus (monopole d'une ressource), déclarée **lacune possible**, non comptée pour le seuil |
| `references/cards.md` | RÉCURSIVITÉ renvoie aux qualificatifs au lieu du hors-corpus |
| `references/prompt_guide.md` | template 4bis |
| `scripts/nexus_tool.py` | `validate` lit les qualificatifs dans R13, les valide et les projette (`⥀{×N}`) ; `lint` vérifie que chaque qualificatif d'une signature du corpus a sa ligne `Q ·` avec fait et contre-observation |
| `SKILL.md`, `README.md` | étapes 6 et 7, format de sortie, section complétude réécrite |

### Correction de conception

La v0.4.1 envisageait `↻±` comme code de la rétroaction : c'est le glyphe de PÉRIODICITÉ, et `+` est
le séparateur du Mode 2. Les noms canoniques et les codes ne contiennent ni glyphe de carte, ni
`+`, `/` ou `⇒`.

### Ce qui n'est pas fait

- Aucune carte ajoutée : la procédure d'admission exige des cas réels, et il n'y en a encore aucun.
- Les qualificatifs n'ont pas de niveau Fort / Faible : un qualificatif est ancré ou retiré. À
  revoir si l'usage montre des cas intermédiaires fréquents.
- Le protocole de test réel (`test_log.md` §3) n'est toujours pas exécuté.

---

## v0.4.1 — Corrections après vérification de la v0.4.0

**Objet** : traiter les points de `VERIFICATION_CORRECTIONS_v0.4.0.md` (12/10/2026) — une
contradiction documentaire, six non-conformités règle ↔ exemple, cinq lacunes fonctionnelles,
cinq effets de bord. Ligne directrice : **ce qui peut être vérifié par machine l'est**. `lint`
contrôle désormais l'application de R3 dans le corpus, les versions, la symétrie des voisines et
les citations.

### Réponse point par point

| # | Point | Traitement |
|---|---|---|
| §2 | `VERIFICATION_AUDIT.md` retenait 3 incompatibilités | note datée en tête et en §5 : 3 → 2 (redéfinition de SEUIL) ; chiffres en vigueur 56/3360 et 0/560 |
| 3.1 | R3 n'était appliqué nulle part | **R3 maintenu tel quel**, appliqué partout : chaque carte Fort des 6 exemples et 10 démonstrations porte une ligne `R3 ·` couvrant **toutes** ses voisines documentées ; quatre verdicts (`→ + ? ←`) ; `lint` rejette une ligne incomplète, un `?` ou un `←` sur une carte Fort |
| 3.2 | R7 contre test_log 09 | tranché au plus strict : ÉMERGENCE « absente » est **Nul** (le constat d'absence n'est pas un effet ; un discours est un fait sur un discours, R2) ; 09 passe en Mode 2 |
| 3.3 | R5 « 4 et plus » sans réserve | ligne unique « 3 ou plus » avec la condition R7 et le repli Mode 2 + liste |
| 3.4 | Config 2 : condition ≠ test, contre-factuel | redéfinie comme **relation de reproduction** (R6) à deux conjoints observables : (a) production datée, (b) réapparition de l'effet. **Plus aucun contre-factuel.** Utilisable en Mode 2 et entre *tient* et *bouge* en Mode 3 |
| 3.5 | Espacement non contrôlé | le validateur rejette `A+B` et indique la forme canonique |
| 3.6 | SKILL.md « 3+ → Mode 3 » | étape 5 alignée mot pour mot sur R5 |
| 4.1 | Paire incompatible non signalée en Mode 2 | signal du validateur ; R6 : une paire incompatible n'admet que la relation « indépendance » |
| 4.2 | Mode 3 aléatoire : positions par ordre de tirage | R1 : **le tirage choisit les cartes, pas les positions** ; positions fixées après ancrage (R7) ; repli R5 sinon ; message du script corrigé |
| 4.3 | `n` du retirage non fixé | R1 : retirage d'**une** carte, parmi les non sorties (`draw --exclude`), deux au plus ; exemple 2 refait avec de vrais tirages (conclu à ∅) |
| 4.4 | Configurations sans lecture ; « Miroir » hérité | R8 : colonnes « ce qu'elle signale » et « question à l'auteur » ; Miroir renommé **Scission** |
| 4.5 | Config 2 non surveillée | indicateur « confirmées / signalées » par configuration (calibration.md §5), avec la règle : taux bas → durcir R6 (a)–(b) |
| 5.1 / 5.2 | SEUIL et TRACE partagent l'hystérésis | déclaré **inclusion** (SEUIL ⊂ TRACE, `antagonismes.md` §4bis, avec HIÉRARCHIE ⊂ RÉSEAU) ; voisines réciproques + question discriminante ; ligne dans la matrice de confusion ; hystérésis retirée de la liste de TRACE |
| 5.3 | « 16 structures » lu comme complétude | README et R12 : pas une revendication de complétude |
| 5.4 | N2 non traité | section **Contrôle d'intégrité** dans SKILL.md ; en-tête `> Version :` dans chaque référence ; `lint` vérifie fichiers requis et versions ; section **Déploiement** du README |
| 5.5 | Citations absentes des références | 7 références ajoutées (Ferguson, Gompertz, Hayek, Kleene, Klein, Shannon, Verhulst) ; `lint` vérifie chaque « Nom année » de cards.md |

### Autres changements

- R6 : nouveau type de relation **appui** (unidirectionnel), requis par la démonstration 06.
- R4 : un contre-exemple pris hors de la situation n'est pas une anti-résonance (explicite).
- R2 : un discours compte comme fait **sur le discours**, pas comme preuve de ce qu'il affirme.
- Graphe des voisines documentées : 26 paires, symétrique (vérifié par `lint`).

### Corrections de `VERIFICATION_AUDIT.md` (audit de l'audit, 12/10/2026)

| # | Point | Traitement |
|---|---|---|
| 2.1 | « six erreurs » pour sept lignes | verdict et §2 disent **sept points** : six erreurs (E1–E6) + une formulation inexacte (E7, marquée comme telle) |
| 2.2 | C3 mal localisé (« table des références dit "trois modes" ») | localisation corrigée : titre « ### Les trois modes » et phrase de la section *Mécanisme de tirage* ; la table des références ne compte pas les modes |
| 2.3 | « cinq faiblesses de fond » repris sans relever les huit sous-sections | le verdict signale que le §3 de l'audit, titré « les cinq qui comptent », en compte **huit** |
| 2.4 | N2 invérifiable depuis le paquet | marqué **observation hors corpus**, avec la preuve (chemin de la copie synchronisée, `version: 0.3`, absence d'`antagonismes.md`), sa portée (copie claude.ai, pas une installation locale) et le moyen de la revérifier |
| 2.5 | Incise « ajouts postérieurs à 1991 » | retirée ; remplacée par ce que la page source dit d'elle-même (compilation Brown « as published in » Pinker 2002, renvois Brown 1991 et 2000) |

Aucun fichier de `references/` ni `SKILL.md` n'est modifié par ces corrections.

### Ce qui n'est pas fait

- Le protocole de test réel (`test_log.md` §3) n'est toujours pas exécuté ; aucune donnée d'usage.
- `lint` vérifie la **présence** et la **forme** des justifications R3, pas leur **justesse**.

---

## v0.4.0 — Réécriture après audit

**Objectif** : supprimer les contradictions internes démontrées par l'audit du 12/10/2026, rendre
le test d'anti-résonance capable de rejeter, rendre le double registre vérifiable, et séparer la
notation NEXUS-ARCHÊ de la grammaire STÈLE. Contrôle préalable de l'audit : `VERIFICATION_AUDIT.md`.

### Fichiers

| Fichier | Changement |
|---|---|
| `SKILL.md` | réécrit : procédure en 9 étapes, politique de chargement, 4 modes + résultat nul, déclencheurs négatifs dans la description, version en `metadata` |
| `references/protocol.md` | réécrit : règles R1–R12, source unique |
| `references/cards.md` | réécrit : marqueurs observables, structures nommées, items Brown exacts et statut |
| `references/notation.md` | **nouveau**, remplace `stele_rules.md` |
| `references/antagonismes.md` | réécrit : 2 incompatibilités, 7 tensions documentées |
| `references/calibration.md` | matrice requalifiée (origine lecteur / source), journal des lacunes |
| `references/examples.md` | réécrit : 6 exemples dont rejet, ∅, hors corpus, tirage réel |
| `references/test_log.md` | requalifié en démonstrations ; protocole de test réel |
| `references/prompt_guide.md` | réécrit : 8 templates, sans redéfinition de règles |
| `scripts/nexus_tool.py` | **nouveau** : draw, validate, stats, lint |
| `references/stele_rules.md` | **supprimé** (voir notation.md §0) |

### Réponse au plan de correction de l'audit

| # | Point | Traitement |
|---|---|---|
| 1 | Tirage sans remise | R1 ; appliqué par `draw` |
| 2 | Config 2 indétectable | nouveau test sur les ancrages (R8) ; test_log 09 désormais détecté |
| 3 | Standard d'ancrage | R2 : aucun ressenti, individuel ou collectif, n'ancre une carte |
| 4 | Régime d'INCERTITUDE | régime unique : indétermination qui organise la conduite des **acteurs** ; l'incertitude de l'analyste n'ancre pas (cards.md) |
| 5 | Statut multi-valué | R11 : une valeur, calculée ; « Performatif » supprimé |
| 6 | « 3 positions max » | notation.md : 1 à 4 cartes, une syntaxe par mode |
| 7 | Ambiguïté de parsing | **traité autrement** : chaîne condensée S+O+M supprimée ; séparateurs à sens unique `+ / ⇒` ; nom de carte canonique |
| 8 | Mode 4 absent de SKILL.md | inscrit (étape 6) |
| 9 | Mode 4 sans déclencheur (Ex. 3) | R10 : deux déclencheurs seulement ; exemple 3 sans Mode 4 |
| 10 | Items Brown exacts | champ dans chaque fiche ; 11 documentées, 3 partielles, 2 à établir |
| 11 | Branches mathématiques | SEUIL (hystérésis, absorption), HIÉRARCHIE (ordres partiels, Landau), RÉCURSIVITÉ (auto-référence seule), TRACE (dépendance au chemin), PROPORTION (sans nombre d'or), COMMUNAUTÉ (biens publics, coalitions, Ostrom), RÉCIPROCITÉ (jeux répétés non coopératifs — oubli de l'audit) |
| 12 | Antagonismes contestables | **2** incompatibilités retenues (et non 4 : l'audit gardait INC↮ÉMER qu'il critiquait) ; 7 tensions documentées ; fréquences recalculées |
| 13 | Démonstration → test | protocole de test réel (test_log §3) ; doublons signalés ; **non exécuté** |
| 14 | Invalidation de l'anti-résonance | R3 + R4 : trois niveaux, quatre portées, effet sur le niveau ; exemples 3 et 4 |
| 15 | Cas nul | R9 + exemple 5 ; structure hors corpus + exemple 6 |
| 16 | Journaux vides | conservés vides et déclarés comme tels ; aucune donnée fabriquée |
| 17 | Glyphes confondables | notation.md §4 ; validation par nom de carte |
| 18 | Vocabulaire | « remarquable » ; Performatif supprimé ; « non séquentiel » ; prévision renvoyée à prediction-engine |
| 19 | Chargement, source unique, déclencheurs négatifs | SKILL.md |
| 20 | Noms d'entités, « autonome » | skills cités par leur nom réel ; autonomie restreinte à la lecture structurelle |

### Points non relevés par l'audit, traités

- **Non-conformité STÈLE** : 8 glyphes de carte sont des opératives ou des modales en STÈLE ; les
  chaînes v0.3.1 étaient illégales en STÈLE. La signature devient une notation propre ; l'export
  STÈLE passe par le skill `stele`.
- **Position d'absence en Mode 2** (test_log 10) : interdite (R6).
- **Statut non calculé** : calculé (R11).
- **Tirage « aléatoire » non tracé** : ligne de journal obligatoire (R1).
- **Contre-exemple hors situation** (test_log 05) : n'est pas une anti-résonance (R4).
- **INCERTITUDE en position *manque* alors que présente** (test_log 06) : erreur de position (R7).

### Décisions

- **Configuration 4 supprimée** : 0 constellation sur 560 avec la table v0.4.
- **SEUIL et TRANSFORMATION deviennent compatibles** : SEUIL est défini par l'irréversibilité, non
  par la soudaineté ; une transformation peut franchir un seuil.
- **RÉCIPROCITÉ** : la symétrie porte sur l'obligation, pas sur les statuts.
- **Mode 2 + carte listée** quand trois structures sont présentes sans absence active (limite
  documentée, R5).

### Limitations connues

- Aucune donnée empirique. Les exemples et démonstrations sont construits.
- Deux cartes sans ancrage anthropologique (ÉMERGENCE, TRANSFORMATION), trois partielles.
- Deux lacunes connues du corpus : rétroaction simple, auto-similarité.
- Les citations de `cards.md` reprises dans `antagonismes.md` §3 doivent être revérifiées à chaque
  modification de `cards.md` ; `nexus_tool.py lint` vérifie la structure des fiches, pas le sens.

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

