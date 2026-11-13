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

%%{init: {
  "theme": "base",
  "flowchart": {
    "curve": "basis",
    "nodeSpacing": 35,
    "rankSpacing": 55,
    "padding": 15
  }
}}%%

graph LR

%% ============================================================
%% DECISION TREE
%% ============================================================

ROOT{"More stringent treatment (uwwOtherTreatment)"}

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
B1 --> C1{"If secondary treatment, N-removal and P-removal is in place"}
C1 -->|NO| T1_NO["Treatment = Not met"]
C1 -->|YES| T1_YES["Treatment = Met"]

T1_NO --> P1_NO{"If COD, BOD5, Nitrogen and Phosphorus performance pass"}
P1_NO -->|NO| R04_1["Performance = Not met"]
R04_1 --- R04_2["Compliance = NC"]
R04_2 -.-> ID04(["02-B-04"])

P1_NO -->|YES| R03_1["Performance = Met"]
R03_1 --- R03_2["Compliance = NC"]
R03_2 -.-> ID03(["02-B-03"])

T1_YES --> P1_YES{"If COD, BOD5, Nitrogen and Phosphorus performance pass"}
P1_YES -->|NO| R02_1["Performance = Not met"]
R02_1 --- R02_2["Compliance = NC"]
R02_2 -.-> ID02(["02-B-02"])

P1_YES -->|YES| R01_1["Performance = Met"]
R01_1 --- R01_2["Compliance = C"]
R01_2 -.-> ID01(["02-B-01"])

%% Branch 2
B2 --> C2{"If secondary treatment and P-removal is in place"}
C2 -->|NO| T2_NO["Treatment = Not met"]
C2 -->|YES| T2_YES["Treatment = Met"]

T2_NO --> P2_NO{"If COD, BOD5 and Phosphorus performance pass"}
P2_NO -->|NO| R08_1["Performance = Not met"]
R08_1 --- R08_2["Compliance = NC"]
R08_2 -.-> ID08(["02-B-08"])

P2_NO -->|YES| R07_1["Performance = Met"]
R07_1 --- R07_2["Compliance = NC"]
R07_2 -.-> ID07(["02-B-07"])

T2_YES --> P2_YES{"If COD, BOD5 and Phosphorus performance pass"}
P2_YES -->|NO| R06_1["Performance = Not met"]
R06_1 --- R06_2["Compliance = NC"]
R06_2 -.-> ID06(["02-B-06"])

P2_YES -->|YES| R05_1["Performance = Met"]
R05_1 --- R05_2["Compliance = C"]
R05_2 -.-> ID05(["02-B-05"])

%% Branch 3
B3 --> C3{"If secondary treatment and N-removal is in place"}
C3 -->|NO| T3_NO["Treatment = Not met"]
C3 -->|YES| T3_YES["Treatment = Met"]

T3_NO --> P3_NO{"If COD, BOD5 and Nitrogen performance pass"}
P3_NO -->|NO| R12_1["Performance = Not met"]
R12_1 --- R12_2["Compliance = NC"]
R12_2 -.-> ID12(["02-B-12"])

P3_NO -->|YES| R11_1["Performance = Met"]
R11_1 --- R11_2["Compliance = NC"]
R11_2 -.-> ID11(["02-B-11"])

T3_YES --> P3_YES{"If COD, BOD5 and Nitrogen performance pass"}
P3_YES -->|NO| R10_1["Performance = Not met"]
R10_1 --- R10_2["Compliance = NC"]
R10_2 -.-> ID10(["02-B-10"])

P3_YES -->|YES| R09_1["Performance = Met"]
R09_1 --- R09_2["Compliance = C"]
R09_2 -.-> ID09(["02-B-09"])

%% Branch 4
B4 --> C4{"If secondary treatment and N-removal is in place"}
C4 -->|NO| T4_NO["Treatment = Not met"]
C4 -->|YES| T4_YES["Treatment = Met"]

T4_NO --> R15_1["Performance = Not met"]
R15_1 --- R15_2["Compliance = NC"]
R15_2 -.-> ID15(["02-B-15"])

T4_YES --> P4_YES{"If COD and BOD5 performance pass"}
P4_YES -->|NO| R14_1["Performance = Not met"]
R14_1 --- R14_2["Compliance = NC"]
R14_2 -.-> ID14(["02-B-14"])

P4_YES -->|YES| R13_1["Performance = Met"]
R13_1 --- R13_2["Compliance = C"]
R13_2 -.-> ID13(["02-B-13"])

%% Branch 5
B5 --> C5{"If secondary treatment and N-removal and P removal is in place"}
C5 -->|NO| T5_NO["Treatment = Not met"]
C5 -->|YES| T5_YES["Treatment = Met"]

T5_NO --> R18_1["Performance = Not met"]
R18_1 --- R18_2["Compliance = NC"]
R18_2 -.-> ID18(["02-B-18"])

T5_YES --> P5_YES{"If COD, BOD5 and Phosphorus performance pass"}
P5_YES -->|NO| R17_1["Performance = Not met"]
R17_1 --- R17_2["Compliance = NC"]
R17_2 -.-> ID17(["02-B-17"])

P5_YES -->|YES| R16_1["Performance = Met"]
R16_1 --- R16_2["Compliance = C"]
R16_2 -.-> ID16(["02-B-16"])

%% Branch 6
BR1 --> C6{"If secondary treatment and N-removal and P-removal and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"}
C6 -->|NO| T6_NO_1["Treatment = Not met"]
T6_NO_1 --- T6_NO_2["Performance = Not met"]
T6_NO_2 --- T6_NO_3["Compliance = NC"]
T6_NO_3 -.-> ID21(["02-B-21"])

C6 -->|YES| T6_YES["Treatment = Met"]

T6_YES --> P6_YES{"If COD, BOD5 and Phosphorus performance pass"}
P6_YES -->|NO| R20_1["Performance = Not met"]
R20_1 --- R20_2["Compliance = NC"]
R20_2 -.-> ID20(["02-B-20"])

P6_YES -->|YES| R19_1["Performance = Met"]
R19_1 --- R19_2["Compliance = C"]
R19_2 -.-> ID19(["02-B-19"])

%% Branch 7
BR2 --> C7{"If secondary treatment and N-removal and P-removal and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"}
C7 -->|NO| T7_NO["Treatment = Not met"]
C7 -->|YES| T7_YES["Treatment = Met"]

T7_NO --> P7_NO{"If COD, BOD5, Nitrogen and Phosphorus performance pass"}
P7_NO -->|NO| R25_1["Performance = Not met"]
R25_1 --- R25_2["Compliance = NC"]
R25_2 -.-> ID25(["02-B-25"])

P7_NO -->|YES| R24_1["Performance = Met"]
R24_1 --- R24_2["Compliance = NC"]
R24_2 -.-> ID24(["02-B-24"])

T7_YES --> P7_YES{"If COD, BOD5, Nitrogen and Phosphorus performance pass"}
P7_YES -->|NO| R23_1["Performance = Not met"]
R23_1 --- R23_2["Compliance = NC"]
R23_2 -.-> ID23(["02-B-23"])

P7_YES -->|YES| R22_1["Performance = Met"]
R22_1 --- R22_2["Compliance = C"]
R22_2 -.-> ID22(["02-B-22"])

%% Branch 8
BR3 --> C8{"If secondary treatment and N-removal and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"}
C8 -->|NO| T8_NO["Treatment = Not met"]
C8 -->|YES| T8_YES["Treatment = Met"]

T8_NO --> P8_NO{"If COD, BOD5 and Nitrogen performance pass"}
P8_NO -->|NO| R29_1["Performance = Not met"]
R29_1 --- R29_2["Compliance = NC"]
R29_2 -.-> ID29(["02-B-29"])

P8_NO -->|YES| R28_1["Performance = Met"]
R28_1 --- R28_2["Compliance = NC"]
R28_2 -.-> ID28(["02-B-28"])

T8_YES --> P8_YES{"If COD, BOD5 and Nitrogen performance pass"}
P8_YES -->|NO| R27_1["Performance = Not met"]
R27_1 --- R27_2["Compliance = NC"]
R27_2 -.-> ID27(["02-B-27"])

P8_YES -->|YES| R26_1["Performance = Met"]
R26_1 --- R26_2["Compliance = C"]
R26_2 -.-> ID26(["02-B-26"])

%% Branch 9
BR4 --> C9{"If secondary treatment and P-removal and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"}
C9 -->|NO| T9_NO["Treatment = Not met"]
C9 -->|YES| T9_YES["Treatment = Met"]

T9_NO --> P9_NO{"If COD, BOD5 and Phosphorus performance pass"}
P9_NO -->|NO| R33_1["Performance = Not met"]
R33_1 --- R33_2["Compliance = NC"]
R33_2 -.-> ID33(["02-B-33"])

P9_NO -->|YES| R32_1["Performance = Met"]
R32_1 --- R32_2["Compliance = NC"]
R32_2 -.-> ID32(["02-B-32"])

T9_YES --> P9_YES{"If COD, BOD5 and Phosphorus performance pass"}
P9_YES -->|NO| R31_1["Performance = Not met"]
R31_1 --- R31_2["Compliance = NC"]
R31_2 -.-> ID31(["02-B-31"])

P9_YES -->|YES| R30_1["Performance = Met"]
R30_1 --- R30_2["Compliance = C"]
R30_2 -.-> ID30(["02-B-30"])

%% Branch 10
BR5 --> C10{"If secondary treatment and N-removal and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"}
C10 -->|NO| T10_NO["Treatment = Not met"]
C10 -->|YES| T10_YES["Treatment = Met"]

T10_NO --> R36_1["Performance = Not met"]
R36_1 --- R36_2["Compliance = NC"]
R36_2 -.-> ID36(["02-B-36"])

T10_YES --> P10_YES{"If COD and BOD5 performance pass"}
P10_YES -->|NO| R35_1["Performance = Not met"]
R35_1 --- R35_2["Compliance = NC"]
R35_2 -.-> ID35(["02-B-35"])

P10_YES -->|YES| R34_1["Performance = Met"]
R34_1 --- R34_2["Compliance = C"]
R34_2 -.-> ID34(["02-B-34"])

%% Branch 11
BR6 --> C11{"If secondary treatment and one or more of UV, Chlorination, Ozonation, Sand filtration, Micro filtration or Other type of more stringent treatment is in place"}
C11 -->|NO| T11_NO["Treatment = Not met"]
C11 -->|YES| T11_YES["Treatment = Met"]

T11_NO --> P11_NO{"If COD and BOD5 performance pass"}
P11_NO -->|NO| R40_1["Performance = Not met"]
R40_1 --- R40_2["Compliance = NC"]
R40_2 -.-> ID40(["02-B-40"])

P11_NO -->|YES| R39_1["Performance = Met"]
R39_1 --- R39_2["Compliance = NC"]
R39_2 -.-> ID39(["02-B-39"])

T11_YES --> P11_YES{"If COD and BOD5 performance pass"}
P11_YES -->|NO| R38_1["Performance = Not met"]
R38_1 --- R38_2["Compliance = NC"]
R38_2 -.-> ID38(["02-B-38"])

P11_YES -->|YES| R37_1["Performance = Met"]
R37_1 --- R37_2["Compliance = C"]
R37_2 -.-> ID37(["02-B-37"])

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

class ROOT,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,P1_NO,P1_YES,P2_NO,P2_YES,P3_NO,P3_YES,P4_YES,P5_YES,P6_YES,P7_NO,P7_YES,P8_NO,P8_YES,P9_NO,P9_YES,P10_YES,P11_NO,P11_YES decision;
class R04_2,R03_2,R02_2,R08_2,R07_2,R06_2,R12_2,R11_2,R10_2,R15_2,R14_2,R18_2,R17_2,T6_NO_3,R20_2,R25_2,R24_2,R23_2,R29_2,R28_2,R27_2,R33_2,R32_2,R31_2,R36_2,R35_2,R40_2,R39_2,R38_2 nc;
class R01_2,R05_2,R09_2,R13_2,R16_2,R19_2,R22_2,R26_2,R30_2,R34_2,R37_2 compliance;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;

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