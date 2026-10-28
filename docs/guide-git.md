# Guide Git de l’équipe

## 1. Création du dépôt

1. Aller sur GitHub, cliquer sur **New repository**, choisir le nom `student-grade-api`, sélectionner la visibilité privée et ajouter un fichier README.
2. Aller dans **Settings → Collaborators** et inviter les trois autres membres de l’équipe.
3. Cloner le dépôt sur l’ordinateur :

```bash
git clone https://github.com/Mayssahammed/student-grade-api.git
cd student-grade-api
```

Le dépôt sera utilisé par les quatre membres pour partager le code et collaborer sur le projet.

## 2. Protection de la branche `main`

Dans GitHub, aller dans **Settings → Branches → Add branch ruleset** ou dans les paramètres de protection des branches, puis configurer une règle pour la branche `main`.

Activer les options suivantes :

- **Require a pull request before merging** : exiger une Pull Request avant la fusion, avec une approbation.
- **Require status checks to pass before merging** : exiger la réussite des vérifications automatiques et sélectionner **Lint et tests**.
- **Require branches to be up to date before merging** : exiger que la branche soit à jour avant la fusion.

Le statut « Lint et tests » n’apparaît dans la liste qu’après une première exécution réussie ou enregistrée du workflow CI correspondant.

Ces règles permettent de protéger le code principal et de limiter l’intégration de modifications non vérifiées.

## 3. Cycle de travail quotidien

Chaque membre doit créer une branche pour travailler sur une fonctionnalité, une correction ou des tests.

### Étape 1 : récupérer la dernière version

```bash
git checkout main
git pull origin main
```

### Étape 2 : créer une branche de travail

```bash
git checkout -b feat/us1-calcul-moyenne
```

### Étape 3 : développer et enregistrer les modifications

Après avoir modifié le code et exécuté les tests :

```bash
git add .
git commit -m "feat: ajoute le calcul de moyenne (US1)"
```

### Étape 4 : envoyer la branche sur GitHub

```bash
git push -u origin feat/us1-calcul-moyenne
```

### Étape 5 : ouvrir une Pull Request

Sur GitHub, ouvrir une Pull Request vers `main`, demander une revue de code à un autre membre, attendre la réussite de la CI et corriger les éventuels problèmes.

Une fois les modifications approuvées et toutes les vérifications réussies, la Pull Request peut être fusionnée dans `main`.

## 4. Convention de nommage des branches et des commits

L’équipe adopte une convention commune pour faciliter la lecture de l’historique Git.

| Type de modification | Nom de la branche | Exemple de commit |
|---|---|---|
| Fonctionnalité | `feat/us2-validation` | `feat: ajoute la validation des notes` |
| Correction | `fix/liste-vide` | `fix: gère le cas d'une liste vide` |
| Tests | `test/cas-limites` | `test: ajoute les tests des cas limites` |
| Refactoring | `refactor/validation` | `refactor: simplifie la validation` |
| Documentation | `docs/backlog` | `docs: met à jour le backlog` |

Cette convention permet d’identifier rapidement la nature de chaque modification.

## 5. Étiquettes des issues GitHub

Les issues du projet utilisent les étiquettes suivantes :

- `bug` : signaler un défaut.
- `bloquant` : identifier un problème qui empêche la poursuite du travail.
- `iteration-A` : identifier les tâches de l’itération classique.
- `iteration-B` : identifier les tâches de l’itération XP.
- `spike` : identifier une expérimentation technique destinée à réduire une incertitude.
- `dette-technique` : identifier un problème de conception ou de code susceptible d’augmenter le coût des modifications futures.

Ces étiquettes facilitent l’organisation du backlog et le suivi des tâches.

## 6. Test volontaire de la CI : rouge puis vert

L’objectif de cette expérience est de démontrer que l’intégration continue détecte automatiquement un test en échec et confirme ensuite sa correction.

### Étape 1 : créer une branche de test

```bash
git checkout main
git pull origin main
git checkout -b test/ci-rouge
```

### Étape 2 : introduire temporairement une assertion incorrecte

Dans un fichier de test, ajouter ou modifier une assertion :

```python
assert average([10, 20]) == 99
```

Si la fonction renvoie correctement la moyenne de 15, ce test doit échouer.

### Étape 3 : envoyer la modification sur GitHub

```bash
git add .
git commit -m "test: vérifie la détection d'un échec CI"
git push -u origin test/ci-rouge
```

Ouvrir ensuite une Pull Request vers `main` et vérifier que le pipeline CI échoue.

**Preuve à conserver :** effectuer une capture d’écran montrant l’échec des tests et le statut rouge de la CI.

### Étape 4 : corriger le test

Remplacer l’assertion incorrecte par :

```python
assert average([10, 20]) == 15
```

Envoyer la correction :

```bash
git add .
git commit -m "test: corrige l'assertion de moyenne"
git push
```

Vérifier que le pipeline CI s’exécute à nouveau et que les tests réussissent.

**Preuve à conserver :** effectuer une capture d’écran montrant la réussite des tests et le statut vert de la CI.

### Étape 5 : terminer l’expérience

Fermer la Pull Request sans la fusionner dans `main`, puisque cette branche a été créée uniquement pour tester le comportement de la CI.

## 7. Conclusion

Ce workflow Git permet à l’équipe de travailler de manière collaborative et contrôlée. La protection de la branche principale, les Pull Requests, les revues de code et les tests automatisés contribuent à réduire les erreurs et à améliorer la qualité du logiciel.

L’expérience de la CI rouge puis verte constitue une preuve concrète de l’intérêt du feedback rapide. Elle illustre un principe fondamental de l’Extreme Programming : détecter les problèmes tôt afin de limiter le coût des corrections et de conserver la capacité d’adaptation de l’équipe.
