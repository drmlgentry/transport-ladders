"""
coxeter.py
Placeholder Coxeter utilities (expand later).
"""

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class CoxeterSystem:
    name: str

def default_system() -> CoxeterSystem:
    return CoxeterSystem(name="placeholder")
