(art23-reference)=
# Reference

:::{warning} Draft
Proposal. The draft reporting guidance does not describe a documents dataset; this table follows
the WISE convention used in the other dataflows ({ref}`art23-oi-documents`).
:::

**Table status:** Conditional. Required where a field of the {ref}`art23-reporting-dataset`
points to a document.
**Rows:** one row per cited place in a document.

A reference identifies a place within a document: a chapter, a section or a bookmark. Fields such
as `programmeReference` and `article3_2InvestmentPlanReference` hold a `referenceCode` from this
table, so several fields can cite different chapters of the same programme without repeating the
document itself.

:::{list-table} Reference fields
:header-rows: 1
:widths: 22 18 30 14 8 8

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `referenceCode`
  - Reference code
  - Unique code of the reference. Primary key, cited by the reporting tables.
  - wiseIdentifier
  - Required
  - –
* - `documentCode`
  - Document code
  - Document the reference points into, from the {ref}`art23-document` table.
  - documentCode
  - Required
  - –
* - `bookmark`
  - Bookmark
  - Chapter, section, page or bookmark within the document.
  - string250
  - Optional
  - –
* - `subject`
  - Subject
  - What the cited place covers, for example the investment plan for Article 3(2).
  - string250
  - Optional
  - –
:::
