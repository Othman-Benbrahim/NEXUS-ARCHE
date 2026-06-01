# NEXUS-ARCHÊ — Protocole de Tirage

---

## PRINCIPE FONDAMENTAL

Le tirage NEXUS-ARCHÊ est **résonant, non narratif**.

Les cartes ne racontent pas une histoire dans le temps.
Elles décrivent **simultanément** les structures actives d'une situation.

**Question de base** : *Quelles structures organisent ce qui est en train de se passer ?*

---

## MODALITÉ DU TIRAGE

Avant de choisir un mode (1, 2 ou 3), choisir la modalité :

### Tirage aléatoire

Sélection d'une ou plusieurs cartes parmi les 16 par procédé aléatoire (simulation numérique, dé à 16 faces, tirage au sort physique).

**Usage recommandé** : provoquer la surprise structurelle — faire apparaître une structure que l'analyste n'aurait pas spontanément identifiée. Contre-biais : il force à tester une hypothèse structurelle non anticipée.

**Contrainte** : la carte tirée doit toujours passer le test d'ancrage observable. Si aucun ancrage n'est trouvable, la carte est déclarée inactive et le tirage est renouvelé.

### Tirage délibératif

Identification directe de la ou des cartes qui résonnent le plus avec la situation, après lecture du corpus des 16 cartes.

**Usage recommandé** : confirmer une intuition structurelle, approfondir une analyse en cours, ou lorsqu'une structure évidente mérite d'être nommée précisément avant d'en explorer les tensions.

**Contrainte** : le biais de confirmation est plus fort dans ce mode. Le test d'anti-résonance est obligatoire et doit être particulièrement exigeant.

### Activation par LLM

Lorsque NEXUS-ARCHÊ est activé par un modèle de langage sur une situation décrite :

1. Lire la description de la situation
2. Identifier 2 à 3 cartes candidates (ne pas en retenir plus de 3 au premier passage)
3. Appliquer le test d'ancrage observable à chaque candidate : nommer une observation concrète dans la situation décrite
4. Écarter toute carte sans ancrage vérifiable
5. Retenir uniquement les cartes ancrables et les présenter à l'utilisateur
6. Appliquer les étapes restantes du protocole de rigueur

---

## LES TROIS MODES DE TIRAGE

### Mode 1 — Tirage Simple (1 carte)

Tirer une carte. Une structure dominante.

Utiliser la **Question IRIS** de la carte comme point d'entrée.
Le **glyphe STÈLE** comme ancre symbolique.

Usage : quand la situation semble confuse — pour nommer sa structure profonde.

**Chaîne STÈLE produite** : 1 glyphe en position substance. Extensible avec une opérative et une modale si la lecture le justifie. Voir `references/stele_rules.md`.

---

### Mode 2 — Tirage de Tension (2 cartes)

Tirer deux cartes simultanément.

Les deux cartes ne se lisent pas en séquence — elles se lisent **en tension**.

Question centrale : *Quelle est la relation structurelle entre ces deux patterns ?*

- Sont-ils en conflit ?
- L'un contient-il l'autre ?
- L'un est-il invisible dans la situation ?

Formuler la relation en termes structurels précis, pas en métaphore.

**Chaîne STÈLE produite** : 2 glyphes en position substance, séparés par un point. Exemple : `✦⊘` → `AXE.NÉGATION`

---

### Mode 3 — Tirage de Constellation (3 cartes)

Tirer trois cartes. Trois plans structurels **simultanés**, non temporels :

| Position | Question |
|---|---|
| **Ce qui tient** | La structure stable, le fond actif |
| **Ce qui bouge** | La structure en transit |
| **Ce qui manque** | La structure absente, la lacune active |

La chaîne STÈLE des trois glyphes forme la **signature compressée** de la situation.

**Chaîne STÈLE produite** : syntaxe positionnelle tient.bouge.manque. Exemple : `⊗⥀⊛` → `LIER.INVERSER.NOEUD`

#### Configurations pathologiques du Mode 3

Certaines configurations de constellation signalent une situation structurellement bloquée ou sous tension extrême. Les reconnaître est aussi informatif qu'une lecture ordinaire.

**Configuration 1 — Miroir (Ce qui tient = Ce qui manque)**
La structure stable est identique à la structure absente. Signal : la situation est définie par une contradiction fondamentale non résolue — ce qui tient est ce qui manque.
→ *Lecture recommandée* : nommer la contradiction explicitement. Appliquer la Question IRIS des deux positions à la même carte. La tension elle-même est l'information.

**Configuration 2 — Immobilité structurelle (Ce qui bouge ≈ Ce qui tient)**
La structure en transit est de même nature que la structure stable. Signal : le mouvement perçu est illusoire — ce qui semble changer reproduit ce qui est stable.
→ *Lecture recommandée* : chercher la source de l'illusion de mouvement. Appliquer le test d'anti-résonance renforcé sur la carte en position "Ce qui bouge".

**Configuration 3 — Lacune active contradictoire (Ce qui manque contredit directement Ce qui tient)**
La structure absente est structurellement incompatible avec la structure stable. Signal : la situation ne peut évoluer sans d'abord déstabiliser ce qui la tient.
→ *Lecture recommandée* : formuler explicitement la contradiction. Activer optionnellement le Mode 4 (ci-dessous).

**Configuration 4 — Tension maximale (les 3 cartes appartiennent à des registres antagonistes)**
Signal rare mais fort : la situation est organisée par plusieurs structures incompatibles simultanées.
→ *Lecture recommandée* : ne pas chercher à résoudre prématurément. Documenter la tension comme elle est. Activer le Mode 4.

---

### Mode 4 — Tirage de Résolution (optionnel)

**Usage** : après un Mode 2 ou Mode 3 ayant produit une tension non résolue ou une configuration pathologique identifiée.

**Procédure** : tirer une carte supplémentaire, posée directement sur la tension identifiée.

**Question** : *Quelle structure permettrait de tenir la tension sans l'effacer ?*

Ce n'est pas une résolution — c'est une structure de tenue. La carte de résolution ne supprime pas la tension ; elle nomme le registre depuis lequel la tension devient habitable.

**Chaîne STÈLE produite** : la chaîne du Mode 2 ou 3 + le glyphe de résolution en position finale, précédé d'un tiret. Exemple : `✦⊘-⊙` → `AXE.NÉGATION - SOURCE`

---

## PROTOCOLE DE RIGUEUR

4 exigences applicables à tout tirage, dans cet ordre.

### 1. Ancrage observable

Avant d'interpréter une carte, nommer **une observation concrète** dans la situation réelle qui correspond à cette structure.

Pas « je sens que RÉSEAU est actif ».
Mais : « le réseau de liens que j'identifie concrètement est... »

> Si on ne trouve pas d'ancrage observable, la carte n'est pas active dans cette lecture. Elle est déclarée inactive et documentée comme telle.

---

### 2. Test d'anti-résonance

Pour chaque carte tirée, poser la question inverse :

*Qu'est-ce qui, dans la situation, **contredit** cette structure ?*

Si rien ne contredit → soit la carte est parfaitement juste, soit il y a biais de confirmation.
Forcer cette question avant de conclure.

> Ce test est le seul mécanisme qui distingue NEXUS-ARCHÊ d'un système projectif ordinaire.

---

### 3. Énoncé structurel de tension

Si plusieurs cartes sont tirées, la relation entre elles doit être formulée en termes **structurels précis**.

Exemple correct :
> « RÉSEAU et CONTRAINTE sont en tension : les liens existants bloquent le mouvement possible. »

Exemple à éviter :
> « Quelque chose entrave quelque chose d'autre. »

---

### 4. Chaîne STÈLE syntaxiquement valide

La compression finale suit les règles grammaticales de STÈLE définies dans `references/stele_rules.md`.

Toujours fournir la **transcription verbale** (mots-codes séparés par des points).

Exemple : `⊥∿◐` → `LIMITE.MOUVEMENT.CONDITIONNEL`

> La validité syntaxique est le seul critère formel objectif du système.

---

## STATUT ÉPISTÉMIQUE

À déclarer en fin de toute lecture :

| Statut | Signification |
|---|---|
| **Descriptif** | La lecture décrit une structure observée et ancrée dans des faits vérifiables |
| **Spéculatif** | La lecture propose une configuration possible non encore confirmée |
| **Performatif** | La lecture agit sur la façon d'habiter la situation — elle produit un effet en étant formulée |

---

## LIMITES

NEXUS-ARCHÊ identifie des structures. Il ne prédit pas, ne prescrit pas, ne diagnostique pas.
Une lecture ne vaut que si elle est testée contre l'observable.
Une carte sans ancrage est une carte inactive — elle ne disparaît pas, elle attend une situation qui lui corresponde.
