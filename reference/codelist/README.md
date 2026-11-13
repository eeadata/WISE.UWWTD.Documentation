# Code lists

The values of the rUWWTD code lists, one CSV file per code list type. These files are the single
source of the values:

* the documentation shows them: each code list table on the *Codelists* pages of
  [Spatial points](../../docs/rUWWTD2024/SpatialPoints/Codelists.md) and
  [Article 23](../../docs/rUWWTD2024/Article23/Codelists.md) is rendered from its CSV by the
  `{codelist}` directive ([docs/_ext/codelist.py](../../docs/_ext/codelist.py));
* the spatial points prefill ([prefill/spatial](../../prefill/spatial/)) stops if it would write a
  value that is not in its code list;
* the Reportnet 3 schema and quality checks can read the same files.

To add, change or remove a value, edit the CSV. Do not edit the tables in the documentation: they
are generated. The text around each table (what the code list is for, where it comes from) stays
in the documentation page.

## Files

| File | Content |
| --- | --- |
| `<Type>.csv` | The values of one code list, named after its type (`ConditionOfFacility.csv` for `ConditionOfFacility`) |
| `codelists.csv` | Every code list: its type, dataflow, the page anchor it belongs to, the table caption, the column headers shown, their widths and the columns that hold codes |

Code lists:

| Dataflow | Types |
| --- | --- |
| Spatial points | `IdentifierScheme`, `WiseEvolutionType`, `SpecialisedZoneType`, `ConditionOfFacility` |
| Article 23 | `DerogationType`, `DerogationStatus`, `EligibilityCriterion`, `ExtensionReason`, `LessStringentGround`, `ComplianceShare`, `ComplianceShareEstimated`, `RiskAssessment`, `ContributionPeriod`, `PlantAgglomerationStatus`, `UWWTDMeasureType`, `UWWTDGeographicCoverage`, `ImplementationStatus`, `CostStatus`, `Priority`, `EUFund`, `FundingSource`, `FundingStatus`, `CurrencyCode`, `EstimateBasis`, `Licence` |
| Article 23 (correspondence) | `UWWTDMeasureTypeWFD`: each measure type with its WFD key type of measure and main pressure |

Code lists already published in the Eionet Data Dictionary and used as they are, such as the
ISO 639-2 languages of `nameLanguage`, are referenced from the documentation and not copied here.

## Format

* UTF-8, comma-separated, a header row, one row per value, in the order shown.
* Columns: `notation`, `label`, `definition`, `notes` (the correspondence table has its own).
* Codes are written plain (`projected`, not `` `projected` ``); the documentation shows them as code.
* An empty cell means nothing to add; the documentation shows a dash.
* Labels, definitions and notes are documentation text and may use MyST markup, such as a
  cross-reference ``{ref}`sp-oi-zonetype` ``. A tool that exports a code list to Reportnet 3 should
  reduce such markup to plain text.
* A new code list needs its CSV, a row in `codelists.csv`, and a `{codelist}` directive on its page:

  ```
  :::{codelist} ConditionOfFacility
  :::
  ```
