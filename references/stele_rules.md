# NEXUS-ARCHÊ — Règles STÈLE (autonomes)

> Ce fichier contient les règles syntaxiques minimales de l'alphabet STÈLE
> nécessaires à la production de chaînes valides dans NEXUS-ARCHÊ.
> Il est autonome — utilisable sans le skill STÈLE complet.
> Pour la grammaire STÈLE complète, se référer au skill STÈLE de l'écosystème IRIS.

---

## LES TROIS CLASSES DE PRIMITIVES

Toute chaîne STÈLE valide suit une syntaxe positionnelle fondée sur trois classes :

| Classe | Position | Rôle | Définition |
|---|---|---|---|
| **Substance** | 1 | Ce qui EST | Nomme une structure, un état, une configuration active |
| **Opérative** | 2 | Ce qui SE FAIT | Nomme un processus, un mouvement, une action en cours |
| **Modale** | 3 | Comment / Sous quelle condition | Qualifie le mode d'existence ou de réalisation de la chaîne |

**Syntaxe canonique** : `[Substance][Opérative][Modale]`

La chaîne minimale valide est une **substance seule** (Mode 1).
La chaîne maximale dans NEXUS-ARCHÊ est **3 positions** (Mode 3 constellation ou chaîne condensée complète).

---

## LES 16 GLYPHES NEXUS-ARCHÊ — CLASSIFICATION ET STATUT

Dans NEXUS-ARCHÊ, les 16 glyphes de carte occupent **toujours la position Substance** dans la chaîne finale — ils nomment une structure active. Leur classe STÈLE primaire indique également leur affinité naturelle lorsqu'ils sont utilisés dans d'autres registres de l'écosystème IRIS.

| Glyphe | Mot-code | Classe primaire STÈLE | Statut |
|---|---|---|---|
| ⊥ | LIMITE | Substance | ✓ Confirmé |
| ⊗ | LIER | Substance / Opérative | ✓ Confirmé |
| ↻ | CYCLE | Substance / Opérative | ✓ Confirmé |
| ↺ | RÉFLEXIVITÉ | Substance / Opérative | ✓ Confirmé |
| ⊙ | SOURCE | Substance | ✓ Confirmé |
| ✦ | AXE | Substance | ✓ Confirmé |
| ⊛ | NOEUD | Substance | ✓ Confirmé |
| ⥀ | INVERSER | Substance / Opérative | ✓ Confirmé |
| Ø | VIDE | Substance | ✓ Confirmé |
| ⊘ | NÉGATION | Substance / Modale | ✓ Confirmé |
| ◯ | FORME | Substance | ✓ Confirmé |
| ∿ | MOUVEMENT | Substance / Opérative | ✓ Confirmé |
| ◊ | TRACE | Substance | ✓ Confirmé |
| **▲** | **INTENSITÉ** | **Substance / Modale** | **✓ Confirmé** |
| **⟶** | **TRANSMETTRE** | **Substance / Opérative** | **✓ Confirmé** |
| **✶** | **RÉVÉLER** | **Substance / Opérative** | **✓ Confirmé** |

> **Note** : Les trois glyphes en gras (▲, ⟶, ✶) étaient antérieurement marqués comme incertains dans les versions précédentes du SKILL. Ils sont désormais confirmés définitifs, cohérents avec la logique d'ensemble de l'alphabet STÈLE.

---

## GLYPHES OPÉRATIFS ET MODAUX MINIMAUX

Pour construire des chaînes condensées (substance + opérative + modale), un ensemble minimal de primitives est disponible sans recourir au skill STÈLE complet.

### Opératives minimales

Les glyphes NEXUS-ARCHÊ à affinité opérative peuvent occuper la position 2 dans une chaîne condensée :

| Glyphe | Mot-code | Usage en position opérative |
|---|---|---|
| ∿ | MOUVEMENT | Processus en cours, flux actif |
| ⟶ | TRANSMETTRE | Circulation, passage, propagation |
| ⥀ | INVERSER | Retournement, basculement |
| ↻ | CYCLE | Répétition active, retour en cours |
| ↺ | RÉFLEXIVITÉ | Boucle active, auto-référence en cours |
| ⊗ | LIER | Action de connecter, de tisser |
| ✶ | RÉVÉLER | Action de porter au visible |

### Modales minimales

| Glyphe | Mot-code | Signification |
|---|---|---|
| ◐ | CONDITIONNEL | Sous condition, si et seulement si |
| ⊘ | NÉGATION | En mode d'absence, de refus, de blocage |
| ▲ | INTENSITÉ | En mode amplifié, accéléré, croissant |

> Pour une liste complète des modales STÈLE (latent, urgent, inversé, etc.), consulter le skill STÈLE de l'écosystème IRIS.

---

## SYNTAXES VALIDES DANS NEXUS-ARCHÊ

### Syntaxe 1 — Chaîne condensée (tout mode)

Décrit une structure unique de manière compressée.

```
[S] seul            → structure identifiée, sans qualificatif
[S][O]              → structure + processus en cours
[S][O][M]           → structure + processus + condition
```

Exemples :
- `⊙` → `SOURCE` — une structure d'émergence est active
- `⊛∿` → `NOEUD.MOUVEMENT` — un réseau est en transit
- `⊥∿◐` → `LIMITE.MOUVEMENT.CONDITIONNEL` — un seuil en cours de franchissement, sous condition

### Syntaxe 2 — Chaîne de tension (Mode 2)

Deux substances en relation de tension, séparées par un point.

```
[S₁].[S₂]
```

Exemple : `✦.⊘` → `AXE.NÉGATION` — une hiérarchie active face à une contrainte

### Syntaxe 3 — Chaîne de constellation (Mode 3)

Trois substances en positions positionnelles tient.bouge.manque.

```
[Ce qui tient].[Ce qui bouge].[Ce qui manque]
```

Exemple : `⊗.⥀.⊛` → `LIER.INVERSER.NOEUD`

### Syntaxe 4 — Chaîne de résolution (Mode 4 optionnel)

Chaîne de tension ou de constellation + glyphe de résolution, séparé par un tiret.

```
[Chaîne Mode 2 ou 3] - [Résolution]
```

Exemple : `✦.⊘ - ⊙` → `AXE.NÉGATION - SOURCE`

---

## RÈGLES DE VALIDATION

Une chaîne NEXUS-ARCHÊ est valide si elle satisfait les 4 critères suivants :

1. **Chaque glyphe de substance correspond à une carte ancrée** dans la situation (ancrage observable validé)
2. **L'ordre positionnel est respecté** : substance avant opérative avant modale
3. **La transcription verbale est fournie** en complément de la chaîne glyphique
4. **La chaîne ne mélange pas les syntaxes** : une chaîne condensée n'est pas une chaîne de constellation

---

## EXEMPLES DE CHAÎNES VALIDES ET INVALIDES

| Chaîne | Transcription | Valide ? | Raison |
|---|---|---|---|
| `⊙` | SOURCE | ✓ | Substance seule, minimale |
| `⊙∿◐` | SOURCE.MOUVEMENT.CONDITIONNEL | ✓ | Chaîne condensée complète |
| `⊗.⥀.⊛` | LIER.INVERSER.NOEUD | ✓ | Constellation Mode 3 |
| `✦.⊘ - ⊙` | AXE.NÉGATION - SOURCE | ✓ | Tension + résolution |
| `◐⊙` | CONDITIONNEL.SOURCE | ✗ | Modale en position 1 — invalide |
| `⊙⊛∿◐` | SOURCE.NOEUD.MOUVEMENT.CONDITIONNEL | ✗ | 4 positions — dépasse le maximum |
