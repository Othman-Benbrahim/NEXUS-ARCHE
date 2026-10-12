# NEXUS-ARCHÊ — Exemples annotés

> Version : 0.4.2
>
> Six lectures qui appliquent les règles R1–R12 de `protocol.md`, y compris R3 : chaque carte
> retenue au niveau Fort porte une ligne `R3 ·` qui passe **toutes** ses voisines documentées
> (contrôlé par `nexus_tool.py lint`).
> Ce sont des **cas construits** à des fins d'illustration, pas des données de test
> (voir `test_log.md`). Les lignes de tirage de l'exemple 2 sont, elles, réelles.

| # | Ce qu'il montre | Issue |
|---|---|---|
| 1 | Mode 1 délibératif, contre-candidate, R3 complet | Descriptif |
| 2 | Tirage aléatoire réel, deux retirages, verdict `←` | ∅ (modalité aléatoire) |
| 3 | Mode 3, rétrogradation par anti-résonance, configurations non établies | Spéculatif |
| 4 | Rejet par anti-résonance, coïncidence lexicale, verdict `+` | Mode 2, Spéculatif |
| 5 | Situation sans faits, puis avec faits | ∅, puis Mode 1 |
| 6 | Motif multi-échelle : qualificatif plutôt que carte ou « hors corpus » (R13) ; puis vrai hors-corpus | Mode 1 qualifié |

---

## Exemple 1 — Mode 1, délibératif

**Situation** : un collectif d'une vingtaine de personnes organise un festival depuis 2024. Trois
sous-groupes (logistique, programmation, communication) se sont formés sans vote ni désignation.
En février, une membre a commencé à rédiger un compte rendu après chaque réunion ; depuis avril,
tous les sous-groupes utilisent son format. La fondatrice a recruté les dix premiers membres.

**Candidates** : ÉMERGENCE (favorite) ; TRANSFORMATION (contre-candidate, voisine documentée
d'ÉMERGENCE) ; HIÉRARCHIE (la fondatrice).

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| ÉMERGENCE | format de compte rendu apparu en février, adopté par imitation en avril, sans consigne ; sous-groupes formés sans vote | Fort | la fondatrice a recruté les dix premiers — mais ni les sous-groupes ni le format ne viennent d'elle (marginale) | Fort |
| TRANSFORMATION | aucune entité préexistante qui change de forme : le collectif est né avec ses pratiques | Nul | — | inactive |
| HIÉRARCHIE | un recrutement initial ne fait pas un ordre de validation : aucun fait de « qui peut dire non à qui » | Nul | — | inactive |

R3 · ÉMERGENCE : TRANSFORMATION → (rien ne préexistait qui changerait de forme) ; RÉCURSIVITÉ → (aucune représentation du collectif par lui-même ne règle ces pratiques) ; CROISSANCE → (aucune grandeur suivie dans le temps) ; INCERTITUDE → (une régularité est apparue, aucun possible n'est en suspens)

**Lecture** — *qu'est-ce qui s'est installé sans que personne ne le décide, et qui le défend
désormais ?* Le format de compte rendu et la division en trois sous-groupes. La question à poser
au collectif : ces conventions ont-elles aujourd'hui des gardiens, ou tiennent-elles par simple
habitude partagée ?

**Signature** : `ÉMERGENCE` · `⊙`
**Statut** : Descriptif — ancrage Fort avec R3 complet, contre-observation trouvée et classée.

---

## Exemple 2 — Tirage aléatoire réel, conclu à ∅

**Situation** : une équipe de huit personnes, dans une administration, veut lancer des projets
innovants. Toute initiative doit être validée par le chef de service, puis la sous-direction,
puis la direction ; en 2025, quatre projets sur cinq ont été arrêtés entre la sous-direction et la
direction. Le périmètre de l'équipe est fixé par fiche de poste ; l'élargir prend six à huit
semaines. Deux managers intermédiaires relaient activement les projets.

**Tirage** (R1) — tirage initial, puis deux retirages d'une carte chacun, parmi les cartes non sorties :

```
TIRAGE 2026-10-12T02:57:19Z · secrets · sans remise · PÉRIODICITÉ | PROPORTION
TIRAGE 2026-10-12T02:57:25Z · secrets · sans remise · exclues : PÉRIODICITÉ, PROPORTION · POLARITÉ
TIRAGE 2026-10-12T02:57:27Z · secrets · sans remise · exclues : PÉRIODICITÉ, PROPORTION, POLARITÉ · TRACE·MÉMOIRE
```

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| PÉRIODICITÉ | une seule année décrite : aucune occurrence répétée datée | Nul | — | inactive |
| PROPORTION | « 4 projets sur 5 arrêtés » est un rapport — mais voir R3 | Nul | — | inactive |
| POLARITÉ (retirage 1) | aucun champ à deux pôles ni de camps déclarés | Nul | — | inactive |
| TRACE·MÉMOIRE (retirage 2) | le périmètre par fiche de poste n'a pas d'origine datée ni d'indice qu'il ne serait plus choisi aujourd'hui | Nul | — | inactive |

R3 · PROPORTION : HIÉRARCHIE ← (le rapport 4/5 mesure l'effet de la chaîne de validation : il relève d'un ordre de préséance, pas d'un rapport entre parties) ; CROISSANCE → (aucune grandeur suivie dans le temps)

Le seul fait de PROPORTION relève de sa voisine (`←`) : la carte est Nul (R3).

```
Signature : ∅ (modalité aléatoire, deux retirages épuisés)
Aucune des cartes tirées n'est ancrée.
```
**Statut** : Nul.

**Ce que l'exemple montre** : HIÉRARCHIE et CONTRAINTE, les cartes évidentes ici, ne sont pas
sorties. Le tirage aléatoire n'est pas fait pour retrouver l'évident : il force à tester des
structures non pressenties, et il peut ne rien trouver. La limite de deux retirages empêche de tirer
jusqu'à ce que l'attendu sorte. La v0.3.1 présentait un tirage « aléatoire » tombant pile sur les
deux cartes attendues (une chance sur 120) : c'est le signe d'un tirage simulé. La lecture
délibérative de la même situation est la démonstration 02 de `test_log.md`.

---

## Exemple 3 — Mode 3, avec rétrogradation

**Situation** : association culturelle régionale, 60 membres. Depuis 2019, les cinq fondateurs
votent en bloc au conseil d'administration et se remplacent les uns les autres aux permanences ;
deux d'entre eux ont avancé des fonds en 2023, remboursés par les trois autres. Pour l'assemblée
générale de novembre, deux listes concurrentes se sont déclarées : « continuité » et « renouveau ».
Aucun membre ne siège à la fois dans la commission programmation (fondateurs) et dans la commission
jeunes (renouveau) ; les décisions de l'une sont apprises par l'autre en assemblée. Une vingtaine de
membres n'ont rejoint aucune liste. Un groupe de travail mixte a existé en 2024, puis s'est dissous.

**Candidates** : RÉCIPROCITÉ, POLARITÉ, RÉSEAU ; COMMUNAUTÉ (contre-candidate, voisine de RÉCIPROCITÉ).

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| RÉCIPROCITÉ | votes en bloc, remplacements mutuels, avances de fonds remboursées entre fondateurs | Fort | plusieurs fondateurs disent le projet initial épuisé — une opinion, pas un arrêt des échanges (marginale) | Fort |
| POLARITÉ | deux listes déclarées, dont les noms s'opposent | Fort | 20 membres sur 60 n'ont rejoint aucune liste : un tiers hors des deux pôles (**substantielle**) | **Faible** |
| RÉSEAU (absent) | aucun membre commun aux deux commissions ; décisions apprises en assemblée (effet observable de l'absence) | Fort | groupe mixte en 2024, dissous (marginale : passé) | Fort |
| COMMUNAUTÉ | bien commun nommé (le festival) ; règles d'adhésion | Faible | les deux camps ne contribuent plus ensemble à la programmation 2026 (**dominante** : le cœur du bien commun n'est plus coproduit) | **rejetée** |

R3 · RÉCIPROCITÉ : COMMUNAUTÉ → (les faits sont des transferts entre personnes identifiées, pas des contributions à un bien commun) ; HIÉRARCHIE → (aucun fondateur ne valide les décisions des autres) ; RÉSEAU → (ce qui est documenté est l'équilibre des transferts, pas la topologie) ; RÉSONANCE → (des dettes et des remboursements, pas un alignement de rythmes)

R3 · POLARITÉ : CONTRAINTE → (aucune règle n'impose les camps) ; SEUIL → (les deux camps coexistent, aucun passage irréversible)

R3 · RÉSEAU : COMMUNAUTÉ → (l'effet porte sur l'absence de chemin entre deux commissions, pas sur un bien commun) ; HIÉRARCHIE → (aucun rang n'est en jeu dans cette absence) ; RÉCIPROCITÉ → (ce qui manque est le lien lui-même, pas l'équilibre de ce qui y circulerait)

**Positions (R7)** : *tient* = RÉCIPROCITÉ (présente, Fort) ; *bouge* = POLARITÉ (présente, Faible) ;
*manque* = RÉSEAU (absente, effet observable).

**Configurations (R8)** :
- Scission : non (trois cartes distinctes).
- Reproduction : conjoint (a) non établi — la situation ne date pas la déclaration des listes par
  rapport à un vote en bloc ; on ne peut pas montrer qu'une occurrence de RÉCIPROCITÉ a déclenché
  les faits de POLARITÉ. Non signalée.
- Lacune contradictoire : RÉCIPROCITÉ / RÉSEAU n'est pas une paire incompatible. Non.

Aucune configuration → **pas de Mode 4**. (La v0.3.1 en recommandait un sans déclencheur.)

**Lecture** : la boucle d'obligations entre fondateurs tient l'association ; une polarisation se
recompose, mais un tiers des membres reste hors des deux pôles ; l'absence de lien entre les deux
commissions fait que chaque camp découvre les décisions de l'autre en assemblée, là où elles ont
le moins de chance d'être discutées.

**Signature** : `RÉCIPROCITÉ / POLARITÉ / RÉSEAU` · `⊗ / ⥀ / ⊛`
**Statut** : Spéculatif — POLARITÉ n'est que Faible.
**À vérifier auprès de vous** : les vingt membres sans liste sont-ils en attente, ou constituent-ils
un troisième groupe ? Les listes se sont-elles déclarées après un vote en bloc précis ?

---

## Exemple 4 — Rejet par anti-résonance

**Situation** : le dirigeant d'une PME parle de « notre croissance ». Effectif : 12 salariés en
janvier 2024, 18 en janvier 2025, 31 en juin 2025. En mars 2025, la PME a absorbé un concurrent et
repris ses 13 salariés. L'intégration est en cours : nouveaux process communs, même nom, mêmes
fondateurs à la direction.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| CROISSANCE | trois mesures datées d'effectif | Fort | 13 des 19 salariés supplémentaires depuis janvier 2024 viennent d'**un seul événement** (la fusion) : pas un taux qui dépend de la taille. Les faits d'ancrage relèvent d'un autre mécanisme (**dominante**). Coïncidence lexicale « croissance » (R2) | **rejetée** |
| SEUIL | absorption juridique du concurrent, sans retour possible | Fort | aucune trouvée (le contrat est définitif) | Fort |
| TRANSFORMATION (contre-candidate) | process en cours d'unification ; nom et direction conservés (invariant) | Fort | une partie des équipes absorbées garde ses outils (marginale) | Fort |

R3 · SEUIL : TRANSFORMATION + (ancrée par d'autres faits : l'unification des process) ; CONTRAINTE → (il y a passage effectif à un nouvel état, deux sociétés en une) ; POLARITÉ → (aucun champ à deux pôles) ; TRACE·MÉMOIRE → (ce qui organise est la fermeture du retour, pas un passé ancien qui oriente les conduites)

R3 · TRANSFORMATION : SEUIL + (ancrée par l'absorption juridique) ; CROISSANCE → (changement de forme, pas de degré : la croissance est rejetée) ; ÉMERGENCE → (l'entité préexistait : même nom, même direction) ; TRACE·MÉMOIRE → (l'unification est en cours, on n'est pas dans ce qui en reste)

**Mode 2 (R6)** — relation : tension documentée SEUIL ~ TRANSFORMATION (`antagonismes.md` §4).
La fusion a passé son point de non-retour ; l'entreprise change de forme en conservant son nom et
sa direction. Ce qui est à l'œuvre n'est pas une dynamique d'amplification, mais une transformation
qui suit un seuil franchi.

**Signature** : `SEUIL + TRANSFORMATION` · `⊥ + ∿`
**Statut** : Spéculatif — pas de contre-observation trouvée pour SEUIL (R4 : plafond).

---

## Exemple 5 — Résultat nul, puis lecture

**Première description** : « Je me sens seul et déconnecté des autres en ce moment. »

Étape 0 (recevabilité) : aucun fait. Si l'utilisateur insiste pour une lecture :

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| RÉSEAU | « déconnecté » est un ressenti, pas une topologie (R2) | Nul | — | inactive |
| INCERTITUDE | aucune conduite organisée par l'indétermination | Nul | — | inactive |

```
Signature : ∅
Aucune des 16 structures n'est ancrée dans la description.
Faits disponibles : aucun — un ressenti.
Ce qui permettrait un ancrage : qu'est-ce qui a changé récemment (lieu, travail, relations) ?
Avec qui êtes-vous encore en contact régulier, et ces personnes se connaissent-elles ?
Quels liens existaient avant et n'existent plus ?
```
**Statut** : Nul.

**Deuxième description** : « J'ai déménagé à Lyon en mars. Je n'ai gardé de contact régulier
qu'avec deux personnes, qui ne se connaissent pas. Mes anciens collègues se voient encore tous
les vendredis, sans moi. »

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| RÉSEAU | deux liens restants, non reliés entre eux ; un groupe dense (collègues) dont le lien avec vous a disparu | Fort | aucune trouvée dans la description | Fort |
| COMMUNAUTÉ (contre-candidate) | aucun bien ou projet commun décrit | Nul | — | inactive |

R3 · RÉSEAU : COMMUNAUTÉ → (aucun bien commun : seuls des liens sont décrits) ; HIÉRARCHIE → (aucune préséance) ; RÉCIPROCITÉ → (rien n'est dit de ce qui circule ni de son équilibre)

**Lecture** — *quel lien, s'il manquait, couperait tout ?* Vos deux contacts sont des ponts
uniques : chacun est le seul chemin vers son entourage.

**Signature** : `RÉSEAU` · `⊛`
**Statut** : Spéculatif — aucune contre-observation trouvée (plafond R4).

> La v0.3.1 « retenait » INCERTITUDE sur « je ne sais pas ce qui m'attend ». Selon R2, une
> déclaration d'ignorance n'ancre pas INCERTITUDE.

---

## Exemple 6 — Qualificatif, puis structure hors corpus

**Situation** : dans une entreprise de logiciels, le même conflit « produit contre commercial »
oppose deux binômes dans l'équipe, deux responsables au niveau du département, et deux directeurs
au comité de direction. Chaque niveau tranche ses arbitrages par le même vote à deux camps.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| POLARITÉ | deux camps nommés à chaque niveau, arbitrages à deux options | Fort | au comité, la DAF arbitre parfois hors des deux camps (marginale) | Fort |
| CONTRAINTE (contre-candidate) | aucune option explicitement exclue n'est décrite | Nul | — | inactive |
| RÉCURSIVITÉ | aucun niveau ne se prend pour objet ni ne se modifie en se regardant | Nul | — | inactive |
| HIÉRARCHIE | trois niveaux décrits — mais le motif ne tient pas à qui valide qui | Faible | les arbitrages ne remontent pas d'un niveau à l'autre : chaque niveau tranche seul (dominante) | rejetée |

R3 · POLARITÉ : CONTRAINTE → (deux camps, aucune règle qui exclut des options) ; SEUIL → (les camps coexistent à chaque niveau, aucun passage irréversible)

**Qualificatif (R13)** : la répétition du même motif à plusieurs échelles n'est pas une structure
de plus. C'est la manière dont POLARITÉ se déploie ici. Avant R9, on vérifie le qualificatif :

Q · POLARITÉ {multi-échelle} : POLARITÉ ancrée par un fait distinct à trois échelles nommées — binômes de l'équipe, responsables du département, directeurs du comité — avec les mêmes rôles (produit / commercial) ; contre-observation : au comité, la DAF arbitre parfois hors des deux camps — cela touche une échelle sur trois sans en retirer les deux pôles (marginale)

En v0.4.1, ce motif était déclaré « structure hors corpus ». Il est désormais lu dans le corpus.

**Signature** : `POLARITÉ {multi-échelle}` · `⥀{×N}`
**Statut** : Descriptif — ancrage Fort avec R3 complet ; contre-observations classées pour la carte
et pour le qualificatif.

**Variante — un vrai hors-corpus.** Même entreprise : toutes les mises en production passent par
un seul ingénieur, seul à détenir les accès ; trois incidents en 2025 ont attendu son retour de
congé. RÉSEAU s'ancre (l'ingénieur est un pont unique), mais il décrit la topologie, pas ce qui
organise les incidents : le **monopole d'une ressource** (les accès), un goulot d'étranglement.
Aucune carte ni aucun qualificatif ne le nomme. On lit RÉSEAU, on nomme le motif en clair (R9) et
on le note au journal des lacunes (`calibration.md` §4) comme **lacune possible** : un cas ne suffit
pas à dire que le corpus manque d'une carte (procédure d'admission, `calibration.md` §6).
