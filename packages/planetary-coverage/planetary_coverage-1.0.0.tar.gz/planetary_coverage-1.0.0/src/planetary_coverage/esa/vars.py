"""ESA variables."""

from pathlib import Path


DATA = Path.home() / '.planetary-coverage' / 'esa-mk'

DATA.mkdir(exist_ok=True, parents=True)
