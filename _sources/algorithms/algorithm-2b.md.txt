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

## Decision Tree

```{mermaid}

graph LR
ROOT["More stringent treatment (uwwOtherTreatment)"]

%% The 11 root branches
ROOT --> B1["More Stringent Nitrogen and Phosphorus (aN + aP) or (rcaParameterN+rcaParameterP)"]
ROOT --> B2["More Stringent Phosphorus (aP) or (rcaParameterP)"]
ROOT --> B3["More Stringent Nitrogen (aN) or (rcaParameterN)"]
ROOT --> B4["More Stringent Nitrogen (b)"]
ROOT --> B5["More Stringent Nitrogen and Phosphorus (aP + b)"]
ROOT --> BR1["More stringent Nitrogen and Phosphorus and Other (aP + b + c)"]
ROOT --> BR2["More stringent Nitrogen and Phosphorus and Other (aN + aP + c) or (rcaParameterN+rcaParameterP+rcaParameterOther)"]
ROOT --> BR3["More stringent Nitrogen and Other (aN + c) or (rcaParameterN+rcaParameterOther)"]
ROOT --> BR4["More Stringent Phosphorus and Other (aP + c) or (rcaParameterP+rcaParameterOther)"]
ROOT --> BR5["More Stringent Nitrogen and Other (b + c)"]
ROOT --> BR6["More stringent Other (c) or (rcaParameterOther)"]

%% Branch 1
B1 --- C1["If secondary treatment, N-removal and P-removal is in place"]
C1 --- N1((NO)) --- T1_NO["Treatment = Not met"]
C1 --- Y1((YES)) --- T1_YES["Treatment = Met"]

T1_NO --- P1_NO["If COD, BOD5, Nitrogen and Phosphorus performance pass"]
P1_NO --- N2((NO)) --- R04["Performance = Not met Compliance = NC"]
R04 -.- ID04(["02-B-04"])
P1_NO --- Y2((YES)) --- R03["Performance = Met Compliance = NC"]
R03 -.- ID03(["02-B-03"])

T1_YES --- P1_YES["If COD, BOD5, Nitrogen and Phosphorus performance pass"]
P1_YES --- N3((NO)) --- R02["Performance = Not met Compliance = NC"]
R02 -.- ID02(["02-B-02"])
P1_YES --- Y3((YES)) --- R01["Performance = Met Compliance = C"]
R01 -.- ID01(["02-B-01"])

%% Branch 2
B2 --- C2["If secondary treatment and P-removal is in place"]
C2 --- N4((NO)) --- T2_NO["Treatment = Not met"]
C2 --- Y4((YES)) --- T2_YES["Treatment = Met"]

T2_NO --- P2_NO["If COD, BOD5 and Phosphorus performance pass"]
P2_NO --- N5((NO)) --- R08["Performance = Not met Compliance = NC"]
R08 -.- ID08(["02-B-08"])
P2_NO --- Y5((YES)) --- R07["Performance = Met Compliance = NC"]
R07 -.- ID07(["02-B-07"])

T2_YES --- P2_YES["If COD, BOD5 and Phosphorus performance pass"]
P2_YES --- N6((NO)) --- R06["Performance = Not met Compliance = NC"]
R06 -.- ID06(["02-B-06"])
P2_YES --- Y6((YES)) --- R05["Performance = Met Compliance = C"]
R05 -.- ID05(["02-B-05"])

%% Branch 3
B3 --- C3["If secondary treatment and N-removal is in place"]
C3 --- N7((NO)) --- T3_NO["Treatment = Not met"]
C3 --- Y7((YES)) --- T3_YES["Treatment = Met"]

T3_NO --- P3_NO["If COD, BOD5 and Nitrogen performance pass"]
P3_NO --- N8((NO)) --- R12["Performance = Not met Compliance = NC"]
R12 -.- ID12(["02-B-12"])
P3_NO --- Y8((YES)) --- R11["Performance = Met Compliance = NC"]
R11 -.- ID11(["02-B-11"])

T3_YES --- P3_YES["If COD, BOD5 and Nitrogen performance pass"]
P3_YES --- N9((NO)) --- R10["Performance = Not met Compliance = NC"]
R10 -.- ID10(["02-B-10"])
P3_YES --- Y9((YES)) --- R09["Performance = Met Compliance = C"]
R09 -.- ID09(["02-B-09"])

%% Branch 4
B4 --- C4["If secondary treatment and N-removal is in place"]
C4 --- N10((NO)) --- T4_NO["Treatment = Not met"]
C4 --- Y10((YES)) --- T4_YES["Treatment = Met"]

T4_NO --- R15["Performance = Not met Compliance = NC"]
R15 -.- ID15(["02-B-15"])

T4_YES --- P4_YES["If COD and BOD5 performance pass"]
P4_YES --- N11((NO)) --- R14["Performance = Not met Compliance = NC"]
R14 -.- ID14(["02-B-14"])
P4_YES --- Y11((YES)) --- R13["Performance = Met Compliance = C"]
R13 -.- ID13(["02-B-13"])

%% Branch 5
B5 --- C5["If secondary treatment and N-removal and P removal is in place"]
C5 --- N12((NO)) --- T5_NO["Treatment = Not met"]
C5 --- Y12((YES)) --- T5_YES["Treatment = Met"]

T5_NO --- R18["Performance = Not met Compliance = NC"]
R18 -.- ID18(["02-B-18"])

T5_YES --- P5_YES["If COD, BOD5 and Phosphorus performance pass"]
P5_YES --- N13((NO)) --- R17["Performance = Not met Compliance = NC"]
R17 -.- ID17(["02-B-17"])
P5_YES --- Y13((YES)) --- R16["Performance = Met Compliance = C"]
R16 -.- ID16(["02-B-16"])

%% Branch 6
BR1 --- C6["If secondary treatment and N-removal and P-removal and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"]
C6 --- N14((NO)) --- T6_NO["Treatment = Not met Performance = Not met Compliance = NC"]
T6_NO -.- ID21(["02-B-21"])
C6 --- Y14((YES)) --- T6_YES["Treatment = Met"]

T6_YES --- P6_YES["If COD, BOD5 and Phosphorus performance pass"]
P6_YES --- N15((NO)) --- R20["Performance = Not met Compliance = NC"]
R20 -.- ID20(["02-B-20"])
P6_YES --- Y15((YES)) --- R19["Performance = Met Compliance = C"]
R19 -.- ID19(["02-B-19"])

%% Branch 7
BR2 --- C7["If secondary treatment and N-removal and P-removal and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"]
C7 --- N16((NO)) --- T7_NO["Treatment = Not met"]
C7 --- Y16((YES)) --- T7_YES["Treatment = Met"]

T7_NO --- P7_NO["If COD, BOD5, Nitrogen and Phosphorus performance pass"]
P7_NO --- N17((NO)) --- R25["Performance = Not met Compliance = NC"]
R25 -.- ID25(["02-B-25"])
P7_NO --- Y17((YES)) --- R24["Performance = Met Compliance = NC"]
R24 -.- ID24(["02-B-24"])

T7_YES --- P7_YES["If COD, BOD5, Nitrogen and Phosphorus performance pass"]
P7_YES --- N18((NO)) --- R23["Performance = Not met Compliance = NC"]
R23 -.- ID23(["02-B-23"])
P7_YES --- Y18((YES)) --- R22["Performance = Met Compliance = C"]
R22 -.- ID22(["02-B-22"])

%% Branch 8
BR3 --- C8["If secondary treatment and N-removal and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"]
C8 --- N19((NO)) --- T8_NO["Treatment = Not met"]
C8 --- Y19((YES)) --- T8_YES["Treatment = Met"]

T8_NO --- P8_NO["If COD, BOD5 and Nitrogen performance pass"]
P8_NO --- N20((NO)) --- R29["Performance = Not met Compliance = NC"]
R29 -.- ID29(["02-B-29"])
P8_NO --- Y20((YES)) --- R28["Performance = Met Compliance = NC"]
R28 -.- ID28(["02-B-28"])

T8_YES --- P8_YES["If COD, BOD5 and Nitrogen performance pass"]
P8_YES --- N21((NO)) --- R27["Performance = Not met Compliance = NC"]
R27 -.- ID27(["02-B-27"])
P8_YES --- Y21((YES)) --- R26["Performance = Met Compliance = C"]
R26 -.- ID26(["02-B-26"])

%% Branch 9
BR4 --- C9["If secondary treatment and P-removal and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"]
C9 --- N22((NO)) --- T9_NO["Treatment = Not met"]
C9 --- Y22((YES)) --- T9_YES["Treatment = Met"]

T9_NO --- P9_NO["If COD, BOD5 and Phosphorus performance pass"]
P9_NO --- N23((NO)) --- R33["Performance = Not met Compliance = NC"]
R33 -.- ID33(["02-B-33"])
P9_NO --- Y23((YES)) --- R32["Performance = Met Compliance = NC"]
R32 -.- ID32(["02-B-32"])

T9_YES --- P9_YES["If COD, BOD5 and Phosphorus performance pass"]
P9_YES --- N24((NO)) --- R31["Performance = Not met Compliance = NC"]
R31 -.- ID31(["02-B-31"])
P9_YES --- Y24((YES)) --- R30["Performance = Met Compliance = C"]
R30 -.- ID30(["02-B-30"])

%% Branch 10
BR5 --- C10["If secondary treatment and N-removal and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"]
C10 --- N25((NO)) --- T10_NO["Treatment = Not met"]
C10 --- Y25((YES)) --- T10_YES["Treatment = Met"]

T10_NO --- R36["Performance = Not met Compliance = NC"]
R36 -.- ID36(["02-B-36"])

T10_YES --- P10_YES["If COD and BOD5 performance pass"]
P10_YES --- N26((NO)) --- R35["Performance = Not met Compliance = NC"]
R35 -.- ID35(["02-B-35"])
P10_YES --- Y26((YES)) --- R34["Performance = Met Compliance = C"]
R34 -.- ID34(["02-B-34"])

%% Branch 11
BR6 --- C11["If secondary treatment and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"]
C11 --- N27((NO)) --- T11_NO["Treatment = Not met"]
C11 --- Y27((YES)) --- T11_YES["Treatment = Met"]

T11_NO --- P11_NO["If COD and BOD5 performance pass"]
P11_NO --- N28((NO)) --- R40["Performance = Not met Compliance = NC"]
R40 -.- ID40(["02-B-40"])
P11_NO --- Y28((YES)) --- R39["Performance = Met Compliance = NC"]
R39 -.- ID39(["02-B-39"])

T11_YES --- P11_YES["If COD and BOD5 performance pass"]
P11_YES --- N29((NO)) --- R38["Performance = Not met Compliance = NC"]
R38 -.- ID38(["02-B-38"])
P11_YES --- Y29((YES)) --- R37["Performance = Met Compliance = C"]
R37 -.- ID37(["02-B-37"])

%% Styles
classDef reference stroke:#00a2ff,color:#00a2ff;
classDef yesBox fill:#4CAF50,color:white,stroke:#2E7D32;
classDef noBox fill:#F44336,color:white,stroke:#C62828;

%% Class Assignments
class ID01,ID02,ID03,ID04,ID05,ID06,ID07,ID08,ID09,ID10,ID11,ID12,ID13,ID14,ID15,ID16,ID17,ID18,ID19,ID20,ID21,ID22,ID23,ID24,ID25,ID26,ID27,ID28,ID29,ID30,ID31,ID32,ID33,ID34,ID35,ID36,ID37,ID38,ID39,ID40 reference;
class Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12,Y13,Y14,Y15,Y16,Y17,Y18,Y19,Y20,Y21,Y22,Y23,Y24,Y25,Y26,Y27,Y28,Y29 yesBox;
class N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11,N12,N13,N14,N15,N16,N17,N18,N19,N20,N21,N22,N23,N24,N25,N26,N27,N28,N29 noBox;

```



## Pseudocode

```{dropdown} Show python code
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