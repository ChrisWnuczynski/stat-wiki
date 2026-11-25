"""Fail the check suite when a change adds non-standard expectation notation.

See ``expectation_notation.py`` for the diff rule and for which subscripted
``E`` counts as a quantity name. Run from anywhere inside the repository.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import expectation_notation


if __name__ == "__main__":
    sys.exit(expectation_notation.main())
