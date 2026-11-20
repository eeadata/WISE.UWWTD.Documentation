(art23-reference)=
# Reference

:::{warning} Draft
Proposal. The draft reporting guidance does not describe a documents dataset; this table follows
the WISE convention used in the other dataflows ({ref}`art23-oi-documents`).
:::

**Table status:** Conditional. Required where a field of the {ref}`art23-descriptive-dataset`
points to a document.
**Rows:** one row per cited place in a document.

A reference identifies a place within a document: a chapter, a section or a bookmark. Fields such
as `programmeReference` and `investmentPlanReference` hold a `referenceCode` from this
table, so several fields can cite different chapters of the same programme without repeating the
document itself.

:::{fieldtable} Article23/Reference
:::
