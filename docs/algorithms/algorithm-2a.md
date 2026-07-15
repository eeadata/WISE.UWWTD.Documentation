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