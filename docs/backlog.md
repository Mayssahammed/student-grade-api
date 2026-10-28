# Product Backlog : Student Grade API

**Produit :** API de calcul de moyenne et de réussite d'un étudiant
**Product Owner (rôle simulé) :** Membre 1 | **Scrum Master (rôle simulé) :** Membre 2
**Seuil de réussite :** 10/20 | **Notes valides :** 0 à 20 inclus

## Backlog initial

| ID | User story | Critères d'acceptation | Priorité (MoSCoW) | Estim. | Lot | Statut |
|----|-----------|------------------------|-------------------|--------|-----|--------|
| US1 | En tant qu'enseignant, je veux calculer la moyenne de plusieurs notes afin d'évaluer un étudiant. | `[10, 20]` → `15.0` ; `[12]` → `12.0` | Must | 1 | À décider | À faire |
| US2 | En tant qu'enseignant, je veux que les notes hors de l'intervalle 0–20 soient refusées afin d'éviter des saisies erronées. | `-1` → erreur ; `21` → erreur ; `0` et `20` acceptés | Must | 1 | À décider | À faire |
| US3 | En tant qu'enseignant, je veux savoir si l'étudiant a réussi afin de décider de sa validation. | moyenne `10` → `True` ; moyenne `9.99` → `False` | Should | 1 | À décider | À faire |
| US4 | En tant que développeur, je veux que la liste vide soit gérée proprement afin d'éviter un crash. | `[]` → exception explicite (`ValueError`) | Should | 1 | À décider | À faire |
| US5 | En tant qu'enseignant, je veux un résumé (moyenne + réussite) en un seul appel afin de gagner du temps. | résumé contenant moyenne arrondie à 2 décimales et booléen de réussite | Could | 2 | Réserve | À faire |

*Échelle d'estimation : points relatifs (1 = très simple, 2 = simple avec petit cas particulier).*

## Répartition prévue des lots (semaine 2)

Les deux lots sont construits pour être de **difficulté comparable** : chacun combine
un calcul et une règle de validation.

| Itération | Stories | Méthode |
|---|---|---|
| **A : classique** | US1 (moyenne) + US4 (liste vide) | Code d'abord, tests après, sans TDD ni binôme imposés |
| **B : XP** | US2 (validation des notes) + US3 (réussite) | TDD, binôme, CI, refactoring, petits lots |

> **Limite à signaler dans le rapport :** les fonctionnalités ne sont pas identiques et
> l'équipe apprend entre A et B (effet d'apprentissage). US5 reste en réserve pour
> d'éventuels tests de changement de besoin en semaine 3.

## Historique des décisions

| Date | Décision | Participants |
|---|---|---|
| JJ/MM | Choix de Student Grade API | Tous |
| JJ/MM | Seuil de réussite fixé à 10/20 | Tous |
| JJ/MM | Répartition des lots A / B | Tous |
