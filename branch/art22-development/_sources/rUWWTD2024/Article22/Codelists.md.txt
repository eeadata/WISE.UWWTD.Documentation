(art22-codelists)=
# Codelists

:::{warning} Draft
All codelists on this page are proposals and may still change.
:::

Every codelist below is named as a WISE enumeration type, given under the heading, and gives for
each value the notation to report, a short label and a definition.

Each codelist field takes one value. The yes or no fields use the {ref}`art23-cl-yesno` codelist of
Article 23.

(art22-cl-sewer-system-type)=
## Sewer system type

**Type:** `SewerSystemType`

Used by `collectingSystemType` in {ref}`art22-agglomeration`.

:::{codelist} SewerSystemType
:::

(art22-cl-collecting-system-connection)=
## Collecting system connection

**Type:** `CollectingSystemConnection`

Used by `collectingSystemConnection` in {ref}`art22-uwwtp`.

:::{codelist} CollectingSystemConnection
:::

(art22-cl-disinfection)=
## Disinfection

**Type:** `Disinfection`

Used by `disinfection` in {ref}`art22-uwwtp`.

:::{codelist} Disinfection
:::

(art22-cl-nature-based-solution)=
## Nature based solution

**Type:** `NatureBasedSolution`

Used by `natureBasedSolution` in {ref}`art22-uwwtp`.

:::{codelist} NatureBasedSolution
:::

(art22-cl-performance)=
## Treatment performance

**Type:** `Performance`

Used by `performanceTSS`, `performanceBOD`, `performanceCOD`, `performanceTOC`,
`performanceNitrogen` and `performancePhosphorus` in {ref}`art22-uwwtp`.

:::{codelist} Performance
:::

(art22-cl-poor-performance-reason)=
## Poor performance reason

**Type:** `PoorPerformanceReason`

Used by `poorPerformanceReason` in {ref}`art22-uwwtp`.

:::{codelist} PoorPerformanceReason
:::

(art22-cl-load-method)=
## Load determination method

**Type:** `LoadMethod`

Used by the incoming and discharged load method fields in {ref}`art22-uwwtp`:
`incomingLoadBODMethod`, `dischargedLoadBODMethod`, `incomingLoadCODMethod`,
`dischargedLoadCODMethod`, `incomingLoadTOCMethod`, `dischargedLoadTOCMethod`,
`incomingLoadNitrogenMethod`, `dischargedLoadNitrogenMethod`, `incomingLoadPhosphorusMethod` and
`dischargedLoadPhosphorusMethod`.

:::{codelist} LoadMethod
:::

(art22-cl-receiving-area)=
## Receiving area type

**Type:** `ReceivingArea`

Used by `receivingAreaType` in {ref}`art22-dischargepoint`.

:::{codelist} ReceivingArea
:::
