(sp-open-issues)=
# Decisions and open issues

:::{warning} Draft
The decisions below are settled for this draft and have been applied to the spatial points pages.
They remain proposals until the dataflow is agreed. Only the items under "Remaining open issues"
still need a decision or technical confirmation.
:::

## Decisions

(sp-oi-representative-point)=
### SP-01 Representative point of an agglomeration

A point already reported is kept where it still represents the agglomeration; a new one lies within
its main settlement. The location of a treatment plant is not used instead ({ref}`sp-location`).

(sp-oi-planned-location)=
### SP-02 Coordinates of planned facilities

For treatment plants, `locationStatus` (`confirmed`, `provisional`, `notYetKnown`) allows a
proposed plant without a selected site. Discharge points have no `locationStatus`: their latitude
and longitude are always required, and a proposed discharge point is reported once its location is
known. Coordinates are never filled with zero ({ref}`sp-location`).

(sp-oi-agglomeration-uwwtp)=
### SP-03 No link between agglomerations and treatment plants

No link table is requested. Article 23(1)(b) does not require one.

(sp-oi-lineage)=
### SP-04 Merges, splits and retirement

A new object formed by a merger or split lists the codes it replaces in `supersedesIdentifier`,
once. An agglomeration that absorbs another keeps its code and is reported as a `change` listing
the absorbed code. `deletion` retires an object that is not replaced. Retired codes stay
identifiable and are not reused; the reverse link and the history are kept centrally. Changes and
retirement apply to current objects only, reactivation only to objects retired without
replacement, and predecessors must be current objects of the same country and table. A delivery is
checked against the accepted state before it, with all the parts of a split checked together
({ref}`sp-lifecycle-rules`). The shared predecessor of the successors of the same split is
explicitly allowed by the quality checks. The first delivery uses the migration baseline instead
of the accepted state (SP-17).

(sp-oi-name-language)=
### SP-05 Names

`nameText` and `nameLanguage` are required, `nameTextInternational` optional, reusing the WISE
spatial data name fields. `nameLanguage` gives the language of `nameText` as a code from the
ISO 639-2 vocabulary of the Eionet Data Dictionary ({ref}`sp-names`).
A proposed treatment plant without an official name uses a working or descriptive name; assigning
its official name later does not change its identifier.

(sp-oi-condition)=
### SP-06 Proposed facilities

`planned` is dropped; `proposed` is the only pre-construction condition. It corresponds to the
INSPIRE value `projected` ({ref}`sp-cl-condition`).

(sp-oi-inspire)=
### SP-07 INSPIRE identifiers

Given only where an INSPIRE identifier already exists; never invented.

(sp-oi-metadata)=
### SP-09 No documents or metadata

Only the three tables are reported. Coordinates are accepted in ETRS89 (EPSG:4258) or WGS 84
(EPSG:4326), with at least four decimal places, without conversion or a declaration of the system.

(sp-oi-storm-overflows)=
### SP-10 Storm water overflows

Not reported in this dataflow ({ref}`sp-dischargepoint`).

(sp-oi-vocabulary)=
### SP-11 Condition codelist

The INSPIRE
[ConditionOfFacilityValue](https://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue) codelist,
checked on 6 October 2026, has the values `functional`, `projected`, `underConstruction`,
`disused` and `decommissioned`, all valid. `conditionOfFacility` uses them, with `projected` called
`proposed` ({ref}`sp-cl-condition`).

(sp-oi-reactivation)=
### SP-11a Reactivation

Three situations sound alike but are reported differently.

**Reactivation: bringing back a retired code.** An object reported with `deletion` no longer
existed and nothing replaced it; its code is retired but kept. If the same object comes back into
use, it is reported with `reactivation`, under its old code, so that its history and earlier
references link up again. For example, agglomeration XXAGG0300 falls below the reporting
threshold and is reported with `deletion`; years later it grows again and is reported with
`reactivation`. WISE has the same value, for monitoring sites that were retired and later reused.

**Not possible: reactivating an object that was replaced.** A code retired because something
replaced it, through a merger, split or absorption, cannot be reactivated. Otherwise the old code
and its successor would both be in use, which would quietly undo the merger or split. For example,
after XXAGG0101 and XXAGG0102 have merged into XXAGG0150, reporting XXAGG0101 with `reactivation`
is rejected. If the merger is reversed, XXAGG0150 is split into new codes; if the merger was a
reporting mistake, it is corrected. WISE likewise excludes superseded objects from reactivation.

**Reopening a closed facility is a `change`.** A treatment plant or discharge point that closes is
not retired: it stays in the register with `conditionOfFacility` set to `disused` or
`decommissioned`. Bringing it back into use only changes that condition. For example, XXUWWTP0005
closes (`change`, `decommissioned`) and later reopens (`change`, `functional`).

| Situation | Code retired? | Report |
| --- | --- | --- |
| Retired without replacement, back in use | Yes, by `deletion` | `reactivation` |
| Replaced by a merger, split or absorption | Yes, superseded | Not possible |
| Facility closed, now reopened | No | `change` |

(sp-oi-dischargepoint-simplicity)=
### SP-12 Discharge points

Reported like the other objects, with no link to a treatment plant or agglomeration. Discharge
points are intended for Article 22 reporting and are not needed for Article 23. Completing this
table is not a prerequisite for an Article 23 delivery.

(sp-oi-legacy-codes)=
### SP-14 Codes from earlier reporting

Codes that meet the WISE identifier rules are copied unchanged. The others are converted by the
EEA in fixed steps, and the EEA keeps the link to the original code. A wrong country prefix, a
code over 42 characters, or two codes that become identical are flagged for the Member State to
resolve, not fixed automatically ({ref}`sp-code-conversion`).

**Review decision, 5 October 2026.** The data owner checked the data and reported that the
collision scenario raised in the review does not occur. No additional collision-handling design
is introduced; the existing flag-and-resolve rule stays.

(sp-oi-schemes)=
### SP-15 Identifier schemes

Each table has one kind of code, so its scheme is fixed and added centrally, not reported
({ref}`sp-cl-scheme`).

(sp-oi-complete-rows)=
### SP-16 Complete rows

A reported row gives all the current values of the object. An optional field left empty clears its
earlier value; an empty `supersedesIdentifier` reports no new replacement and never removes one
already accepted. Omitting an object means no change ({ref}`sp-reporting`).

(sp-oi-first-reporting)=
### SP-17 First reporting with noChange

The first reporting is a table prefilled from the reporting under Directive 91/271/EEC, every row
`noChange`. Lifecycle checks use the EEA-prepared migration baseline for this delivery, so the
Member State can confirm, correct, retire or replace baseline objects before first acceptance.
New codes must not reuse baseline codes. The accepted delivery puts the objects into the register;
only then can Article 22 or Article 23 reference them. Later deliveries are checked against the
accepted register. This follows the WISE GIS Guidance's use of `noChange` for objects
reported before and not replaced. A converted code is also reported as `noChange`, not as the WISE
`changeCode`: those original codes were not valid WISE identifiers, so this is the first WISE
registration of the object, and the EEA keeps the link to the original code
({ref}`first reporting <sp-first-reporting>`).

## Remaining open issues

(sp-oi-wise)=
### SP-13 Differences from WISE

This is a simplified UWWTD proposal, not a copy of the WISE spatial data schema. Reporting
`latitude` and `longitude` instead of a WISE `geometry` is settled for this draft. Points still
to settle:

* How an absorption, reported as a `change` with `supersedesIdentifier`, is published to WISE.
* Whether `conditionOfFacility` is kept, or replaced or complemented by the WISE operational period
  dates.
* Whether the EU Registry link, `euRegistryFacilityId`, is still wanted.

(sp-oi-reportnet)=
### SP-20 Reportnet

A dataflow that stays open, accepts only new, changed or retired objects, and lets other dataflows
check codes against accepted objects needs technical confirmation in Reportnet. So does
prefilling the reporting tables, for the first reporting from the reporting under Directive
91/271/EEC and later with the accepted values. How an object reported by mistake is
corrected through the helpdesk is to be agreed.
