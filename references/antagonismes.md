# NEXUS-ARCHÊ — Antagonismes Structurels

> Ce fichier définit la relation **d'antagonisme** entre cartes : deux structures dont les
> définitions ne peuvent pas être vraies du même objet en même temps.
>
> Il est requis par les configurations pathologiques 3 et 4 du Mode 3
> (`references/protocol.md`), qui supposent cette relation sans la fournir.
>
> Il ne remplace pas `references/calibration.md` : **la confusion et l'antagonisme sont deux
> relations distinctes**, et les confondre est l'erreur que ce fichier existe pour éviter.

---

## 1. Ce que l'antagonisme n'est pas

`calibration.md` documente des **risques de confusion** : la probabilité qu'un lecteur ou un
modèle prenne une carte pour une autre. C'est une propriété du lecteur.

L'antagonisme est une propriété des **structures** : deux cartes sont antagonistes lorsque
leurs registres rationnels s'excluent logiquement sur un même objet. Le lecteur n'y est pour
rien.

Les deux relations se recoupent en partie — on confond souvent des structures voisines et
incompatibles — mais ni l'une n'implique l'autre :

| Paire | Confusion | Antagonisme | Pourquoi |
|---|---|---|---|
| HIÉRARCHIE ↔ RÉSEAU | ⚠⚠ matrice | **non** | Une hiérarchie *est* un graphe : cards.md range HIÉRARCHIE sous « Théorie des graphes / lois de puissance — arbres dirigés ». Les deux cartes peuvent décrire le même objet. |
| CROISSANCE ↔ CONTRAINTE | aucune | **non** | CROISSANCE est définie par sa limite : « Ce qui s'amplifie jusqu'à sa limite structurelle. » La contrainte est la condition de la croissance logistique, pas son contraire. |
| TRACE ↔ TRANSFORMATION | ⚠ matrice | **non** | « La trace est le résidu stable après une transformation » : relation séquentielle, pas exclusion. |
| PROPORTION ↔ CROISSANCE | distinction cards.md | **non** | Une croissance homothétique conserve les rapports. Les deux cartes tiennent ensemble. |
| ÉMERGENCE ↔ CONTRAINTE | aucune | **non** | L'auto-organisation opère sous contraintes locales ; c'est même sa condition ordinaire. |
| RÉCIPROCITÉ ↔ HIÉRARCHIE | aucune | **oui** | Un même rapport ne peut pas être à la fois « échange symétrique » et « distribution inégale ». Antagonisme sans risque de confusion. |

> Cinq des neuf antagonismes du §3 figurent dans la matrice de risque de `calibration.md` ;
> les douze autres paires de cette matrice ne sont pas antagonistes.

> **Règle** : ne jamais dériver un antagonisme du critère discriminant d'une distinction. Le
> « ou » d'un critère (« s'agit-il de X **ou** de Y ? ») dit quelle carte retenir pour *cette
> lecture*, pas que les deux structures s'excluent dans le monde. Appliqué mécaniquement, il
> ferait de HIÉRARCHIE et RÉSEAU des antagonistes, ce qui est faux.

---

## 2. Critère d'inscription

Une paire entre dans la table si, et seulement si, les **registres rationnels** des deux
cartes portent des prédicats contradictoires sur un même objet. Chaque ligne cite le texte
de `references/cards.md` qui la fonde, et porte un statut :

- **explicite** — l'incompatibilité est écrite dans les références ;
- **déduit** — elle se déduit des deux définitions ; la déduction est montrée et peut être
  contestée.

Aucune ligne n'est admise sur une intuition, une proximité de vocabulaire ou une symétrie
esthétique de la table.

---

## 3. Table des antagonismes

Neuf paires sur les 120 possibles. La relation est **symétrique** et **non transitive**.

### Axe 1 — Préexistence de l'entité

| Paire | Statut | Fondement |
|---|---|---|
| ÉMERGENCE ↮ TRANSFORMATION | explicite | « L'émergence fait apparaître quelque chose de fondamentalement nouveau à partir de règles locales simples ; la transformation mute une entité existante en conservant son essence. » Une même entité préexiste ou ne préexiste pas. |
| ÉMERGENCE ↮ CROISSANCE | explicite | « La croissance amplifie quelque chose d'existant ; l'émergence fait apparaître quelque chose de fondamentalement nouveau. » Même exclusion. |

### Axe 2 — Auto-référence

| Paire | Statut | Fondement |
|---|---|---|
| ÉMERGENCE ↮ RÉCURSIVITÉ | explicite | « L'émergence est un ordre global non planifié sans auto-référence ; la récursivité implique une boucle explicite. » La négation est dans le texte. |

### Axe 3 — Détermination

| Paire | Statut | Fondement |
|---|---|---|
| INCERTITUDE ↮ CONTRAINTE | explicite | « Le vide est ouvert, la contrainte est fermée. » Un même possible est indéterminé ou exclu, pas les deux. |
| INCERTITUDE ↮ ÉMERGENCE | explicite | « L'incertitude est l'état d'indétermination avant qu'un pattern n'apparaisse ; l'émergence est l'apparition effective d'un ordre nouveau. » Exclusion temporelle sur une même forme. |

### Axe 4 — Retour

| Paire | Statut | Fondement |
|---|---|---|
| PÉRIODICITÉ ↮ TRACE · MÉMOIRE | explicite | « La trace est ce qui reste après une transformation et ne revient pas ; la périodicité est ce qui revient régulièrement. » |
| PÉRIODICITÉ ↮ SEUIL | déduit | SEUIL : « Le seuil ne se franchit qu'une fois. » PÉRIODICITÉ : « retour régulier d'un état ». Un même état ne peut pas revenir régulièrement et être hors de retour. *Absente de la matrice de confusion : personne ne confond ces deux cartes, elles n'en sont pas moins incompatibles.* |

### Axe 5 — Continuité du changement

| Paire | Statut | Fondement |
|---|---|---|
| SEUIL ↮ TRANSFORMATION | déduit | SEUIL : « un instant discret et irréversible après lequel rien ne peut reprendre sa forme précédente ». TRANSFORMATION : « changement continu avec conservation d'un invariant ». Un même changement est discret-irréversible ou continu-conservatif. **Objection connue** : un processus long peut contenir un point de non-retour (la chrysalide). L'antagonisme vaut pour *le même changement*, pas pour un processus et l'un de ses instants — voir §4. |

### Axe 6 — Symétrie du rapport

| Paire | Statut | Fondement |
|---|---|---|
| RÉCIPROCITÉ ↮ HIÉRARCHIE | déduit | RÉCIPROCITÉ : « échange symétrique avec conservation ». HIÉRARCHIE : « distribution inégale mais structurante selon des lois de puissance ». Un même rapport est symétrique ou inégal. |

### Paires examinées et écartées

| Paire | Raison du rejet |
|---|---|
| POLARITÉ ↮ RÉSONANCE | « Deux pôles en tension » et « alignement de rythmes » ne s'excluent pas : deux oscillateurs peuvent se coupler en opposition de phase. Alignement n'est pas identité. |
| PROPORTION ↮ INCERTITUDE | Un rapport peut être mal connu sans cesser d'être un rapport. L'opposition n'existe qu'entre les glyphes STÈLE `◯` (advenu) et `Ø` (non-encore-advenu) — pas entre les cartes. Ne jamais dériver un antagonisme de cartes depuis la grammaire STÈLE. |
| COMMUNAUTÉ ↮ RÉSEAU | Une communauté possède une topologie ; un réseau peut porter un projet. Voisinage, pas exclusion. |

---

## 4. Portée : la condition du même objet

**Un antagonisme entre deux cartes ne devient une contradiction que si les deux structures
portent sur le même objet de la situation.**

Deux structures incompatibles décrivant deux objets distincts ne se contredisent pas : une
équipe peut connaître une CROISSANCE de son effectif pendant qu'une ÉMERGENCE se produit
dans ses pratiques. Rien n'est pathologique là-dedans.

Il s'ensuit que la table ne peut pas conclure seule. Elle produit un **signal**, et le signal
ouvre une question — celle-ci, à poser à l'auteur de la situation, jamais au modèle :

> *Ces deux structures portent-elles sur la même chose ?*

Si oui : la configuration pathologique est avérée, et se lit selon `protocol.md`.
Si non : la constellation est ordinaire ; le signal est retiré et la paire notée au journal
(§7) comme faux positif de portée.

C'est le même partage que le test d'ancrage observable : la machine vérifie ce qui est
vérifiable, l'auteur tranche ce qui demande de connaître la situation.

---

## 5. Définitions opératoires des configurations du Mode 3

Les quatre configurations de `protocol.md` deviennent calculables ainsi. Les positions sont
celles du Mode 3 : *ce qui tient*, *ce qui bouge*, *ce qui manque*.

| Config | Nom | Condition |
|---|---|---|
| 1 | Miroir | `tient` et `manque` sont **la même carte**. Impossible en tirage aléatoire sans remise ; possible en tirage délibératif. |
| 2 | Immobilité structurelle | `tient` et `bouge` sont en **voisinage documenté** (§6). |
| 3 | Lacune active contradictoire | `tient` et `manque` sont **antagonistes** (§3). |
| 4 | Tension maximale | **Au moins deux** des trois paires de la constellation sont antagonistes. |

### Sur la configuration 4

Le texte de `protocol.md` dit « les 3 cartes appartiennent à des registres antagonistes ».
Deux lectures étaient possibles.

La première suppose une partition des 16 cartes en *registres*, puis une relation
d'antagonisme entre registres. Cette partition n'existe nulle part dans NEXUS-ARCHÊ : il
aurait fallu l'inventer, et une taxonomie inventée aurait servi de fondement à un diagnostic.
Elle est écartée.

La seconde, retenue, lit « registres antagonistes » comme *plusieurs structures incompatibles
simultanées* — la formulation même du signal donné trois lignes plus bas — et la calcule sur
les paires déjà fondées au §3.

Le seuil est fixé à **deux paires sur trois**, et non trois. La table ne contient aucun
triangle : aucune constellation de trois cartes n'a ses trois paires antagonistes. Exiger les
trois rendrait la configuration 4 inatteignable par construction. Avec deux, une carte est
incompatible avec les deux autres, ou les incompatibilités forment une chaîne — dans les deux
cas, la constellation porte bien plusieurs structures qui ne peuvent pas tenir ensemble.

### Fréquences

Sur les 560 constellations possibles et les 3 360 constellations ordonnées :

| Configuration | Déclenchements | Taux |
|---|---|---|
| 3 — Lacune active contradictoire | 252 / 3 360 ordonnées | 7,5 % |
| 4 — Tension maximale | 10 / 560 | 1,8 % |
| 3 ou 4 | 272 / 3 360 | 8,1 % |

« Signal rare mais fort » : 1,8 % pour la configuration 4. Ces taux sont ceux du tirage
aléatoire uniforme ; en tirage délibératif ils n'ont pas de sens, l'analyste ne tirant pas au
hasard.

Les dix constellations de configuration 4 :

```
SEUIL + PÉRIODICITÉ + TRANSFORMATION      SEUIL + PÉRIODICITÉ + TRACE·MÉMOIRE
SEUIL + ÉMERGENCE + TRANSFORMATION        RÉCURSIVITÉ + ÉMERGENCE + INCERTITUDE
RÉCURSIVITÉ + ÉMERGENCE + TRANSFORMATION  RÉCURSIVITÉ + ÉMERGENCE + CROISSANCE
ÉMERGENCE + INCERTITUDE + CONTRAINTE      ÉMERGENCE + INCERTITUDE + TRANSFORMATION
ÉMERGENCE + INCERTITUDE + CROISSANCE      ÉMERGENCE + TRANSFORMATION + CROISSANCE
```

> ÉMERGENCE figure dans huit des dix. C'est un fait sur le corpus, pas un défaut de la table :
> avec quatre antagonistes, c'est la carte la plus contraignante des seize. Une constellation
> qui la contient mérite un examen particulier.

---

## 6. Voisinage documenté (configuration 2)

La configuration 2 demande que `bouge` soit « de même nature » que `tient`. Aucun axe de
*nature* n'est défini dans NEXUS-ARCHÊ, et en inventer un poserait le problème du §5.

Définition retenue, entièrement dérivée des références : **deux cartes sont en voisinage
documenté lorsque l'une figure dans la rubrique « À ne pas confondre avec » de l'autre, et
qu'elles ne sont pas antagonistes.**

La justification est que les références n'ont eu à écrire un critère de séparation que pour
des structures assez proches pour être prises l'une pour l'autre : le voisinage est attesté
par l'existence même du critère. L'exclusion des paires antagonistes est nécessaire — deux
structures incompatibles ne sont pas « de même nature », quelle que soit leur proximité
apparente.

Seize paires sur 120 (13,3 %) :

```
COMMUNAUTÉ ~ RÉCIPROCITÉ    COMMUNAUTÉ ~ RÉSEAU        COMMUNAUTÉ ~ RÉSONANCE
CONTRAINTE ~ HIÉRARCHIE     CONTRAINTE ~ POLARITÉ      CONTRAINTE ~ SEUIL
CROISSANCE ~ PROPORTION     CROISSANCE ~ TRANSFORMATION  HIÉRARCHIE ~ PROPORTION
HIÉRARCHIE ~ RÉSEAU         PÉRIODICITÉ ~ RÉCURSIVITÉ  PÉRIODICITÉ ~ RÉSONANCE
POLARITÉ ~ SEUIL            RÉCIPROCITÉ ~ RÉSEAU       RÉCIPROCITÉ ~ RÉSONANCE
TRACE·MÉMOIRE ~ TRANSFORMATION
```

Sept paires de « À ne pas confondre avec » sont exclues parce qu'antagonistes ; deux
antagonismes (RÉCIPROCITÉ ↮ HIÉRARCHIE, PÉRIODICITÉ ↮ SEUIL) ne figurent dans aucune rubrique
de distinction, ce qui confirme que les deux relations ne se recouvrent pas.

Cette définition est la plus fragile du fichier : elle utilise une relation écrite pour un
autre usage. Elle est marquée comme telle et devra être révisée sur données réelles avant
d'être considérée comme acquise.

---

## 7. Journal des antagonismes

*Vide à la publication. À remplir en conditions d'usage réel, comme le journal de
`calibration.md`.*

### Template

```
## Entrée N — [date]

**Constellation** : [tient] / [bouge] / [manque]
**Configuration signalée** : [1 / 2 / 3 / 4]
**Même objet ?** : [oui / non] — [ce sur quoi portent les deux structures]
**Verdict** : [configuration avérée / faux positif de portée]
**Observation** : [ce que cette entrée apprend sur la table]
```

### Règles d'évolution

- Une paire dont trois faux positifs de portée sont documentés sans aucune configuration
  avérée est **retirée** de la table : son incompatibilité est vraie en principe et sans
  portée en pratique.
- Une paire nouvelle n'est **ajoutée** qu'en produisant la citation de `cards.md` qui la
  fonde, selon le critère du §2. Une paire sans citation n'entre pas.
- Le statut *déduit* passe à *explicite* si `cards.md` est un jour précisé en ce sens, jamais
  par accumulation d'usages.

---

## 8. Limites

Cette table dit ce que les seize définitions s'interdisent mutuellement. Elle ne dit rien de
la situation.

Une configuration pathologique signalée est une **hypothèse à vérifier auprès de l'auteur**,
au même titre qu'une carte proposée sans ancrage. Un dispositif qui l'annoncerait comme un
diagnostic ferait exactement ce que `protocol.md` interdit en dernière ligne : « NEXUS-ARCHÊ
identifie des structures. Il ne prédit pas, ne prescrit pas, ne diagnostique pas. »
