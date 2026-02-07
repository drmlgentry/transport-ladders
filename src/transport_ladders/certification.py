"""
certification.py
Minimal polynomial recognition hooks + root separation / uniqueness margins.

v1 scaffold returns None; wire this to your minpoly + root-separation toolchain.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Certificate:
    poly: str
    root_repr: str
    eps: float
    margin: float

def certify_float(_x: float) -> Optional[Certificate]:
    # Placeholder: replace with minpoly + root-separation checks.
    return None
