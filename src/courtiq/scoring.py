"""Transparent scoring mechanics, NOT a validated historical player ranking."""
from dataclasses import dataclass
from math import isfinite
from typing import Mapping

DIMENSIONS = ("era_performance", "playoffs", "accolades", "championships", "longevity")
DEFAULT_WEIGHTS = {
    "era_performance": 30.0,
    "playoffs": 25.0,
    "accolades": 20.0,
    "championships": 15.0,
    "longevity": 10.0,
}


@dataclass(frozen=True)
class ScoreResult:
    overall: float
    normalized_weights: dict[str, float]
    contributions: dict[str, float]
    dimension_scores: dict[str, float]


def _check_keys(values: Mapping[str, float], kind: str) -> None:
    if set(values) != set(DIMENSIONS):
        missing = sorted(set(DIMENSIONS) - set(values))
        extra = sorted(set(values) - set(DIMENSIONS))
        raise ValueError(f"{kind} must have exactly five dimensions; missing={missing}; extra={extra}")


def _number(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    result = float(value)
    if not isfinite(result):
        raise ValueError(f"{name} must be a finite number")
    return result


def score_player(
    scores: Mapping[str, float], weights: Mapping[str, float] | None = None
) -> ScoreResult:
    """Score five ALREADY-NORMALIZED 0–100 category scores.

    Positive custom weights are normalized to sum to 1. This is only a
    calculation engine: collecting, era-adjusting and validating real historical
    inputs is future work. Missing inputs are rejected, not imputed as zero.
    """
    _check_keys(scores, "scores")
    supplied_weights = DEFAULT_WEIGHTS if weights is None else weights
    _check_keys(supplied_weights, "weights")
    clean_scores = {k: _number(scores[k], f"scores.{k}") for k in DIMENSIONS}
    for key, value in clean_scores.items():
        if not 0 <= value <= 100:
            raise ValueError(f"scores.{key} must be between 0 and 100")
    clean_weights = {k: _number(supplied_weights[k], f"weights.{k}") for k in DIMENSIONS}
    if any(value < 0 for value in clean_weights.values()):
        raise ValueError("weights cannot be negative")
    total = sum(clean_weights.values())
    if total <= 0:
        raise ValueError("at least one weight must be greater than zero")
    normalized = {k: clean_weights[k] / total for k in DIMENSIONS}
    contributions = {k: clean_scores[k] * normalized[k] for k in DIMENSIONS}
    return ScoreResult(
        overall=sum(contributions.values()),
        normalized_weights=normalized,
        contributions=contributions,
        dimension_scores=clean_scores,
    )
