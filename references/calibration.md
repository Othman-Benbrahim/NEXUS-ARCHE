# NEXUS-ARCHÊ — Calibration des Distinctions Inter-Cartes

> Ce fichier sert deux fonctions :
> (1) documenter les risques de confusion identifiés à l'analyse et confirmés par les tests ;
> (2) fournir un protocole de suivi des erreurs de distinction en conditions réelles.
> Mettre à jour ce fichier après chaque série de 10 situations documentées.

> **Confusion n'est pas antagonisme.** Ce fichier mesure le risque qu'un lecteur prenne une
> carte pour une autre. L'incompatibilité structurelle entre deux cartes — le fait que leurs
> définitions ne puissent pas être vraies du même objet — est une relation distincte, définie
> dans `references/antagonismes.md`. Cinq des dix-sept paires listées ici sont aussi
> antagonistes ; les douze autres ne le sont pas, à commencer par HIÉRARCHIE ↔ RÉSEAU, dont
> les deux structures peuvent parfaitement décrire le même objet.

---

## Matrice de risque de confusion

Chaque paire est évaluée selon deux critères :
- **Risque** : probabilité qu'un utilisateur ou un LLM confonde les deux cartes (Élevé / Moyen / Faible)
- **Critère discriminant** : la question qui tranche entre les deux de manière structurelle

### Risque élevé — confusion probable sans protocole de rigueur

| Paire | Risque | Critère discriminant |
|---|---|---|
| PÉRIODICITÉ ↔ RÉCURSIVITÉ | ⚠⚠⚠ | Ce qui se répète est-il *dans le temps* (→ PÉRIODICITÉ) ou *dans la forme* (→ RÉCURSIVITÉ) ? |
| RÉSEAU ↔ COMMUNAUTÉ | ⚠⚠⚠ | Ce qui importe est-il la *topologie des liens* (→ RÉSEAU) ou le *projet commun qui unit* (→ COMMUNAUTÉ) ? |
| SEUIL ↔ TRANSFORMATION | ⚠⚠⚠ | S'agit-il d'un *basculement ponctuel irréversible* (→ SEUIL) ou d'un *processus de mutation continu* (→ TRANSFORMATION) ? |
| ÉMERGENCE ↔ TRANSFORMATION | ⚠⚠⚠ | Y a-t-il *apparition de quelque chose de fondamentalement nouveau* (→ ÉMERGENCE) ou *mutation d'une entité existante* (→ TRANSFORMATION) ? |
| RÉCIPROCITÉ ↔ COMMUNAUTÉ | ⚠⚠⚠ | La relation est-elle *bilatérale entre deux parties* (→ RÉCIPROCITÉ) ou *multi-acteurs autour d'un bien commun* (→ COMMUNAUTÉ) ? |

### Risque moyen — confusion possible dans des situations ambiguës

| Paire | Risque | Critère discriminant |
|---|---|---|
| HIÉRARCHIE ↔ RÉSEAU | ⚠⚠ | La structure définit-elle des *rangs et positions* (→ HIÉRARCHIE) ou seulement des *connexions* (→ RÉSEAU) ? |
| TRACE · MÉMOIRE ↔ PÉRIODICITÉ | ⚠⚠ | Le passé est-il présent comme *empreinte résiduelle* (→ TRACE) ou comme *retour cyclique* (→ PÉRIODICITÉ) ? |
| RÉSONANCE ↔ COMMUNAUTÉ | ⚠⚠ | S'agit-il d'un *alignement de rythmes* (→ RÉSONANCE) ou d'une *coopération organisée* (→ COMMUNAUTÉ) ? |
| CONTRAINTE ↔ SEUIL | ⚠⚠ | Y a-t-il *limitation du champ d'action sans changement d'état* (→ CONTRAINTE) ou *basculement irréversible vers un nouvel état* (→ SEUIL) ? |
| INCERTITUDE ↔ ÉMERGENCE | ⚠⚠ | Est-on dans *l'avant sans forme* (→ INCERTITUDE) ou dans *l'apparition d'un ordre nouveau* (→ ÉMERGENCE) ? |
| CROISSANCE ↔ TRANSFORMATION | ⚠⚠ | S'agit-il d'un *changement de degré quantitatif* (→ CROISSANCE) ou d'un *changement de nature qualitatif* (→ TRANSFORMATION) ? |
| RÉCIPROCITÉ ↔ RÉSEAU | ⚠⚠ | Ce qui importe est-il *la qualité symétrique de l'échange* (→ RÉCIPROCITÉ) ou *la topologie des connexions* (→ RÉSEAU) ? |

### Risque faible — distinction généralement claire

| Paire | Risque | Critère discriminant |
|---|---|---|
| POLARITÉ ↔ CONTRAINTE | ⚠ | Y a-t-il *deux pôles en tension* (→ POLARITÉ) ou *une règle qui bloque certains mouvements* (→ CONTRAINTE) ? |
| PROPORTION ↔ HIÉRARCHIE | ⚠ | S'agit-il d'un *équilibre de mesures* (→ PROPORTION) ou d'un *ordre de rangs* (→ HIÉRARCHIE) ? |
| RÉSONANCE ↔ RÉCIPROCITÉ | ⚠ | L'alignement est-il *spontané et rythmique* (→ RÉSONANCE) ou *délibéré et symétrique* (→ RÉCIPROCITÉ) ? |
| TRACE · MÉMOIRE ↔ TRANSFORMATION | ⚠ | Est-on dans *le résidu stable après mutation* (→ TRACE) ou dans *le processus de mutation lui-même* (→ TRANSFORMATION) ? |
| INCERTITUDE ↔ CONTRAINTE | ⚠ | Y a-t-il de *l'inconnu structurel* (→ INCERTITUDE) ou une *règle d'interdiction* (→ CONTRAINTE) ? |

---

## Faux positifs structurels documentés

Un faux positif est une situation où une carte semble évidente depuis le ressenti ou la description superficielle, mais ne passe pas le test d'ancrage observable.

| Faux positif | Situation déclenchante | Raison du rejet | Carte correcte |
|---|---|---|---|
| RÉSEAU | "Je me sens seul et déconnecté" | La topologie de liens n'est pas nommable — le ressenti ne suffit pas | INCERTITUDE, POLARITÉ ou CONTRAINTE selon ancrage |
| COMMUNAUTÉ | Projet open-source sans "nous" articulé | Les contributeurs partagent un intérêt mais pas un projet commun conscient | ÉMERGENCE |
| RÉCIPROCITÉ | Conflit conjugal — "on ne se donne plus" | L'échange n'est pas symétrique — son absence est la structure active | POLARITÉ + RÉCURSIVITÉ |
| HIÉRARCHIE | Déséquilibre de volumes horaires dans un cursus | Le déséquilibre est un rapport d'échelle, pas un ordre de rangs | PROPORTION |
| TRANSFORMATION | Plan de transformation organisationnel | Le plan est nommé "transformation" mais la structure réelle est cyclique | PÉRIODICITÉ |

> **Règle de vigilance** : lorsque le nom d'une carte correspond au vocabulaire utilisé dans la situation (une "transformation" nommée, un "réseau" mentionné), renforcer le test d'anti-résonance. La coïncidence lexicale n'est pas un ancrage.

---

## Protocole de suivi des erreurs de distinction

À remplir après chaque lecture où une confusion a été identifiée (soit a priori par auto-correction, soit a posteriori par révision).

### Template d'entrée de journal

```
## Erreur N — [date]

**Situation** : [description en 2 phrases]
**Carte initialement retenue** : [Carte A]
**Ancrage initial** : [ce qui semblait justifier la carte]
**Carte correcte** : [Carte B]
**Raison de la confusion** : [ce qui a induit en erreur]
**Critère discriminant applicable** : [question qui aurait tranché]
**Leçon systémique** : [ce que cette erreur dit du système]
```

---

## Journal de calibration

*Ce journal est vide à la publication de v0.3. À remplir en conditions d'usage réel.*

> Format : chaque erreur documentée alimente la matrice de risque ci-dessus.
> Lorsqu'une paire de risque "Moyen" accumule 3 erreurs documentées → passer en "Élevé".
> Lorsqu'une paire de risque "Élevé" atteint 0 erreur sur 20 lectures → passer en "Moyen".

---

## Indicateurs de calibration à terme

À calculer après 50 situations documentées :

| Indicateur | Définition | Cible |
|---|---|---|
| Taux de rejet | % de tirages où au moins une carte est déclarée inactive | > 20 % (signe que le protocole est appliqué) |
| Taux de confusion corrigée | % de lectures où la première carte retenue a été remplacée | < 15 % (signe de maîtrise des distinctions) |
| Paires les plus confondues | Top 3 des paires ayant généré le plus d'erreurs | À observer empiriquement |
| Statuts épistémiques | Distribution Descriptif / Spéculatif / Performatif | Indicateur de la nature des situations traitées |
