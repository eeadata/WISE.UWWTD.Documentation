(sp-open-issues)=
# Open issues

:::{warning} Draft
The decisions below have been applied to the spatial points pages. They remain proposals until the
dataflow is agreed.
:::

## Decisions

(sp-oi-representative-point)=
### SP-01 Representative point of an agglomeration

A point already reported is kept where it still represents the agglomeration; a new one lies within
its main settlement. The location of a treatment plant is not used instead ({ref}`sp-location`).

(sp-oi-planned-location)=
### SP-02 Coordinates of planned facilities

`locationStatus` (`confirmed`, `provisional`, `notYetKnown`) allows a projected facility without a
selected site. Coordinates are never filled with zero ({ref}`sp-location`).

(sp-oi-agglomeration-uwwtp)=
### SP-03 No link between agglomerations and treatment plants

No link table is requested. Article 23(1)(b) does not require one.

(sp-oi-lineage)=
### SP-04 Merges, splits and retirement

A new object formed by a merger or split lists the codes it replaces in `supersedesIdentifier`,
once. An agglomeration that absorbs another keeps its code and is reported as a `change` listing
the absorbed code. `deletion` retires an object that is not replaced. Retired codes stay
identifiable and are not reused; the reverse link and the history are kept centrally
({ref}`sp-lifecycle`).

(sp-oi-name-language)=
### SP-05 Names

`nameText` and `nameLanguage` are required, `nameTextInternational` optional, as in the WISE
spatial data definitions ({ref}`sp-names`).

(sp-oi-condition)=
### SP-06 Projected facilities

`planned` is dropped; `projected` is the only pre-construction condition ({ref}`sp-cl-condition`).

(sp-oi-inspire)=
### SP-07 INSPIRE identifiers

Given only where an INSPIRE identifier already exists; never invented.

(sp-oi-metadata)=
### SP-09 No documents or metadata

Only the three tables are reported. ETRS89 or WGS-84 coordinates are accepted, without conversion,
a declaration of the system, or a required number of decimal places.

(sp-oi-storm-overflows)=
### SP-10 Storm water overflows

Not reported in this dataflow ({ref}`sp-dischargepoint`).

(sp-oi-reactivation)=
### SP-11a Reactivation

`reactivation` is kept, as in the WISE evolution vocabulary, for an object retired with `deletion`
that is in use again. It does not apply to an object that has been replaced. Reopening a closed
facility is a `change`.

(sp-oi-dischargepoint-simplicity)=
### SP-12 Discharge points

Reported like the other objects. `uwwCode` and `aggCode` are not reported in this table.

(sp-oi-legacy-codes)=
### SP-14 Codes from earlier reporting

Existing codes are reused where they follow the WISE identifier rules. Where a code has to change,
the mapping to the old code is maintained centrally ({ref}`sp-reporting`).

(sp-oi-schemes)=
### SP-15 Identifier schemes

Each table has one kind of code, so its scheme is fixed and added centrally, not reported
({ref}`sp-cl-scheme`).

## Still open

(sp-oi-vocabulary)=
### SP-11 Condition codelist

The current INSPIRE register for the condition of a facility could not be retrieved. Its accepted
values should be confirmed, including the status of `decommissioned`.

(sp-oi-wise)=
### SP-13 Differences from WISE

This is a simplified UWWTD proposal, not a copy of the WISE spatial data schema. Points to settle:

* Location is reported as `latitude` and `longitude`, not as a WISE `geometry`.
* How an absorption, reported as a `change` with `supersedesIdentifier`, is published to WISE.
* Whether `conditionOfFacility` is kept, or replaced or complemented by the WISE operational period
  dates.
* Whether the EU Registry link, `euRegistryFacilityId`, is still wanted.

(sp-oi-reportnet)=
### SP-20 Reportnet

A dataflow that stays open, accepts only new, changed or retired objects, and lets other dataflows
check codes against accepted objects needs technical confirmation in Reportnet. How an object
reported by mistake is corrected through the helpdesk is to be agreed.
