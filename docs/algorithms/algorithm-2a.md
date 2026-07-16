# Algorithm 2a. UWWTD: Treatment and Performance Compliance (except more stringent treatment)

## Overview

Determines whether a treatment plant is **compliant**, **non-compliant**, or **indeterminate** based on:

* the existence of discharge points,
* whether connected agglomerations are active,
* whether the plant itself is active and connected,
* whether the plan is active but not connected (sewer with no treatment plant),
* and the required treatment level (**NR, Appropriate, Primary, Secondary, or More Stringent**).

It then checks whether the actual treatment in place and performance (**BOD5, TSS, COD**) meet the required standard.

## Simplified Logic

### 1. Check discharge points (`dcp_exists`)

* If no discharge points exist → compliance is **unknown (?)**.
* If info missing → compliance is **not information (NI)**.

### 2. Check if there is an active connected agglomeration (`agg_exists_active`)

* If none → result is **"NR / not calculable"**.

### 3. Check plant status (`active_and_connected`, `active_and_not_connected`)

* If **active & connected** → evaluate treatment requirements.
* If **active but not connected** → **"NR / False / False"**.
* If **not active or not connected** → **"NR / not calculable"**.

### 4. Check required treatment (`result_required`)

* **"?" or "NI"** →
  * Compliance unknown (**?**), NR required.

* **"Appropriate" or "NR"** →
  * Compliance **NR**, not calculable.

#### Primary

* If **primary treatment installed**:
  * Performance good (**TSS & BOD5 pass**) → **Compliant (C)**
  * Otherwise → **Non-compliant (NC)**

* If **not installed**:
  * Performance good → **NC**
  * Otherwise → **NC**

#### Secondary

* If **secondary treatment installed**:
  * Performance good (**COD & BOD5 pass**) → **Compliant (C)**
  * Otherwise → **NC**

* If **not installed**:
  * Performance good → **NC**
  * Otherwise → **NC**

#### More stringent

* Passes control to **Algorithm 2b**.

## Decision Tree

```{mermaid}
graph TB
A["Check agg info exists"]

A -->|YES| B["Check dcp info exists"]
A -->|NO| A2["Compliance = NI Treatment = not calculable Performance = not calculable"]
A2 -.- ID02A02(["02-A-02"])

B -->|YES| C["Check at least one agglomeration connected to the treatment plant has status = active"]
B -->|NO| A1["Compliance = ? Treatment = False Performance = False"]
A1 -.- ID02A01(["02-A-01"])

C -->|YES| D["Check if the treatment plant is active, connected and receives waste water (status=active + ISCON + load entering >0)"]
C -->|NO| A13["Compliance = NR Treatment = not calculable Performance = not calculable"]
A13 -.- ID02A13(["02-A-13"])

D -->|NO| SEWER["Check if there is only a sewer (status= active + NOTCON)"]
D -->|YES| REQ["Get required treatment (see algorithm 1)"]

SEWER -->|NO| A14["Treatment = not calculable Performance = not calculable Compliance = NR"]
SEWER -->|YES| A15["Treatment = False Performance = False compliance = NR"]
A14 -.- ID02A14(["02-A-14"])
A15 -.- ID02A15(["02-A-15"])

REQ --> MORE["More stringent: see algorithm 2b more stringent"]
REQ -->|Secondary| SEC["Secondary treatment in place?"]
REQ -->|Primary| PRI["If primary treatment in place"]
REQ -->|Appropriate or NR| APP["Treatment = not calculable Performance = not calculable compliance = NR"]
REQ -->|NI or ?| NI["Treatment = NR Performance = NR compliance = ?"]

APP -.- ID02A04(["02-A-04"])
NI -.- ID02A03(["02-A-03"])

SEC -->|NO| SECF["Treatment= False"]
SEC -->|YES| SECT["Treatment = True"]

SECF --> SECF_PERF["COD and BOD5 performance = pass?"]
SECT --> SECT_PERF["COD and BOD5 performance = pass?"]

SECF_PERF -->|NO| A12["Performance = False Compliance = NC"]
SECF_PERF -->|YES| A11["Performance = True Compliance = NC"]
A12 -.- ID02A12(["02-A-12"])
A11 -.- ID02A11(["02-A-11"])

SECT_PERF -->|NO| A10["Performance = False Compliance = NC"]
SECT_PERF -->|YES| A09["Performance = True Compliance = C"]
A10 -.- ID02A10(["02-A-10"])
A09 -.- ID02A09(["02-A-09"])

PRI -->|NO| PRIF["Treatment = False"]
PRI -->|YES| PRIT["Treatment = True"]

PRIF --> PRIF_PERF["TSS and BOD5 performance = pass?"]
PRIT --> PRIT_PERF["TSS and BOD5 performance = pass?"]

PRIF_PERF -->|NO| A08["Performance = False Compliance = NC"]
PRIF_PERF -->|YES| A07["Performance = True Compliance = NC"]
A08 -.- ID02A08(["02-A-08"])
A07 -.- ID02A07(["02-A-07"])

PRIT_PERF -->|NO| A06["Performance = False Compliance = NC"]
PRIT_PERF -->|YES| A05["Performance = True Compliance = C"]
A06 -.- ID02A06(["02-A-06"])
A05 -.- ID02A05(["02-A-05"])

classDef reference stroke:#00a2ff,color:#00a2ff;
class ID02A02,ID02A01,ID02A13,ID02A14,ID02A15,ID02A04,ID02A03,ID02A12,ID02A11,ID02A10,ID02A09,ID02A08,ID02A07,ID02A06,ID02A05 reference;

%% Apply YES (Green) and NO (Red) Link Styles
linkStyle 0,3,6,10,12,23,27,31,35,39,43 stroke:green,color:green,stroke-width:2px;
linkStyle 1,4,7,9,11,22,26,30,34,38,42 stroke:red,color:red,stroke-width:2px;
```

## Pseudocode

```python
if dcp_exists == 1: 
  if agg_exists_active == 1: 
    if active_and_connected == 1: 

      if result_required in {"?", "NI"}: 
        result_compliance = "?" 
        result_treatment = "NR" 
        result_performance = "NR" 
        exit_leaf = "02-A-03" 

      elif result_required in {"Appropriate", "NR"}: 
        result_compliance = "NR" 
        result_treatment = "not calculable" 
        result_performance = "not calculable" 
        exit_leaf = "02-A-04" 

      elif result_required == "Primary": 
        if primary_treatment == 1: 
          result_treatment = "True" 
          if uwwTSSPerf == "P" and uwwBOD5Perf == "P": 
            result_performance = "True" 
            result_compliance = "C" 
            exit_leaf = "02-A-05"                      
          else: 
            result_performance = "False" 
            result_compliance = "NC" 
            exit_leaf = "02-A-06" 
          else: 
            result_treatment = "False" 
            if uwwTSSPerf == "P" and uwwBOD5Perf == "P": 
              result_performance = "True" 
              result_compliance = "NC" 
              exit_leaf = "02-A-07" 
            else: 
              result_performance = "False" 
              result_compliance = "NC" 
              exit_leaf = "02-A-08" 

      elif result_required == "Secondary": 
        
        if secondary_treatment == 1: 
          result_treatment = "True" 
          if uwwCODPerf == "P" and uwwBOD5Perf == "P": 
            result_performance = "True" 
            result_compliance = "C" 
            exit_leaf = "02-A-09" 
          else: 
            result_performance = "False" 
            result_compliance = "NC" 
            exit_leaf = "02-A-10" 

        else: 
          result_treatment = "False" 
          if uwwCODPerf == "P" and uwwBOD5Perf == "P": 
            result_performance = "True" 
            result_compliance = "NC" 
            exit_leaf = "02-A-11" 
          else:
            result_performance = "False" 
            result_compliance = "NC" 
            exit_leaf = "02-A-12" 

      else: 
          # More stringent → call Algorithm 2b 
          algorithm_2b() 

        elif active_and_not_connected == 1: 
          result_compliance = "NR" 
          result_treatment = "False" 
          result_performance = "False" 
          exit_leaf = "02-A-15" 

        else: 
          result_compliance = "NR" 
          result_treatment = "not calculable" 
          result_performance = "not calculable" 
          exit_leaf = "02-A-14" 
 
    else: 
        result_compliance = "NR" 
        result_treatment = "not calculable" 
        result_performance = "not calculable" 
        exit_leaf = "02-A-13" 
 
else: 
  result_compliance = "?" 
  result_treatment = "False" 
  result_performance = "False" 
  exit_leaf = "02-A-01" 
 
if dcp_exists is None: 
    result_compliance = "NI" 
    result_treatment = "not calculable" 
    result_performance = "not calculable" 
    exit_leaf = "02-A-02"
```