"""
io.py
Deterministic logging, run manifests, and output tables.
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict

def write_manifest(path: str, data: Dict[str, Any]) -> None:
    Path(path).write_text(
        json.dumps(data, indent=2, sort_keys=True),
        encoding="utf-8"
    )
