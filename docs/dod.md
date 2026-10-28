# Definition of Done (DoD) technique : version 1.0 (semaine 1)

Une user story n'est **terminée** que si **tous** les critères ci-dessous sont satisfaits.
Chaque critère est **vérifiable** (pas de critère vague du type « le code est propre »).

| # | Critère | Comment le vérifier | Responsable de la vérification |
|---|---------|---------------------|-------------------------------|
| 1 | Le code respecte les conventions de l'équipe (PEP 8). | `flake8 src tests` ne renvoie aucune erreur | Auteur + CI |
| 2 | Les tests automatisés passent avec succès. | `pytest` : 0 échec | CI |
| 3 | Les nouveaux comportements et les cas limites sont testés. | Au moins un test par critère d'acceptation de la story | Relecteur |
| 4 | La revue de code est effectuée. | Pull Request approuvée par un autre membre | Relecteur |
| 5 | Le pipeline CI est vert. | Statut GitHub Actions « success » | CI |
| 6 | La documentation nécessaire est mise à jour. | README / backlog / journal modifiés si impactés | Auteur |
| 7 | Aucun défaut bloquant connu ne reste ouvert. | Aucune issue étiquetée `bloquant` | Équipe |

## Règles d'application

- La DoD s'applique **aux deux itérations** pour que la comparaison reste équitable. Les
  pratiques XP (TDD, binôme) changent *la façon d'atteindre* la DoD, pas la DoD elle-même.
- Toute exception doit être consignée dans la Pull Request avec sa justification.
- La DoD est **révisée en semaine 3** à partir des résultats de l'expérience, pour produire
  une version réutilisable par une équipe Scrum.

## Validation d'équipe

| Membre | Validé | Date |
|---|---|---|
| Membre 1 | [ ] | |
| Membre 2 | [ ] | |
| Membre 3 | [ ] | |
| Membre 4 | [ ] | |
