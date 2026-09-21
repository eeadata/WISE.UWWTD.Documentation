(art23-derogation)=
# Derogation

:::{warning} Draft
Draft baseline. Legal conditions on this page are taken from Directive (EU) 2024/3019.
Field design is not final.
:::

**Table status:** Required in the first programme. After that, the draft asks for the table only
if derogation requests change.
**Rows:** one row per Member State.

The table records whether the Member State extends deadlines, together with the numbers and
documents the Directive requires as justification. The Commission uses it to check whether the
conditions for each extension are met. Under Articles 3(2), 6(3) and 7(4), the Commission must
notify Member States by 31 July 2028 if the conditions are not fulfilled.

The table covers deadline extensions under Articles 3(2), 6(3), 7(4) and 23(1), and less stringent
treatment under Article 6(4). Other derogations in the Directive, such as Article 7(8), are not
part of this table in the draft.

The reference fields may point to a chapter of the programme. Where no extension is requested, report
`noDerogation`: the extension fields are Required.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Derogation_ClassDiagram.mmd
:name: Article23_Derogation_ClassDiagram
:caption: Article 23 - Derogation - draft
:align: center
```

In {numref}`Article23_Derogation_ClassDiagram`, `[1]` marks the Required fields and `[0..1]` the
Optional and Conditional ones ({ref}`art23-requirement-status`).

## Article 3(2) - collecting systems (1 000 to 1 999 p.e.)

Agglomerations of 1 000 to 1 999 p.e. must have collecting systems by 31 December 2035. A Member
State may extend this deadline by up to 8 years where, on 1 January 2025, less than 50 % of these
agglomerations were provided with collecting systems or less than 50 % of their load was
collected, or by up to 10 years where the figure was less than 25 % (12 and 14 years for
Bulgaria, Croatia and Romania). The first programme must then include the number of these
agglomerations lacking complete collecting systems on 1 January 2025, an investment plan, and the
technical or economic reasons.

:::{list-table} Derogation fields - Article 3(2)
:header-rows: 1
:widths: 30 18 22 10 8 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `article3_2DeadlineExtension`
  - Article 3(2) deadline extension
  - Extension of the Article 3(2) deadline.
  - DeadlineExtension_Enum
  - Required
  - {ref}`art23-cl-deadline-ext`
* - `article3_2CompleteCollectingSystem`
  - Agglomerations with complete collecting system
  - Number of agglomerations of 1 000 to 1 999 p.e. with complete collecting systems on
    1 January 2025.
  - nonNegativeValue
  - Conditional
  - See note below the table
* - `article3_2NonCompleteCollectingSystem`
  - Agglomerations lacking complete collecting system
  - Number of agglomerations of 1 000 to 1 999 p.e. lacking complete collecting systems
    on 1 January 2025.
  - nonNegativeValue
  - Conditional
  - See note below the table
* - `article3_2CompleteCollectingSystemLoad`
  - Load with complete collecting system
  - Generated load of the agglomerations with complete collecting systems on
    1 January 2025.
  - nonNegativeValue (p.e.)
  - Conditional
  - See note below the table
* - `article3_2NonCompleteCollectingSystemLoad`
  - Load lacking complete collecting system
  - Generated load of the agglomerations lacking complete collecting systems on
    1 January 2025.
  - nonNegativeValue (p.e.)
  - Conditional
  - See note below the table
* - `article3_2InvestmentPlanReference`
  - Article 3(2) investment plan reference
  - Reference to the plan detailing the investments needed to reach full compliance within
    the extended deadline.
  - referenceCode
  - Conditional
  - Required if `article3_2DeadlineExtension` is not `noDerogation`
* - `article3_2ExtensionReasonReference`
  - Article 3(2) extension reason reference
  - Reference to the technical or economic reasons justifying the extension.
  - referenceCode
  - Conditional
  - Required if `article3_2DeadlineExtension` is not `noDerogation`
:::

The draft condition for the four count and load fields applies when
`article3_2DeadlineExtension` is not `noDerogation`. It asks for either the numbers of
agglomerations or the loads, which mirrors the
two alternative conditions in Article 3(2). It refers to "treated and untreated load", although
the fields describe collected load. See {ref}`art23-oi-derogation`.

## Cultural heritage - Articles 3(2) and 6(3)

Under Article 23(1), a Member State that establishes, while implementing its programme, that the
need to preserve cultural heritage makes it impossible to meet the deadline of Article 3(2) or
6(3) in specific areas must update its programme. The update lists the agglomerations and areas
concerned and gives a detailed justification and an adjusted timeline. Extensions are
area-specific, kept as short as possible and may not exceed 8 years. The updated programme is
submitted by 31 December of the year of the update.

:::{list-table} Derogation fields - cultural heritage
:header-rows: 1
:widths: 30 18 24 10 8 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `article3_2CulturalHeritage`
  - Article 3(2) cultural heritage
  - Declaration that the Article 3(2) deadline must be postponed to preserve cultural
    heritage (Article 23(1)).
  - YesNo
  - Required
  - –
* - `article3_2CulturalHeritageReference`
  - Article 3(2) cultural heritage reference
  - Reference to the list of the agglomerations, detailed justification and adjusted
    timeline.
  - referenceCode
  - Conditional
  - Required if `article3_2CulturalHeritage` = yes
* - `article6_3CulturalHeritage`
  - Article 6(3) cultural heritage
  - Declaration that the Article 6(3) deadline must be postponed to preserve cultural
    heritage.
  - YesNo
  - Required
  - –
* - `article6_3CulturalHeritageReference`
  - Article 6(3) cultural heritage reference
  - Reference to the list of the agglomerations, detailed justification and adjusted
    timeline.
  - referenceCode
  - Conditional
  - Required if `article6_3CulturalHeritage` = yes
:::

## Article 6(3) - secondary treatment (1 000 to 1 999 p.e.)

Discharges from plants treating wastewater from agglomerations of 1 000 to 1 999 p.e. must meet
the secondary treatment requirements by 31 December 2035. The possible extensions and the content
required in the first programme follow the same pattern as Article 3(2), based on secondary
treatment on 1 January 2025.

:::{list-table} Derogation fields - Article 6(3)
:header-rows: 1
:widths: 32 18 22 10 8 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `article6_3DeadlineExtension`
  - Article 6(3) deadline extension
  - Extension of the Article 6(3) deadline.
  - DeadlineExtension_Enum
  - Required
  - {ref}`art23-cl-deadline-ext`
* - `article6_3AgglomerationsWithSecondaryTreatment`
  - Agglomerations with secondary treatment
  - Number of agglomerations of 1 000 to 1 999 p.e. with secondary treatment on
    1 January 2025.
  - nonNegativeValue
  - Conditional
  - Required if `article6_3DeadlineExtension` is not `noDerogation`
* - `article6_3AgglomerationsWithoutSecondaryTreatment`
  - Agglomerations without secondary treatment
  - Number of agglomerations of 1 000 to 1 999 p.e. lacking secondary treatment on
    1 January 2025.
  - nonNegativeValue
  - Conditional
  - Required if `article6_3DeadlineExtension` is not `noDerogation`
* - `article6_3LoadWithSecondaryTreatment`
  - Load with secondary treatment
  - Generated load of these agglomerations meeting the secondary treatment requirements
    on 1 January 2025.
  - nonNegativeValue (p.e.)
  - Conditional
  - Required if `article6_3DeadlineExtension` is not `noDerogation`
* - `article6_3LoadWithoutSecondaryTreatment`
  - Load without secondary treatment
  - Generated load of these agglomerations not meeting the secondary treatment
    requirements on 1 January 2025.
  - nonNegativeValue (p.e.)
  - Conditional
  - Required if `article6_3DeadlineExtension` is not `noDerogation`
* - `article6_3InvestmentPlanReference`
  - Article 6(3) investment plan reference
  - Reference to the plan detailing the investments needed to reach full compliance within
    the extended deadline.
  - referenceCode
  - Conditional
  - Required if `article6_3DeadlineExtension` is not `noDerogation`
* - `article6_3ExtensionReasonReference`
  - Article 6(3) extension reason reference
  - Reference to the technical or economic reasons justifying the extension.
  - referenceCode
  - Conditional
  - Required if `article6_3DeadlineExtension` is not `noDerogation`
:::

Unlike the Article 3(2) fields, all four count and load fields are required here when an extension
is requested.

## Article 6(4) - less stringent treatment

Under Article 6(4), discharges may be subject to less stringent treatment than secondary treatment
until 31 December 2045 where they go into high mountain waters above 1 500 m, certain deep marine
waters in less-populated outermost regions, or come from agglomerations of 1 000 to 1 999 p.e. in
cold climates. The Member State must provide the Commission with detailed studies showing that the
discharges do not adversely affect the environment and human health.

:::{list-table} Derogation fields - Article 6(4)
:header-rows: 1
:widths: 32 18 24 10 8 12

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `article6_4LessStringentTreatment`
  - Article 6(4) less stringent treatment
  - Whether urban wastewater discharges are subject to less stringent treatment under
    Article 6(4).
  - YesNo
  - Required
  - –
* - `article6_4LessStringentStudyReference`
  - Article 6(4) study reference
  - Reference to the study justifying less stringent treatment under Article 6(4), until
    31 December 2045.
  - referenceCode
  - Conditional
  - If `article6_4LessStringentTreatment` = yes
:::

This field concerns less stringent treatment, not a deadline extension.

## Article 7(4) - tertiary treatment in sensitive areas

Article 7(3) requires discharges from agglomerations of 10 000 p.e. and above into areas sensitive
to eutrophication to meet the tertiary treatment requirements in stages, with all agglomerations
by 31 December 2045. A Member State may extend that final deadline by up to 8 years if at least
50 % of the agglomerations concerned did not apply tertiary treatment, or did not meet the
requirements, on 1 January 2025. The first programme must include their number, an investment
plan and the justification. Plants treating 150 000 p.e. and above must still meet the deadlines
of Article 7(1).

:::{list-table} Derogation fields - Article 7(4)
:header-rows: 1
:widths: 32 18 22 10 8 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `article7_4DeadlineExtension`
  - Article 7(4) deadline extension
  - Extension of the Article 7(3), point (d), deadline.
  - DeadlineExtensionArticle7_4_Enum
  - Required
  - {ref}`art23-cl-deadline-ext-7-4`
* - `article7_4AgglomerationsWithTertiaryTreatment`
  - Agglomerations with tertiary treatment
  - Number of agglomerations subject to tertiary treatment that met the requirements on
    1 January 2025.
  - nonNegativeValue
  - Conditional
  - Required if `article7_4DeadlineExtension` is not `noDerogation`
* - `article7_4AgglomerationsWithoutTertiaryTreatment`
  - Agglomerations without tertiary treatment
  - Number of agglomerations subject to tertiary treatment that lacked it or did not meet
    the requirements on 1 January 2025.
  - nonNegativeValue
  - Conditional
  - Required if `article7_4DeadlineExtension` is not `noDerogation`
* - `article7_4InvestmentPlanReference`
  - Article 7(4) investment plan reference
  - Reference to the plan detailing the investments needed to reach full compliance within
    the extended deadline.
  - referenceCode
  - Conditional
  - Required if `article7_4DeadlineExtension` is not `noDerogation`
* - `article7_4ExtensionReasonReference`
  - Article 7(4) extension reason reference
  - Reference to the technical or economic reasons justifying the extension.
  - referenceCode
  - Conditional
  - Required if `article7_4DeadlineExtension` is not `noDerogation`
:::

Both situations, lacking tertiary treatment and not meeting the requirements, count towards
`article7_4AgglomerationsWithoutTertiaryTreatment`, as in Article 7(4)(a).

## Related open issues

* {ref}`art23-oi-derogation` - definition of a complete collecting system, individual systems,
  agglomerations served by one plant, and the expected content of the linked documents.
