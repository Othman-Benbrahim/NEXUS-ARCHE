# NEXUS-ARCHÊ — Guide d'Activation LLM

> 7 templates d'activation pour différents contextes.
> Chaque template est conçu pour être copié-collé directement dans un LLM disposant du skill NEXUS-ARCHÊ.
> Les parties entre crochets [ ] sont à remplacer par le contenu réel.

---

## Principes d'une bonne activation

**Ce qui produit de bons résultats :**
- Décrire la situation en 3 à 6 phrases avec des éléments concrets (qui, quoi, quand, quel comportement observable)
- Préciser le mode souhaité (1, 2 ou 3) — sinon le LLM choisit le plus adapté
- Accepter que des cartes soient rejetées — un rejet bien documenté est une bonne lecture
- Demander explicitement la chaîne STÈLE et le statut épistémique

**Ce qui produit de mauvaises activations :**
- Descriptions uniquement en termes de ressentis ("je me sens perdu") sans éléments observables
- Demander une "solution" — NEXUS-ARCHÊ identifie des structures, il ne prescrit pas
- Forcer une carte préférée ("analyse avec ÉMERGENCE") — laisser le protocole d'ancrage décider

---

## Template 1 — Activation standard (mode libre)

```
Activez NEXUS-ARCHÊ. Choisissez le mode le plus adapté à la situation.

Situation : [description en 3 à 6 phrases avec des éléments concrets et observables]

Appliquez le protocole complet :
1. Nommez les cartes candidates et leurs ancrages observables
2. Appliquez le test d'anti-résonance à chaque carte retenue
3. Déclarez toute carte sans ancrage comme inactive
4. Formulez l'énoncé structurel (si plusieurs cartes)
5. Produisez la chaîne STÈLE avec transcription verbale
6. Déclarez le statut épistémique (Descriptif / Spéculatif / Performatif)
```

**Usage** : quand vous ne savez pas quel mode choisir. Le LLM sélectionnera le mode en fonction de la complexité de la situation.

---

## Template 2 — Mode 1 : identification de la structure dominante

```
Activez NEXUS-ARCHÊ — Mode 1 (Tirage simple).

Situation : [description en 3 à 5 phrases]

Identifiez la structure dominante. Nommez-en une seule, sauf si deux structures
sont aussi solidement ancrées l'une que l'autre. Dans ce cas, passez en Mode 2.

Protocole attendu :
- Carte retenue + ancrage observable
- Test d'anti-résonance
- Cartes candidates rejetées (le cas échéant)
- Question IRIS de la carte retenue, posée à la situation
- Chaîne STÈLE + transcription
- Statut épistémique
```

**Usage** : quand la situation semble confuse et qu'on cherche à nommer sa structure profonde. Mode le plus rapide.

**Exemple d'échange :**

> **Utilisateur** : Activez NEXUS-ARCHÊ — Mode 1. Situation : Une startup que j'ai fondée il y a 3 ans vient d'accueillir un investisseur majoritaire. La gouvernance change. Mon rôle de CEO est maintenu sur le papier mais la structure décisionnelle est désormais orientée par le board. Je ne sais pas encore ce que ça change vraiment.
>
> **LLM** :
> **Carte retenue** : SEUIL · ⊥ LIMITE
> **Ancrage** : Le changement d'actionnariat majoritaire est un fait juridique irréversible. La structure décisionnelle a basculé — le board a désormais les droits de vote qui confèrent l'autorité finale. Ce n'est pas un processus en cours : c'est un état nouveau.
> **Anti-résonance** : Votre rôle est maintenu et vous décrivez de l'incertitude sur les effets réels — le basculement n'a pas encore produit tous ses effets visibles. Mais la structure formelle du franchissement est accomplie.
> **Question IRIS** : Qu'est-ce qui ne peut plus être défait — et qu'est-ce que ça implique pour la façon dont vous prenez des décisions désormais ?
> **Chaîne STÈLE** : `⊥` → `LIMITE`
> **Statut** : Descriptif

---

## Template 3 — Mode 2 : analyse d'une tension

```
Activez NEXUS-ARCHÊ — Mode 2 (Tirage de tension).

Situation : [description en 3 à 6 phrases]

Je perçois une tension entre [élément A] et [élément B] — ou identifiez vous-même
la tension structurelle.

Protocole attendu :
- Deux cartes retenues avec leurs ancrages respectifs
- Test d'anti-résonance pour chacune
- Énoncé structurel de tension (formulé en termes structurels précis, pas en métaphore)
- Nature de la relation : conflit / inclusion / couplage symbiotique / autre
- Chaîne STÈLE à deux glyphes + transcription
- Statut épistémique
```

**Usage** : quand une tension est perceptible entre deux dynamiques dans une situation. Mode intermédiaire.

---

## Template 4 — Mode 3 : constellation complète

```
Activez NEXUS-ARCHÊ — Mode 3 (Tirage de constellation).

Situation : [description en 5 à 8 phrases, suffisamment détaillée pour identifier trois plans structurels]

Produisez une constellation Ce qui tient / Ce qui bouge / Ce qui manque.

Protocole attendu :
- Trois cartes avec leurs positions et leurs ancrages observables
- Test d'anti-résonance pour chacune
- Vérification des configurations pathologiques (Miroir / Immobilité / Lacune contradictoire / Tension maximale)
- Énoncé structurel de constellation
- Chaîne STÈLE à trois glyphes + transcription
- Proposition de Mode 4 si une configuration pathologique est identifiée
- Statut épistémique
```

**Usage** : quand la situation est complexe et nécessite une cartographie de ses plans structurels simultanés.

---

## Template 5 — Compression STÈLE post-tirage

```
J'ai réalisé le tirage NEXUS-ARCHÊ suivant :

Cartes retenues : [liste des cartes avec leurs positions]
Énoncé structurel : [votre formulation]

Compressez ce tirage en une chaîne STÈLE valide selon les règles de stele_rules.md.

Attendu :
- Identification de la syntaxe applicable (condensée / tension / constellation / résolution)
- Chaîne glyphique
- Transcription verbale mot-code
- Vérification de la validité syntaxique (ordre des classes, nombre de positions)
```

**Usage** : quand le tirage a été réalisé manuellement et qu'on cherche uniquement la compression finale.

---

## Template 6 — Intégration OSINT / Superforecasting

```
Avant d'analyser la situation suivante avec les outils OSINT ou de prédiction,
activez NEXUS-ARCHÊ en Mode [1/2/3] pour identifier la structure invariante de fond.

Situation : [description de l'objet d'analyse — acteur, événement, dynamique]

La structure identifiée par NEXUS-ARCHÊ servira de cadre d'ancrage pour :
- L'analyse OSINT : identifier à quelle structure appartient le signal observé
- Le Superforecasting : formuler les hypothèses depuis la structure de la situation, pas seulement depuis les événements

Attendu :
1. Tirage NEXUS-ARCHÊ complet (cartes + chaîne STÈLE)
2. Traduction structurelle : comment cette structure oriente-t-elle l'analyse ?
3. Questions prioritaires que la structure impose à l'investigation OSINT
```

**Usage** : en amont d'une analyse stratégique ou prédictive. NEXUS-ARCHÊ nomme le type de situation avant que l'analyse prospective ne commence.

**Exemple de traduction structurelle :**

> Tirage : PÉRIODICITÉ + CONTRAINTE (Mode 2) sur une situation de blocage institutionnel récurrent
>
> Traduction pour OSINT : chercher non pas les causes du blocage actuel, mais le rythme du cycle (à quelle fréquence ce type de blocage apparaît-il ? à quelle phase du cycle sommes-nous ?). Chercher les contraintes institutionnelles qui ont changé de forme sans changer de nature.
>
> Questions prioritaires : Quel était l'état du système au cycle précédent ? Qu'est-ce qui a déclenché la sortie du blocage la dernière fois ? La contrainte actuelle est-elle nouvelle ou renommée ?

---

## Template 7 — Intégration Fractales du Destin

```
J'ai réalisé un tirage Fractales du Destin avec les cartes suivantes :
[liste des cartes FdD avec leurs positions]

Activez NEXUS-ARCHÊ pour identifier la structure invariante sous-jacente à ce tirage.

Attendu :
1. Lecture des cartes FdD comme indices d'une structure plus profonde
2. Identification de 1 à 2 cartes NEXUS-ARCHÊ qui nomment la structure sous-jacente
3. Dialogue entre les deux registres : ce que le symbolique (FdD) révèle que le structurel ne nomme pas, et vice versa
4. Chaîne STÈLE de la structure NEXUS-ARCHÊ
5. Question IRIS posée à la situation FdD

Ne pas remplacer la lecture FdD — l'approfondir depuis la structure.
```

**Usage** : pour ajouter un plan structurel rationnel à un tirage oraculaire. Les deux lectures coexistent sans se réduire l'une à l'autre.

**Exemple de dialogue entre registres :**

> FdD : La Tour (rupture soudaine) + L'Étoile (renouveau) — situation de crise professionnelle
>
> NEXUS-ARCHÊ : SEUIL (⊥) — un point de non-retour structurel est actif
>
> Dialogue : FdD nomme la rupture et son potentiel de renouveau (registre symbolique-narratif). NEXUS-ARCHÊ confirme que la rupture est structurellement irréversible (registre structurel). Ce que FdD dit que NEXUS-ARCHÊ ne dit pas : il y a un potentiel de lumière après le franchissement (L'Étoile). Ce que NEXUS-ARCHÊ dit que FdD ne dit pas : le basculement est une propriété du système, pas seulement un événement subi.

---

## Tableau récapitulatif des templates

| Template | Mode | Contexte d'usage | Complexité |
|---|---|---|---|
| 1 — Standard | Libre | Exploration générale | ★★ |
| 2 — Mode 1 | 1 | Structure dominante à nommer | ★ |
| 3 — Mode 2 | 2 | Tension perceptible à analyser | ★★ |
| 4 — Mode 3 | 3 | Situation complexe multi-plans | ★★★ |
| 5 — Compression STÈLE | Post-tirage | Tirage réalisé, compression manquante | ★ |
| 6 — OSINT / Forecasting | 1, 2 ou 3 | Avant analyse stratégique ou prédictive | ★★★ |
| 7 — Fractales du Destin | 1 ou 2 | Après tirage FdD, approfondissement structurel | ★★ |
