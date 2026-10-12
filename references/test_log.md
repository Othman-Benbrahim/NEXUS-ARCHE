# NEXUS-ARCHÊ — Journal de tests

> Version : 0.4.2
>
> **Statut honnête de ce fichier** : il ne contient encore **aucun test**. Les dix situations du §2
> sont des **démonstrations construites** en v0.3, choisies pour faire apparaître des cartes
> précises, puis relues avec les règles R1–R12. Elles servent de cas d'école et de **régression**
> (`nexus_tool.py lint` vérifie que chaque carte Fort y porte une ligne R3 complète), pas de preuve.
> Le protocole de test réel est au §3 ; son journal (§4) est vide.

---

## 1. Ce que les relectures ont changé

| Démo | Changement | Règle | Version |
|---|---|---|---|
| toutes | ligne R3 sur toutes les voisines documentées pour chaque carte Fort | R3 | 0.4.1 |
| 01 | signature condensée `LIMITE.MOUVEMENT` supprimée | notation.md §2 | 0.4.0 |
| 02 | même cas que l'exemple 2 (lecture délibérative) — non indépendant | — | 0.4.0 |
| 03 | même forme que l'exemple 1 — non indépendant | — | 0.4.0 |
| 04 | RÉCIPROCITÉ « absente » en Mode 2 : position inexistante, ancrage par ressenti ; relation requalifiée en renforcement mutuel | R6, R2 | 0.4.0 / 0.4.1 |
| 05 | le contre-exemple « autres lycées » porte sur un autre objet : ce n'est pas une anti-résonance | R4 | 0.4.0 |
| 06 | INCERTITUDE placée en *manque* alors qu'elle est présente → Mode 2 + carte listée ; relation « appui » | R7, R5, R6 | 0.4.0 / 0.4.1 |
| 07 | « pattern générique des mouvements sociaux » retiré (prévision) ; COMMUNAUTÉ rétrogradée | R12, R4 | 0.4.0 |
| 08 | INCERTITUDE relue sous le régime « acteurs de la situation » | cards.md | 0.4.0 |
| 09 | ÉMERGENCE en *manque* sans effet observable → Nul ; Mode 3 → Mode 2 ; l'immobilité est lue comme **relation de reproduction** vérifiée par deux faits | R7, R6 | 0.4.1 |
| 10 | PÉRIODICITÉ rétablie (écartée en v0.3 pour préserver un antagonisme) ; RÉSONANCE non ancrée | R2, antagonismes.md §4 | 0.4.0 |

Bilan : sur dix démonstrations, **deux** ne sont pas indépendantes des exemples, **une** carte est
rétrogradée par anti-résonance (07), **une** carte non retenue en v0.3 est rétablie (10), **une**
carte retenue en v0.4.0 est retirée par R7 (09).

---

## 2. Les dix démonstrations, relues

### 01 — Reconversion professionnelle
Démission remise et acceptée ; contrat de prestation signé ; aucun mécanisme de retour.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| SEUIL | démission acceptée, contrat signé, pas de clause de retour | Fort | préavis de deux mois en cours (marginale : le départ est acté) | Fort |
| TRANSFORMATION (contre-candidate) | aucun changement de forme à invariant décrit | Nul | — | inactive |

R3 · SEUIL : TRANSFORMATION → (aucun processus de changement de forme décrit) ; CONTRAINTE → (passage effectif à un nouvel état) ; POLARITÉ → (aucun champ à deux pôles) ; TRACE·MÉMOIRE → (ce qui organise est la fermeture du retour, pas un passé qui agit)

**Signature** `SEUIL` · **Statut** Descriptif.

### 02 — PME, validation centralisée
Toutes les décisions d'innovation passent par le PDG ; délais de 6 à 14 semaines ; périmètre de
l'équipe contractuellement borné ; autocensure avant soumission.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| HIÉRARCHIE | validation par le seul PDG, délais de 6 à 14 semaines | Fort | deux managers décident seuls sous 5 000 € (marginale) | Fort |
| CONTRAINTE | périmètre contractuellement borné ; autocensure avant soumission | Fort | des contraintes levées l'an dernier sur demande collective (marginale) | Fort |

R3 · HIÉRARCHIE : CONTRAINTE + (ancrée par le périmètre contractuel) ; PROPORTION → (une préséance, pas un rapport de grandeurs) ; RÉCIPROCITÉ → (aucune boucle d'obligations) ; RÉSEAU → (un ordre de validation, pas une topologie de liens)

R3 · CONTRAINTE : HIÉRARCHIE + (ancrée par la validation centrale) ; INCERTITUDE → (des options exclues, pas ouvertes) ; POLARITÉ → (pas de deux pôles) ; SEUIL → (aucun changement d'état) ; TRACE·MÉMOIRE → (aucune origine datée du périmètre : c'est la règle actuelle qui agit)

**Relation (R6)** : renforcement mutuel — la centralisation fixe les périmètres, les périmètres
rendent la validation centrale nécessaire.
**Signature** `HIÉRARCHIE + CONTRAINTE` · **Statut** Descriptif.

### 03 — Projet open source repris
11 contributeurs en 6 semaines sans concertation ; convention de nommage apparue par convergence ;
CONTRIBUTING.md adopté sans vote.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| ÉMERGENCE | convention de nommage apparue par convergence ; CONTRIBUTING.md adopté sans vote | Fort | un contributeur plus actif influence les orientations (marginale : il n'a prescrit ni la convention ni le fichier) | Fort |
| COMMUNAUTÉ | pas de bien commun nommé par les contributeurs | Nul | — | inactive |

R3 · ÉMERGENCE : TRANSFORMATION → (l'objet est la convention, qui n'existait pas) ; RÉCURSIVITÉ → (aucune représentation du projet par lui-même) ; CROISSANCE → (un comptage unique, pas une série) ; INCERTITUDE → (une régularité est apparue)

**Signature** `ÉMERGENCE` · **Statut** Descriptif.

### 04 — Conflit conjugal récurrent
Même conflit depuis 4 ans (« ma liberté » / « notre avenir ») ; le couple a analysé son conflit
ensemble et cette analyse alimente l'épisode suivant.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| POLARITÉ | deux termes opposés, ceux des partenaires eux-mêmes | Fort | accord sur finances, lieu de vie, enfants (marginale : hors de l'objet du conflit) | Fort |
| RÉCURSIVITÉ | l'analyse du conflit par le couple déclenche l'épisode suivant | Fort | certaines résolutions ont tenu 3 à 4 mois (marginale) | Fort |

R3 · POLARITÉ : CONTRAINTE → (aucune règle ne bloque, deux pôles s'opposent) ; SEUIL → (aucun passage irréversible)

R3 · RÉCURSIVITÉ : PÉRIODICITÉ → (le retour est produit par l'analyse du conflit, pas par une échéance) ; ÉMERGENCE → (aucune régularité collective nouvelle)

RÉCIPROCITÉ n'est pas lisible ici : le Mode 2 n'a pas de position d'absence, et « les concessions
ne sont pas perçues comme équivalentes » est un ressenti. Un fait (concessions datées et non rendues)
permettrait un Mode 3 avec RÉCIPROCITÉ en *manque*.
**Relation** : renforcement mutuel — la polarité produit les épisodes que l'analyse prend pour objet,
et l'analyse produit l'épisode suivant.
**Signature** `POLARITÉ + RÉCURSIVITÉ` · **Statut** Spéculatif (relation non confirmée par les deux partenaires).

### 05 — Déséquilibre d'un cursus
Volume STEM 72 % (55 % il y a 8 ans) ; notes d'expression écrite en baisse de 1,4 point sur 5 ans.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| PROPORTION | ratio 72/28 contre 55/45 il y a 8 ans | Fort | aucune trouvée dans la situation (le contre-exemple v0.3 « autres lycées » porte sur un autre objet) | Fort |
| HIÉRARCHIE | aucune préséance entre matières, seulement des volumes | Nul | — | inactive |

R3 · PROPORTION : HIÉRARCHIE → (des volumes, pas des rangs) ; CROISSANCE → (un rapport à deux dates, pas un taux qui dépend de la grandeur)

**Signature** `PROPORTION` · **Statut** Spéculatif (plafond R4).

### 06 — Fédération en restructuration
3 fondateurs sur 5 partis en 18 mois ; statuts de 2003 ; deux groupes de travail ; consultations ;
aucun projet de nouveaux statuts déposé.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| TRACE·MÉMOIRE | statuts de 2003, mêmes lieux et partenaires depuis | Fort | pratiques historiques déjà abandonnées (marginale) | Fort |
| TRANSFORMATION | nouvelle gouvernance cherchée, objet social conservé | Fort | des membres militent pour le statu quo (marginale) | Fort |
| INCERTITUDE | groupes de travail et consultations : conduites organisées par l'indétermination | Fort | une esquisse de modèle horizontal a été présentée (marginale) | Fort |

R3 · TRACE·MÉMOIRE : TRANSFORMATION + (ancrée par la recherche de gouvernance) ; PÉRIODICITÉ → (aucun retour régulier) ; CONTRAINTE → (les statuts ne règlent plus les pratiques : c'est leur persistance qui agit, pas une exclusion d'options) ; SEUIL → (le retour à l'ancienne structure reste possible, des membres le demandent)

R3 · TRANSFORMATION : TRACE·MÉMOIRE + (ancrée par les statuts et lieux hérités) ; ÉMERGENCE → (la fédération préexiste) ; CROISSANCE → (changement de forme, pas de degré) ; SEUIL → (aucun point de non-retour franchi)

R3 · INCERTITUDE : CONTRAINTE → (les options sont ouvertes, aucune n'est exclue) ; ÉMERGENCE → (aucune forme nouvelle n'est apparue)

Les trois cartes sont **présentes** ; aucune absence aux effets observables n'est ancrée → pas de
position *manque* (R7) → Mode 2 sur les deux cartes aux faits les plus nombreux (R5) ;
INCERTITUDE est listée « ancrée non retenue ».
**Relation** : appui — la trace fournit l'invariant (objet social, lieux, partenaires) de la transformation.
**Signature** `TRACE·MÉMOIRE + TRANSFORMATION` · **Statut** Descriptif.

### 07 — Mouvement citoyen en expansion
15 → 280 membres en 4 mois ; réunions ingérables ; deux factions (action directe / plaidoyer).

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| CROISSANCE | effectif 15 → 280 en 4 mois, mesures mensuelles | Fort | départs de fondateurs (marginale) | Fort |
| COMMUNAUTÉ | défense de la zone nommée par les membres ; dons mutuels | Fort | deux factions aux stratégies opposées (**substantielle**) | **Faible** |

R3 · CROISSANCE : TRANSFORMATION → (augmentation de degré : l'effectif) ; ÉMERGENCE → (aucune propriété nouvelle ancrée) ; PROPORTION → (une grandeur, pas un rapport)

R3 · COMMUNAUTÉ : RÉSEAU → (ce qui unit est le bien défendu, pas la topologie) ; RÉCIPROCITÉ → (un collectif autour d'un bien, pas des paires qui se rendent) ; RÉSONANCE → (une coopération organisée, pas un alignement de rythmes)

**Relation** : conflit — la taille dépasse les règles de contribution existantes.
La phrase v0.3 « pattern générique des mouvements sociaux en expansion » est retirée : c'est une
généralisation prédictive (R12), à formuler, si besoin, dans `prediction-engine`.
**Signature** `CROISSANCE + COMMUNAUTÉ` · **Statut** Spéculatif.

### 08 — Enquête sur des flux financiers
7 entités et leurs liens documentés ; 3 à 5 connexions supposées non documentées ; l'enquêteur tient
des hypothèses et collecte des actes.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| RÉSEAU | 7 entités et leurs liens documentés (actes, rapports annuels) | Fort | topologie incomplète (marginale : le graphe partiel est observable) | Fort |
| INCERTITUDE | l'enquêteur, **acteur** de la situation, tient des hypothèses et collecte des documents | Fort | certaines connexions confirmées à 80 % (marginale) | Fort |

R3 · RÉSEAU : COMMUNAUTÉ → (pas de bien commun : des flux entre entités) ; HIÉRARCHIE → (aucune préséance documentée) ; RÉCIPROCITÉ → (la topologie est l'objet, pas l'équilibre des flux)

R3 · INCERTITUDE : CONTRAINTE → (des connexions possibles, aucune exclue) ; ÉMERGENCE → (aucune régularité nouvelle)

La v0.3 disait « INCERTITUDE ne décrit pas l'état de l'enquêteur » ; c'était l'inverse : les
connexions existent, c'est leur connaissance qui manque, et cette ignorance organise la conduite
de l'enquêteur.
**Relation** : inclusion — l'indétermination porte sur des arêtes du réseau.
**Signature** `RÉSEAU + INCERTITUDE` · **Statut** Descriptif.

### 09 — Plans de transformation tous les 18 mois
4 plans en 6 ans, chacun abandonné vers 60–70 % et remplacé par le suivant ; chaque plan redéfinit
les règles et périmètres ; « révolution permanente », disent les salariés avec ironie.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| PÉRIODICITÉ | 4 plans, intervalle de 18 mois, même séquence de phases | Fort | outils numériques conservés (marginale) | Fort |
| CONTRAINTE | règles et périmètres redéfinis à chaque plan | Fort | quelques validations simplifiées définitivement (marginale) | Fort |
| ÉMERGENCE (absente) | « rien de nouveau n'est apparu » est le constat de l'absence, pas un effet ; le discours ironique est un fait sur un discours (R2, R7) | Nul | — | inactive |
| TRANSFORMATION | coïncidence lexicale (« plan de transformation ») | Nul | — | inactive |

R3 · PÉRIODICITÉ : RÉCURSIVITÉ → (le retour suit une échéance de 18 mois ; le discours des salariés ne modifie pas le cycle) ; RÉSONANCE → (un seul rythme, aucun couplage) ; TRACE·MÉMOIRE → (ce qui agit est le retour lui-même ; les outils conservés sont marginaux)

R3 · CONTRAINTE : HIÉRARCHIE → (aucun rang décrit) ; INCERTITUDE → (options exclues, pas ouvertes) ; POLARITÉ → (pas de deux pôles) ; SEUIL → (contraintes redéfinies, aucun non-retour) ; TRACE·MÉMOIRE → (contraintes nouvelles à chaque plan, pas héritées)

**Mode 2** (R5 : deux cartes ancrées). La v0.4.0 gardait ÉMERGENCE en *manque* tout en notant
qu'elle n'était pas ancrée par un effet : R7 l'interdit.
**Relation (R6)** : **reproduction** —
(a) production : chaque redéfinition des contraintes est datée du lancement d'un plan (4 sur 4) ;
(b) reproduction : après chaque redéfinition, l'effet de l'ancrage de PÉRIODICITÉ est de nouveau
observé (abandon vers 60–70 %, plan suivant 18 mois plus tard).
Les deux conjoints sont établis par des faits. Relation signalée, à confirmer par l'auteur.
**Mode 4 (R10)**, après confirmation : SEUIL comme carte de tenue — non ancrée (aucun point de
non-retour en germe n'est décrit), donc proposée comme hypothèse.
**Signature** `PÉRIODICITÉ + CONTRAINTE ⇒ SEUIL` · **Statut** Spéculatif.

### 10 — Rituel familial
Depuis 40 ans, chaque premier dimanche de janvier, mêmes plats, mêmes chansons, même lieu ; les
grands-parents qui le portaient sont décédés.

| Carte | Fait d'ancrage | Niveau | Contre-observation (portée) | Final |
|---|---|---|---|---|
| PÉRIODICITÉ | retour annuel au même jour depuis 40 ans | Fort | aucune trouvée | Fort |
| TRACE·MÉMOIRE | recettes, chansons, lieu hérités | Fort | gestes abandonnés depuis les décès (marginale) | Fort |
| RÉSONANCE (absente) | « une absence de quelque chose » est un ressenti | Nul | — | inactive |

R3 · PÉRIODICITÉ : TRACE·MÉMOIRE + (ancrée par les recettes et chansons héritées) ; RÉCURSIVITÉ → (le retour suit le calendrier) ; RÉSONANCE → (aucun alignement de rythmes documenté aujourd'hui)

R3 · TRACE·MÉMOIRE : PÉRIODICITÉ + (ancrée par le retour annuel) ; TRANSFORMATION → (la forme est conservée, pas changée) ; CONTRAINTE → (rien n'est imposé, tout est perpétué) ; SEUIL → (ce qui organise est la persistance des formes, pas le non-retour des décès)

La v0.3 écartait PÉRIODICITÉ (« la famille se réunit par habitude ») pour préserver l'antagonisme
PÉRIODICITÉ ↮ TRACE, retiré en v0.4. Un fait sur RÉSONANCE (« les chansons ne sont plus reprises en
chœur ») l'ancrerait en *manque* et ouvrirait le Mode 3.
**Relation** : tension documentée PÉRIODICITÉ ~ TRACE — un retour régulier qui transporte un héritage.
**Signature** `PÉRIODICITÉ + TRACE·MÉMOIRE` · **Statut** Spéculatif (aucune contre-observation pour PÉRIODICITÉ).

---

## 3. Protocole de test réel (à exécuter)

Objectif : savoir si deux lecteurs indépendants, appliquant ce protocole, retiennent les mêmes
cartes — et si R4 et R9 produisent réellement des rejets et des résultats nuls.

1. **Corpus** : 20 situations **non choisies par l'auteur du skill** (par exemple tirées au sort dans
   un recueil d'études de cas publiées ou de faits rapportés), décrites en 4 à 8 phrases factuelles.
2. **Cas adverses** (5, en plus des 20), avec issue attendue **écrite avant la lecture** :
   une description sans faits (attendu : ∅) ; un piège lexical ; une structure hors corpus ;
   un cas où l'anti-résonance doit être dominante ; un cas où la carte « évidente » n'est pas
   ancrable.
3. **Lecteurs** : deux, indépendants (deux personnes, ou deux instances de modèle sans contexte
   partagé), qui ne voient pas les lectures l'un de l'autre.
4. **Mesures** : accord sur la présence de chaque carte (kappa de Cohen) ; accord sur le mode ;
   taux de rejet R4 ; taux de ∅ ; taux de reproduction confirmée / signalée ; résultats des cas
   adverses.
5. **Seuils de lecture** : kappa < 0,4 → le protocole ne produit pas des lectures reproductibles ;
   taux de rejet R4 = 0 → R4 reste décoratif ; un cas adverse « sans faits » non conclu en ∅ →
   R2 n'est pas appliqué.

## 4. Journal des tests réels

*Vide.*

```
## Test N — [date]
Situation : [source + texte]
Lecteur A : [signature, statut, cartes rejetées et pourquoi]
Lecteur B : [idem]
Accord : [cartes communes / divergentes]
Cas adverse ? : [non / oui — issue attendue / obtenue]
```
