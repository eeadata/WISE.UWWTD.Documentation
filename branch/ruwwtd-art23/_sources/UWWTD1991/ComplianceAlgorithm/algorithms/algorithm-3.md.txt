(algorithm3)=
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

ROOT{"RESULTS: Algorithm n°2"}

ROOT --> L1{"If required=appropriate check date article 4: if = null OR if deadline is before or equal reporting reference date."}
ROOT --> M1{"If required=primary or secondary check date article 4: if = null OR if deadline is before or equal reporting reference date."}
ROOT --> R1{"if required= more stringent, check date article 4: if = null OR if deadline is before or equal reporting reference date."}

%% Left Branch
L1 -->|YES| L_YES["compliance = result of algorithm n°2"]
L_YES -.-> ID01(["03-01"])

L1 -->|NO| L_NO["compliance = PD"]
L_NO -.-> ID02(["03-02"])

%% Middle Branch
M1 -->|NO| M_NO["Compliance = PD"]
M_NO -.-> ID03A(["03-03"])

M1 -->|YES| A5_CHECK{"check date article 5: if = null OR if deadline is before or equal reporting reference date."}

%% Right Branch
R1 -->|YES| A5_CHECK
R1 -->|NO| R_NO["Compliance = PD"]
R_NO -.-> ID03B(["03-03"])

%% Article 5 Check
A5_CHECK -->|YES| A5_YES["compliance = result of algorithm n°2"]
A5_YES -.-> ID04(["03-04"])

A5_CHECK -->|NO| A5_NO{"If secondary treatment in place AND if COD and BOD5 performance = pass"}

%% A5_NO branch
A5_NO -->|YES| N6["Compliance = C"]
N6 -.-> ID05(["03-05"])

A5_NO -->|NO| N7["Compliance = NC"]
N7 -.-> ID06(["03-06"])

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

class ROOT,L1,M1,R1,A5_CHECK,A5_NO decision;
class N7 nc;
class N6 compliance;
class L_NO,M_NO,R_NO pd;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
```

## Pseudocode

```{dropdown} Show python code
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