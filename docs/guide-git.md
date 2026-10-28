# Guide Git de l'Ã©quipe

## 1. CrÃ©ation du dÃ©pÃ´t
1. GitHub â†’ **New repository** â†’ nom `student-grade-api`, visibilitÃ© privÃ©e, ajouter un README.
2. **Settings â†’ Collaborators** : inviter les 3 autres membres.
3. Cloner puis pousser le contenu initial sur `main`.

```bash
git clone https://github.com/Mayssahammed/student-grade-api.git
cd student-grade-api
```

## 2. Protection de la branche `main`
**Settings â†’ Branches â†’ Add branch ruleset / protection rule** pour `main` :
- â˜‘ Require a pull request before merging (1 approbation)
- â˜‘ Require status checks to pass before merging â†’ sÃ©lectionner **Lint et tests**
- â˜‘ Require branches to be up to date before merging

> Le statut Â« Lint et tests Â» n'apparaÃ®t dans la liste qu'aprÃ¨s une premiÃ¨re exÃ©cution de la CI.

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
| FonctionnalitÃ© | `feat/us2-validation` | `feat: ...` |
| Correction | `fix/liste-vide` | `fix: ...` |
| Tests | `test/cas-limites` | `test: ...` |
| Refactoring | `refactor/validation` | `refactor: ...` |
| Documentation | `docs/backlog` | `docs: ...` |

## 5. Ã‰tiquettes (labels) d'issues
`bug`, `bloquant`, `iteration-A`, `iteration-B`, `spike`, `dette-technique`.

## 6. Test volontaire de la CI (preuve pour le rapport)
1. CrÃ©er la branche `test/ci-rouge`.
2. Modifier un test pour qu'il Ã©choue (`assert average([10, 20]) == 99`).
3. Pousser, ouvrir une PR, **capturer l'Ã©cran avec la CI rouge**.
4. Corriger le test, pousser, **capturer l'Ã©cran avec la CI verte**.
5. Fermer la PR sans la fusionner.
