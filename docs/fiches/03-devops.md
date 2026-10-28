# Fiche 3 : DevOps et intégration continue

## 1. Définition
DevOps est une culture et un ensemble de pratiques qui rapprochent **développement** (Dev) et
**exploitation** (Ops) pour livrer plus vite, plus souvent et plus sûrement grâce à
l'automatisation et à la collaboration.

## 2. Notions clés
| Notion | Définition |
|---|---|
| Intégration continue (CI) | Fusionner souvent le code dans le dépôt commun, avec build et tests automatiques à chaque modification |
| Livraison continue (CD) | Garder le logiciel toujours livrable, déploiement validé par un humain |
| Déploiement continu | Déploiement automatique en production après validation du pipeline |
| Pipeline | Suite d'étapes automatisées : récupération, installation, lint, tests, build, déploiement |
| Feedback loop | Délai entre un changement et son résultat |

## 3. Exemple Student Grade API
Pipeline GitHub Actions (`.github/workflows/ci.yml`) :
1. récupération du code ;
2. installation de Python et des dépendances ;
3. contrôle de style (`flake8`) ;
4. tests avec couverture (`pytest --cov`).

## 4. Lien avec l'adaptation
Un pipeline fiable réduit le temps de feedback et donne confiance pour modifier le code.

## 5. Limites
Une CI verte prouve seulement que les tests existants passent. Elle ne remplace ni de bons
tests ni la revue de code.

## 6. Sources
- Humble, J. & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.
- Fowler, M. (2006). « Continuous Integration ». martinfowler.com
- Documentation GitHub Actions. docs.github.com/actions
