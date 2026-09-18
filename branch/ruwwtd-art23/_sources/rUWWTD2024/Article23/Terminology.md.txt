(art23-terminology)=
# Terminology

## Acronyms

:::{list-table}
:header-rows: 1
:widths: 20 80

* - Acronym
  - Meaning
* - aggl.
  - Agglomeration (Article 2(4))
* - C, NC, PD
  - Compliant, non-compliant, pending deadline - status values used in the draft codelists
    (see {ref}`art23-status-values`)
* - EEA
  - European Environment Agency
* - EPR
  - Extended producer responsibility
* - IS
  - Individual system (Article 2(28))
* - IUWMP
  - Integrated urban wastewater management plan (Article 5)
* - MS
  - Member State
* - NIP
  - National implementation programme (Article 23)
* - p.e.
  - Population equivalent (Article 2(10))
* - PRO
  - Producer responsibility organisation (Article 2(20))
* - RBMP
  - River basin management plan
* - SWO
  - Storm water overflow (Article 2(6))
* - UWWTD
  - Urban Wastewater Treatment Directive (EU) 2024/3019
* - UWWTP
  - Urban wastewater treatment plant
* - 1T, 2T, 3T, 4T
  - Primary, secondary, tertiary and quaternary treatment (Article 2(11) to 2(14))
:::

## Legal definitions

The following definitions from Article 2 of the Directive are used most in this section.

Agglomeration
: An area where the population, expressed in population equivalent, with or without economic
  activities, is sufficiently concentrated for urban wastewater to be collected and conducted to
  one or more urban wastewater treatment plants or final discharge points (Article 2(4)).

Individual system
: A sanitation facility that collects, stores, treats or disposes of domestic wastewater from
  buildings or parts of buildings not connected to a collecting system (Article 2(28)).

Population equivalent (p.e.)
: 1 p.e. is the organic biodegradable load with a five-day biochemical oxygen demand (BOD5) of
  60 g of oxygen per day (Article 2(10)).

Producer responsibility organisation
: A nationally recognised organisation established to enable producers to fulfil their
  obligations under Articles 9 and 10 (Article 2(20)).

Secondary, tertiary and quaternary treatment
: Treatment that reduces biodegradable organic matter, that reduces nitrogen and/or phosphorus,
  and that reduces a broad spectrum of micropollutants, respectively (Article 2(12) to 2(14)).

Storm water overflow
: Discharge of untreated urban wastewater into receiving waters from combined sewers caused by
  precipitation or system failures (Article 2(6)).

## Terms used in the draft reporting format

National implementation programme (NIP)
: The programme each Member State establishes under Article 23. The reported tables summarise it
  and link to the full document (`programmeReference`).

Measure
: An action to reach or maintain compliance, selected from the measure codelists of the
  {ref}`art23-uwwtp` and {ref}`art23-agglomeration` tables.

Investment
: The forecast cost of measures, in million EUR. See {ref}`art23-investments`.

Expected date of compliance
: For a treatment plant, the draft defines it as the date by which 12 months of compliant samples
  are expected (`expectedDatePerformance`).

Organic design capacity
: The design capacity of a plant expressed in p.e. (`expectedCapacity`).

Derogation
: In the {ref}`art23-derogation` table, an extension of a deadline under Article 3(2), 6(3),
  7(4) or 23(1), or less stringent treatment under Article 6(4).

(art23-status-values)=
## Status values C, NC and PD

The codelists for the national self-assessment and for plant and agglomeration status use
three main values:

* **C** - compliant;
* **NC** - non-compliant;
* **PD** - pending deadline, used where the relevant deadline has not yet passed.

The draft does not yet explain when each value applies, how several applicable values are
reported, or what "not yet transposed at national level" means. See {ref}`art23-oi-self-assessment`
and {ref}`art23-oi-status`.

(art23-requirement-status)=
## Requirement status

Each field in the draft has one of three statuses:

Required
: Mandatory. The report cannot be completed without it.

Conditional
: Mandatory only when the stated condition, which depends on other reported data, is met.

Optional
: Desirable, but the report can be submitted without it.

In the class diagrams these statuses are shown as the attribute multiplicity, following the WISE
modelling conventions:

* `[1]` - exactly one value: a Required field;
* `[0..1]` - zero or one value: an Optional field, or a Conditional field, which is required
  only when its condition is met;
* `[1..n]` and `[0..n]` - one or many, and zero or many, distinct values. Multivalued fields are
  reported in Reportnet 3 as a comma-separated list of values.

The diagrams therefore do not distinguish Optional from Conditional fields; the field tables do,
and give the condition.

(art23-notation)=
## Notation, label and definition

Each field and each codelist value is described with the same three columns:

* **Notation** - the name used when reporting the field or value. Notations are written in
  camelCase, acronyms are written out in full, and the name of the table is not repeated in
  them: the contact name is `name` in the Contact table, not `contactName`.
* **Label** - a short human-readable name for the field or value.
* **Definition** - what the field or value means.

Field tables add the data type, the requirement status and any condition or codelist. Codelist
tables add notes. Notations are proposals and are not final ({ref}`art23-oi-naming`).

## Data types

The field tables use the WISE attribute types, as defined for the other WISE dataflows:

* **string*n*** - character string of at most *n* characters, UTF-8 encoded, for example
  `string100`. Plain **string** allows up to 4 000 characters;
* **nonNegativeValue** - a non-negative number. The unit follows in brackets, for example
  a load in p.e. or an amount in million EUR;
* **Percentage** - a value in the interval [0, 100];
* **gYear** - a Gregorian year;
* **date** - a date in the format yyyy-mm-dd;
* **YesNo** - a yes or no answer;
* **Email** - an e-mail address, at most 250 characters, validated with a regular expression;
* **URL** - a web address, at most 2 100 characters, validated with a regular expression;
* **wiseIdentifier** - a WISE identifier of at most 42 characters, starting with the ISO 3166-1
  alpha-2 country code, used here for the codes of plants, agglomerations, documents and
  references;
* **documentCode** - a wiseIdentifier identifying a document of the {ref}`art23-documents-dataset`;
* **referenceCode** - a wiseIdentifier identifying a place within such a document, for example a
  chapter or a bookmark;
* **Attachment** - a file uploaded to Reportnet 3, at most 100 MB, as pdf, xlsx or docx;
* ***Name*_Enum** - a value from the codelist of that name (see {ref}`art23-codelists`).

These types are proposals for aligning Article 23 with the rest of WISE
({ref}`art23-oi-naming`).
