"""Data loader: the manifest of the spatial points prefill release, with its tag and address."""

import json
import sys

import release

manifest = json.loads(release.read('manifest.json'))
json.dump({**manifest, 'tag': release.TAG, 'url': release.RELEASE_URL}, sys.stdout, ensure_ascii=False)
