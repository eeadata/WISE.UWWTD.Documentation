"""Data loader: the empty template database of the Article22 dataflow (reference/schema/template.py)."""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'reference' / 'schema'))
import template  # noqa: E402

with tempfile.TemporaryDirectory() as tmp:
    path = template.build('Article22', Path(tmp) / template.FILES['Article22'])
    sys.stdout.buffer.write(path.read_bytes())
