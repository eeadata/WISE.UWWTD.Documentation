# Algorithm 8. Agglomeration: Article 6 only

## Overview

Calculate compliance of an agglomeration with **Article 6** of the 1991 urban wastewater treatment directive.

Compliance depends on:

* treatment type at connected plants, and
* load entering plants.

## Simplified Logic

### 1. No primary treatment required

* → **NR**
* (`exit_leaf = 08-01`)

### 2. At least one primary treatment plant exists

* If any plant compliance = **NC** and load entering NC plants > 1% of collected load and ≥ 2000 p.e. →
  * **NC**
  * (`exit_leaf = 08-02`)

* Else, if any plant compliance = **PD** →
  * **PD**
  * (`exit_leaf = 08-03`)

* Else, if any plant compliance = **C** →
  * **C**
  * (`exit_leaf = 08-04`)

* Else →
  * **NR**
  * (`exit_leaf = 08-05`)

## Decision Tree

```{mermaid}
graph TB
ROOT["At least one plant has treatment required = primary"]

ROOT --> N1((NO)) --- C_NR_1["Compliance Article 6 = NR"]
C_NR_1 -.- ID01(["08-01"])

ROOT --> Y1((YES)) --- COND_1["At least one compliance for Article 6 = NC and (Sum of load entering for all plants with compliance for article 6 = NC) >1% and >= 2000p.e."]

COND_1 --- Y2((YES)) --- C_NC_1["Compliance article 6 = NC"]
C_NC_1 -.- ID02(["08-02"])

COND_1 --- N2((NO)) --- COND_2["At least one compliance for Article 6 = PD"]

COND_2 --- Y3((YES)) --- C_PD_1["Compliance article 6 = PD"]
C_PD_1 -.- ID03(["08-03"])

COND_2 --- N3((NO)) --- COND_3["At least one compliance for Article 6 = C"]

COND_3 --- Y4((YES)) --- C_C_1["Compliance article 6 = C"]
C_C_1 -.- ID04(["08-04"])

COND_3 --- N4((NO)) --- C_NR_2["Compliance article 6 = NR"]
C_NR_2 -.- ID05(["08-05"])

%% Styles
classDef reference stroke:#00a2ff,color:#00a2ff;
classDef yesBox fill:#4CAF50,color:white,stroke:#2E7D32;
classDef noBox fill:#F44336,color:white,stroke:#C62828;

%% Class Assignments
class ID01,ID02,ID03,ID04,ID05 reference;
class Y1,Y2,Y3,Y4 yesBox;
class N1,N2,N3,N4 noBox;
```

## Pseudocode

```{dropdown} Show python code
```python
A = (aggC1 * aggGenerated) * 0.01 
 
if np_treat_primary > 0: 
    # At least one primary treatment plant 
    if np_6NC > 0 and sp_load_enter_6NC > A*0.01 and sp_load_enter_6NC >= 2000: 
        return "NC", "08-02" 
    elif np_6PD > 0: 
        return "PD", "08-03" 
    elif np_6C > 0: 
        return "C", "08-04" 
    else: 
        return "NR", "08-05" 
else: 
    # No primary treatment plant 
    return "NR", "08-01" 
```