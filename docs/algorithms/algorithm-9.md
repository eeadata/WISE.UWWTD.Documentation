# Algorithm 9. Agglomeration: Article 5 only

## Overview

Determine compliance of an agglomeration with **Article 5** of the 1991 urban wastewater treatment directive, which focuses on nitrogen (**N**) and phosphorus (**P**) removal but also other more stringent parameters such as disinfection or specific treatments required for the purpose of the implementation of other EU Directives, and treatment stringency.

Compliance depends on:

* Agglomeration size.
* Applicability of Article 5(4).
* RCA removal rates.
* Load discharged without treatment.
* Load entering treatment plants.
* Treatment level of connected plants.
* Deadline for Article 5 relative to reporting year.

## Simplified Logic

### 1. Agglomeration < 10,000 p.e.

* → **NR**
* (`exit_leaf = 09-01`)

### 2. Agglomeration ≥ 10,000 p.e.

* If **Art.5(4) applies** and **N & P removal ≥ 75%** →
  * **C**
  * (`exit_leaf = 09-02`)

* Else, if **Art.5(4) applies** and **N or P removal < 75%** →
  * **NC**
  * (`exit_leaf = 09-13`)

* Else, if **no more stringent treatment required** →
  * **NR**
  * (`exit_leaf = 09-03`)

### 3. Check load discharged without treatment

#### If ≤ 2% and ≤ 2000 p.e.:

* If any plant **NC** and load entering NC > 1% & ≥ 2000 →
  * **NC**
  * (`exit_leaf = 09-06`)

* Else, if any plant **PD** →
  * **PD**
  * (`exit_leaf = 09-07`)

* Else, if any plant **C** →
  * **C**
  * (`exit_leaf = 09-08`)

* Else →
  * **NR**
  * (`exit_leaf = 09-09`)

#### Else (load > thresholds):

* Check **Article 5 deadline vs reporting date**:

  * If **aggDateArt5 ≤ repSituationAt** →
    * **NC**
    * (`exit_leaf = 09-04 or 09-11`)

  * If **aggDateArt5 > repSituationAt** →
    * **PD**
    * (`exit_leaf = 09-05 or 09-12`)

## Decision Tree

```{mermaid}

```

## Pseudocode

```{dropdown} Show python code
```python
 
A = (aggC1 * aggGenerated) * 0.01 
 
if aggGenerated < 10000: 
    return "NR", "09-01" 
 
if np_54 > 0: 
    if remN_remP_75 > 0: 
        return "C", "09-02" 
    else: 
        return "NC", "09-13" 
 
if np_treat_more_str == 0: 
    return "NR", "09-03" 
 
# Check load discharged without treatment 
if (aggPercWithoutTreatment <= 2.0 and (aggGenerated * aggPercWithoutTreatment * 0.01) <= 2000): 
    if np_5NC > 0 and sp_load_enter_5NC > A * 0.01 and sp_load_enter_5NC >= 2000: 
        return "NC", "09-06" 
    elif np_5PD > 0: 
        return "PD", "09-07" 
    elif np_5C > 0: 
        return "C", "09-08" 
    else: 
        return "NR", "09-09" 
        
else: 
    # Check Article 5 deadline 
    if aggDateArt5 is None: 
        return "NR", "09-10" 
    elif aggDateArt5 <= repSituationAt: 
        return "NC", "09-04"  # or 09-11 depending on branch 
    else: 
        return "PD", "09-05"  # or 09-12 depending on branch
```