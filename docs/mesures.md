# Tableau de mesures (semaine 2)

**Règle générale :** aucun chiffre ne doit être inventé. Toutes les données doivent être enregistrées à partir des observations réelles effectuées pendant les deux itérations.

## 1. Conditions de chaque itération

| Élément | Itération A (classique) | Itération B (XP) |
|---|---|---|
| Stories traitées | US1 + US4 | US2 + US3 |
| Durée de travail | À mesurer | À mesurer |
| Nombre de tests écrits | À mesurer | À mesurer |
| Couverture des tests (pytest-cov) | À mesurer | À mesurer |
| Nombre de commits / Pull Requests | À mesurer | À mesurer |

## 2. Indicateurs de mesure

| Mesure | Itération A | Itération B | Source de la preuve |
|---|---|---|---|
| Bugs découverts tardivement | À mesurer | À mesurer | Issues GitHub et historique des commits |
| Temps moyen de feedback | À mesurer | À mesurer | Durée d'exécution de pytest et de la CI |
| Temps de correction des bugs | À mesurer | À mesurer | Journal de travail de l'équipe |
| Tests automatisés réussis | À mesurer | À mesurer | Résultats d'exécution de pytest |
| Pipelines réussis / échoués | À mesurer | À mesurer | Onglet Actions de GitHub |
| Confiance pour modifier le code (échelle de 1 à 5) | À mesurer | À mesurer | Auto-évaluation de chaque développeur |

## 3. Méthode de collecte des données

Pour chaque itération, l'équipe doit :

1. Enregistrer le temps réellement consacré au développement.
2. Compter les tests écrits et vérifier leur résultat d'exécution.
3. Mesurer la couverture des tests à l'aide de `pytest-cov`.
4. Consulter l'historique GitHub pour compter les commits, les Pull Requests et les exécutions du pipeline.
5. Noter les bugs découverts, leur moment de détection et le temps nécessaire à leur correction.
6. Demander à chaque développeur d'évaluer sa confiance pour modifier le code sur une échelle de 1 à 5.

Les données doivent être accompagnées de preuves vérifiables : captures d'écran, résultats de tests, historique GitHub et journal d'itération.

## 4. Limites de l'expérimentation

Plusieurs limites doivent être prises en compte dans l'analyse des résultats :

- **Différence entre les fonctionnalités :** les stories traitées pendant les deux itérations ne sont pas identiques, ce qui peut influencer les résultats.
- **Effet d'apprentissage :** les membres de l'équipe peuvent être plus expérimentés pendant la deuxième itération.
- **Couverture des tests :** une couverture élevée ne garantit pas que les tests vérifient correctement tous les comportements.
- **Taille de l'échantillon :** une expérience courte sur un seul mini-produit ne permet pas de généraliser les résultats à toutes les équipes.
- **Variabilité du travail :** la complexité des fonctionnalités, les interruptions et la répartition des tâches peuvent influencer les mesures.

## 5. Analyse comparative et conclusion

À la fin de la semaine 2, les données des deux itérations seront comparées afin d'étudier l'influence des pratiques XP sur la qualité du code, la détection des défauts et la rapidité du feedback.

Les résultats devront être interprétés avec prudence, en tenant compte des limites de l'expérience. L'objectif est de déterminer si les pratiques techniques mises en œuvre ont facilité les modifications du code et la détection des erreurs.

**Conclusion attendue :** l'analyse devra s'appuyer sur les données réellement observées pour expliquer comment les pratiques XP peuvent contribuer à améliorer la qualité logicielle et la capacité d'adaptation de l'équipe.
