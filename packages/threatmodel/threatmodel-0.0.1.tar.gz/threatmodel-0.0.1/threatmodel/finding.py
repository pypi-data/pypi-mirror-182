from .element import Element
from .threat import Threat

class Finding:
    def __init__(self, element: Element, threat: Threat) -> None:
        self.target = element.name
        self.description = threat.description
        self.details = threat.details
        self.severity = threat.severity

    def __str__(self) -> str:
        return f"'{self.target}': {self.description}\n{self.details}\n{self.severity}"