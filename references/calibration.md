# NEXUS-ARCHÊ — Calibration

> Version : 0.4.1

> Mesure le risque qu'un lecteur ou un modèle prenne une carte pour une autre (**confusion**),
> documente les faux positifs et les lacunes du corpus, et définit les indicateurs de suivi.
> Confusion ≠ incompatibilité : voir `antagonismes.md` §1.
>
> **Statut** : la matrice ci-dessous est une **estimation a priori**. Aucun chiffre n'est encore
> issu de l'usage ; les journaux sont vides.

---

## 1. Matrice de risque de confusion (a priori)

Les questions discriminantes complètes sont dans `cards.md`. Colonne « Origine » : *lecteur*
(les définitions sont nettes, le risque vient de la lecture) ou *source* (le recouvrement est dans
le corpus lui-même — registre anthropologique partagé ou structures compatibles).

### Risque élevé

| Paire | Origine | Indice rapide |
|---|---|---|
| PÉRIODICITÉ ↔ RÉCURSIVITÉ | lecteur | rythme / échéance → PÉRIODICITÉ ; le système se prend pour objet → RÉCURSIVITÉ |
| RÉSEAU ↔ COMMUNAUTÉ | **source** (même cluster Brown) | liens → RÉSEAU ; bien commun → COMMUNAUTÉ |
| RÉCIPROCITÉ ↔ COMMUNAUTÉ | **source** (même cluster Brown) | deux parties → RÉCIPROCITÉ ; plus de deux autour d'un bien → COMMUNAUTÉ |
| ÉMERGENCE ↔ TRANSFORMATION | lecteur — **incompatibles** | l'entité est apparue → ÉMERGENCE ; elle préexistait → TRANSFORMATION |
| SEUIL ↔ TRANSFORMATION | **source** (compatibles depuis v0.4) | non-retour → SEUIL ; changement de forme à invariant → TRANSFORMATION ; souvent les deux |
| SEUIL ↔ TRACE·MÉMOIRE | **source** (inclusion mathématique depuis v0.4 : l'hystérésis est une dépendance au chemin) | retour fermé → SEUIL ; passé qui continue d'agir → TRACE ; souvent les deux |

### Risque moyen

| Paire | Origine | Indice rapide |
|---|---|---|
| RÉCIPROCITÉ ↔ RÉSEAU | **source** | ce qui circule dans un lien → RÉCIPROCITÉ ; topologie → RÉSEAU |
| HIÉRARCHIE ↔ RÉSEAU | lecteur (réduit en v0.4 : HIÉRARCHIE n'invoque plus les réseaux scale-free) | préséance → HIÉRARCHIE ; liens → RÉSEAU |
| HIÉRARCHIE ↔ PROPORTION | lecteur (augmenté en v0.4 : les inégalités de grandeur relèvent de PROPORTION) | rang → HIÉRARCHIE ; rapport de grandeurs → PROPORTION |
| TRACE·MÉMOIRE ↔ PÉRIODICITÉ | **source** (compatibles) | ce qui persiste → TRACE ; le retour lui-même → PÉRIODICITÉ |
| RÉSONANCE ↔ COMMUNAUTÉ | **source** (cluster « rituals ») | alignement de rythmes → RÉSONANCE ; coopération autour d'un bien → COMMUNAUTÉ |
| CONTRAINTE ↔ SEUIL | lecteur | options retirées → CONTRAINTE ; état sans retour → SEUIL |
| INCERTITUDE ↔ ÉMERGENCE | lecteur | possibles non tranchés → INCERTITUDE ; régularité apparue → ÉMERGENCE |
| CROISSANCE ↔ TRANSFORMATION | lecteur | degré → CROISSANCE ; forme → TRANSFORMATION |
| CONTRAINTE ↔ TRACE·MÉMOIRE | **source** (règle héritée) | exclusion d'options → CONTRAINTE ; persistance du passé → TRACE |

### Risque faible

| Paire | Origine | Indice rapide |
|---|---|---|
| POLARITÉ ↔ CONTRAINTE | lecteur | deux pôles → POLARITÉ ; règle qui bloque → CONTRAINTE |
| RÉSONANCE ↔ RÉCIPROCITÉ | lecteur | synchronisation → RÉSONANCE ; échange obligé → RÉCIPROCITÉ |
| TRACE·MÉMOIRE ↔ TRANSFORMATION | lecteur (séquentiel) | ce qui reste → TRACE ; le processus → TRANSFORMATION |
| INCERTITUDE ↔ CONTRAINTE | lecteur — **incompatibles** | option ouverte → INCERTITUDE ; exclue → CONTRAINTE. Glyphes confondables `Ø` / `⊘` |
| RÉCIPROCITÉ ↔ HIÉRARCHIE | lecteur (compatibles) | boucle d'obligations → RÉCIPROCITÉ ; préséance → HIÉRARCHIE |

> Quand l'origine est **source**, aucun entraînement du lecteur ne supprimera la confusion : seule
> une révision des définitions le peut. Ces paires sont les premières à surveiller dans le journal.

---

## 2. Faux positifs typiques

| Faux positif | Déclencheur | Pourquoi | Issue correcte |
|---|---|---|---|
| RÉSEAU | « je me sens seul et déconnecté » | ressenti, pas de topologie (R2) | résultat nul puis demande de faits (exemple 5) |
| INCERTITUDE | « je ne sais pas ce qui m'attend » | ignorance déclarée, pas de conduite organisée (R2) | Nul tant qu'aucune conduite n'est décrite |
| CROISSANCE | « notre croissance » après une acquisition | coïncidence lexicale ; mécanisme concurrent dominant (R4) | SEUIL + TRANSFORMATION (exemple 4) |
| TRANSFORMATION | « plan de transformation » récurrent | coïncidence lexicale ; structure cyclique | PÉRIODICITÉ (test_log 09) |
| HIÉRARCHIE | déséquilibre de volumes horaires | rapport de grandeurs, pas de préséance | PROPORTION (test_log 05) |
| RÉCURSIVITÉ | « on tourne en rond » | rétroaction ou répétition sans représentation de soi | PÉRIODICITÉ, ou structure hors corpus |
| COMMUNAUTÉ | contributeurs sans bien commun nommé | intérêt partagé ≠ projet commun | ÉMERGENCE (test_log 03) |

**Règle de vigilance** : quand le nom d'une carte figure dans la description, chercher
l'anti-résonance du côté de la carte voisine (R2).

---

## 3. Journal des erreurs de distinction

*Vide.* Template :

```
## Erreur N — [date]
Situation : [2 phrases]
Carte retenue d'abord : [A] — ancrage : [fait]
Carte correcte : [B] — question discriminante qui aurait tranché : [question]
Origine : [lecteur / source]
Leçon : [ce que l'erreur dit des définitions ou du protocole]
```

**Règles** : une paire de risque moyen qui accumule 3 erreurs passe en élevé ; une paire de
risque élevé à 0 erreur sur 20 lectures concernées passe en moyen. Une paire d'origine *source*
qui accumule 3 erreurs déclenche une révision de `cards.md`.

---

## 4. Journal des lacunes du corpus (structures hors corpus, R9)

*Vide en données réelles.* Lacunes identifiées à l'analyse, à confirmer par l'usage :
- **rétroaction simple** (sortie qui influence l'entrée, sans représentation de soi) — exclue de
  RÉCURSIVITÉ en v0.4 ;
- **auto-similarité** (même motif à plusieurs échelles) — idem (exemple 6).

Template :

```
## Lacune N — [date]
Situation : [2 phrases]
Motif nommé en clair : [...]
Cartes testées et pourquoi elles ne conviennent pas : [...]
```

Une lacune notée trois fois sur des situations indépendantes justifie d'examiner une carte nouvelle.

---

## 5. Indicateurs (à calculer après 50 lectures réelles)

| Indicateur | Définition | Lecture |
|---|---|---|
| Taux de rejet par anti-résonance | % de cartes ancrées puis rejetées ou rétrogradées par R4 | **0 % = R4 décoratif** ; à surveiller en premier |
| Taux de résultat nul | % de lectures concluant ∅ | 0 % sur 50 lectures suggère une obligation de trouver |
| Taux de rejet d'ancrage | % de candidates déclarées Nul | |
| Taux de confusion corrigée | % de lectures où la première carte a été remplacée | |
| Accord inter-lecteurs | kappa de Cohen entre deux lecteurs indépendants sur les mêmes situations | voir `test_log.md` §3 |
| Répartition des statuts | Descriptif / Spéculatif / Nul | |
| Lacunes | nombre et récurrence des structures hors corpus | |
| Configurations confirmées / signalées | par configuration (Scission, Reproduction, Lacune contradictoire) et pour la relation de reproduction en Mode 2 | **Reproduction** est la seule configuration sans fréquence combinatoire et la plus exposée au sur-déclenchement (un mouvement est souvent en aval de la structure stable) : un taux de confirmation bas impose de durcir R6 (a)–(b) |
