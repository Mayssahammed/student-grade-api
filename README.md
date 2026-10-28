# Student Grade API

[![CI](https://github.com/<ORGANISATION>/student-grade-api/actions/workflows/ci.yml/badge.svg)](https://github.com/<ORGANISATION>/student-grade-api/actions)

Mini-produit expérimental du **Sujet 3 : Extreme Programming et agilité technique,
« sans qualité, pas d'agilité »**.

L'objectif n'est pas le produit lui-même, mais de **mesurer l'effet des pratiques
techniques XP** (TDD, binômage, intégration continue, refactoring) en comparant deux
itérations de développement : classique (A) et XP (B).

## Décisions de l'expérience

| Décision | Valeur retenue |
|---|---|
| Langage | Python 3.12 |
| Framework de tests | pytest (+ pytest-cov) |
| Contrôle de style | flake8 (PEP 8, 100 caractères max) |
| Intégration continue | GitHub Actions |
| Notes valides | 0 à 20 (bornes incluses) |
| Seuil de réussite | moyenne ≥ 10/20 |
| Équipe | 4 membres |
| Durée | 3 semaines |

## Installation

```bash
git clone https://github.com/<ORGANISATION>/student-grade-api.git
cd student-grade-api
python -m venv venv
source venv/bin/activate          # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

## Commandes utiles

| Action | Commande |
|---|---|
| Lancer les tests | `pytest -v` |
| Tests + couverture | `pytest --cov=src --cov-report=term-missing` |
| Vérifier le style | `flake8 src tests` |

## Structure

```
student-grade-api/
├── src/grades.py              # code du produit
├── tests/test_grades.py       # tests automatisés
├── docs/
│   ├── backlog.md             # Product Backlog
│   ├── dod.md                 # Definition of Done technique
│   ├── plan-experience.md     # protocole de comparaison A / B
│   ├── mesures.md             # tableau de mesures (semaine 2)
│   ├── journal-pairing.md     # journal de programmation en binôme
│   ├── guide-git.md           # workflow Git et protection de main
│   ├── synthese-theorie.md    # XP / Scrum / DevOps
│   └── fiches/                # fiches d'étude
└── .github/workflows/ci.yml   # pipeline CI
```

## Règles d'équipe

1. Aucune modification directe sur `main` : tout passe par une Pull Request.
2. Une PR nécessite **1 revue approuvée** et une **CI verte**.
3. Messages de commit : `feat:`, `fix:`, `test:`, `refactor:`, `docs:`, `ci:`.
4. Convention de codage : PEP 8, noms en anglais dans le code, docstrings en français.
5. On n'invente jamais de chiffres : on enregistre uniquement ce qui est observé.
