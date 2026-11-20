# rUWWTD data explorer

An [Observable Framework](https://observablehq.com/framework/) app, published with the documentation
under `explorer/`: <https://eeadata.github.io/WISE.UWWTD.Documentation/explorer/>.

**Under development.** Every page says so, and the spatial points pages say that the prefill is
provisional data under Member State review, not an EEA publication.

| Section | Pages | Data |
| --- | --- | --- |
| Reference data | `src/reference/codelists.md`, `src/reference/fields.md` | The CSV files of `reference/codelist` and `reference/schema`, read at build time |
| Spatial points prefill | `src/spatial/agglomerations.md`, `uwwtps.md`, `discharge-points.md` | The Parquet files of a prefill release, downloaded at build time |

The pages link to the documentation, and the documentation links to them
(`docs/_ext/explorer.py`). All links are relative, so a branch preview links to its own pages.

## Building it

Node.js 18 or later and Python 3:

```sh
cd explorer
npm ci
npm run dev      # preview at http://127.0.0.1:3000, rebuilt on every change
npm run build    # the site in dist/
```

The documentation workflow builds it after the Sphinx build and copies `dist/` into the published
site under `explorer/`. Links to the documentation only work there; in `npm run dev` they lead
nowhere.

## Data

**Reference data.** `src/reference/data/reference.json.py` reads the code lists, field tables and
types, and the labels of the documentation pages, so that the explorer links each one to its
definition. `reference.zip.py` packs the CSV files for download. Nothing to do: a change to a CSV
file shows in the next build.

**Spatial points prefill.** The prefill holds provisional Member State data and is not in git. Each
version is a GitHub release of this repository whose files are made from a prefill baseline; the
data loaders in `src/spatial/data/` download them (`release.py` names the release). To make a new
version:

1. Make the files from the baseline made by `prefill/spatial/prefill_spatial.py`. This needs the
   DuckDB command-line tool:

   ```sh
   python3 explorer/scripts/prefill_release.py prefill/spatial/output/SpatialPoints_2024_baseline /tmp/prefill-release
   ```

2. Check them locally, without publishing them:

   ```sh
   cd explorer
   PREFILL_RELEASE_DIR=/tmp/prefill-release npm run dev
   ```

3. Publish them as a pre-release, with the README as release notes:

   ```sh
   gh release create spatialpoints-prefill-2024-v0.2 --prerelease \
     --title "Spatial points prefill, reference year 2024, v0.2 (provisional)" \
     --notes-file /tmp/prefill-release/README.md /tmp/prefill-release/*.parquet /tmp/prefill-release/manifest.json
   ```

4. Set `TAG` in `src/spatial/data/release.py` to the new tag, and push.

Releases are named `spatialpoints-prefill-<reference year>-v<major>.<minor>`. The files of a release
are public: publish one only for data that may be shown, as provisional, to reporters.
