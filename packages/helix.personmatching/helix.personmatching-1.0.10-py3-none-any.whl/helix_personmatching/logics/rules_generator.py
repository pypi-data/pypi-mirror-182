from typing import List, Optional

from helix_personmatching.models.rules.attribute_rule import AttributeRule
from helix_personmatching.models.constants import Attribute
from helix_personmatching.models.rules.fixed_score_rule import FixedScoreRule
from helix_personmatching.models.rule import Rule
from helix_personmatching.models.scoring_option import ScoringOption


class RulesGenerator:
    @staticmethod
    def generate_rules(*, options: Optional[List[ScoringOption]] = None) -> List[Rule]:
        """
        generate default match rules
        :return: generated rules for matching
        """

        rules: List[Rule] = [
            AttributeRule(
                name="Rule-001",
                description="given name, family name, gender, dob, zip",
                number=1,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.GENDER,
                    Attribute.BIRTH_DATE,
                    Attribute.ADDRESS_POSTAL_CODE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-002",
                description="given name, dob, address 1, zip",
                number=2,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.ADDRESS_LINE_1,
                    Attribute.ADDRESS_POSTAL_CODE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-003",
                description="given name, date of birth, email",
                number=3,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.EMAIL,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-004",
                description="given name, date of birth, phone",
                number=4,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.PHONE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-005",
                description="given name, family name, year of date of birth, gender, address 1, zip",
                number=5,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE_YEAR,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1,
                    Attribute.ADDRESS_POSTAL_CODE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-006",
                description="given name, family name, dob month, dob date, gender, address 1, zip",
                number=6,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE_MONTH,
                    Attribute.BIRTH_DATE_DAY,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1,
                    Attribute.ADDRESS_POSTAL_CODE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-007",
                description="given name, family name, date of birth, gender, phone",
                number=7,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.PHONE_AREA,
                    Attribute.PHONE_LOCAL,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-008",
                description="first name, last name, date of birth, gender, phone local exchange, phone line",
                number=8,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.PHONE_LOCAL,
                    Attribute.PHONE_LINE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-009",
                description="first name, last name, date of birth, gender, phone area code, phone line",
                number=9,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.PHONE_AREA,
                    Attribute.PHONE_LINE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-010",
                description="given name, dob, gender, address 1 street number, zip, email username, phone line",
                number=10,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1_ST_NUM,
                    Attribute.ADDRESS_POSTAL_CODE,
                    Attribute.EMAIL_USERNAME,
                    Attribute.PHONE_LINE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-011",
                description="given name, dob, gender, address 1 street number, zip, "
                + "phone area code, phone local exchange code",
                number=11,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1_ST_NUM,
                    Attribute.ADDRESS_POSTAL_CODE,
                    Attribute.PHONE_AREA,
                    Attribute.PHONE_LOCAL,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-012",
                description="given name, dob, gender, address 1 street number, zip, phone area code, phone line number",
                number=12,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1_ST_NUM,
                    Attribute.ADDRESS_POSTAL_CODE,
                    Attribute.PHONE_AREA,
                    Attribute.PHONE_LINE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-013",
                description="given name, dob, gender, address 1 street number, zip, "
                + "phone local exchange code, phone line number",
                number=13,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1_ST_NUM,
                    Attribute.ADDRESS_POSTAL_CODE,
                    Attribute.PHONE_LOCAL,
                    Attribute.PHONE_LINE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-014",
                description="family name, date of birth, is adult today flag, gender, address 1, zip, phone",
                number=14,
                attributes=[
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.IS_ADULT_TODAY,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1,
                    Attribute.ADDRESS_POSTAL_CODE,
                    Attribute.PHONE,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-015",
                description="family name, date of birth, is adult today flag, gender, address 1, zip, email",
                number=15,
                attributes=[
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.IS_ADULT_TODAY,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1,
                    Attribute.ADDRESS_POSTAL_CODE,
                    Attribute.EMAIL,
                ],
                weight=1.0,
            ),
            AttributeRule(
                name="Rule-016",
                description="given name, email, phone, dob_year",
                number=16,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.EMAIL,
                    Attribute.PHONE,
                    Attribute.BIRTH_DATE_YEAR,
                ],
                weight=1.0,
            ),
        ]

        if options and len(options) > 0:
            available_extra_rules = [
                FixedScoreRule(
                    name="Rule-050", description="fixed score", number=50, weight=1.0
                )
            ]
            rules.extend(
                [
                    rule
                    for rule in available_extra_rules
                    if any([r for r in options if rule.name == r.rule_name])
                ]
            )

            for option in options:
                matching_rules = [
                    rule for rule in rules if rule.name == option.rule_name
                ]
                if len(matching_rules) > 0:
                    matching_rule = matching_rules[0]
                    matching_rule.weight = option.weight

        return rules
