from typing import List
from .finding import Finding

class Result:
    def __init__(self) -> None:
        self.findings: List[Finding] = list() 

    def add_finding(self, finding: Finding) -> None:
        self.findings.append(finding)