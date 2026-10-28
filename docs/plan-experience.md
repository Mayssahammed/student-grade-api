# Protocole de l'expérience (A classique vs B XP)

## Question de recherche
Dans quelle mesure les pratiques techniques d'XP améliorent-elles la capacité d'une équipe
à s'adapter aux changements et à livrer un logiciel de qualité ?

## Hypothèses (à confirmer ou infirmer par les mesures)
- H1 : le TDD et la CI réduisent le nombre de bugs découverts tardivement.
- H2 : la CI réduit le temps de feedback.
- H3 : les tests et le refactoring réduisent la « peur de modifier le code ».

## Conditions communes aux deux itérations
- Même équipe, même langage, mêmes outils, même DoD technique.
- Lots de difficulté comparable (voir `backlog.md`).
- Durée de travail enregistrée pour chaque itération.

## Itération A : développement classique
- Développer sans imposer les tests préalables, tester principalement après.
- Sans binôme obligatoire, intégration moins fréquente.
- Ne pas écrire volontairement du mauvais code.
- Noter bugs, temps de feedback et corrections.

## Itération B : développement XP
- TDD : test rouge → code minimal → test vert → refactoring.
- Binôme avec alternance pilote / navigateur.
- Intégration fréquente, CI surveillée, petits lots.

## Biais et limites à documenter
| Limite | Effet possible | Mitigation |
|---|---|---|
| Effet d'apprentissage entre A et B | B favorisée | Le mentionner dans le rapport |
| Fonctionnalités différentes | Difficulté non identique | Lots de complexité comparable |
| Petit échantillon (4 personnes) | Résultats peu généralisables | Ne pas extrapoler |
| Mesures auto-déclarées (confiance 1–5) | Subjectivité | Présenter comme indicatif |
| Intérêt pour XP | Biais de confirmation | Rapporter honnêtement tout résultat neutre |
