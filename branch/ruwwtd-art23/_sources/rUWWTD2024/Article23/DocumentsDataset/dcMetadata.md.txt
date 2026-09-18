(art23-dcmetadata)=
# dcMetadata

:::{warning} Draft
Proposal. The draft reporting guidance does not describe a documents dataset; this table follows
the WISE convention used in the other dataflows ({ref}`art23-oi-documents`).
:::

**Table status:** Required.
**Rows:** one row per delivery.

The table provides the basic Dublin Core metadata elements about the delivery: who produced it,
when, under which licence, and the rights held over it. See
{numref}`Article23_Documents_ClassDiagram`.

## dcMetadata fields

:::{list-table} dcMetadata fields
:header-rows: 1
:widths: 24 18 26 14 8 10

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `title`
  - Title
  - Title of the delivery.
  - string
  - Required
  - –
* - `creatorOrganisationName`
  - Creator organisation
  - Name of the organisation that produced the delivery.
  - string
  - Required
  - –
* - `creatorElectronicMailAddress`
  - Creator e-mail address
  - Contact address of the creator organisation.
  - Email
  - Required
  - –
* - `description`
  - Description
  - Free text describing the delivery.
  - string
  - Optional
  - –
* - `created`
  - Created
  - Date the delivery was produced.
  - date
  - Optional
  - –
* - `language`
  - Language
  - Language or languages of the delivery.
  - Language_Enum [1..n]
  - Required
  - –
* - `license`
  - Licence
  - Licence under which the delivery is published.
  - Licence_Enum
  - Required
  - {ref}`art23-cl-licence`
* - `rights`
  - Rights
  - Statement of the rights held over the delivery.
  - string
  - Optional
  - –
* - `rightsHolder`
  - Rights holder
  - Organisation holding those rights.
  - string
  - Optional
  - –
* - `licenseDocument`
  - Licence document
  - Document stating the licence, where it is not one of the standard licences.
  - documentCode [0..n]
  - Optional
  - –
* - `metadataDocument`
  - Metadata document
  - Document holding further metadata about the delivery.
  - documentCode [0..n]
  - Optional
  - –
:::
