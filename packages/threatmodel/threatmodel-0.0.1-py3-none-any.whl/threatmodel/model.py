from typing import List

from .finding import Finding
from .node import Construct
from .asset import Asset
from .element import Element
from .threat import Threat
from .threatlib import Threatlib
from .result import Result


class Model(Construct):
    def __init__(self, title: str, threatlib: List[Threat] = Threatlib) -> None:
        super().__init__(None, "")

        self.title = title
        self._threatlib = threatlib

    @property
    def assets(self):
        return list(filter(lambda c: isinstance(c, Asset), self.node.find_all()))

    def evaluate(self) -> Result:
        result = Result()

        for c in self.node.find_all():
            if isinstance(c, Element):
                for t in self._threatlib:
                    if t.apply(c):
                        result.add_finding(Finding(c, t))

        return result
