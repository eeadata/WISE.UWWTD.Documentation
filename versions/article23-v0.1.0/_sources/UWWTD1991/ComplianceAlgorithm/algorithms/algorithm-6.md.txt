# Algorithm 6. Agglomeration: UWWTP Compliance for Article 4, 5, and 6

## Overview

Determines the compliance status (**NR, NC, PD, C**) based on:

* treatment requirements,
* treatment in place,
* COD/BOD performance,
* deadlines,
* and country-specific rules.

## Simplified Logic

### 1. No wastewater collected or treatment not required (NR)

* Directly mark compliance **NR** for all articles
* (`exit_leaf = 06-01`)

### 2. Treatment required is Primary

* For all countries except **PT** all compliance = **NR**
  * (`06-21`)

* If compliance = **C** →
  * Art6 = **C**, Art4/5 = **NR**
  * (`06-02`)

* Else →
  * Check if Portugal then Art.6 deadline vs reporting year (**C or NC or PD**)
  * (`06-02 / 06-04`)

### 3. Treatment required is Secondary

* **Primary treatment in place** →
  * Check Art.4 deadline (**NC / PD**)
  * (`06-05 / 06-06`)

* **Secondary or stringent treatment in place** →
  * Check COD/BOD performance → check Art.4 deadline (**C, NC, PD**)
  * (`06-07 → 06-09`)

* **Treatment not in place** →
  * Fallback to deadline checks and more stringent rules
  * (`06-10 → 06-11`)

### 4. Treatment required is More stringent treatment for N and/or P and/or other parameters

* **More stringent treatment in place** →
  * Check COD/BOD performance →
  * If pass → check Art.5 deadline (**C, NC, PD**)
  * (`06-15 → 06-17`)

* If **fail** →
  * Check Art.4 and Art.5 deadlines (**C, NC, PD**)
  * (`06-18 → 06-20`)

* **Treatment not in place** →
  * Fallback to deadline checks for Art.4 and Art.5 and rules
  * (`06-12 → 06-14`)

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

ROOT{"collected in collective system = 0 OR Treatment required = NR"}

ROOT -->|YES| T06_01_1["Compliance for Article 4 = NR Compliance for Article 5 = NR Compliance for Article 6 = NR"]
T06_01_1 -.-> ID06_01(["06-01"])

ROOT -->|NO| B1{"treatment required = primary"}

B1 -->|YES| C45_1["Compliance for Article 4 = NR Compliance for Article 5 = NR"]
C45_1 --> PT{"if country is not PT"}

PT -->|YES| T06_21A["compliance for article 6=NR"]
T06_21A -.-> ID06_21A(["06-21"])

PT -->|NO| CC1{"compliance = C"}
CC1 -->|YES| T06_02["Compliance for Article 6 = C"]
T06_02 -.-> ID06_02(["06-02"])

CC1 -->|NO| D6{"Deadline of article 6 is before or equal to reporting reference year"}
D6 -->|YES| T06_03["Compliance for Article 6 = NC"]
T06_03 -.-> ID06_03(["06-03"])

D6 -->|NO| T06_04["Compliance for Article 6 = PD"]
T06_04 -.-> ID06_04(["06-04"])

B1 -->|NO| B1a["Compliance for Article 6 = NR"]
B1a --> B2{"Treatment required = secondary and treatment in place = primary"}

B2 -->|YES| D4_1{"Deadline of article 4 is before or equal to reporting reference year"}
D4_1 -->|YES| T06_05_1["Compliance for Article 4 = NC"]
T06_05_1 --- T06_05_2["Compliance for Article 5 = NR"]
T06_05_2 -.-> ID06_05(["06-05"])

D4_1 -->|NO| T06_06_1["Compliance for Article 4 = PD"]
T06_06_1 --- T06_06_2["Compliance for Article 5 = NR"]
T06_06_2 -.-> ID06_06(["06-06"])

B2 -->|NO| B3{"treatment required = secondary and treatment in place = secondary or more stringent"}

B3 -->|YES| Perf1{"COD and BOD5 performance = pass"}
Perf1 -->|YES| D5_1{"Deadline of article 5 is before or equal to reporting reference year"}
D5_1 -->|YES| T06_07_1["Compliance for Article 4 = C"]
T06_07_1 --- T06_07_2["Compliance for Article 5 = NC"]
T06_07_2 -.-> ID06_07(["06-07"])

D5_1 -->|NO| T06_21B_1["Compliance for Article 4 = C"]
T06_21B_1 --- T06_21B_2["Compliance for Article 5 = PD"]
T06_21B_2 -.-> ID06_21B(["06-21"])

Perf1 -->|NO| D4_2{"Deadline of article 4 is before or equal to reporting reference year"}
D4_2 -->|YES| T06_08_1["Compliance for Article 4 = NC"]
T06_08_1 --- T06_08_2["Compliance for Article 5 = NR"]
T06_08_2 -.-> ID06_08(["06-08"])

D4_2 -->|NO| T06_09_1["Compliance for Article 4 = PD"]
T06_09_1 --- T06_09_2["Compliance for Article 5 = NR"]
T06_09_2 -.-> ID06_09(["06-09"])

B3 -->|NO| B4{"treatment required = secondary and treatment in place = NR"}
B4 -->|YES| D4_3{"Deadline of article 4 is before or equal to reporting reference year"}
D4_3 -->|YES| T06_10_1["Compliance for Article 4 = NC"]
T06_10_1 --- T06_10_2["Compliance for Article 5 = NR"]
T06_10_2 -.-> ID06_10(["06-10"])

D4_3 -->|NO| T06_11_1["Compliance for Article 4 = PD"]
T06_11_1 --- T06_11_2["Compliance for Article 5 = NR"]
T06_11_2 -.-> ID06_11(["06-11"])

B4 -->|NO| B5{"treatment required = more stringent and treatment in place = NR"}
B5 -->|YES| D4_4{"Deadline of article 4 is before or equal to reporting reference year"}
D4_4 -->|YES| D5_2{"Deadline of article 5 is before or equal to reporting reference year"}
D5_2 -->|YES| T06_13_1["Compliance for Article 4 = NC"]
T06_13_1 --- T06_13_2["Compliance for Article 5 = NC"]
T06_13_2 -.-> ID06_13(["06-13"])

D5_2 -->|NO| T06_14_1["Compliance for Article 4 = NC"]
T06_14_1 --- T06_14_2["Compliance for Article 5 = PD"]
T06_14_2 -.-> ID06_14(["06-14"])

D4_4 -->|NO| T06_15_1["Compliance for Article 4 = PD"]
T06_15_1 --- T06_15_2["Compliance for Article 5 = PD"]
T06_15_2 -.-> ID06_12(["06-12"])

B5 -->|NO| B6{"COD and BOD5 performance = pass"}
B6 -->|YES| CompC2{"Compliance = C"}

CompC2 -->|YES| ASDF_1["Compliance for Article 4 = C"]
ASDF_1 --- ASDF_2["Compliance for Article 5 = C"]
ASDF_2 -.-> ID06_15(["06-15"])

CompC2 -->|NO| D5_4{"Deadline of article 5 is before or equal to reporting reference year"}
D5_4 -->|YES| T06_16_1["Compliance for Article 4 = C"]
T06_16_1 --- T06_16_2["Compliance for Article 5 = NC"]
T06_16_2 -.-> ID06_16(["06-16"])

D5_4 -->|NO| T06_17_1["Compliance for Article 4 = C"]
T06_17_1 --- T06_17_2["Compliance for Article 5 = PD"]
T06_17_2 -.-> ID06_17(["06-17"])

B6 -->|NO| Perf2{"Deadline of article 4 is before or equal to reporting reference year"}
Perf2 -->|YES| D4_6{"Deadline of article 4 is before or equal to reporting reference year"}
D4_6 -->|YES| T06_18_1["Compliance for Article 4 = NC"]
T06_18_1 --- T06_18_2["Compliance for Article 5 = NC"]
T06_18_2 -.-> ID06_18(["06-18"])

D4_6 -->|NO| T06_19_1["Compliance for Article 4 = NC"]
T06_19_1 --- T06_19_2["Compliance for Article 5 = PD"]
T06_19_2 -.-> ID06_19(["06-19"])

Perf2 -->|NO| T06_20_1["Compliance for Article 4 = PD"]
T06_20_1 --- T06_20_2["Compliance for Article 5 = PD"]
T06_20_2 -.-> ID06_20(["06-20"])

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

class ROOT,B1,PT,CC1,D6,B2,D4_1,B3,Perf1,D5_1,D4_2,B4,D4_3,B5,D4_4,D5_2,B6,CompC2,D5_4,Perf2,D4_6 decision;

class T06_03,T06_05_1,T06_07_2,T06_08_1,T06_10_1,T06_13_1,T06_13_2,T06_14_1,T06_16_2,T06_18_1,T06_18_2,T06_19_1 nc;
class T06_02,T06_07_1,T06_21B_1,ASDF_1,ASDF_2,T06_16_1,T06_17_1 compliance;
class T06_01_1,T06_01_2,T06_01_3,C45_1,C45_2,T06_21A,B1a,T06_05_2,T06_06_2,T06_08_2,T06_09_2,T06_10_2,T06_11_2 nr;
class T06_04,T06_06_1,T06_21B_2,T06_09_1,T06_11_1,T06_14_2,T06_15_1,T06_15_2,T06_17_2,T06_19_2,T06_20_1,T06_20_2 pd;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
```

## Pseudocode

```{dropdown} Show python code
```python
# Determine if a more stringent treatment is required 
stringent_treatments = [ 
    '(aN)', 
    '(aN+aP)', 
    '(aN+aP+c)', 
    '(aN+c)', 
    '(aP)', 
    '(aP+b)', 
    '(aP+b+c)', 
    '(aP+c)', 
    '(b)', 
    '(b+c)', 
    '(c)', 
    '(nitrogen)', 
    '(nitrogen+other)', 
    '(nitrogen+phosphorus)', 
    '(nitrogen+phosphorus+other)', 
    '(other)',   
    '(phosphorus)', 
    '(phosphorus+other)'
    ] 
 
# --- Main decision tree --- 
if sum_percent_wastewater_collected + discharge_without_treatment == 0 or 
result_required == 'NR': 
    # Case 06-01 
    add_note(alg_agglo_id, 4, "Collected wastewater + discharge_without_treatment = 0 OR Treatment required = NR => Compliance = NR for Art.4, Art.5, Art.6") 
    update_plant_compliance(alg_plant_id, art4='NR', art5='NR', art6='NR', exit_leaf='06-01') 
 
elif result_required == 'Primary': 
    add_note(alg_agglo_id, 4, "Treatment required = Primary => Compliance has to be checked") 
    add_note(alg_agglo_id, 4, "Country not Portugal => Compliance = NR for Art.4, Art.5, Art.6") 
    update_plant_compliance(alg_plant_id, art4='NR', art5='NR', art6='NR', exit_leaf='06-21') 

    if result_compliance == 'C': 
        add_note(alg_agglo_id, 4, "Compliance = 'C' => Art.6 = C, Art.4/5 = NR") 
        update_plant_compliance(alg_plant_id, art4='NR', art5='NR', art6='C', exit_leaf='06-02') 
    else: 
        if aggDateArt3 <= rep_situation_at: 
            add_note(alg_agglo_id, 4, "Deadline art.6 <= Reporting year => Art.6 = NC, Art.4/5 = NR") 
            update_plant_compliance(alg_plant_id, art4='NR', art5='NR', art6='NC', exit_leaf='06-03') 
        else: 
            add_note(alg_agglo_id, 4, "Deadline art.6 > Reporting year => Art.6 = PD, Art.4/5 = NR") 
            update_plant_compliance(alg_plant_id, art4='NR', art5='NR', art6='PD', exit_leaf='06-04') 
 
else:  # Treatment not Primary 
    add_note(alg_agglo_id, 4, "Treatment required not Primary => Treatment and treatment in place have to be checked") 
 
    # Secondary treatment required and primary treatment in place 
    if result_required == 'Secondary' and highest_treatment_in_place == '1': 
        if aggDateArt4 <= rep_situation_at: 
            update_plant_compliance(alg_plant_id, art4='NC', art5='NR', art6='NR', exit_leaf='06-05') 
        else: 
            update_plant_compliance(alg_plant_id, art4='PD', art5='NR', art6='NR', exit_leaf='06-06') 
 
    # Secondary treatment required and secondary or stringent treatment in place 
    elif result_required == 'Secondary' and highest_treatment_in_place in ['2', 'S']:
        if uwwCODPerf == 'P' and uwwBOD5Perf == 'P': 
            if aggDateArt5 <= rep_situation_at: 
                update_plant_compliance(alg_plant_id, art4='C', art5='NR', art6='NR', exit_leaf='06-07') 
            else: 
                update_plant_compliance(alg_plant_id, art4='C', art5='PD', art6='NR', exit_leaf='06-21') 
        else: 
            if aggDateArt4 <= rep_situation_at: 
                if aggDateArt5 <= rep_situation_at: 
                    update_plant_compliance(alg_plant_id, art4='NC', art5='NC', art6='NR', exit_leaf='06-18') 
                else: 
                    update_plant_compliance(alg_plant_id, art4='NC', art5='PD', art6='NR', exit_leaf='06-19') 
            else: 
                update_plant_compliance(alg_plant_id, art4='PD', art5='PD', art6='NR', exit_leaf='06-20') 
 
    # More stringent treatment required 
    elif required_more_stringent and result_treatment == 'NR': 
        if aggDateArt4 <= rep_situation_at: 
            if aggDateArt5 <= rep_situation_at: 
                update_plant_compliance(alg_plant_id, art4='NC', art5='NC', art6='NR', exit_leaf='06-13') 
            else: 
                update_plant_compliance(alg_plant_id, art4='NC', art5='PD', art6='NR', exit_leaf='06-14') 
        else: 
            update_plant_compliance(alg_plant_id, art4='PD', art5='PD', art6='NR', exit_leaf='06-12') 
 
    # COD/BOD check fallback 
    else: 
        if uwwCODPerf == 'P' and uwwBOD5Perf == 'P': 
            if result_compliance == 'C': 
                update_plant_compliance(alg_plant_id, art4='C', art5='C', art6='NR', exit_leaf='06-15') 
            else: 
                if aggDateArt5 <= rep_situation_at: 
                    update_plant_compliance(alg_plant_id, art4='C', art5='NC', art6='NR', exit_leaf='06-16') 
                else: 
                    update_plant_compliance(alg_plant_id, art4='C', art5='PD', art6='NR', exit_leaf='06-17') 
        else: 
            if aggDateArt4 <= rep_situation_at: 
                if aggDateArt5 <= rep_situation_at: 
                    update_plant_compliance(alg_plant_id, art4='NC', art5='NC', art6='NR', exit_leaf='06-18') 
                else: 
                    update_plant_compliance(alg_plant_id, art4='NC', art5='PD', art6='NR', exit_leaf='06-19') 
            else: 
                update_plant_compliance(alg_plant_id, art4='PD', art5='PD', art6='NR', exit_leaf='06-20') 
```