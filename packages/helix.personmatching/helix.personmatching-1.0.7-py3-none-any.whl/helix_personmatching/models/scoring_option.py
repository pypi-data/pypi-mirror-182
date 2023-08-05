from dataclasses import dataclass


@dataclass
class ScoringOption:
    rule_name: str
    weight: float
