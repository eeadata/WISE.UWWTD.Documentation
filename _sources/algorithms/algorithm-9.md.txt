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
graph TB
ROOT["Agglomeration is <10.000pe"]

%% Left Branch
ROOT --> Y1((YES)) --- C_NR_01["Compliance Article 5 = NR"]
C_NR_01 -.- ID01(["09-01"])

%% Main NO Branch
ROOT --> N1((NO)) --- ART5["Article 5(4) applies"]

%% Art 5(4) YES
ART5 --- Y2((YES)) --- RCA["rca removal rate N<75% and removal rate P<75%"]

RCA --- Y3((YES)) --- C_NC_13["Compliance Article 5 = NC"]
C_NC_13 -.- ID13(["09-13"])

RCA --- N2((NO)) --- C_C_02["Compliance Article 5 = C"]
C_C_02 -.- ID02(["09-02"])

%% Art 5(4) NO
ART5 --- N3((NO)) --- MORE_STR["At least one plant has treatment required = more stringent"]

%% More stringent NO
MORE_STR --- N4((NO)) --- C_NR_03["Compliance Article 5 = NR"]
C_NR_03 -.- ID03(["09-03"])

%% More stringent YES
MORE_STR --- Y4((YES)) --- LOAD_DIS["Load discharged without treatment <=2% of generated load and <= 2000p.e"]

%% Load discharged NO
LOAD_DIS --- N5((NO)) --- DL5A["Deadline of article 5 is before or equal to reporting reference year"]

DL5A --- Y5((YES)) --- C_NC_04["Compliance article 5=NC"]
C_NC_04 -.- ID04(["09-04"])

DL5A --- N6((NO)) --- C_PD_05["Compliance article 5=PD"]
C_PD_05 -.- ID05(["09-05"])

%% Load discharged YES
LOAD_DIS --- Y6((YES)) --- SUM_LOAD["(Sum of load entering for all plants with treatment in place = primary or secondary or NI or compliance for article 5 = NC) <=1% and < 2000p.e."]

%% Sum load YES
SUM_LOAD --- Y7((YES)) --- COND_NC["At least one compliance for Article 5 = NC AND (Sum of load entering for all plants with compliance for article 5 = NC) >1% or >= 2000p.e."]

COND_NC --- Y8((YES)) --- C_NC_06["Compliance article 5 = NC"]
C_NC_06 -.- ID06(["09-06"])

COND_NC --- N7((NO)) --- COND_PD["At least one compliance for Article 5 = PD"]

COND_PD --- Y9((YES)) --- C_PD_07["Compliance article 5 =PD"]
C_PD_07 -.- ID07(["09-07"])

COND_PD --- N8((NO)) --- COND_C["At least one compliance for Article 5 = C"]

COND_C --- Y10((YES)) --- C_C_08["Compliance article 5 = C"]
C_C_08 -.- ID08(["09-08"])

COND_C --- N9((NO)) --- C_NR_09["Compliance article 5 = NR"]
C_NR_09 -.- ID09(["09-09"])

%% Sum load NO
SUM_LOAD --- N10((NO)) --- DL5B["Deadline of article 5 is <> (null or NR or NI or ?)"]

DL5B --- N11((NO)) --- C_NR_10["Compliance article 5=NR"]
C_NR_10 -.- ID10(["09-10"])

DL5B --- Y11((YES)) --- DL5C["Deadline of article 5 is before or equal to reporting reference year"]

DL5C --- Y12((YES)) --- C_NC_11["Compliance article 5=NC"]
C_NC_11 -.- ID11(["09-11"])

DL5C --- N12((NO)) --- C_PD_12["Compliance article 5=PD"]
C_PD_12 -.- ID12(["09-12"])


%% Styles
classDef reference stroke:#00a2ff,color:#00a2ff;
classDef yesBox fill:#4CAF50,color:white,stroke:#2E7D32;
classDef noBox fill:#F44336,color:white,stroke:#C62828;

%% Class Assignments
class ID01,ID02,ID03,ID04,ID05,ID06,ID07,ID08,ID09,ID10,ID11,ID12,ID13 reference;
class Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12 yesBox;
class N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11,N12 noBox;
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