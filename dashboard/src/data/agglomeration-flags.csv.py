"""Data loader: the quality-check flags of the prefilled Agglomeration table.

One row per agglomeration and failed check, from qc_flags.csv of the spatial points migration
baseline (see agglomerations.csv.py for where the baseline comes from). Standard library only.
"""

import csv
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
BASELINE = Path(os.environ.get('PREFILL_BASELINE',
                               REPO / 'prefill' / 'spatial' / 'output' / 'SpatialPoints_2024_baseline'))


def main():
    path = BASELINE / 'qc_flags.csv'
    if not path.exists():
        sys.exit(f'Prefill baseline not found: {path}. Run prefill/spatial/prefill_spatial.py, '
                 'or set PREFILL_BASELINE to its output folder.')
    out = csv.writer(sys.stdout, lineterminator='\n')
    out.writerow(['countryCode', 'thematicIdIdentifier', 'severity', 'check', 'detail'])
    with open(path, encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            if r['table'] == 'Agglomeration':
                out.writerow([r['countryCode'], r['thematicIdIdentifier'], r['severity'], r['check'],
                              r['detail']])


if __name__ == '__main__':
    main()
