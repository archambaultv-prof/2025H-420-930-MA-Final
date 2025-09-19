# Épreuve finale - 2025H-420-930-MA

Vous disposez d'un code initial contenant plusieurs faiblesses.
Votre objectif est de produire une version refactorisée en appliquant les
notions enseignées dans le cours.

## Modalités

- Travail individuel.
- Durée : 3 heures.
- Remise du code via Omnivox.
- Notes de cours et documentation Python autorisées.
- Utilisation de l'IA selon la politique du département d'informatique. En gros, vous pouvez
  utiliser des outils d'IA pour poser des questions, mais vous devez écrire votre
  code vous-même. Un code généré par une IA sera considéré comme du plagiat.

## Contexte

Le programme calcule le temps total et le coût de facturation pour des projets
composés de tâches individuelles. Pour l'instant, il ne supporte pas les
sous-projets, ce que vous devrez corriger. De plus, la logique de calcul du
coût est rigide et ne permet pas d'ajouter facilement de nouvelles stratégies
de coût.

Un système de notes est également fourni pour documenter les tâches, mais il
utilise une liste au lieu d'une structure de données appropriée.

### Structure actuelle du code

- `main.py` : Contient une démonstration de l'utilisation des classes.
- `taches.py` : Contient les classes `Tache`, `Projet`.
- `notes.py` : Contient la classe `SystemeNotes`.
- `facturation.py` : Contient le calculateur de facturation.

## Problèmes à résoudre dans le code

Les problèmes sont identifiés par des commentaires `# FIXME ...` dans le code.
Tous les fichiers contiennent des problèmes à résoudre.

Vous ne devez PAS ajouter de logique métier nouvelle hors du cadre décrit (pas
de calculs de bonus supplémentaires, etc.).

Vous pouvez ajouter et/ou modifier des classes, fonctions, méthodes, etc.

## Exigences de conception (OBLIGATOIRE)

Vous **DEVEZ** appliquer les éléments suivants :

1. Patron composite

	- Pour représenter la hiérarchie des tâches et projets :
	  - Tâche simple (feuille) : tâche individuelle avec temps et taux
	  - Projet (composite) : contient d'autres tâches et/ou sous-projets
	- Les deux types doivent implémenter la même interface pour calculer temps et coût

2. Patron Strategy

	- Pour encapsuler le calcul exact du coût d'une tâche ou d'un projet.
	- Utiliser l'injection de dépendances pour fournir la stratégie au
	moment de la création de l'objet.

3. Extensibilité
	
	- L'ajout d'un nouveau type de calcul de coût ou une nouvelle priorité ne doit
	nécessiter AUCUNE modification dans le code de calcul principal (principe ouvert/fermé).

4. Structure de données pour les notes

	- Remplacer la liste par une structure de données plus appropriée.
	- Conserver la classe `SystemeNotes` pour gérer les notes avec ses méthodes.

## Livrables

Le code sera à remettre via Omnnivox le 19 septembre 2025 à 15h15.

Le code doit pouvoir être exécuté via:

```bash
uv run main
```

## Grille d'évaluation

| Critère                               | Points |
|---------------------------------------|--------|
| Patron Composite                      | 30     |
| Patron Strategy                       | 30     |
| Structure de données pour les notes   | 20     |
| Le code fonctionne correctement       | 10     |
| Qualité du code (PEP8, commentaires)  | 10     |