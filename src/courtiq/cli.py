"""Small command-line demonstration using clearly synthetic player profiles."""
import json
from importlib.resources import files
from .scoring import score_player


def main() -> None:
    sample = json.loads((files("courtiq") / "synthetic_players.json").read_text())
    print("SYNTHETIC DEMO — not real NBA player data or a historical GOAT ranking")
    for player in sorted(sample, key=lambda p: score_player(p["scores"]).overall, reverse=True):
        result = score_player(player["scores"])
        print(f"{player['name']}: {result.overall:.2f}/100")


if __name__ == "__main__":
    main()
