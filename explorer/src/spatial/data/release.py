"""The spatial points prefill release that the explorer shows, and how its files are fetched.

The prefill holds provisional Member State data and is not in git. Each version is published as a
GitHub release of this repository, whose files are made by explorer/scripts/prefill_release.py.
The data loaders next to this file download them when the explorer is built.

To use a local copy instead, for example before a release is published, set PREFILL_RELEASE_DIR to
the folder made by prefill_release.py. Standard library only.
"""

import os
import sys
import urllib.request
from pathlib import Path

REPOSITORY = 'eeadata/WISE.UWWTD.Documentation'
TAG = 'spatialpoints-prefill-2024-v0.2'
RELEASE_URL = f'https://github.com/{REPOSITORY}/releases/tag/{TAG}'


def read(name):
    """The bytes of the release file `name`."""
    local = os.environ.get('PREFILL_RELEASE_DIR')
    if local:
        return (Path(local) / name).read_bytes()
    url = f'https://github.com/{REPOSITORY}/releases/download/{TAG}/{name}'
    with urllib.request.urlopen(url, timeout=120) as response:
        return response.read()


def fetch(name):
    """Write the release file `name` to standard output."""
    sys.stdout.buffer.write(read(name))
