from typing import Optional

from helix_personmatching.logics.rule_score import RuleScore
from helix_personmatching.logics.scoring_input import ScoringInput


class Rule:
    def __init__(
        self, *, name: str, description: str, number: int, weight: float
    ) -> None:
        self.name: str = name
        self.description: str = description
        self.number: int = number
        self.weight: float = weight

    def score(self, source: ScoringInput, target: ScoringInput) -> Optional[RuleScore]:
        raise NotImplementedError()
