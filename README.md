# WISE.UWWTD.Documentation

This repository contains the public documentation of the
**Urban Waste Water Treatment Directive** dataflows.

## Contents

The documentation is organised in two sections, one per Directive.

- **UWWTD - Directive 91/271/EEC** (`docs/UWWTD1991/`): the **Compliance Algorithm**
  (`docs/UWWTD1991/ComplianceAlgorithm/`) used to evaluate reported wastewater data against the
  requirements of the Directive in force until 31 July 2027, with the notation and definitions it
  relies on.
- **rUWWTD - Directive (EU) 2024/3019** (`docs/rUWWTD2024/`): documentation of the electronic
  reporting under the revised Directive. It currently covers **Article 23 - National
  implementation programmes**: draft reporting guidance for the national implementation
  programmes due by 1 January 2028, covering purpose, scope, timing, terminology, the six draft
  reporting tables (Contact, MSSummary, Derogation, UWWTP, Agglomeration, OtherInvestment) with
  field references and codelists, practical guidance on reporting investments, and open issues.
  The content is a draft and is not final.

Information will be added as it becomes available.

## Building the documentation

```sh
pip install -r docs/requirements.txt
sphinx-build -n --keep-going -b html docs _build/html
```

### Build and view locally with one click

Two scripts rebuild the documentation and open it in the browser at `http://127.0.0.1:8765/`.
Both need Python 3. The first run creates a `.venv` folder and installs Sphinx and its
extensions, which can take several minutes; later runs only rebuild.

| System | Script | How to run it |
| --- | --- | --- |
| macOS | `build-docs.command` | Double-click it in Finder |
| Linux | `build-docs.command` | Run `./build-docs.command` in a terminal |
| Windows | `build-docs.bat` | Double-click it in File Explorer |

To open a specific page instead of the home page, set `PAGE` at the top of the script, for
example `rUWWTD2024/SpatialPoints/`.

The scripts never stop another program. If port 8765 is already in use, for example by the
server from an earlier run, the documentation is still rebuilt but no new server is started: the
script says so and stops. Reload the page if the earlier server is still open, or set the
`DOCS_PORT` environment variable to another port. The browser is opened only once the server
answers.

**First-time setup on macOS.** If double-clicking does nothing or macOS refuses to open the file,
make it executable once in Terminal, from the repository folder:

```sh
chmod +x build-docs.command
```

If macOS warns that the file is from an unidentified developer, right-click it, choose **Open**,
and confirm.

**First-time setup on Windows.** Install Python 3 from <https://www.python.org/downloads/> and
tick **Add python.exe to PATH** during installation. The documentation is served from a minimised
window called "Documentation server"; closing it stops the local server.
