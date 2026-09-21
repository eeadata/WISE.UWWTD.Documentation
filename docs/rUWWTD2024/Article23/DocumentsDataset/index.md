---
html_theme.sidebar_secondary.remove: true
---
(art23-documents-dataset)=
# Documents dataset

The documents dataset follows the standard structure used in various WISE dataflows
({numref}`Article23_Documents_ClassDiagram`):

* The `dcMetadata` table provides the basic Dublin Core metadata elements about the delivery.

  - If required by the data providers, the `licenseDocument` and the `metadataDocument`
    attributes allow the provision of additional information about the dataset.

* The `Document` table allows the upload of documents (for example, PDFs) or the provision of a
  `hyperlink` to a document stored in a publicly accessible national web site.

* The `Reference` table is also standard in the WISE dataflows: the `bookmark` allows the
  identification of the chapter(s), section(s) or page range(s) where the relevant information
  about a `subject` can be found within a document.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Documents_ClassDiagram.mmd
:name: Article23_Documents_ClassDiagram
:caption: Article 23 - Documents
:align: center
```

The fields of the {ref}`art23-descriptive-dataset` that refer to a document - the programme, the
prioritisation methodology, the investment plans, the extension reasons, the cultural heritage
lists, the Article 6(4) study and the risk summary - hold a `referenceCode` from the `Reference`
table rather than a web address ({ref}`art23-oi-documents`). The same document can therefore be
cited from several fields, and a single field can point to one chapter of a larger document.

:::{toctree}
:maxdepth: 1
dcMetadata
Reference
Document
:::
