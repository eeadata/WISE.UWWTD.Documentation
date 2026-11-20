# Algorithm 2a. UWWTD: Treatment and Performance Compliance (except more stringent treatment)

## Overview

Determines whether a treatment plant is **compliant**, **non-compliant**, or **indeterminate** based on:

* the existence of discharge points,
* whether connected agglomerations are active,
* whether the plant itself is active and connected,
* whether the plan is active but not connected (sewer with no treatment plant),
* and the required treatment level (**NR, Appropriate, Primary, Secondary, or More Stringent**).

It then checks whether the actual treatment in place and performance (**BOD5, If TSS, If COD**) meet the required standard.

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
  * Performance good (**If TSS & BOD5 pass*) → **Compliant (C)**
  * Otherwise → **Non-compliant (NC)**

* If **not installed**:
  * Performance good → **NC**
  * Otherwise → **NC**

#### Secondary

* If **secondary treatment installed**:
  * Performance good (**If COD & BOD5 pass*) → **Compliant (C)**
  * Otherwise → **NC**

* If **not installed**:
  * Performance good → **NC**
  * Otherwise → **NC**

#### More stringent

* Passs control to **Algorithm 2b**.

## Decision Tree

```{mermaid}
%%{init: {
  "theme": "base",
  "flowchart": {
    "curve": "basis",
    "nodeSpacing": 35,
    "rankSpacing": 55,
    "padding": 15
  }
}}%%

graph TB

%% ============================================================
%% DECISION TREE
%% ============================================================

A{"Check agg info exists"}

A -->|YES| B{"Check dcp info exists"}
A -->|NO| A2_1["Compliance = NI"]
A2_1 --- A2_2["Treatment = not calculable"]
A2_2 --- A2_3["Performance = not calculable"]
A2_3 -.-> ID02A02(["02-A-02"])

B -->|YES| C{"Check at least one agglomeration connected to the treatment plant has status = active"}
B -->|NO| A1_1["Compliance = ?"]
A1_1 --- A1_2["Treatment = False"]
A1_2 --- A1_3["Performance = False"]
A1_3 -.-> ID02A01(["02-A-01"])

C -->|YES| D{"Check if the treatment plant is active, connected and receives waste water (status=active + ISCON + load entering >0)"}
C -->|NO| A13_1["Compliance = NR"]
A13_1 --- A13_2["Treatment = not calculable"]
A13_2 --- A13_3["Performance = not calculable"]
A13_3 -.-> ID02A13(["02-A-13"])

D -->|NO| SEWER{"Check if there is only a sewer (status= active + NOTCON)"}
D -->|YES| REQ{"Get required treatment (see algorithm 1)"}

SEWER -->|NO| A14_1["Treatment = not calculable"]
A14_1 --- A14_2["Performance = not calculable"]
A14_2 --- A14_3["Compliance = NR"]
A14_3 -.-> ID02A14(["02-A-14"])

SEWER -->|YES| A15_1["Treatment = False"]
A15_1 --- A15_2["Performance = False"]
A15_2 --- A15_3["Compliance = NR"]
A15_3 -.-> ID02A15(["02-A-15"])

REQ -->|Secondary| SEC{"Secondary treatment in place?"}
REQ -->|Primary| PRI{"If primary treatment in place"}
REQ -->|Appropriate or NR| APP_1["Treatment = not calculable"]
APP_1 --- APP_2["Performance = not calculable"]
APP_2 --- APP_3["Compliance = NR"]
APP_3 -.-> ID02A04(["02-A-04"])

REQ -->|More stringent| MORE["More stringent: see algorithm 2b more stringent"]

REQ -->|NI or ?| NI_1["Treatment = NR"]
NI_1 --- NI_2["Performance = NR"]
NI_2 --- NI_3["Compliance = ?"]
NI_3 -.-> ID02A03(["02-A-03"])

SEC -->|NO| SECF["Treatment = False"]
SEC -->|YES| SECT["Treatment = True"]

SECF --> SECF_PERF{"If COD and BOD5 performance = pass"}
SECT --> SECT_PERF{"If COD and BOD5 performance = pass"}

SECF_PERF -->|NO| A12_1["Performance = False"]
A12_1 --- A12_2["Compliance = NC"]
A12_2 -.-> ID02A12(["02-A-12"])

SECF_PERF -->|YES| A11_1["Performance = True"]
A11_1 --- A11_2["Compliance = NC"]
A11_2 -.-> ID02A11(["02-A-11"])

SECT_PERF -->|NO| A10_1["Performance = False"]
A10_1 --- A10_2["Compliance = NC"]
A10_2 -.-> ID02A10(["02-A-10"])

SECT_PERF -->|YES| A09_1["Performance = True"]
A09_1 --- A09_2["Compliance = C"]
A09_2 -.-> ID02A09(["02-A-09"])

PRI -->|NO| PRIF["Treatment = False"]
PRI -->|YES| PRIT["Treatment = True"]

PRIF --> PRIF_PERF{"If TSS and BOD5 performance = pass"}
PRIT --> PRIT_PERF{"If TSS and BOD5 performance = pass"}

PRIF_PERF -->|NO| A08_1["Performance = False"]
A08_1 --- A08_2["Compliance = NC"]
A08_2 -.-> ID02A08(["02-A-08"])

PRIF_PERF -->|YES| A07_1["Performance = True"]
A07_1 --- A07_2["Compliance = NC"]
A07_2 -.-> ID02A07(["02-A-07"])

PRIT_PERF -->|NO| A06_1["Performance = False"]
A06_1 --- A06_2["Compliance = NC"]
A06_2 -.-> ID02A06(["02-A-06"])

PRIT_PERF -->|YES| A05_1["Performance = True"]
A05_1 --- A05_2["Compliance = C"]
A05_2 -.-> ID02A05(["02-A-05"])

%% ============================================================
%% DECISION STYLE
%% ============================================================

classDef decision fill:#FFF7E6,stroke:#D97706,stroke-width:2px,color:#1E293B;

%% ============================================================
%% COMPLIANCE OUTCOME STYLES
%% ============================================================

%% NC = RED
classDef nc fill:#FEE2E2,stroke:#DC2626,stroke-width:2px,color:#991B1B;

%% C = GREEN
classDef compliance fill:#DCFCE7,stroke:#16A34A,stroke-width:2px,color:#166534;

%% NR = BLUE
classDef nr fill:#DBEAFE,stroke:#2563EB,stroke-width:2px,color:#1E40AF;

%% PD = GREY
classDef pd fill:#E5E7EB,stroke:#6B7280,stroke-width:2px,color:#374151;

%% ============================================================
%% APPLY STYLES
%% ============================================================

class A,B,C,D,SEWER,REQ,SEC,PRI,SECF_PERF,SECT_PERF,PRIF_PERF,PRIT_PERF decision;
class A12_2,A11_2,A10_2,A08_2,A07_2,A06_2 nc;
class A09_2,A05_2 compliance;
class A13_1,A14_3,A15_3,APP_3,NI_1,NI_2 nr;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
```

## PseudoIf code

```{dropdown} Show python If code
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
          if uwwIf TSSPerf == "P" and uwwBOD5Perf == "P": 
            result_performance = "True" 
            result_compliance = "C" 
            exit_leaf = "02-A-05"                      
          else: 
            result_performance = "False" 
            result_compliance = "NC" 
            exit_leaf = "02-A-06" 
          else: 
            result_treatment = "False" 
            if uwwIf TSSPerf == "P" and uwwBOD5Perf == "P": 
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
          if uwwIf CODPerf == "P" and uwwBOD5Perf == "P": 
            result_performance = "True" 
            result_compliance = "C" 
            exit_leaf = "02-A-09" 
          else: 
            result_performance = "False" 
            result_compliance = "NC" 
            exit_leaf = "02-A-10" 

        else: 
          result_treatment = "False" 
          if uwwIf CODPerf == "P" and uwwBOD5Perf == "P": 
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