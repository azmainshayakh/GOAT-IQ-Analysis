[README.md](https://github.com/user-attachments/files/32519045/README.md)
# 🏀 GOAT-IQ Analysis - The GOAT Index

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

[PRODUCT_BRIEF.md](https://github.com/user-attachments/files/32519281/PRODUCT_BRIEF.md)
[ROADMAP.md](https://github.com/user-attachments/files/32519299/ROADMAP.md)
# CourtIQ — Eight-week delivery roadmap

**Planning window:** September 21–November 15, 2026  
**Status:** Proposed targets, not completed milestones or guaranteed dates.  
**Capacity assumption:** Approximately 10–12 hours/week alongside a full-time job.

## Release strategy

Build an accurate **small** product before a comprehensive but unreliable NBA history database. Protect the distinction between the shipped synthetic demonstration (V0.1) and a sourced historical leaderboard (V1). When a release gate fails, narrow scope, document the blocker, and delay real-player scoring instead of inventing data.

| Week / dates | Outcome | Work to complete | Acceptance / evidence |
| --- | --- | --- | --- |
| **1 · Sep 21–27** | **V0.1 foundation** | Public repository, scoring engine, synthetic demo, tests, README and these product docs. | All needed folders at repository root; tests green in GitHub Actions; synthetic disclaimer visible. **Partially prepared locally; confirm uploads and CI.** |
| **2 · Sep 28–Oct 4** | **Source feasibility** | Evaluate providers, access and use terms; identify 10–15 candidate players; design data dictionary and player-season schema. | Written source/rights decision, initial coverage matrix, no unsourced values committed. |
| **3 · Oct 5–11** | **Era-adjustment prototype** | Build reproducible raw-to-feature pipeline for adequately covered seasons; define cohorts and denominators. | Unit tests on transformations; documented unsupported eras and data exclusions. |
| **4 · Oct 12–18** | **Historical scoring specification** | Define and implement five category transformations, award eligibility and career aggregation; inspect double counting. | Methodology versioned; manual sample cross-checks; full coverage required before ranking. |
| **5 · Oct 19–25** | **Historical alpha** | If the gates pass, show a clearly population-limited real-data leaderboard and player evidence pages. | Each metric traceable to source; coverage warning prominent; reproducible output. Otherwise ship a sourced comparison explorer without a GOAT score. |
| **6 · Oct 26–Nov 1** | **Interactive comparison** | Connect weight sliders to verified scores; add two-player breakdown and shareable configurations if time permits. | Score contribution arithmetic verified; clear results when weights change. |
| **7 · Nov 2–8** | **Usability + robustness** | Test with ~5 fans and an analyst if available; run ranking sensitivity; audit data and explanations. | Dated research log with actual observations; sensitivity report; documented resulting changes. |
| **8 · Nov 9–15** | **V1 release review** | Fix critical findings; improve documentation and screenshots; deploy permitted demo; publish case study and limitations. | Release checklist complete; reproducible source/method versions and tests; live demo only if ready. |

## Milestones and go/no-go checks

### Milestone A — Public, trustworthy prototype (Week 1)
- [ ] README visible at repository root; all five `docs/` links resolve.
- [ ] `app.py`, `pyproject.toml`, `src/`, `tests/` and `.github/workflows/` uploaded at the correct level.
- [ ] GitHub Actions tests run successfully in the **actual GitHub repository**.
- [ ] Demo and README explicitly say player inputs are fictional.

### Milestone B — Data feasibility (Week 2)
- [ ] Document permitted collection, caching and redistribution for chosen sources.
- [ ] Document per-season metric coverage and award availability.
- [ ] Decide eligible player population and minimum evidence standard.

### Milestone C — Real-scoring readiness (Weeks 3–4)
- [ ] Define every 0–100 dimension calculation and normalization population.
- [ ] Test source transformations and independent sample calculations.
- [ ] Agree rules for missing data, era coverage and overlapping categories.
- [ ] Record an explicit release decision in `DECISIONS.md`.

### Milestone D — Public historical release (Weeks 5–8)
- [ ] Present only players meeting the published inclusion standard.
- [ ] Show source provenance and explanations for each score.
- [ ] Run user research and sensitivity checks; document limitations.
- [ ] Demonstrate a live app, reproduce the pipeline and publish a case study.

## Prioritization and dependencies

**Critical path:** Provider permissions → historical coverage → category definitions → data tests → ranked UI → evaluation. The Streamlit presentation can be improved in parallel, but a beautiful leaderboard is not a substitute for defensible data.

**Cut first if behind:** Accounts, social features, player photos, shareable links, large player pool, prediction features. **Do not cut:** source verification, missing-data visibility, calculation tests or synthetic labels.

## After V1 (not committed)

- Expand coverage only where reliable historical comparability is possible.
- Add a peak-vs-career exploration mode and alternative methodology presets.
- Publish a versioned data dictionary and contributor review process.
- Consider broader cohorts, interactive plots and API endpoints after user validation.

## Portfolio evidence to collect

Save real screenshots and a demo GIF; open issues with acceptance criteria; document why scope changed; share test execution results; capture dated user feedback and follow-up experiments. Never report unmeasured user numbers, model accuracy or adoption.

**Next actionable issue:** See [ISSUE_001.md](ISSUE_001.md) for V0.1 verification; create a new GitHub issue for the provider and licensing spike immediately afterward.

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
