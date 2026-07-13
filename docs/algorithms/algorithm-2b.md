# Algorithm 2b. UWWTD: Treatment and Performance Compliance (more stringent treatment)

## Overview

Wastewater treatment compliance based on the type of required treatment, presence of actual treatment, and performance metrics.

It assigns compliance results (**C = Compliant, NC = Non Compliant**), treatment and performance flags.

## Simplified Logic

### 1. Look up the “Required” treatment type

* From Algorithm 1 (`result_required`).
* Could be things like:
  * "phosphorus"
  * "nitrogen"
  * "other"
  * "(aN+aP)"
  * "(aP+b)"
  * "(aP+b+c)"

### 2. Decision Tree per Required Case

For each required case, it runs a branch of the decision tree:

* Does the plant have the right infrastructure?
  * (e.g., nitrogen removal installed?)

* Did the plant’s performance tests pass for the relevant pollutants?

### 3. Outputs

* `result_treatment` → whether the plant has the right equipment.
* `result_performance` → whether the plant’s monitoring shows compliant performance.
* `result_compliance` →
  * **"C" (compliant)** or
  * **"NC" (non-compliant)**

## Pseudocode

```python
# ------------------------------------------------------------------- 
# CASE 1: Nitrogen + Phosphorus ( (aN+aP) or (nitrogen+phosphorus) ) 
# ------------------------------------------------------------------- 

if result_required in ["(aN+aP)", "(nitrogen+phosphorus)"]: 
    add_note(f"Required = {result_required}. Need Secondary + N-removal + P-removal.") 
 
    if secondary_treatment and n_removal and p_removal: 
        add_note("Secondary, N-removal, P-removal present.") 
 
        if ( 
            uwwCODPerf == "P" 
            and uwwBOD5Perf == "P" 
            and uwwNTotPerf == "P" 
            and uwwPTotPerf == "P" 
        ): 
            add_note("COD, BOD5, N, P all pass → Compliant.") 
            result_treatment = "True" 
            result_performance = "True" 
            result_compliance = "C" 
            alg2_exit_leaf = "02-B-01" 
        else: 
            add_note("Performance failed → Non-compliant.") 
            result_treatment = "True" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-02" 
 
    else: 
        add_note("Missing Secondary or N/P removal.") 
 
        if ( 
            uwwCODPerf == "P" 
            and uwwBOD5Perf == "P" 
            and uwwNTotPerf == "P" 
            and uwwPTotPerf == "P" 
        ): 
            add_note("Performance ok but treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "True" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-03" 
        else: 
            add_note("Performance + treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-04"

# ------------------------------------------------------------------- 
# CASE 2: Phosphorus only ( (aP) or (phosphorus) ) 
# ------------------------------------------------------------------- 

elif result_required in ["(aP)", "(phosphorus)"]: 
    add_note(f"Required = {result_required}. Need Secondary + P-removal.")

    if secondary_treatment and p_removal: 
        add_note("Secondary + P-removal present.") 

        if uwwCODPerf == "P" and uwwBOD5Perf == "P" and uwwPTotPerf == "P": 
            add_note("COD, BOD5, P pass → Compliant.") 
            result_treatment = "True" 
            result_performance = "True" 
            result_compliance = "C" 
            alg2_exit_leaf = "02-B-05" 
        else: 
            add_note("Performance failed → Non-compliant.") 
            result_treatment = "True" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-06" 

    else: 
        add_note("Missing Secondary or P-removal.") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P" and uwwPTotPerf == "P": 
            add_note("Performance ok but treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "True" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-07" 
        else: 
            add_note("Performance + treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-08"

# ------------------------------------------------------------------- 
# CASE 3: Nitrogen only ( (aN) or (nitrogen) ) 
# ------------------------------------------------------------------- 

elif result_required in ["(aN)", "(nitrogen)"]: 
    add_note(f"Required = {result_required}. Need Secondary + N-removal.") 
 
    if secondary_treatment and n_removal: 
        add_note("Secondary + N-removal present.") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P" and uwwNTotPerf == "P": 
            add_note("COD, BOD5, N pass → Compliant.") 
            result_treatment = "True" 
            result_performance = "True" 
            result_compliance = "C" 
            alg2_exit_leaf = "02-B-09" 
        else: 
            add_note("Performance failed → Non-compliant.") 
            result_treatment = "True" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-10" 
 
    else: 
        add_note("Missing Secondary or N-removal.") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P" and uwwNTotPerf == "P":
            add_note("Performance ok but treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "True" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-11" 
        else: 
            add_note("Performance + treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-12" 

# ------------------------------------------------------------------- 
# CASE 4: Other treatment ( (c) or (other) ) 
# ------------------------------------------------------------------- 

elif result_required in ["(c)", "(other)"]: 
    add_note(f"Required = {result_required}. Need Secondary + Other treatment flag.") 
 
    if secondary_treatment and other_stringent_treatment: 
        add_note("Secondary + Other treatment present.") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P": 
            add_note("COD, BOD5 pass → Compliant.") 
            result_treatment = "True" 
            result_performance = "True" 
            result_compliance = "C" 
            alg2_exit_leaf = "02-B-13" 
        else: 
            add_note("Performance failed → Non-compliant.") 
            result_treatment = "True" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-14" 
 
    else: 
        add_note("Missing Secondary or Other treatment.") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P": 
            add_note("Performance ok but treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "True" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-15" 
        else: 
            add_note("Performance + treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-16" 
 
# ------------------------------------------------------------------- 
# CASE 5: More Stringent Nitrogen and Phosphorus (aP + b) 
# ------------------------------------------------------------------- 

elif result_required == "(aP+b)": 
    add_note(f"Required = {result_required}. Need Secondary + N-removal + P-removal.") 
 
    if secondary_treatment and n_removal and p_removal: 
         add_note("Secondary, N-removal, P-removal present.") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P" and uwwPTotPerf == "P": 
            add_note("COD, BOD5, P pass → Compliant.") 
            result_treatment = "True" 
            result_performance = "True" 
            result_compliance = "C" 
            alg2_exit_leaf = "02-B-17" 
        else: 
            add_note("Performance failed → Non-compliant.") 
            result_treatment = "True" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-18" 
 
    else: 
        add_note("Missing Secondary or N/P removal.") 
        result_treatment = "False" 
        result_performance = "True" 
        result_compliance = "NC" 
        alg2_exit_leaf = "02-B-19" 
 
# ------------------------------------------------------------------- 
# CASE 6: Nitrogen + Phosphorus + Other ( (aN+aP+c) or (nitrogen+phosphorus+other)  
# ------------------------------------------------------------------- 

elif result_required in ["(aN+aP+c)", "(nitrogen+phosphorus+other)"]: 
    add_note(f"Required = {result_required}. Need Secondary + N-removal + P-removal + (any advanced).") 
 
    if secondary_treatment and n_removal and p_removal and advanced_any: 
        add_note("All required treatments present.") 
 
        if ( 
            uwwCODPerf == "P" 
            and uwwBOD5Perf == "P" 
            and uwwNTotPerf == "P" 
            and uwwPTotPerf == "P" 
        ): 
            add_note("COD, BOD5, N, P pass → Compliant.") 
            result_treatment = "True" 
            result_performance = "True" 
            result_compliance = "C" 
            alg2_exit_leaf = "02-B-20" 
        else: 
            add_note("Performance failed → Non-compliant.") 
            result_treatment = "True" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-21" 
 
    else: 
        add_note("Missing treatment(s).") 
 
        if ( 
            uwwCODPerf == "P" 
            and uwwBOD5Perf == "P"
            and uwwNTotPerf == "P" 
            and uwwPTotPerf == "P" 
        ): 
            add_note("Performance ok but treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "True" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-22" 
        else: 
            add_note("Performance + treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-23" 
 
# ------------------------------------------------------------------- 
# CASE 7: Nitrogen + Other ( (aN+c) or (nitrogen+other) ) 
# ------------------------------------------------------------------- 
elif result_required in ["(aN+c)", "(nitrogen+other)"]: 
    add_note(f"Required = {result_required}. Need Secondary + N-removal + (any advanced).") 
 
    if secondary_treatment and n_removal and advanced_any: 
        add_note("Secondary + N-removal + advanced present.") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P" and uwwNTotPerf == "P": 
            add_note("COD, BOD5, N pass → Compliant.") 
            result_treatment = "True" 
            result_performance = "True" 
            result_compliance = "C" 
            alg2_exit_leaf = "02-B-24" 
        else: 
            add_note("Performance failed → Non-compliant.") 
            result_treatment = "True" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-25" 
 
    else: 
        add_note("Missing treatment(s).") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P" and uwwNTotPerf == "P": 
            add_note("Performance ok but treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "True" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-26" 
        else: 
            add_note("Performance + treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-27" 
 
# ------------------------------------------------------------------- 
# CASE 8: Phosphorus + Other ( (aP+c) or (phosphorus+other) ) 
# ------------------------------------------------------------------- 

elif result_required in ["(aP+c)", "(phosphorus+other)"]: 
    add_note(f"Required = {result_required}. Need Secondary + P-removal + (any advanced).") 
 
    if secondary_treatment and p_removal and advanced_any: 
        add_note("Secondary + P-removal + advanced present.") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P" and uwwPTotPerf == "P": 
            add_note("COD, BOD5, P pass → Compliant.") 
            result_treatment = "True" 
            result_performance = "True" 
            result_compliance = "C" 
            alg2_exit_leaf = "02-B-28" 
        else: 
            add_note("Performance failed → Non-compliant.") 
            result_treatment = "True" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-29" 
 
    else: 
        add_note("Missing treatment(s).") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P" and uwwPTotPerf == "P": 
            add_note("Performance ok but treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "True" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-30" 
        else: 
            add_note("Performance + treatment missing → NC.") 
            result_treatment = "False" 
            result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-31" 
 
# ------------------------------------------------------------------- 
# CASE 9: N-removal + Advanced ( (b+c) ) 
# ------------------------------------------------------------------- 

elif result_required == "(b+c)": 
    add_note(f"Required = {result_required}. Need Secondary + N-removal + (any advanced)." ) 
 
    if secondary_treatment and n_removal and advanced_any: 
        add_note("Secondary + N-removal + advanced present.") 
 
        if uwwCODPerf == "P" and uwwBOD5Perf == "P": 
            add_note("COD, BOD5 pass → Compliant.") 
            result_treatment = "True" 
            result_performance = "True" 
            result_compliance = "C" 
            alg2_exit_leaf = "02-B-32" 
        else: 
            add_note("Performance failed → Non-compliant.") 
            result_treatment = "True"
             result_performance = "False" 
            result_compliance = "NC" 
            alg2_exit_leaf = "02-B-33" 
 
    else: 
        add_note("Missing treatment(s).") 
        result_treatment = "False" 
        result_performance = "False" 
        result_compliance = "NC" 
        alg2_exit_leaf = "02-B-34"




```