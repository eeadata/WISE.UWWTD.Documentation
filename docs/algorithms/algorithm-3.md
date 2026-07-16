# Algorithm 3. UWWTD: Treatment and Performance Compliance (Correction for Transitional Period)

## Overview

This is the transitional period correction step. It takes the output of Algorithm 2 (treatment/performance compliance) and adjusts it depending on deadlines in the 1991 UWWTD:

* **Article 4** → requires secondary treatment.
* **Article 5** → requires more stringent treatment (nutrients or advanced).

Some countries had derogations/delays. If the reporting date (**repSituationAt**) is before the legal deadline, then a non-compliant plant may temporarily be classified as **“Pending Deadline (PD)”** instead of **“Non-Compliant”**.

Algorithm 3’s role is to take compliance from Algorithm 2 and adjust it to **C / NC / PD**, depending on deadlines and minimal checks.

## Simplified Logic

### 1. If required = "Appropriate"

* Deadline of **Article 4 passed or unknown** →
  * compliance = result from Algorithm 2
  * (`alg3_exit_leaf = 03-01`)

* Deadline of **Article 4 not yet passed** →
  * compliance = **PD**
  * (`alg3_exit_leaf = 03-02`)

### 2. If required = primary, secondary, or more stringent

* Deadline of **Article 4 passed or unknown** → check Article 5 deadline:
  * Deadline of **Article 5 passed or unknown** →
    * compliance = result from Algorithm 2
    * (`alg3_exit_leaf = 03-04`)

  * Deadline of **Article 5 not yet passed** → check plant treatment:
    * Secondary treatment present and **COD & BOD5 pass** →
      * compliance = **C**
      * (`alg3_exit_leaf = 03-05`)
    * Otherwise →
      * compliance = **NC**
      * (`alg3_exit_leaf = 03-06`)

* Deadline of **Article 4 not yet passed** →
  * compliance = **PD**
  * (`alg3_exit_leaf = 03-03`)

## Decision Tree

```{mermaid}
graph TB
ROOT(["RESULTS: Algorithm n°2"])

ROOT --> L1["If required=appropriate check date article 4: if = null OR if deadline is before or equal reporting reference date."]
ROOT --> M1["If required=primary or secondary check date article 4: if = null OR if deadline is before or equal reporting reference date."]
ROOT --> R1["if required= more stringent, check date article 4: if = null OR if deadline is before or equal reporting reference date."]

%% Left Branch
L1 -->|YES| L_YES["compliance = result of algorithm n°2"]
L_YES -.- ID01(["03-01"])
L1 -->|NO| L_NO["compliance = PD"]
L_NO -.- ID02(["03-02"])

%% Middle Branch
M1 -->|NO| M_NO["Compliance = PD"]
M_NO -.- ID03A(["03-03"])
M1 -->|YES| A5_CHECK["check date article 5: if = null OR if deadline is before or equal reporting reference date."]

%% Right Branch
R1 -->|YES| A5_CHECK
R1 -->|NO| R_NO["Compliance = PD"]
R_NO -.- ID03B(["03-03"])

%% Article 5 Check
A5_CHECK -->|YES| A5_YES["compliance = result of algorithm n°2"]
A5_YES -.- ID04(["03-04"])
A5_CHECK -->|NO| A5_NO["If secondary treatment in place AND if COD and BOD5 performance = pass"]

%% Secondary Treatment Check
A5_NO -->|YES| SEC_YES["Compliance = C"]
SEC_YES -.- ID05(["03-05"])
A5_NO -->|NO| SEC_NO["Compliance = NC"]
SEC_NO -.- ID06(["03-06"])

classDef reference stroke:#00a2ff,color:#00a2ff;
class ID01,ID02,ID03A,ID03B,ID04,ID05,ID06 reference;

%% Apply YES (Green) and NO (Red) Link Styles
linkStyle 3,9,10,13,16 stroke:green,color:green,stroke-width:2px;
linkStyle 5,7,11,15,18 stroke:red,color:red,stroke-width:2px;
```

## Pseudocode

```python
# --- Case 1: Required = Appropriate --- 
if required == "Appropriate": 
    if deadline_art4 is None or deadline_art4 <= rep_date: 
        log("Deadline art.4 passed, required=Appropriate → Compliance = Algorithm 2 result") 
        alg3_exit_leaf = "03-01" 
        # compliance stays = compliance_alg2 
    else: 
        log("Deadline art.4 not yet reached, required=Appropriate → Compliance = PD") 
        compliance_alg2 = "PD" 
        alg3_exit_leaf = "03-02" 
 
# --- Case 2: Required = Primary / Secondary / More stringent --- 
elif required in [ 
    "Primary",
    "Secondary", 
    "(aN)",
    "(aN+aP)",
    "(aN+aP+c)",
    "(aN+c)", 
    "(aP)",
    "(aP+b)",
    "(aP+b+c)",
    "(aP+c)", 
    "(b)",
    "(b+c)",
    "(c)", 
    "(nitrogen)",
    "(nitrogen+other)", 
    "(nitrogen+phosphorus)",
    "(nitrogen+phosphorus+other)", 
    "(other)",
    "(phosphorus)",
    "(phosphorus+other)" 
]: 
    if deadline_art4 is None or deadline_art4 <= rep_date: 
        log("Deadline art.4 passed → check art.5 deadline") 
 
        if deadline_art5 is None or deadline_art5 <= rep_date: 
            log("Deadline art.5 passed → Compliance = Algorithm 2 result") 
            alg3_exit_leaf = "03-04" 
 
        else: 
            log("Deadline art.5 not passed → check secondary treatment + COD + BOD5") 
            if has_secondary and bod5_perf == "P" and cod_perf == "P": 
                log("Secondary present & COD+BOD5 passed → Compliance = C") 
                compliance_alg2 = "C" 
                alg3_exit_leaf = "03-05" 
            else: 
                log("Secondary missing or COD/BOD5 failed → Compliance = NC") 
                compliance_alg2 = "NC" 
                alg3_exit_leaf = "03-06" 
    else: 
        log("Deadline art.4 not yet reached → Compliance = PD") 
        compliance_alg2 = "PD" 
        alg3_exit_leaf = "03-03"
```