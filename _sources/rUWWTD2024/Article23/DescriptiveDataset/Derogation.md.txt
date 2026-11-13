(art23-derogation)=
# Derogation

:::{warning} Draft
Legal conditions on this page are taken from Directive (EU) 2024/3019. The one-row-per-provision
structure is a proposal, and field design is not final ({ref}`art23-oi-derogation`).
:::

**Table status:** Required in the first programme. After that, the draft asks for the table only
if derogation requests change.
**Rows:** one row per extension provision, three rows per Member State: Articles 3(2), 6(3) and
7(4). `derogationType` is the primary key. A provision under which no extension is requested has a
row with `derogationStatus` = `notRequested`.

The table records whether the Member State extends the deadlines of Articles 3(2), 6(3) and 7(4),
together with the numbers and documents the Directive requires as justification. The Commission
uses it to check whether the conditions for each extension are met: under Articles 3(2), 6(3) and
7(4), it must notify Member States by 31 July 2028 if they are not.

The three provisions ask the same questions, so each is one row with the same fields. A row for a
provision that is not used states explicitly that no extension is requested: an absent row could
not be told apart from an incomplete delivery.

Two other derogations are reported in their own tables:

* extensions to preserve cultural heritage, which arise during the implementation of the
  programme and are listed per agglomeration, in {ref}`art23-culturalheritageextension`;
* less stringent treatment under Article 6(4), which is not a deadline extension, in
  {ref}`art23-lessstringenttreatment`.

Other derogations in the Directive, such as Article 7(8), are not part of the draft.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Derogation_ClassDiagram.mmd
:name: Article23_Derogation_ClassDiagram
:caption: Article 23 - Derogation - draft
:align: center
```

In {numref}`Article23_Derogation_ClassDiagram`, `[1]` marks the Required fields and `[0..1]` the
Optional and Conditional ones ({ref}`art23-requirement-status`).

## What the Directive requires

The three provisions extend a deadline for a requirement on agglomerations. Where a Member State
uses one, the first programme must include the number of agglomerations not meeting the
requirement on 1 January 2025, an investment plan, and the technical or economic reasons
(Articles 3(2), 6(3) and 7(4), and Article 23(1)(e)).

:::{list-table} The three extension provisions
:header-rows: 1
:widths: 14 30 14 42

* - `derogationType`
  - Requirement
  - Deadline
  - Eligibility on 1 January 2025
* - `article3_2`
  - Collecting systems in agglomerations of 1 000 to 1 999 p.e.
  - 31 December 2035
  - Less than 50 % of these agglomerations provided with collecting systems, or less than 50 % of
    their load collected
* - `article6_3`
  - Secondary treatment of discharges from agglomerations of 1 000 to 1 999 p.e.
  - 31 December 2035
  - Less than 50 % of these agglomerations, or of their load, meeting the secondary treatment
    requirements
* - `article7_4`
  - Tertiary treatment of discharges from agglomerations of 10 000 p.e. and above into areas
    sensitive to eutrophication (Article 7(3), point (d))
  - 31 December 2045
  - At least 50 % of the agglomerations concerned not applying tertiary treatment or not meeting
    its requirements
:::

For Articles 3(2) and 6(3) the test is on agglomerations or on load, and the Member State says
which one it relies on in `eligibilityCriterion`. For Article 7(4) it is on agglomerations only.
Plants treating 150 000 p.e. and above must still meet the deadlines of Article 7(1).

The maximum extension follows from the share meeting the requirement:

:::{list-table} Maximum extended deadline
:header-rows: 1
:widths: 14 46 20 20

* - `derogationType`
  - Share on 1 January 2025
  - Maximum extension
  - Latest `extendedDeadlineYear`
* - `article3_2`, `article6_3`
  - 50 % or more meeting the requirement, by agglomerations and by load
  - Not eligible
  - –
* - `article3_2`, `article6_3`
  - Less than 50 % meeting it, by the chosen criterion
  - 8 years (12 for Bulgaria, Croatia and Romania)
  - 2043 (2047)
* - `article3_2`, `article6_3`
  - Less than 25 % meeting it, by the chosen criterion
  - 10 years (14 for Bulgaria, Croatia and Romania)
  - 2045 (2049)
* - `article7_4`
  - At least 50 % of the agglomerations concerned not meeting it
  - 8 years
  - 2053
:::

## Derogation fields

:::{list-table} Derogation fields
:header-rows: 1
:widths: 24 16 28 12 8 12

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `derogationType`
  - Derogation type
  - The provision under which the deadline may be extended.
  - DerogationType
  - Required
  - {ref}`art23-cl-derogation-type`; `article3_2`, `article6_3` or `article7_4`
* - `derogationStatus`
  - Derogation status
  - Whether an extension is requested under the provision.
  - DerogationStatus
  - Required
  - {ref}`art23-cl-derogation-status`
* - `extendedDeadlineYear`
  - Extended deadline
  - The year by the end of which the requirement will be met, under the extension.
  - gYear
  - Conditional
  - Required if `derogationStatus` = `requested`
* - `eligibilityCriterion`
  - Eligibility criterion
  - The criterion on which the Member State relies for eligibility: the share of agglomerations
    or the share of their load.
  - EligibilityCriterion
  - Conditional
  - Required if `derogationStatus` = `requested`. {ref}`art23-cl-eligibility-criterion`
* - `agglomerationsNotMeeting`
  - Agglomerations not meeting the requirement
  - Number of agglomerations concerned not meeting the requirement on 1 January 2025.
  - nonNegativeValue
  - Conditional
  - Required if `derogationStatus` = `requested`
* - `agglomerationsMeeting`
  - Agglomerations meeting the requirement
  - Number of agglomerations concerned meeting the requirement on 1 January 2025.
  - nonNegativeValue
  - Conditional
  - Required if `eligibilityCriterion` = `shareOfAgglomerations`
* - `loadNotMeeting`
  - Load not meeting the requirement
  - Generated load of the agglomerations concerned not meeting the requirement on
    1 January 2025.
  - nonNegativeValue (p.e.)
  - Conditional
  - Required if `eligibilityCriterion` = `shareOfLoad`
* - `loadMeeting`
  - Load meeting the requirement
  - Generated load of the agglomerations concerned meeting the requirement on 1 January 2025.
  - nonNegativeValue (p.e.)
  - Conditional
  - Required if `eligibilityCriterion` = `shareOfLoad`
* - `reasonType`
  - Reason type
  - Whether the reasons for the extension are technical, economic or both. Select one or both.
  - ExtensionReason [0..n]
  - Conditional
  - Required if `derogationStatus` = `requested`. {ref}`art23-cl-extension-reason`
* - `reasonReference`
  - Reason reference
  - Reference to the technical or economic reasons justifying the extension.
  - referenceCode
  - Conditional
  - Required if `derogationStatus` = `requested`
* - `investmentPlanReference`
  - Investment plan reference
  - Reference to the plan detailing the investments needed to meet the requirement within the
    extended deadline.
  - referenceCode
  - Conditional
  - Required if `derogationStatus` = `requested`
:::

"The requirement" is complete collecting systems for `article3_2`, secondary treatment for
`article6_3` and tertiary treatment for `article7_4`. For `article7_4`, agglomerations lacking
tertiary treatment and those not meeting its requirements both count as not meeting it, as in
Article 7(4)(a).

The number not meeting the requirement is always required when an extension is requested, since
the Directive lists it as content of the programme. The other numbers are asked for only for the
chosen criterion: the Commission needs them to calculate the share, and cannot do so from the
number not meeting alone. The reasons themselves stay in the referenced document; `reasonType`
allows them to be counted across Member States.

The reference fields may point to a chapter of the programme.

## Quality checks

:::{list-table} Proposed quality checks for the Derogation table
:header-rows: 1
:widths: 10 70 20

* - Code
  - Rule
  - Severity
* - D01
  - Exactly one row for each of `article3_2`, `article6_3` and `article7_4`
  - Blocker
* - D02
  - With `derogationStatus` = `requested`: `extendedDeadlineYear`, `eligibilityCriterion`,
    `agglomerationsNotMeeting`, `reasonType`, `reasonReference` and `investmentPlanReference`
    are given, and so are the numbers of the chosen criterion
  - Error
* - D03
  - With `derogationStatus` = `notRequested`: all other fields are empty
  - Warning
* - D04
  - `eligibilityCriterion` = `shareOfLoad` is not used with `article7_4`
  - Error
* - D05
  - The share calculated from the numbers of the chosen criterion meets the eligibility condition
  - Error
* - D06
  - `extendedDeadlineYear` is after the deadline and not after the latest year allowed for the
    calculated share and the Member State
  - Error
:::

## Mapping from the previous fields

The previous design had one row per Member State, with the same questions repeated for each
provision under prefixed names.

:::{list-table} Previous fields and their place in the proposal
:header-rows: 1
:widths: 55 45

* - Previous
  - Proposal
* - `article3_2DeadlineExtension`, `article6_3DeadlineExtension`, `article7_4DeadlineExtension`,
    as a number of whole years
  - `derogationStatus` and `extendedDeadlineYear`, one row each
* - `article3_2NonCompleteCollectingSystem`, `article6_3AgglomerationsWithoutSecondaryTreatment`,
    `article7_4AgglomerationsWithoutTertiaryTreatment`
  - `agglomerationsNotMeeting`
* - `article3_2CompleteCollectingSystem`, `article6_3AgglomerationsWithSecondaryTreatment`,
    `article7_4AgglomerationsWithTertiaryTreatment`
  - `agglomerationsMeeting`
* - `article3_2NonCompleteCollectingSystemLoad`, `article6_3LoadWithoutSecondaryTreatment`
  - `loadNotMeeting`
* - `article3_2CompleteCollectingSystemLoad`, `article6_3LoadWithSecondaryTreatment`
  - `loadMeeting`
* - `article3_2InvestmentPlanReference`, `article6_3InvestmentPlanReference`,
    `article7_4InvestmentPlanReference`
  - `investmentPlanReference`
* - `article3_2ExtensionReasonReference`, `article6_3ExtensionReasonReference`,
    `article7_4ExtensionReasonReference`
  - `reasonType` and `reasonReference`
* - `article3_2CulturalHeritage`, `article3_2CulturalHeritageReference`,
    `article6_3CulturalHeritage`, `article6_3CulturalHeritageReference`
  - {ref}`art23-culturalheritageextension`, in programme updates
* - `article6_4LessStringentTreatment`, `article6_4LessStringentStudyReference`
  - {ref}`art23-lessstringenttreatment`
:::

The previous design allowed, for Article 3(2), either the numbers of agglomerations or the loads,
so the number not meeting the requirement could be left out; for Article 6(3) it required all four
numbers. The proposal always requires the number not meeting the requirement, and the other
numbers only for the chosen criterion.

## Related open issues

* {ref}`art23-oi-derogation` - definition of a complete collecting system, individual systems,
  agglomerations served by one plant, and the expected content of the linked documents.
