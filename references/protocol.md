# NEXUS-ARCHÊ — Protocole

> Version : 0.4.1
>
> **Source de vérité des règles** (R1–R12). `SKILL.md` donne l'ordre des étapes et renvoie ici ;
> aucun autre fichier ne redéfinit une règle. `examples.md`, `test_log.md` et `prompt_guide.md`
> les appliquent ; `scripts/nexus_tool.py lint` vérifie une partie de cette application.

---

## Principe

La lecture est **simultanée, non séquentielle** : les cartes décrivent des structures actives en
même temps, pas les étapes d'une histoire. Rien n'interdit de *raconter* une lecture ; ce qui est
interdit, c'est de lire les positions comme un avant / après.

Question de base : *quelles structures du corpus organisent ce qui se passe — s'il y en a ?*
Le « s'il y en a » est constitutif : le résultat nul (R9) est une issue normale, et les 16 cartes
ne prétendent pas couvrir toutes les structures possibles.

---

## R1 — Modalité du tirage

| Modalité | Quand | Exigence |
|---|---|---|
| **Délibérative** (par défaut) | toujours disponible | inclure au moins une **contre-candidate** : une voisine documentée de la carte favorite (`cards.md`, « À ne pas confondre avec »), testée comme les autres |
| **Aléatoire** | si un générateur réel est disponible | `python3 scripts/nexus_tool.py draw -n <1..3>` ou tirage physique fait par l'utilisateur ; la **ligne de journal** produite est recopiée dans la lecture |

- Le tirage aléatoire est **sans remise** : une carte ne sort qu'une fois par lecture, retirages
  compris.
- Un modèle de langage ne simule jamais un tirage « au hasard » de tête. Sans générateur réel, la
  modalité aléatoire est impossible : le dire, et passer en délibératif.
- **Le tirage choisit les cartes, pas les positions.** En Mode 3, l'ordre de sortie ne vaut pas
  position : les positions sont attribuées après ancrage, selon R7 (une présente stable Fort →
  *tient*, une présente en recomposition → *bouge*, une absente aux effets observables → *manque*).
  Si aucune attribution ne satisfait R7, on applique le repli de R5.
- **Retirage** : une carte tirée d'ancrage Nul est déclarée **inactive** et reste dans la lecture.
  Elle peut être remplacée par un retirage d'**une** carte, parmi les cartes non encore sorties :
  `draw -n 1 --exclude "<cartes déjà sorties>"`. Au plus **deux** retirages par lecture, chacun
  journalisé. Au-delà, la lecture se fait avec les cartes ancrées obtenues, ou conclut à ∅.
  (Sans cette limite, le retirage converge vers ce que l'analyste attendait.)
- Option reproductible pour audit : `draw --seed "<texte de la situation>"`.

---

## R2 — Ancrage : ce qui compte comme fait

Un **ancrage** est un fait de la situation qui remplit un **marqueur observable** de la carte
(`cards.md`). Est un fait : un acte, un document, un événement daté, une mesure, un comportement
décrit avec précision — quelque chose qu'un tiers présent aurait pu constater. Un discours compte
comme fait **sur le discours** (qui a dit quoi), pas comme preuve de ce qu'il affirme.

- **Un ressenti n'est jamais un ancrage**, qu'il soit individuel (« je me sens seul ») ou collectif
  (« ils se sentent redevables »). C'est un fait sur l'état de la personne, pas sur la structure.
  Il peut accompagner un fait ; il ne le remplace pas.
- Une déclaration d'ignorance (« je ne sais pas ») n'ancre pas INCERTITUDE. Il faut une conduite
  organisée par l'indétermination (voir la carte).
- **Coïncidence lexicale** : quand le nom de la carte figure dans la description (« plan de
  transformation », « mon réseau »), le mot ne compte pas comme fait et l'anti-résonance est
  obligatoirement cherchée du côté de la carte voisine.
- Les faits rapportés par l'auteur sont admis tels que rapportés ; un fait vague (sans date, sans
  nombre, sans acteur identifiable) ne dépasse pas le niveau Faible (R3).

---

## R3 — Niveaux d'ancrage

| Niveau | Condition |
|---|---|
| **Fort** | au moins un fait précis remplit un marqueur, **et** pour **chaque voisine documentée** de la carte, la question discriminante est passée (voir ci-dessous) |
| **Faible** | un fait remplit un marqueur, mais il est vague, ou au moins une voisine n'est pas tranchée |
| **Nul** | aucun fait : reformulation, ressenti, vocabulaire → carte **inactive** |

**Voisines documentées** : la liste fermée « À ne pas confondre avec » de la carte dans `cards.md`
(2 à 5 cartes selon la carte). Pour chacune, une ligne, avec l'un de quatre verdicts :

| Verdict | Sens |
|---|---|
| `→` | la question discriminante tranche pour cette carte : le fait d'ancrage n'est pas mieux expliqué par la voisine |
| `+` | la voisine est **aussi** présente, ancrée par d'autres faits ; les deux sont retenues (cas des paires compatibles) |
| `?` | la question ne tranche pas → la carte ne dépasse pas Faible |
| `←` | la question tranche pour la **voisine** : le fait relève d'elle et ne compte pas comme ancrage de cette carte (si c'était son seul fait, la carte est Nul) |

Format dans une lecture :
`R3 · ÉMERGENCE : TRANSFORMATION → (aucune entité préexistante) ; RÉCURSIVITÉ → (…) ; …`
La justification entre parenthèses est obligatoire. Une ligne R3 qui omet une voisine n'établit
pas le niveau Fort (contrôlé par `nexus_tool.py lint` sur les fichiers du corpus).

---

## R4 — Anti-résonance : un test qui peut rejeter

Pour chaque carte d'ancrage Fort ou Faible : chercher **activement** la contre-observation la plus
forte (un fait **de la situation** qui contredit la structure, ou une autre carte qui explique
aussi bien les faits d'ancrage). Un contre-exemple pris hors de la situation n'est pas une
anti-résonance. Puis classer sa **portée** :

| Portée | Critère | Effet |
|---|---|---|
| **Marginale** | exception, épisode isolé, sous-ensemble minoritaire | niveau inchangé ; nuance notée |
| **Substantielle** | part importante de l'objet, **ou** mécanisme concurrent qui rend compte des faits d'ancrage aussi bien | niveau **baisse d'un cran** (Fort → Faible ; Faible → Nul = rejet) |
| **Dominante** | touche le cœur de l'objet, **ou** les faits d'ancrage relèvent manifestement d'une autre carte | **rejet** |
| **Aucune trouvée** | dire où l'on a cherché | niveau inchangé ; statut plafonné à **Spéculatif** (R11) |

Une lecture où toutes les contre-observations sont « marginales » doit le justifier pour chacune.
Le rejet par anti-résonance est un résultat attendu, pas un échec (voir `examples.md`, exemple 4).

---

## R5 — Choix du mode

Le mode découle des **cartes ancrées** après R3–R4 (niveau Fort ou Faible), pas d'une préférence
ni de la longueur de la notation.

| Cartes ancrées | Mode |
|---|---|
| 0 | **résultat nul** (R9) |
| 1 | Mode 1 |
| 2 | Mode 2 |
| 3 ou plus | **Mode 3 si** trois d'entre elles remplissent les positions de R7 (*tient* présente et Fort ; *bouge* présente ; *manque* absente aux effets observables). Choisir les trois par niveau, puis par nombre de faits indépendants. **Sinon** : Mode 2 sur les deux cartes les plus fortes. Dans les deux cas, les autres cartes ancrées sont listées « ancrées non retenues ». |

Si l'utilisateur demande un mode exigeant plus de cartes qu'il n'y en a d'ancrées, le dire et
livrer le mode atteint. On ne complète jamais une constellation avec une carte sans ancrage.

Conséquence connue : trois structures **présentes** ou plus, sans aucune absence active, se lisent
en Mode 2 + liste (`test_log.md`, situation 06).

---

## R6 — Mode 2 : énoncé et relation

Formuler la relation entre les deux structures en termes structurels (qui agit sur quoi, par quel
mécanisme), pas en métaphore. Qualifier la relation par **un** des types suivants :

| Relation | Critère observable |
|---|---|
| **Renforcement mutuel** | chaque structure produit des faits qui ancrent l'autre |
| **Conflit** | les faits de l'une entravent ceux de l'autre sur le même objet |
| **Inclusion** | l'une est un cas ou une partie de l'autre (`antagonismes.md` §4bis) |
| **Appui** | les faits de l'une fournissent un élément constitutif de l'autre (par exemple l'invariant d'une transformation), sans réciprocité |
| **Reproduction** | (a) **production** : chaque fait d'ancrage de B est déclenché par une occurrence de A (datation, séquence documentée) ; **et** (b) **reproduction** : après ce fait, l'effet décrit dans l'ancrage de A est de nouveau observé. Les deux conjoints sont vérifiés par des faits, sans contre-factuel. |
| **Indépendance** | les deux structures portent sur des objets distincts, nommés |
| **Tension documentée** | la paire figure dans `antagonismes.md` §4 |

- Si A et B forment une paire **incompatible** (`antagonismes.md` §3), la seule relation admise est
  **indépendance**, avec les deux objets nommés. Sinon, l'un des deux ancrages est erroné : revenir
  à R3–R4.
- Le Mode 2 n'a pas de position d'absence : une structure absente se lit en Mode 3, position *manque*.

---

## R7 — Mode 3 : positions

| Position | Contenu | Exigence d'ancrage |
|---|---|---|
| **tient** | structure présente et stable sur laquelle repose la situation | **Fort** |
| **bouge** | structure présente, en cours de recomposition | Fort ou Faible |
| **manque** | structure **absente** dont l'absence a des effets observables | Fort ou Faible ; l'ancrage porte sur un **effet** de l'absence |

Une absence s'ancre par ses effets (« aucun pont entre les deux groupes : les décisions de l'un
sont apprises par l'autre en assemblée »). Ne sont pas des effets : le constat de l'absence lui-même
(« rien de nouveau n'est apparu »), ni un discours sur la situation. Une carte présente ne peut pas
occuper *manque*.

---

## R8 — Mode 3 : configurations remarquables

« Remarquable » remplace « pathologique » (v0.3.1). Chaque configuration est une **hypothèse**
signalée à l'auteur, jamais un verdict. Une configuration confirmée ouvre le Mode 4 (R10).

| Config | Condition vérifiable | Ce qu'elle signale | Question à l'auteur |
|---|---|---|---|
| **Scission** (ex-« Miroir ») | la même carte en *tient* et *manque*, ancrée sur **deux objets nommés** : présente pour l'un, absente pour l'autre. Délibératif seulement. | la structure existe dans la situation mais n'atteint pas l'objet où elle manque | qu'est-ce qui empêche la structure de passer d'un objet à l'autre ? |
| **Reproduction** | *tient* (A) et *bouge* (B) sont en relation de **reproduction** (R6, conjoints a et b) | le mouvement observé est produit par la structure stable et la reconduit : il ne la modifie pas | ce qui change a-t-il déjà changé de cette façon lors d'un cycle précédent ? |
| **Lacune contradictoire** | *tient* et *manque* forment une paire **incompatible** (`antagonismes.md` §3) **et** portent sur le même objet (§6) | la structure absente ne peut pas apparaître sur cet objet sans déplacer celle qui tient | êtes-vous prêt à perdre ce qui tient pour obtenir ce qui manque ? |

« Miroir » est renommé : depuis v0.4, la configuration ne désigne plus une contradiction mais une
**localisation** (même structure, deux objets). L'ancienne configuration 4 (« tension maximale »)
est supprimée : elle est inatteignable avec la table d'incompatibilités v0.4
(`antagonismes.md` §5).

---

## R9 — Résultat nul et structure hors corpus

**Résultat nul** : aucune carte n'atteint Faible après R2–R4. On le déclare :

```
Signature : ∅
Aucune des 16 structures n'est ancrée dans la description.
Faits disponibles : [ce qui est effectivement observable]
Ce qui permettrait un ancrage : [faits manquants, sous forme de questions précises]
```

Le résultat nul n'est pas un refus d'aider : il dit ce que la description ne permet pas d'affirmer,
et quelles informations le permettraient.

**Structure hors corpus** : un motif clair organise la situation mais aucune carte ne le décrit
(rétroaction simple, auto-similarité, dépendance à une ressource unique…). Le nommer en clair,
**sans** le rabattre sur la carte la plus proche, et le noter au journal de `calibration.md` §4.

---

## R10 — Mode 4 : carte de tenue

**Déclencheurs** (l'un des deux, pas d'autre) :
- une configuration de R8, ou une relation de **reproduction** en Mode 2 (R6), **confirmée** par
  l'auteur ;
- une demande explicite de l'utilisateur après un Mode 2 ou 3.

**Question** : *quelle structure, déjà disponible dans la situation, permettrait de tenir la tension
sans l'effacer ?*

La carte de tenue doit être ancrée comme les autres : un fait montre que cette structure **existe
déjà** dans la situation, au moins en germe. Sans ancrage, la proposer comme hypothèse, statut
Spéculatif. Ce n'est pas une prescription : la lecture nomme une ressource, elle ne dit pas quoi
faire.

---

## R11 — Statut épistémique (calculé, une seule valeur)

| Statut | Condition |
|---|---|
| **Descriptif** | toutes les cartes retenues sont **Fort** (R3 complet), au moins une contre-observation a été trouvée et classée pour chacune, et toute configuration ou relation de reproduction signalée a été confirmée par l'auteur |
| **Spéculatif** | dans tous les autres cas |
| **Nul** | résultat nul (R9) |

Le statut « Performatif » de la v0.3.1 est supprimé : il réintroduisait une fonction prescriptive
que le skill exclut.

---

## R12 — Limites

NEXUS-ARCHÊ identifie des structures. Il **ne prescrit pas** et **ne diagnostique pas** (ni
psychologiquement, ni médicalement).
Il **ne prévoit pas** : une lecture peut suggérer des hypothèses, mais toute affirmation sur
l'avenir (« ce type de situation évolue généralement vers… ») est hors protocole. Pour la
transformer en prévision scorable, la confier à `prediction-engine` ou `osint-intel`.
Les 16 cartes ne sont pas une liste complète des structures possibles (R9).
