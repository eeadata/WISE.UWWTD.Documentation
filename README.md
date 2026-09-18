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
