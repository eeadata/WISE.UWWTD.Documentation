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