"""Data loader: the empty template database of the SpatialPoints dataflow (reference/schema/template.py)."""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'reference' / 'schema'))
import template  # noqa: E402

with tempfile.TemporaryDirectory() as tmp:
    path = template.build('SpatialPoints', Path(tmp) / template.FILES['SpatialPoints'])
    sys.stdout.buffer.write(path.read_bytes())
