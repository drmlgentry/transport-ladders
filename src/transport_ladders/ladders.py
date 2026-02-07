"""
ladders.py
Ladder family constructors + domain restrictions.

Paper IIIa: completeness criteria for a chosen ladder family.
Paper IIIb: ladders as probe families for certified exclusion results.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Tuple

@dataclass(frozen=True)
class LadderDomain:
    name: str
    m_min: int
    m_max: int
    n_min: int
    n_max: int

def ladder_pairs(domain: LadderDomain) -> Iterable[Tuple[int, int]]:
    for m in range(domain.m_min, domain.m_max + 1):
        for n in range(domain.n_min, domain.n_max + 1):
            yield (m, n)

def default_domain() -> LadderDomain:
    return LadderDomain(
        name="placeholder_box",
        m_min=-5,
        m_max=5,
        n_min=-5,
        n_max=5
    )
