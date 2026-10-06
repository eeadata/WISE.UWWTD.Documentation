(art23-document)=
# Document

:::{warning} Draft
Proposal. The draft reporting guidance does not describe a documents dataset; this table follows
the WISE convention used in the other dataflows ({ref}`art23-oi-documents`).
:::

**Table status:** Conditional. Required where a field of the {ref}`art23-descriptive-dataset`
points to a document.
**Rows:** one row per document.

Each document is delivered either as a hyperlink to a published document or as a file uploaded to
Reportnet 3. Where a Member State publishes its programme on a national website, report the
hyperlink; where it does not, upload the file.

:::{list-table} Document fields
:header-rows: 1
:widths: 22 18 30 14 8 8

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `documentCode`
  - Document code
  - Unique code of the document. Primary key, cited by the {ref}`art23-reference` table.
  - wiseIdentifier
  - Required
  - –
* - `documentName`
  - Document name
  - Name of the document.
  - string250
  - Required
  - –
* - `hyperlink`
  - Hyperlink
  - Web address of the published document.
  - URL
  - Conditional
  - Required if `documentFile` is empty
* - `documentFile`
  - Document file
  - The document uploaded to Reportnet 3.
  - Attachment
  - Conditional
  - Required if `hyperlink` is empty
:::
