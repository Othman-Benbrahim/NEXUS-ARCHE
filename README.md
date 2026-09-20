# NEXUS-ARCHÊ

**Système de lecture résonante des structures invariantes**

NEXUS-ARCHÊ est un outil d'analyse structurelle à double registre, conçu pour identifier les patterns qui organisent une situation en les faisant résonner simultanément dans deux langages : les mathématiques des systèmes et les universaux comportementaux humains documentés par Donald Brown.

---

## Ce que c'est

16 cartes structurelles, chacune portant :
- Une structure mathématique précise (attracteur, réseau, bifurcation...) avec sa branche mathématique explicite
- Un universel comportemental documenté (Brown, *The Universal People*, 1991)
- Un glyphe STÈLE primaire pour la compression symbolique
- Une Question IRIS pour activer la lecture
- Des critères de distinction avec les cartes proches (À ne pas confondre avec)

Le mécanisme est **résonant, non narratif** : les cartes décrivent simultanément les structures actives d'une situation, sans raconter une histoire.

---

## Démarrage rapide

### Prompt d'activation (pour LLM)

```
Activez NEXUS-ARCHÊ. Situation : [décrire la situation en 3 à 5 phrases].
Mode demandé : [1 / 2 / 3]. Modalité : [aléatoire / délibératif].
```

### Exemple minimal (Mode 1, délibératif)

```
Activez NEXUS-ARCHÊ. Situation : Un projet a démarré sans plan directeur.
Des rôles émergent naturellement. Personne ne coordonne vraiment mais ça
fonctionne. Mode 1. Modalité délibérative.

→ Carte : ÉMERGENCE · ⊙ SOURCE
→ Ancrage : les rôles se sont constitués spontanément sans désignation.
→ Anti-résonance : un initiateur a posé le cadre de départ — l'émergence
   est partielle.
→ Chaîne STÈLE : ⊙ → SOURCE
→ Statut : Descriptif
```

Pour des templates d'activation avancés (Mode 2/3, OSINT, Fractales du Destin), voir `references/prompt_guide.md`.

### Questions IRIS directes (sans tirage formel)

Si la situation est déjà claire, poser directement la Question IRIS de la carte suspectée :

- *Quelle structure tient tout en place ici — et est-ce qu'elle tient encore ?* → HIÉRARCHIE
- *Qu'est-ce qui est en train d'apparaître sans qu'on l'ait décidé ?* → ÉMERGENCE
- *Quel cycle se rejoue — et à quel point du cycle es-tu ?* → PÉRIODICITÉ

---

## Positionnement dans l'écosystème IRIS

| Skill | Ce qu'il fait |
|---|---|
| Fractales du Destin | Lecture oraculaire symbolique |
| Miroir-Trans-Échelle | Pont entre FdD et registre analytique |
| **NEXUS-ARCHÊ** | Identification des structures invariantes — registre propre, autonome |
| STÈLE | Compression glyphique des sorties |
| OSINT-Intel | Analyse stratégique — NEXUS-ARCHÊ identifie la structure avant l'analyse |
| Superforecasting | Prédiction — NEXUS-ARCHÊ nomme le type de situation avant de projeter |

---

## Dépendances

### Dépendances internes à ce dépôt (autonomes)

| Fichier | Rôle |
|---|---|
| `references/stele_rules.md` | Règles syntaxiques STÈLE minimales — autonomes, utilisables sans le skill STÈLE |
| `references/cards.md` | Les 16 fiches complètes |
| `references/protocol.md` | Protocole de tirage complet |
| `references/examples.md` | Exemples annotés |
| `references/test_log.md` | Journal de tests — 10 situations documentées |
| `references/calibration.md` | Calibration des distinctions inter-cartes |
| `references/antagonismes.md` | Antagonismes structurels et configurations pathologiques |
| `references/prompt_guide.md` | Guide d'activation LLM — 7 templates |

### Dépendances externes (écosystème IRIS)

| Skill | Nature de la dépendance | Requis ? |
|---|---|---|
| **STÈLE** | Grammaire STÈLE complète (modales avancées, règles étendues) | Non — `stele_rules.md` couvre l'usage de base |
| Fractales du Destin | Complémentarité oraculaire | Non — optionnel |
| OSINT-Intel | Analyse prédictive post-structurelle | Non — optionnel |

> NEXUS-ARCHÊ est utilisable de façon entièrement autonome à partir de ce dépôt seul.

---

## Contenu du dépôt

```
SKILL.md                      — Fichier principal : architecture, cartes, protocole résumé
README.md                     — Ce fichier
CHANGELOG.md                  — Historique des versions (v0.1 → v0.2 → v0.3 → v0.3.1)
references/
  cards.md                    — Les 16 fiches complètes (+ branche mathématique + distinctions)
  protocol.md                 — Protocole de tirage complet (modes 1-4, configurations pathologiques)
  stele_rules.md              — Règles syntaxiques STÈLE autonomes pour NEXUS-ARCHÊ
  examples.md                 — Tirages annotés : Mode 1, Mode 2, Mode 3 + tirage rejeté
  test_log.md                 — 10 situations documentées, couverture des 16 cartes, bilan
  calibration.md              — Matrice de risque, faux positifs, journal de calibration (template)
  antagonismes.md             — Incompatibilités structurelles, configurations pathologiques du Mode 3
  prompt_guide.md             — 7 templates d'activation LLM
```

---

## Fondements

- **Mathématiques** : systèmes dynamiques, topologie, théorie des graphes, probabilité, algèbre des transformations, physique des oscillateurs couplés — voir tableau détaillé dans `SKILL.md`
- **Anthropologie** : Donald Brown (*The Universal People*, 1991) — universaux comportementaux documentés
- **Symbolique** : Alphabet STÈLE (écosystème IRIS) — règles autonomes dans `references/stele_rules.md`

---

## Statut et roadmap

**Version actuelle** : v0.3.1

Voir `CHANGELOG.md` pour l'historique complet des modifications.

### Roadmap v0.4

- Alimentation du journal de calibration avec des situations réelles (objectif : 50 entrées)
- Alimentation du journal des antagonismes ; révision de la définition du voisinage documenté (configuration 2) sur données réelles
- Révision des distinctions inter-cartes à risque élevé selon les données de calibration empirique
- Interface de tirage interactif (optionnel — selon retours d'usage)

---

*Projet IRIS — Dépôt public, usage libre.*
