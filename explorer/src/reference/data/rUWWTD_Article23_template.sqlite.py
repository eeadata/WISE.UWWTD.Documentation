"""Data loader: the empty template database of the Article23 dataflow (reference/schema/template.py)."""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'reference' / 'schema'))
import template  # noqa: E402

with tempfile.TemporaryDirectory() as tmp:
    path = template.build('Article23', Path(tmp) / template.FILES['Article23'])
    sys.stdout.buffer.write(path.read_bytes())
