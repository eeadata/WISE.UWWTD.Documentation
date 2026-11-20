# rUWWTD spatial points prefill (provisional, under development)

**Provisional and under development. Not an EEA publication.** These files are the prefill of the
first delivery of the rUWWTD spatial points dataflow: the agglomerations, treatment plants and
discharge points already reported under Directive 91/271/EEC, for reference year 2024. That
reporting is provisional and under Member State review. Every object is prefilled as `noChange`,
for the Member State to confirm, correct, retire or replace in its delivery.

They are published so that reporters can look at the prefill before their delivery, in the
[explorer](https://eeadata.github.io/WISE.UWWTD.Documentation/explorer/), and are not to be used as
a reference for the objects themselves.

## Files

| File | Content |
| --- | --- |
| `agglomerations.parquet` | One row per prefilled agglomeration |
| `uwwtps.parquet` | One row per prefilled urban wastewater treatment plant |
| `discharge-points.parquet` | One row per prefilled discharge point |
| `flags.parquet` | One row per object and failed quality check, with its severity and detail |
| `manifest.json` | Row counts, source, dates and the SHA-256 checksum of each file |

Each table has the location (`longitude`, `latitude`, ETRS89 decimal degrees), the fields of the
table, and what the prefill changed: `reportedName` and `nameSteps` where the name was cleaned,
`reportedLongitude` and `reportedLatitude` where the location was corrected, and `originalCode`
where the code was converted to meet the WISE identifier rules.

## Fields

The fields are those of the specification of 13 November 2026, when the prefill was made. The
spatial points tables were since aligned with the UML diagram of 16 November 2026
([documentation](https://eeadata.github.io/WISE.UWWTD.Documentation/rUWWTD2024/SpatialPoints/)).
The differences:

| Table | In these files | In the current specification |
| --- | --- | --- |
| Agglomeration | `specialisedZoneType` (the reported `aggState`) | Removed |
| UWWTP | `conditionOfFacility` | `status` |
| UWWTP | `uwwCapacity` | Moved to a later Article 22 table |
| DischargePoint | `relatedZoneIdentifier`, `relatedZoneIdentifierScheme` | `groupingInstallation` |
| All | – | `link`, and `validFrom`, `validTo` for UWWTP and DischargePoint |

A later release will follow the current specification.
