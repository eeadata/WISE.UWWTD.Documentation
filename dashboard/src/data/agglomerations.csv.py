"""Data loader: the prefilled Agglomeration table of the spatial points migration baseline.

One row per agglomeration, with the prefilled values, its location, the country, and what the
prefill changed: the reported name, the reported location where it was corrected, and the original
code where it was converted. Standard library only.

The baseline is made by prefill/spatial/prefill_spatial.py and is not in git: it holds
provisional Member State data.
PREFILL_BASELINE names its folder; by default prefill/spatial/output/SpatialPoints_2024_baseline.
"""

import csv
import os
import sqlite3
import struct
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
BASELINE = Path(os.environ.get('PREFILL_BASELINE',
                               REPO / 'prefill' / 'spatial' / 'output' / 'SpatialPoints_2024_baseline'))
TABLE = 'Agglomeration'

FIELDS = ['inspireIdLocalId', 'inspireIdNamespace', 'inspireIdVersionId', 'thematicIdIdentifier',
          'thematicIdIdentifierScheme', 'nameTextInternational', 'nameText', 'nameLanguage',
          'beginLifespanVersion', 'endLifespanVersion', 'predecessorsIdentifier',
          'predecessorsIdentifierScheme', 'wiseEvolutionType', 'designationPeriodBegin',
          'designationPeriodEnd', 'zoneType', 'specialisedZoneType']


def point(blob):
    """Longitude and latitude of a GeoPackage point geometry."""
    if blob is None:
        return None, None
    flags = blob[3]
    envelope = {0: 0, 1: 32, 2: 48, 3: 48, 4: 64}[(flags >> 1) & 7]
    wkb = blob[8 + envelope:]
    order = '<' if wkb[0] == 1 else '>'
    if struct.unpack(order + 'I', wkb[1:5])[0] % 1000 != 1:
        return None, None
    x, y = struct.unpack(order + 'dd', wkb[5:21])
    return (None, None) if x != x or y != y else (round(x, 6), round(y, 6))


def side_table(name, key='thematicIdIdentifier'):
    with open(BASELINE / name, encoding='utf-8', newline='') as f:
        return {r[key]: r for r in csv.DictReader(f) if r['table'] == TABLE}


def main():
    gpkg = BASELINE / 'SpatialPoints_2024_baseline.gpkg'
    if not gpkg.exists():
        sys.exit(f'Prefill baseline not found: {gpkg}. Run prefill/spatial/prefill_spatial.py, '
                 'or set PREFILL_BASELINE to its output folder.')
    names = side_table('name_cleaning.csv')
    moved = side_table('coordinate_corrections.csv')
    codes = side_table('code_conversion.csv')

    con = sqlite3.connect(f'file:{gpkg}?mode=ro', uri=True)
    rows = con.execute(f'select geometry, {", ".join(FIELDS)} from {TABLE} order by thematicIdIdentifier')
    out = csv.writer(sys.stdout, lineterminator='\n')
    out.writerow(['countryCode', 'longitude', 'latitude', *FIELDS, 'reportedName', 'nameSteps',
                  'reportedLongitude', 'reportedLatitude', 'originalCode'])
    for geom, *values in rows:
        r = dict(zip(FIELDS, values))
        code = r['thematicIdIdentifier']
        n, m, c = names.get(code, {}), moved.get(code, {}), codes.get(code, {})
        lon, lat = point(geom)
        out.writerow([n.get('countryCode') or code[:2], lon, lat, *values,
                      n.get('reportedName', ''), n.get('steps', ''),
                      m.get('reportedLongitude', ''), m.get('reportedLatitude', ''),
                      c.get('originalCode', '')])


if __name__ == '__main__':
    main()
