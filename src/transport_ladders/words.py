"""
words.py
Finite words over num_gens generators, enumerated up to max_len.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Tuple

@dataclass(frozen=True)
class Word:
    letters: Tuple[int, ...]

    def __len__(self) -> int:
        return len(self.letters)

def iter_words(num_gens: int, max_len: int) -> Iterable[Word]:
    if num_gens <= 0:
        raise ValueError("num_gens must be >= 1")

    # empty word
    yield Word(tuple())

    if max_len <= 0:
        return

    # length-1
    frontier = [Word((i,)) for i in range(num_gens)]
    for w in frontier:
        yield w

    # length >= 2
    for _L in range(2, max_len + 1):
        new_frontier = []
        for w in frontier:
            for i in range(num_gens):
                ww = Word(w.letters + (i,))
                new_frontier.append(ww)
                yield ww
        frontier = new_frontier
