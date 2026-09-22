[README.md](https://github.com/user-attachments/files/32519045/README.md)
# 🏀 CourtIQ — The GOAT Index

**Can basketball greatness across eras be quantified transparently?** CourtIQ is a portfolio project exploring that question through an inspectable scoring model and an interactive prototype.

> **Current status: V0.1 scoring-engine prototype.** The included players and category scores are **fictional/synthetic**. This repository does **not** currently rank real NBA players or claim to have a validated cross-era methodology.

## The problem

Fans often compare raw statistics, championships, awards and longevity across eras without consistent context. A single unexplained ranking hides subjective value judgments and historical data limitations.

## The solution

An explainable score with five categories, user-adjustable weights and a contribution breakdown. Over time, the product will incorporate sourced, era-adjusted historical data and sensitivity analysis.

## What works today

- Tested Python scoring engine for five already-normalized category inputs, each 0–100.
- Default weights: era-adjusted performance 30%, playoffs 25%, accolades 20%, championships 15%, longevity 10%.
- Custom nonnegative weights, normalized automatically (positive total required).
- Transparent score contributions, strict validation of inputs and missing categories.
- Streamlit demo using three **fictional** player profiles.
- CLI demonstration and automated unit tests.

## Quick start

Requirements: Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -e ".[app]"
streamlit run app.py
```

For the command-line prototype:

```bash
courtiq
```

For tests (no Streamlit dependency needed):

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Formula

`GOAT = Σ (dimension_score × dimension_weight / sum_of_weights)`

The engine accepts **already-normalized** category scores. It does not calculate historical category scores yet. Example:

```python
from courtiq import score_player

fictional_scores = {
    "era_performance": 95,
    "playoffs": 90,
    "accolades": 92,
    "championships": 85,
    "longevity": 74,
}
result = score_player(fictional_scores)
print(result.overall)
print(result.contributions)
```

## Product documentation

- [Product brief](docs/PRODUCT_BRIEF.md)
- [Methodology and limitations](docs/METHODOLOGY.md)
- [Roadmap](docs/ROADMAP.md)
- [Decision log](docs/DECISIONS.md)
- [First GitHub issue](docs/ISSUE_001.md)

## Responsible comparison principles

1. Data sources, seasons and eligibility rules must be traceable.
2. Missing categories are not zeros. This engine rejects missing inputs.
3. Era-relative dominance is not a prediction of how a player would perform today.
4. Award availability, changing league conditions and double-counting must be addressed before publishing historical rankings.
5. Rankings depend on chosen weights; future releases will show sensitivity.

## How to contribute

Open an issue with a reproducible example, source, proposed methodology improvement or usability problem. Never add unsourced player data or claim synthetic demo results reflect actual athletes.

## License

MIT. Basketball statistics, logos, photographs and external data may have their own rights; this repository includes none of those assets.
