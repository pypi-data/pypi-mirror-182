from typing import List, Optional, Any

from rapidfuzz import fuzz

from helix_personmatching.logics.rule_attribute_score import RuleAttributeScore
from helix_personmatching.logics.rule_score import RuleScore
from helix_personmatching.logics.scoring_input import ScoringInput
from helix_personmatching.models.rule import Rule


class AttributeRule(Rule):
    def __init__(
        self,
        *,
        name: str,
        description: str,
        number: int,
        attributes: List[str],
        weight: float = 1.0
    ) -> None:
        super().__init__(
            name=name, description=description, number=number, weight=weight
        )
        self.attributes: List[str] = attributes

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

        rule_attribute_scores: List[RuleAttributeScore] = []
        score_avg: float = 0.0
        for attribute in self.attributes:
            rule_attribute_score: RuleAttributeScore = RuleAttributeScore(
                attribute=attribute, score=0.0, present=False, source=None, target=None
            )
            val_source: Optional[str] = getattr(source, attribute)
            val_target: Optional[str] = getattr(target, attribute)

            if val_source and val_target:
                rule_attribute_score.present = True
                # calculate exact string match on "trimmed lower" string values
                # returns a number between 0 and 100
                score_for_attribute = fuzz.ratio(
                    str(val_source).strip().lower(), str(val_target).strip().lower()
                )
                score_avg += score_for_attribute
                rule_attribute_score.score = score_for_attribute
                rule_attribute_score.source = val_source
                rule_attribute_score.target = val_target
            rule_attribute_scores.append(rule_attribute_score)

        score_avg /= len(self.attributes)
        my_score = score_avg * self.weight

        rule_score: RuleScore = RuleScore(
            id_source=str(id_data_source),
            id_target=str(id_data_target),
            rule_name=self.name,
            rule_description=self.description,
            rule_score=my_score,
            rule_unweighted_score=score_avg,
            rule_weight=self.weight,
            attribute_scores=rule_attribute_scores,
        )

        return rule_score
