from typing import List
from .asset import Asset
from .threat import Threat, Likelihood, Severity

Threatlib: List["Threat"] = list()

INP01 = Threat("INP01", (Asset,), 
    description="Buffer Overflow via Environment Variables",
    details="This attack pattern involves causing a buffer overflow through manipulation of environment variables. Once the attacker finds that they can modify an environment variable, they may try to overflow associated buffers. This attack leverages implicit trust often placed in environment variables.",
    likelihood=Likelihood.HIGH,
    severity=Severity.HIGH,
)

Threatlib.append(INP01)