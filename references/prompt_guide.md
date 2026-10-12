# NEXUS-ARCHÊ — Guide d'activation

> Version : 0.4.1

> Templates à copier-coller. Les règles citées (R1–R12) sont dans `protocol.md` ; ce fichier ne
> les redéfinit pas. Les parties entre crochets sont à remplacer.

## Ce qui fait une bonne demande

- **Des faits** : qui, quoi, quand, combien, quel comportement. Un ressenti peut accompagner un
  fait ; seul, il conduit à un résultat nul (R2, R9).
- **Laisser le mode se déterminer** (R5) : il dépend du nombre de cartes ancrées. Demander un
  mode est possible ; le skill dira s'il n'est pas atteint.
- **Ne pas imposer de carte** : une carte proposée est testée comme une candidate parmi d'autres.
- **Ne pas demander de solution ni de prévision** (R12).

---

## Template 1 — Lecture standard

```
NEXUS-ARCHÊ. Situation : [4 à 8 phrases factuelles].
Modalité : délibérative.
```

Le skill applique la procédure complète et rend le format de sortie de `SKILL.md`.

## Template 2 — Tirage aléatoire

```
NEXUS-ARCHÊ, tirage aléatoire de [1 / 2 / 3] cartes. Situation : [...].
```

Le tirage passe par `python3 scripts/nexus_tool.py draw -n [n]` ; la ligne de journal figure dans
la lecture. Le tirage choisit les cartes, pas les positions (R1). Une carte non ancrée peut être
remplacée deux fois au plus : `draw -n 1 --exclude "[cartes déjà sorties]"`. Si aucun outil d'exécution n'est disponible, le skill le dit et passe en délibératif.
Pour un tirage rejouable : `draw -n [n] --seed "[texte de la situation]"`.

## Template 3 — Constellation (Mode 3)

```
NEXUS-ARCHÊ, je cherche une constellation tient / bouge / manque.
Situation : [6 à 10 phrases, en incluant ce qui fait défaut et ses effets observables].
```

Le Mode 3 exige une structure dont l'absence a des effets observables (R7). Les configurations
signalées (R8) reviennent sous forme de questions à confirmer.

## Template 4 — Mode 4 après une configuration confirmée

```
Je confirme la configuration [Scission / Reproduction / Lacune contradictoire]
(ou la relation de reproduction du Mode 2) :
[ce qui la confirme]. Quelle structure, déjà présente, permettrait de tenir cette tension ?
```

## Template 5 — Vérifier une signature

```
Valide cette signature NEXUS-ARCHÊ : [signature].
```

→ `python3 scripts/nexus_tool.py validate "[signature]"`. Pour en faire une phrase STÈLE légale,
confier la signature et l'énoncé structurel au skill `stele` (notation.md §5).

## Template 6 — Avant une analyse OSINT ou prédictive

```
Avant l'analyse OSINT / prédictive, identifie la structure de cette situation avec NEXUS-ARCHÊ.
Situation : [acteurs, événements datés, données disponibles].
Puis traduis la structure retenue en questions d'investigation.
```

Exemple de traduction : PÉRIODICITÉ + CONTRAINTE sur un blocage institutionnel récurrent →
chercher le rythme du cycle (dates des épisodes précédents, phase actuelle) et les contraintes
renommées sans changer d'effet. La lecture fournit des **questions** ; les probabilités relèvent de
`prediction-engine` ou `osint-intel`.

## Template 7 — Après un tirage Fractales du Destin

```
Tirage Fractales du Destin : [cartes et positions], sur la situation : [faits].
Quelle structure NEXUS-ARCHÊ est ancrée dans les faits de cette situation ?
```

Les cartes FdD ne sont **pas** des ancrages : l'ancrage porte sur les faits de la situation.
Les deux lectures coexistent ; NEXUS-ARCHÊ dit ce que les faits permettent d'affirmer
structurellement, FdD ce que le registre symbolique fait apparaître.

## Template 8 — Auditer une lecture

```
Voici une lecture NEXUS-ARCHÊ : [lecture]. Vérifie : ancrages (R2–R3), portée des
contre-observations (R4), lignes R3 sur toutes les voisines, choix du mode (R5), relation (R6),
configurations (R8), signature, statut (R11).
```

---

| Template | Usage |
|---|---|
| 1 | lecture standard |
| 2 | tirage aléatoire réel |
| 3 | constellation |
| 4 | carte de tenue |
| 5 | signature / export STÈLE |
| 6 | cadrage OSINT ou prédictif |
| 7 | complément Fractales du Destin |
| 8 | audit d'une lecture |
