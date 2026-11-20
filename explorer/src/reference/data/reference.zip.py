"""Data loader: all the code lists and field tables of the repository, as one zip file.

The files are the CSV sources in reference/codelist and reference/schema, with their README, as
they are in git. Standard library only.
"""

import io
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]

buffer = io.BytesIO()
with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as z:
    for folder in ('codelist', 'schema'):
        root = REPO / 'reference' / folder
        for path in sorted(root.rglob('*')):
            if path.suffix in ('.csv', '.md') and path.is_file():
                z.write(path, f'rUWWTD-reference/{folder}/{path.relative_to(root).as_posix()}')
sys.stdout.buffer.write(buffer.getvalue())
