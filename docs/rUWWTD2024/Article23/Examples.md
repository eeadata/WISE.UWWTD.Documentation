(art23-examples)=
# Examples

:::{warning} Draft
The examples follow the proposed measure-first model ({ref}`art23-oi-measure-model`). The
situations come from questions and objections raised by Member States in the May 2026
consultation. The names, figures and codes are invented.
:::

Each example is shown twice: first from the reporter's side, filling in the tables, then from the
analyst's side, adding the money back up. The last section puts all six together.

To keep the tables readable:

* codes are shown without the country code that a real code starts with;
* all names are in English, so `measureNameLanguage` is `eng` throughout, and all amounts are in
  millions of euro, so `millionUnitsOfNationalCurrency` is `EUR` in every financing row and is not
  shown;
* optional fields that are left empty are not shown.

(art23-example-two-dates)=
## 1. Two projects at one plant, on different dates

**The question.** A Member State asked what to do when several investments are planned at one
treatment plant, on different dates. The draft format allowed several measures per plant, but only
one start date and one completion date.

**Filling it in.** Rivermouth plant must remove nitrogen and phosphorus by 2033, and
micropollutants by 2040. These are two separate projects, with different designs, budgets and
funders, seven years apart. They are reported as two measures, each with its own dates and cost.
The nitrogen and phosphorus works are one construction contract with one budget, so they are one
measure of type `upgradeTertiaryNitrogenPhosphorus`, and the cost is not split between the two
nutrients. The first measure is already under way: its 18.0 is what remains to be spent from
2028, all in the 1st cycle. The second starts in 2035, so all its cost falls after the 1st cycle.

Both measures list the same plant in `euUWWTPCode`, and the agglomeration it serves, `AGG0007`, in
`euAgglomerationCode`, so that the investments can be found for that agglomeration, as Article
23(1)(b) requires. The status, projected load and capacity of the plant and the agglomeration are
reported once, in the UWWTP and Agglomeration tables, not on either measure.

:::{list-table} Measure: what
:header-rows: 1
:widths: 8 20 32 13 16 11

* - Code
  - Name
  - Type
  - Coverage
  - Plants or agglomerations
  - Priority
* - `M001`
  - Rivermouth nitrogen and phosphorus removal
  - `upgradeTertiaryNitrogenPhosphorus`
  - `listedObjects`
  - `UWWTP0007`

    `AGG0007`
  - `high`
* - `M002`
  - Rivermouth quaternary treatment
  - `upgradeQuaternary`
  - `listedObjects`
  - `UWWTP0007`

    `AGG0007`
  - `medium`
:::

:::{list-table} Measure: when
:header-rows: 1
:widths: 16 24 30 30

* - Code
  - Status
  - Period
  - Cost status
* - `M001`
  - `ongoing`
  - `[2027,2033]`
  - `known`
* - `M002`
  - `planned`
  - `[2035,2040]`
  - `estimated`
:::

:::{list-table} MeasureFinancing
:header-rows: 1
:widths: 8 28 24 12 12 8 8

* - measureCode
  - fundingSource
  - europeanUnionFundName
  - loanName
  - fundingStatus
  - 1st cycle
  - After 1st cycle
* - `M001`
  - `europeanUnionFund`
  - `cohesionFund`
  - –
  - `appliedFor`
  - 11.0
  - –
* - `M001`
  - `nationalFederal`
  - –
  - –
  - `secured`
  - 7.0
  - –
* - `M002`
  - `producerResponsibilityOrganisation`
  - –
  - –
  - `planned`
  - –
  - 14.0
* - `M002`
  - `loan`
  - –
  - National Development Bank
  - `planned`
  - –
  - 8.0
:::

:::{list-table} UWWTP
:header-rows: 1

* - thematicIdIdentifier
  - status
  - expectedLoad
  - expectedCapacity
* - `UWWTP0007`
  - `nonCompliant`
  - 205 000
  - 240 000
:::

:::{list-table} Agglomeration
:header-rows: 1

* - thematicIdIdentifier
  - status
  - expectedLoad
* - `AGG0007`
  - `nonCompliant`
  - 205 000
:::

**Adding it back up.**

:::{list-table} Adding it back up
:header-rows: 1
:widths: 34 26 40

* - Question
  - Answer
  - How
* - Total investment at the plant
  - 40.0
  - Sum of both expenditure fields over the financing rows of the two measures
* - Investments identified for agglomeration `AGG0007`
  - 2 measures, 40.0
  - Measures listing `AGG0007` in `euAgglomerationCode`, with their financing rows
* - Capital expenditure in the 1st cycle, 2028 to 2033
  - 18.0
  - Sum of `totalCapitalExpenditure1stCycle`
* - Capital expenditure after the 1st cycle
  - 22.0
  - Sum of `totalCapitalExpenditureAfter1stCycle`
* - Secured financing
  - 7.0
  - Financing rows with `fundingStatus` = `secured`
* - Financing gap
  - 33.0
  - 40.0 − 7.0; of which 11.0 applied for from the Cohesion Fund
* - Borrowing
  - 8.0
  - Financing rows with `fundingSource` = `loan`
* - Projected capacity of the plant
  - 240 000 p.e., once
  - The UWWTP row, not repeated per measure
:::

The cost of each measure is the sum of its financing rows: 11.0 + 7.0 = 18.0, and 14.0 + 8.0 =
22.0. In the
draft format, the plant would have been one row of 40.0 with one start and one completion date,
and the quaternary project of 2035 would not have been visible as a separate commitment.

(art23-example-collecting-individual)=
## 2. A collecting system and individual systems in one agglomeration

**The question.** A Member State asked what happens when both the collecting system and individual
systems are to be invested in, in the same agglomeration: should one total be given, or one row
for each?

**Filling it in.** Northtown is extending its collecting system and, for the outlying houses,
supporting individual systems. These are two measures, with their own dates and costs, both
listing the agglomeration in `euAgglomerationCode`. Had they been one project, with one budget and
one completion year, they could have been one measure with both types. The Agglomeration table
gives the expected split of the load between the two.

:::{list-table} Measure: what
:header-rows: 1
:widths: 8 20 32 13 16 11

* - Code
  - Name
  - Type
  - Coverage
  - Plants or agglomerations
  - Priority
* - `M003`
  - Northtown collecting system extension
  - `newCollectingSystemArticle3_1`
  - `listedObjects`
  - `AGG0101`
  - `high`
* - `M004`
  - Northtown individual systems
  - `individualSystemsArticle4`
  - `listedObjects`
  - `AGG0101`
  - `medium`
:::

:::{list-table} Measure: when
:header-rows: 1
:widths: 16 24 30 30

* - Code
  - Status
  - Period
  - Cost status
* - `M003`
  - `planned`
  - `[2028,2031]`
  - `known`
* - `M004`
  - `planned`
  - `[2029,2032]`
  - `estimated`
:::

:::{list-table} MeasureFinancing
:header-rows: 1
:widths: 8 28 24 12 12 8 8

* - measureCode
  - fundingSource
  - europeanUnionFundName
  - loanName
  - fundingStatus
  - 1st cycle
  - After 1st cycle
* - `M003`
  - `municipal`
  - –
  - –
  - `secured`
  - 2.6
  - –
* - `M003`
  - `europeanUnionFund`
  - `europeanRegionalDevelopmentFund`
  - –
  - `appliedFor`
  - 3.0
  - –
* - `M004`
  - `ownFunds`
  - –
  - –
  - `planned`
  - 0.8
  - –
:::

:::{list-table} Agglomeration
:header-rows: 1

* - thematicIdIdentifier
  - status
  - expectedLoad
  - expectedLoadCollected
  - expectedLoadIndividualSystems
* - `AGG0101`
  - `nonCompliant`
  - 12 500
  - 92
  - 8
:::

**Adding it back up.**

:::{list-table} Adding it back up
:header-rows: 1
:widths: 34 26 40

* - Question
  - Answer
  - How
* - Total investment in the agglomeration
  - 6.4
  - 5.6 + 0.8
* - Collecting system
  - 5.6
  - Measure of type `newCollectingSystemArticle3_1`
* - Individual systems
  - 0.8
  - Measure of type `individualSystemsArticle4`
* - Secured financing
  - 2.6
  - Financing rows with `fundingStatus` = `secured`
* - Financing gap
  - 3.8
  - 6.4 − 2.6; of which 3.0 applied for from the European Regional Development Fund
:::

In the draft format, the agglomeration had one row with one total, and the split between the
collecting system and individual systems could only be described in remarks.

(art23-example-several-funds)=
## 3. One project, several funds, several agglomerations

**The question.** A Member State pointed out that one fund name per row is not enough, because
several funds may be requested for one project.

**Filling it in.** The Eastvale interconnection is one project that connects three agglomerations
to a shared collecting system. It is one measure, with the three agglomerations in
`euAgglomerationCode`. Its cost is given once, for the whole project, and not divided between the
agglomerations. Each source of financing, including each EU fund, is its own row with its own
expenditure.

:::{list-table} Measure: what
:header-rows: 1
:widths: 8 20 32 13 16 11

* - Code
  - Name
  - Type
  - Coverage
  - Plants or agglomerations
  - Priority
* - `M005`
  - Eastvale interconnection
  - `newCollectingSystemArticle3_1`
  - `listedObjects`
  - `AGG0201`

    `AGG0202`

    `AGG0203`
  - `high`
:::

:::{list-table} Measure: when
:header-rows: 1
:widths: 16 24 30 30

* - Code
  - Status
  - Period
  - Cost status
* - `M005`
  - `planned`
  - `[2028,2033]`
  - `known`
:::

:::{list-table} MeasureFinancing
:header-rows: 1
:widths: 8 28 24 12 12 8 8

* - measureCode
  - fundingSource
  - europeanUnionFundName
  - loanName
  - fundingStatus
  - 1st cycle
  - After 1st cycle
* - `M005`
  - `europeanUnionFund`
  - `europeanRegionalDevelopmentFund`
  - –
  - `appliedFor`
  - 4.0
  - –
* - `M005`
  - `europeanUnionFund`
  - `justTransitionFund`
  - –
  - `appliedFor`
  - 2.0
  - –
* - `M005`
  - `regional`
  - –
  - –
  - `secured`
  - 3.0
  - –
* - `M005`
  - `ownFunds`
  - –
  - –
  - `secured`
  - 1.0
  - –
:::

**Adding it back up.**

:::{list-table} Adding it back up
:header-rows: 1
:widths: 34 26 40

* - Question
  - Answer
  - How
* - Total investment
  - 10.0
  - Sum of the financing rows of the measure, counted once
* - Agglomerations concerned
  - 3
  - Codes in `euAgglomerationCode`
* - EU funds sought
  - 6.0: 4.0 from the European Regional Development Fund and 2.0 from the Just Transition Fund
  - Financing rows with `fundingSource` = `europeanUnionFund`
* - Secured financing
  - 4.0
  - Financing rows with `fundingStatus` = `secured`
* - Financing gap
  - 6.0
  - 10.0 − 4.0, all applied for from EU funds
:::

The cost is not divided between the agglomerations, because nothing in the project says how it
would be. Adding up the cost once per agglomeration would count it three times.

(art23-example-cost-estimate)=
## 4. A cost that can only be roughly estimated

**The question.** Several Member States said that investment costs cannot be estimated before the
planning, design or feasibility studies are done, and that forecasts for less advanced projects
would be very uncertain.

**Filling it in.** The Member State knows that ten small coastal plants must remove nitrogen
within the next ten years, but not yet which plants come first or what the work will cost exactly.
It reports one measure that lists the ten plants and the agglomerations they serve. Article
23(1)(b) asks for an indicative financial estimation, and a rough one is enough: at a typical cost
of 1.5 million per plant, the measure costs about 15.0. Spread evenly over the years 2028 to 2036,
that is 10.0 in the 1st cycle and 5.0 after it. No source of financing is identified yet.

:::{list-table} Measure: what
:header-rows: 1
:widths: 8 20 32 13 16 11

* - Code
  - Name
  - Type
  - Coverage
  - Plants or agglomerations
  - Priority
* - `M006`
  - Nitrogen removal at small coastal plants
  - `upgradeTertiaryNitrogen`
  - `listedObjects`
  - `UWWTP0601` to
    `UWWTP0610`;
    `AGG0601` to
    `AGG0610`
  - `medium`
:::

:::{list-table} Measure: when
:header-rows: 1
:widths: 16 24 30 30

* - Code
  - Status
  - Period
  - Cost status
* - `M006`
  - `planned`
  - `[,2036]`
  - `estimated`
:::

:::{list-table} MeasureFinancing
:header-rows: 1
:widths: 8 28 24 12 12 8 8

* - measureCode
  - fundingSource
  - europeanUnionFundName
  - loanName
  - fundingStatus
  - 1st cycle
  - After 1st cycle
* - `M006`
  - `notIdentified`
  - –
  - –
  - `notIdentified`
  - 10.0
  - 5.0
:::

The plants and agglomerations are listed even though the order of the work is not yet decided:
Article 23(1)(b) asks for the investments for each agglomeration.

The cost cannot be left unknown: every measure has at least one financing row (check RF04), and
each row gives more than 0 in at least one cycle (check R18). The estimate is refined in the next
update of the programme, and `costStatus` becomes `known` once a project, tender or contract gives
the cost.

**Adding it back up.**

:::{list-table} Adding it back up
:header-rows: 1
:widths: 34 26 40

* - Question
  - Answer
  - How
* - Total investment
  - 15.0
  - 10.0 in the 1st cycle and 5.0 after it
* - Of which only estimated
  - 15.0
  - Measures with `costStatus` = `estimated`
* - No source identified yet
  - 15.0
  - Financing rows with `fundingSource` = `notIdentified`
:::

The measure counts in the totals like any other. A total can say how much of it is only an
estimate, from `costStatus`.

(art23-example-gap)=
## 5. Part of the money still to be found

**The question.** The Commission wants to know whether funding has been secured, and what is still
missing. For example: a measure costs 100, half of it is secured, and the Member State is applying
for more.

**Filling it in.** The Lakeside upgrade concerns two plants, which both serve agglomeration
`AGG0301`. It adds nutrient removal and quaternary treatment at both, under one contract with one
budget and one completion year. It is therefore one measure with two types,
`upgradeTertiaryNitrogenPhosphorus` and `upgradeQuaternary`, and its cost is given once, not split
between them. Half of the cost is secured from the operators' own funds, an application for the
Cohesion Fund is pending, and the source of the rest is not yet identified. Of the 100.0, 70.0 is
expected to be spent from 2030 to 2033, in the 1st cycle, and 30.0 from 2034 to 2036. Each source
is split between the cycles in the same proportion as the measure: 70 % in the 1st cycle.

:::{list-table} Measure: what
:header-rows: 1
:widths: 8 20 32 13 16 11

* - Code
  - Name
  - Type
  - Coverage
  - Plants or agglomerations
  - Priority
* - `M007`
  - Lakeside nutrient removal and quaternary treatment
  - `upgradeTertiaryNitrogenPhosphorus`

    `upgradeQuaternary`
  - `listedObjects`
  - `UWWTP0301`

    `UWWTP0302`

    `AGG0301`
  - `high`
:::

:::{list-table} Measure: when
:header-rows: 1
:widths: 16 24 30 30

* - Code
  - Status
  - Period
  - Cost status
* - `M007`
  - `planned`
  - `[2030,2036]`
  - `estimated`
:::

:::{list-table} MeasureFinancing
:header-rows: 1
:widths: 8 28 24 12 12 8 8

* - measureCode
  - fundingSource
  - europeanUnionFundName
  - loanName
  - fundingStatus
  - 1st cycle
  - After 1st cycle
* - `M007`
  - `ownFunds`
  - –
  - –
  - `secured`
  - 35.0
  - 15.0
* - `M007`
  - `europeanUnionFund`
  - `cohesionFund`
  - –
  - `appliedFor`
  - 21.0
  - 9.0
* - `M007`
  - `notIdentified`
  - –
  - –
  - `notIdentified`
  - 14.0
  - 6.0
:::

**Adding it back up.**

:::{list-table} Adding it back up
:header-rows: 1
:widths: 34 26 40

* - Question
  - Answer
  - How
* - Total investment
  - 100.0
  - 70.0 in the 1st cycle and 30.0 after it
* - Secured financing
  - 50.0
  - Financing rows with `fundingStatus` = `secured`
* - Financing gap
  - 50.0
  - 100.0 − 50.0
* - Financing gap in the 1st cycle
  - 35.0
  - 70.0 − 35.0 secured: the rows that are not `secured`, 1st cycle only
* - Of which applied for
  - 30.0
  - Financing rows with `fundingStatus` = `appliedFor`
* - Of which no source identified yet
  - 20.0
  - Financing rows with `fundingSource` = `notIdentified`
* - Measures including quaternary treatment
  - 1, at 2 plants
  - Measures whose `uwwtdMeasureType` includes `upgradeQuaternary`
* - Investment in quaternary treatment alone
  - Not known
  - The cost covers both types and is not split
:::

The two types share one cost. Counting this measure under each of its types answers "which
measures include quaternary treatment?", but adding its cost once per type would count the 100.0
twice.

(art23-example-national)=
## 6. Renewal of collecting systems nationwide

**The question.** Renewal of existing infrastructure under Article 23(1)(c) is often planned as a
national programme, without a list of agglomerations. The draft format reported it as a total in
the OtherInvestment table.

**Filling it in.** The Member State plans to renew collecting systems across the country. It
reports one national measure, with no plants or agglomerations listed. The renewal is under way;
the 450.0 still to be spent from 2028 is spread evenly over the eight years to 2035: 337.5 in the
1st cycle and 112.5 after it. Each source is split in the same proportion.

:::{list-table} Measure: what
:header-rows: 1
:widths: 8 20 32 13 16 11

* - Code
  - Name
  - Type
  - Coverage
  - Plants or agglomerations
  - Priority
* - `M008`
  - National renewal of collecting systems
  - `renewOrReplaceCollectingSystem`
  - `national`
  - –
  - `medium`
:::

:::{list-table} Measure: when
:header-rows: 1
:widths: 16 24 30 30

* - Code
  - Status
  - Period
  - Cost status
* - `M008`
  - `ongoing`
  - `[2027,2035]`
  - `estimated`
:::

:::{list-table} MeasureFinancing
:header-rows: 1
:widths: 8 28 24 12 12 8 8

* - measureCode
  - fundingSource
  - europeanUnionFundName
  - loanName
  - fundingStatus
  - 1st cycle
  - After 1st cycle
* - `M008`
  - `ownFunds`
  - –
  - –
  - `planned`
  - 225.0
  - 75.0
* - `M008`
  - `municipal`
  - –
  - –
  - `planned`
  - 112.5
  - 37.5
:::

**Adding it back up.**

:::{list-table} Adding it back up
:header-rows: 1
:widths: 34 26 40

* - Question
  - Answer
  - How
* - Total renewal investment
  - 450.0
  - 337.5 in the 1st cycle and 112.5 after it
* - Secured financing
  - 0.0
  - No financing rows are `secured`
* - Planned financing
  - 450.0
  - 300.0 own funds and 150.0 municipal funds
:::

(art23-examples-together)=
## All six together

**The correct roll-up.**

:::{list-table} All six examples together
:header-rows: 1
:widths: 34 20 46

* - Figure
  - Value
  - How
* - Measures reported
  - 8
  - Rows in Measure
* - Total investment
  - 621.4
  - Sum of both expenditure fields over the financing rows
* - In the 1st cycle, 2028 to 2033
  - 451.9
  - Sum of `totalCapitalExpenditure1stCycle`
* - After the 1st cycle
  - 169.5
  - Sum of `totalCapitalExpenditureAfter1stCycle`
* - For listed plants or agglomerations
  - 171.4
  - Examples 1 to 5
* - National
  - 450.0
  - Example 6
* - Secured financing
  - 63.6
  - Financing rows with `fundingStatus` = `secured`
* - Financing gap
  - 557.8
  - 621.4 − 63.6
* - EU funds sought
  - 50.0
  - All applied for; none secured yet
* - Borrowing
  - 8.0
  - Example 1
* - No source identified yet
  - 35.0
  - Examples 4 and 5
:::

**The wrong answers, and why.**

:::{list-table} Common mistakes
:header-rows: 1
:widths: 40 20 40

* - Method
  - Result
  - What went wrong
* - Add up the capital expenditure after joining the measures to their plants and agglomerations
  - 1 166.4
  - Example 1 is counted twice, examples 3 and 5 three times, and example 4 twenty times
* - Count only the secured financing as the investment
  - 63.6
  - The investment is all the financing rows, whatever their `fundingStatus`
* - Add up the capital expenditure once per measure type
  - 721.4
  - Example 5 has two types and is counted twice
:::

**The rule.** Add up costs per measure, then join to plants and agglomerations, or to measure
types, only to see which ones a measure concerns, never to divide or repeat its cost. Keep secured
financing apart from financing that is only applied for or planned, and keep loans apart from
grants.
