# Fiche 4 : Qualité logicielle et dette technique

## 1. Définitions
- **Qualité logicielle :** capacité du logiciel à répondre au besoin tout en restant fiable,
  maintenable et testable (cf. ISO/IEC 25010).
- **Dette technique :** coût futur induit par des raccourcis ou des choix de conception pris
  aujourd'hui. Métaphore proposée par Ward Cunningham (1992) : on emprunte du temps, et on
  paie des « intérêts » à chaque modification ultérieure.

## 2. Sources de dette technique
| Source | Exemple |
|---|---|
| Absence de tests | Peur de modifier le code |
| Code dupliqué | Un correctif à appliquer à plusieurs endroits |
| Conception trop complexe | Nouvelle fonctionnalité difficile à ajouter |
| Documentation absente | Perte de temps à comprendre |
| Intégration tardive | Conflits et bugs découverts à la fin |

## 3. Pourquoi « sans qualité, pas d'agilité » ?
Plus la dette s'accumule, plus chaque changement coûte cher. La **vélocité** baisse et
l'équipe perd sa capacité à répondre vite aux changements, ce qui est l'objectif même de
l'agilité.

## 4. Illustration (à remplacer par des observations réelles en semaine 3)
| Situation | Modification d'une règle de validation |
|---|---|
| Avec tests automatisés | Modification + relance des tests : résultat en quelques secondes |
| Sans tests | Vérification manuelle de tous les cas : long et risqué |

> Ne pas citer de durées inventées : utiliser les temps mesurés dans `mesures.md`.

## 5. Mesures liées
Bugs découverts tardivement, temps de correction, confiance pour modifier le code (1–5).

## 6. Sources
- Cunningham, W. (1992). « The WyCash Portfolio Management System ». OOPSLA '92.
- Fowler, M. (2018). *Refactoring* (2e éd.). Addison-Wesley.
- ISO/IEC 25010:2011, Modèle de qualité des systèmes et du logiciel.
