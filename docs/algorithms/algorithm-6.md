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

```

## Pseudocode

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