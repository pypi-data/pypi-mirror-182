from typing import Any, Tuple
from enum import Enum
from .element import Element

class Severity(Enum):
    HIGH = "High"
    VERY_HIGH = "Very High"


class Likelihood(Enum):
    HIGH = "High"


class Threat:
    def __init__(self, id: str, target: Tuple[Any, ...], description: str = "", details: str = "", severity: Severity = Severity.HIGH, likelihood: Likelihood = Likelihood.HIGH, condition: str = "", prerequisites: str = "", mitigations: str = "", example: str = "", references: str = "") -> None:
        self.id = id
        self.description = description
        self.target = target
        self.details = details
        self.severity = severity
        self.likelihood = likelihood
        self.condition = condition

    def apply(self, target: "Element") -> bool:
        if not isinstance(target, self.target):
            return False
        return True

