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
graph TB
ROOT["collected in collective system = 0 OR Treatment required = NR"]

ROOT --> Y1((YES)) --- T06_01["Compliance for Article 4 = NR <br> Compliance for Article 5 = NR <br> Compliance for Article 6 = NR"]
T06_01 -.- ID06_01(["06-01"])

ROOT --> N1((NO)) --- B1["treatment required = primary"]

B1 --- Y2((YES)) --- C45["Compliance for Article 4 = NR <br> Compliance for Article 5 = NR"]
C45 --- PT["if country is not PT"]

PT --- Y3((YES)) --- T06_21A["compliance for article 6=NR"]
T06_21A -.- ID06_21A(["06-21"])

PT --- N3((NO)) --- CC1["compliance = C"]
CC1 --- Y4((YES)) --- T06_02["Compliance for Article 6 = C"]
T06_02 -.- ID06_02(["06-02"])

CC1 --- N4((NO)) --- D6["Deadline of article 6 is before or equal to reporting reference year"]
D6 --- Y5((YES)) --- T06_03["Compliance for Article 6 = NC"]
T06_03 -.- ID06_03(["06-03"])

D6 --- N5((NO)) --- T06_04["Compliance for Article 6 = PD"]
T06_04 -.- ID06_04(["06-04"])

B1 --- N2((NO)) --- B1a["Compliance for Article 6 = NR"]
B1a --- B2["Treatment required = secondary and treatment in place = primary"]

B2 --- Y6((YES)) --- D4_1["Deadline of article 4 is before or equal to reporting reference year"]
D4_1 --- Y7((YES)) --- T06_05["Compliance for Article 4 = NC <br> Compliance for Article 5 = NR"]
T06_05 -.- ID06_05(["06-05"])
D4_1 --- N6((NO)) --- T06_06["Compliance for Article 4 = PD <br> Compliance for Article 5 = NR"]
T06_06 -.- ID06_06(["06-06"])

B2 --- N7((NO)) --- B3["treatment required = secondary and treatment in place = secondary or more stringent"]

B3 --- Y8((YES)) --- Perf1["COD and BOD5 performance = pass"]
Perf1 --- Y9((YES)) --- D5_1["Deadline of article 5 is before or equal to reporting reference year"]
D5_1 --- Y10((YES)) --- T06_07["Compliance for Article 4 = C <br> Compliance for Article 5 = NC"]
T06_07 -.- ID06_07(["06-07"])
D5_1 --- N8((NO)) --- T06_21B["Compliance for Article 4 = C <br> Compliance for Article 5 = PD"]
T06_21B -.- ID06_21B(["06-21"])

Perf1 --- N9((NO)) --- D4_2["Deadline of article 4 is before or equal to reporting reference year"]
D4_2 --- Y11((YES)) --- T06_08["Compliance for Article 4 = NC <br> Compliance for Article 5 = NR"]
T06_08 -.- ID06_08(["06-08"])
D4_2 --- N10((NO)) --- T06_09["Compliance for Article 4 = PD <br> Compliance for Article 5 = NR"]
T06_09 -.- ID06_09(["06-09"])

B3 --- N11((NO)) --- B4["treatment required = secondary and treatment in place = NR"]
B4 --- Y12((YES)) --- D4_3["Deadline of article 4 is before or equal to reporting reference year"]
D4_3 --- Y13((YES)) --- T06_10["Compliance for Article 4 = NC <br> Compliance for Article 5 = NR"]
T06_10 -.- ID06_10(["06-10"])
D4_3 --- N12((NO)) --- T06_11["Compliance for Article 4 = PD <br> Compliance for Article 5 = NR"]
T06_11 -.- ID06_11(["06-11"])

B4 --- N13((NO)) --- B5["treatment required = more stringent and treatment in place = NR"]
B5 --- Y14((YES)) --- D4_4["Deadline of article 4 is before or equal to reporting reference year"]
D4_4 --- Y15((YES)) --- D5_2["Deadline of article 5 is before or equal to reporting reference year"]
D5_2 --- Y16((YES)) --- T06_13["Compliance for Article 4 = NC <br> Compliance for Article 5 = NC"]
T06_13 -.- ID06_13(["06-13"])
D5_2 --- N14((NO)) --- T06_14["Compliance for Article 4 = NC <br> Compliance for Article 5 = PD"]
T06_14 -.- ID06_14(["06-14"])

D4_4 --- N15((NO)) --- T06_15["Compliance for Article 4 = PD <br> Compliance for Article 5 = PD"]
T06_15 -.- ID06_12(["06-12"])

B5 --- N16((NO)) --- B6["COD and BOD5 performance = pass"]
B6 --- Y17((YES)) --- CompC2["Compliance = C"]

CompC2 --- Y18((YES)) --- ASDF["Compliance for Article 4 = C <br> Compliance for Article 5 = C"]
ASDF -.- ID06_15(["06-15"])

CompC2 --- N17((NO)) --- D5_4["Deadline of article 5 is before or equal to reporting reference year"]
D5_4 --- Y19((YES)) --- T06_16["Compliance for Article 4 = C <br> Compliance for Article 5 = NC"]
T06_16 -.- ID06_16(["06-16"])
D5_4 --- N18((NO)) --- T06_17["Compliance for Article 4 = C <br> Compliance for Article 5 = PD"]
T06_17 -.- ID06_17(["06-17"])

B6 --- N19((NO)) --- Perf2["Deadline of article 4 is before or equal to reporting reference year"]
Perf2 --- Y20((YES)) --- D4_6["Deadline of article 4 is before or equal to reporting reference year"]
D4_6 --- Y21((YES)) --- T06_18["Compliance for Article 4 = NC <br> Compliance for Article 5 = NC"]
T06_18 -.- ID06_18(["06-18"])
D4_6 --- N20((NO)) --- T06_19["Compliance for Article 4 = NC <br> Compliance for Article 5 = PD"]
T06_19 -.- ID06_19(["06-19"])
Perf2 --- N21((NO)) --- T06_20["Compliance for Article 4 = PD <br> Compliance for Article 5 = PD"]
T06_20 -.- ID06_20(["06-20"])

%% Styles
classDef reference stroke:#00a2ff,color:#00a2ff;
classDef yesBox fill:#4CAF50,color:white,stroke:#2E7D32;
classDef noBox fill:#F44336,color:white,stroke:#C62828;

%% Class Assignments
class ID06_01,ID06_21A,ID06_02,ID06_03,ID06_04,ID06_05,ID06_06,ID06_07,ID06_21B,ID06_08,ID06_09,ID06_10,ID06_11,ID06_13,ID06_14,ID06_12,ID06_15,ID06_16,ID06_17,ID06_18,ID06_19,ID06_20 reference;
class Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12,Y13,Y14,Y15,Y16,Y17,Y18,Y19,Y20,Y21 yesBox;
class N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11,N12,N13,N14,N15,N16,N17,N18,N19,N20,N21 noBox;
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