# Guide Git de l'équipe

## 1. Création du dépôt
1. GitHub → **New repository** → nom `student-grade-api`, visibilité privée, ajouter un README.
2. **Settings → Collaborators** : inviter les 3 autres membres.
3. Cloner puis pousser le contenu initial sur `main`.

```bash
git clone https://github.com/<ORGANISATION>/student-grade-api.git
cd student-grade-api
```

## 2. Protection de la branche `main`
**Settings → Branches → Add branch ruleset / protection rule** pour `main` :
- ☑ Require a pull request before merging (1 approbation)
- ☑ Require status checks to pass before merging → sélectionner **Lint et tests**
- ☑ Require branches to be up to date before merging

> Le statut « Lint et tests » n'apparaît dans la liste qu'après une première exécution de la CI.

## 3. Cycle de travail quotidien
```bash
git checkout main && git pull
git checkout -b feat/us1-calcul-moyenne
# ... travail ...
git add .
git commit -m "feat: ajoute le calcul de moyenne (US1)"
git push -u origin feat/us1-calcul-moyenne
```
Puis ouvrir une **Pull Request** vers `main`, demander une revue, attendre la CI verte, fusionner.

## 4. Convention de nommage
| Type | Branche | Commit |
|---|---|---|
| Fonctionnalité | `feat/us2-validation` | `feat: ...` |
| Correction | `fix/liste-vide` | `fix: ...` |
| Tests | `test/cas-limites` | `test: ...` |
| Refactoring | `refactor/validation` | `refactor: ...` |
| Documentation | `docs/backlog` | `docs: ...` |

## 5. Étiquettes (labels) d'issues
`bug`, `bloquant`, `iteration-A`, `iteration-B`, `spike`, `dette-technique`.

## 6. Test volontaire de la CI (preuve pour le rapport)
1. Créer la branche `test/ci-rouge`.
2. Modifier un test pour qu'il échoue (`assert average([10, 20]) == 99`).
3. Pousser, ouvrir une PR, **capturer l'écran avec la CI rouge**.
4. Corriger le test, pousser, **capturer l'écran avec la CI verte**.
5. Fermer la PR sans la fusionner.
