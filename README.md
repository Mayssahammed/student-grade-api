# Student Grade API

[![CI](https://github.com/Mayssahammed/student-grade-api/actions/workflows/ci.yml/badge.svg)](https://github.com/Mayssahammed/student-grade-api/actions)

Mini-produit expÃ©rimental du **Sujet 3 : Extreme Programming et agilitÃ© technique,
Â« sans qualitÃ©, pas d'agilitÃ© Â»**.

L'objectif n'est pas le produit lui-mÃªme, mais de **mesurer l'effet des pratiques
techniques XP** (TDD, binÃ´mage, intÃ©gration continue, refactoring) en comparant deux
itÃ©rations de dÃ©veloppement : classique (A) et XP (B).

## DÃ©cisions de l'expÃ©rience

| DÃ©cision | Valeur retenue |
|---|---|
| Langage | Python 3.12 |
| Framework de tests | pytest (+ pytest-cov) |
| ContrÃ´le de style | flake8 (PEP 8, 100 caractÃ¨res max) |
| IntÃ©gration continue | GitHub Actions |
| Notes valides | 0 Ã  20 (bornes incluses) |
| Seuil de rÃ©ussite | moyenne â‰¥ 10/20 |
| Ã‰quipe | 4 membres |
| DurÃ©e | 3 semaines |

## Installation

```bash
git clone https://github.com/Mayssahammed/student-grade-api.git
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
| VÃ©rifier le style | `flake8 src tests` |

## Structure

```
student-grade-api/
â”œâ”€â”€ src/grades.py              # code du produit
â”œâ”€â”€ tests/test_grades.py       # tests automatisÃ©s
â”œâ”€â”€ docs/
â”‚   â”œâ”€â”€ backlog.md             # Product Backlog
â”‚   â”œâ”€â”€ dod.md                 # Definition of Done technique
â”‚   â”œâ”€â”€ plan-experience.md     # protocole de comparaison A / B
â”‚   â”œâ”€â”€ mesures.md             # tableau de mesures (semaine 2)
â”‚   â”œâ”€â”€ journal-pairing.md     # journal de programmation en binÃ´me
â”‚   â”œâ”€â”€ guide-git.md           # workflow Git et protection de main
â”‚   â”œâ”€â”€ synthese-theorie.md    # XP / Scrum / DevOps
â”‚   â””â”€â”€ fiches/                # fiches d'Ã©tude
â””â”€â”€ .github/workflows/ci.yml   # pipeline CI
```

## RÃ¨gles d'Ã©quipe

1. Aucune modification directe sur `main` : tout passe par une Pull Request.
2. Une PR nÃ©cessite **1 revue approuvÃ©e** et une **CI verte**.
3. Messages de commit : `feat:`, `fix:`, `test:`, `refactor:`, `docs:`, `ci:`.
4. Convention de codage : PEP 8, noms en anglais dans le code, docstrings en franÃ§ais.
5. On n'invente jamais de chiffres : on enregistre uniquement ce qui est observÃ©.
