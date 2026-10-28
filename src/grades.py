"""Student Grade API : module de calcul de moyenne.

Semaine 1 : seule la fonction `average` existe, afin de valider
la chaîne d'outils (tests, lint, CI). Les fonctionnalités du backlog
(US1 à US4) seront développées en semaine 2 selon l'itération A
(classique) ou B (XP).
"""


def average(grades):
    """Retourne la moyenne arithmétique d'une liste de notes."""
    if not grades:
        raise ValueError("La liste de notes est vide")
    return sum(grades) / len(grades)
