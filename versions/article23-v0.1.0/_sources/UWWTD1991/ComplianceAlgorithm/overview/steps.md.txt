# Level of treatment definition steps

The level of treatment required depends on the type of receiving area—freshwater, estuarine, or 
coastal—and on whether it is classified as a sensitive area (due to susceptibility to eutrophication, its 
use for drinking water production, or designation under other Directives) or as a less sensitive area 
(open marine waters). 

The assessment algorithm is organised into a sequence of decision trees applied step by step.

## 1. Determine required treatment

The first step is to calculate the required level of treatment for each Urban Wastewater Treatment Plant (UWWTP).

This calculation is based on two factors:

- The size of the agglomeration
- The type of receiving area

> See algorithms:
> - **Algorithm 1a.** UWWTP: Treatment Required
> - **Algorithm 1b.** UWWTP: Treatment Required (Sensitive Areas)
> - **Algorithm 1c.** UWWTP: Treatment Required (Catchment of Sensitive Areas)

## 2. Assess treatment in place

Next, the treatment in place at each UWWTP must be assessed.

The assessment consists of two checks:

1. Verify that the treatment installed matches the treatment required as calculated in Step 1.
2. Verify that performance results for all required parameters are reported as passing.

A treatment plant is considered **compliant** only if **both** conditions are met:

- The correct treatment is in place.
- The reported performance is satisfactory.

> See algorithms:
> - **Algorithm 2a.** UWWTD: Treatment and Performance Compliance (except more stringent treatment)
> - **Algorithm 2b.** UWWTD: Treatment and Performance Compliance (more stringent treatment)

## 3. Country awarded a delay

If a country has been granted a deadline extension for implementing the Directive, an exception applies:

- Treatment plants that are not yet compliant are excluded from further compliance calculations.
- These plants are classified as **Pending Deadline (PD)**.

> See **Algorithm 3.** UWWTD: Treatment and Performance Compliance (Correction for Transitional Period)

## 4. Agglomeration compliance (Article 3)

The next step is to calculate the compliance of the agglomeration with Article 3, which concerns wastewater collection.

> See **Algorithm 4.** Agglomeration: Article 3 Compliance

## 5. Agglomeration Excluded

Because of limitations in the quality of reported data or other special cases, some agglomerations must be excluded from the subsequent compliance calculations.

These special cases may be one of the following:

- Not enough information: all end points with at least one "?"
- 100% treated in Individual and Appropriate Systems (IAS)
- Agglomeration &lt;10000pe which discharges in waterbody of type LC
- Agglomeration &lt;10000pe which discharges in waterbody of type CW

> See **Algorithm 5.** Agglomeration: Article 4, 5, 6 Compliance Exclusion

## 6. Agglomeration compliance (Article 4, 5, and 6)

To determine the compliance of an agglomeration with the three relevant articles (4, 5, and 6).

Since many agglomerations have multiple treatment plants, the first step is to calculate the compliance of each individual treatment plant with the requirements of these three articles.

> See **Algorithm 6.** Agglomeration: Plant Compliance with Article 4, 5, and 6

## 7. Aggregate the compliance of all treatment plant for an Agglomeration

Once the compliance of each treatment plant has been determined, the compliance of the agglomeration can be calculated by aggregating the compliance of all treatment plants connected to that agglomeration.

This aggregation is done separately for each article.

> See algorithms:
>
> - **Algorithm 7.** Agglomeration: Article 4 only
> - **Algorithm 8.** Agglomeration: Article 6 only
> - **Algorithm 9.** Agglomeration: Article 5 only

## 8. Overall compliance

To determine the overall compliance of an agglomeration:

- Use the compliance results for each individual article calculated in previous steps.
- Apply the general rule: if any single article is non-compliant, the agglomeration as a whole is considered non-compliant.

> See **Algorithm 10.** Agglomeration: Overall Compliance

## 9. Legal compliance

To determine the legal compliance for each article (4, 5, and 6), apply the hierarchical compliance rule, which defines how the compliance of individual treatment plants and agglomerations influences the legal status of each article.

> See **Algorithm 11.** Agglomeration: Legal Compliance of Articles 4, 5, and 6 

If a situation is non-compliant but the deadline has not yet passed, it is shown as “Not Relevant”, 
indicating that it is non-compliant but still within the allowed timeframe. Meanwhile, the platform 
internally records the calculation as “Pending Deadline” to enable administrators to easily track and 
verify these cases.