(art23-contact)=
# Contact

:::{warning} Draft
Draft baseline. Field names, types and statuses are not final.
:::

**Table status:** Required.
**Rows:** preferably one row per Member State; several rows are allowed where necessary.

The Commission, the EEA and their contractors use these details to contact national Reporters
about the report.

The table holds personal data. According to the draft, it is kept in a private dataset and is
available only on a need-to-know basis to users with access to the Member State's dataflow, a
limited number of external consultants, EEA staff working with the dataflow and DG ENV staff.
See the Reportnet 3 privacy policy.

## Contact fields

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Contact_ClassDiagram.mmd
:name: Article23_Contact_ClassDiagram
:caption: Article 23 - Contact - draft
:align: center
```

All fields are Required, shown as `[1]` in {numref}`Article23_Contact_ClassDiagram`
({ref}`art23-requirement-status`).

:::{list-table} Contact fields
:header-rows: 1
:widths: 16 16 30 12 12 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `name`
  - Name
  - Name of the person to contact about the report.
  - string100
  - Required
  - –
* - `institution`
  - Institution
  - Name of the institution the contact person works for.
  - string255
  - Required
  - –
* - `phone`
  - Phone
  - Contact person's phone number.
  - string100
  - Required
  - –
* - `email`
  - E-mail
  - Contact person's e-mail address.
  - Email
  - Required
  - –
:::
