from typing import Optional, Any

from helix_personmatching.logics.rule_score import RuleScore
from helix_personmatching.logics.scoring_input import ScoringInput
from helix_personmatching.models.rule import Rule


class FixedScoreRule(Rule):
    def __init__(
        self, *, name: str, description: str, number: int, weight: float = 1.0
    ) -> None:
        super().__init__(
            name=name, description=description, number=number, weight=weight
        )
        self.weight: float = weight

    def score(self, source: ScoringInput, target: ScoringInput) -> Optional[RuleScore]:
        """
        Calculate a matching score for one rule between FHIR Person-Person, or Person-Patient, or Person/Patient-AppUser
        :param source: Dictionary of Pii data for FHIR Person/Patient data, or AppUser data
        :param target: Dictionary of Pii data for FHIR Person/Patient data, or AppUser data
        :return: Dictionary of 1 rule score result
        """

        id_data_source: Optional[Any] = source.id_
        id_data_target: Optional[Any] = target.id_
        if not (id_data_source and id_data_target):
            return None

        rule_score: RuleScore = RuleScore(
            id_source=str(id_data_source),
            id_target=str(id_data_target),
            rule_name=self.name,
            rule_description=self.description,
            rule_score=100.0 * self.weight,
            rule_unweighted_score=100.0,
            rule_weight=self.weight,
            attribute_scores=[],
        )

        return rule_score
