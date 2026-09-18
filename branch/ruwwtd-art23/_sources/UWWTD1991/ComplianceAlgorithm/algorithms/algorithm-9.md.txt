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
%%{init: {
  "theme": "base",
  "flowchart": {
    "curve": "basis",
    "nodeSpacing": 35,
    "rankSpacing": 55,
    "padding": 15
  },
  "themeVariables": {
    "fontFamily": "Arial, sans-serif",
    "fontSize": "14px",
    "lineColor": "#64748B",
    "textColor": "#1E293B" 
  }
}}%%

graph TB

%% ============================================================
%% DECISION TREE
%% ============================================================

ROOT{"Agglomeration is <10.000pe"}

%% Left Branch
ROOT -->|YES| C_NR_01["Compliance Article 5 = NR"]
C_NR_01 -.-> ID01(["09-01"])

%% Main NO Branch
ROOT -->|NO| ART5{"Article 5(4) applies"}

%% Art 5(4) YES
ART5 -->|YES| RCA{"rca removal rate N<75% and removal rate P<75%"}

RCA -->|YES| C_NC_13["Compliance Article 5 = NC"]
C_NC_13 -.-> ID13(["09-13"])

RCA -->|NO| C_C_02["Compliance Article 5 = C"]
C_C_02 -.-> ID02(["09-02"])

%% Art 5(4) NO
ART5 -->|NO| MORE_STR{"At least one plant has treatment required = more stringent"}

%% More stringent NO
MORE_STR -->|NO| C_NR_03["Compliance Article 5 = NR"]
C_NR_03 -.-> ID03(["09-03"])

%% More stringent YES
MORE_STR -->|YES| LOAD_DIS{"Load discharged without treatment <=2% of generated load and <= 2000p.e"}

%% Load discharged NO
LOAD_DIS -->|NO| DL5A{"Deadline of article 5 is before or equal to reporting reference year"}

DL5A -->|YES| C_NC_04["Compliance article 5=NC"]
C_NC_04 -.-> ID04(["09-04"])

DL5A -->|NO| C_PD_05["Compliance article 5=PD"]
C_PD_05 -.-> ID05(["09-05"])

%% Load discharged YES
LOAD_DIS -->|YES| SUM_LOAD{"(Sum of load entering for all plants with treatment in place = primary or secondary or NI or compliance for article 5 = NC) <=1% and < 2000p.e."}

%% Sum load YES
SUM_LOAD -->|YES| COND_NC{"At least one compliance for Article 5 = NC AND (Sum of load entering for all plants with compliance for article 5 = NC) >1% or >= 2000p.e."}

COND_NC -->|YES| C_NC_06["Compliance article 5 = NC"]
C_NC_06 -.-> ID06(["09-06"])

COND_NC -->|NO| COND_PD{"At least one compliance for Article 5 = PD"}

COND_PD -->|YES| C_PD_07["Compliance article 5 =PD"]
C_PD_07 -.-> ID07(["09-07"])

COND_PD -->|NO| COND_C{"At least one compliance for Article 5 = C"}

COND_C -->|YES| C_C_08["Compliance article 5 = C"]
C_C_08 -.-> ID08(["09-08"])

COND_C -->|NO| C_NR_09["Compliance article 5 = NR"]
C_NR_09 -.-> ID09(["09-09"])

%% Sum load NO
SUM_LOAD -->|NO| DL5B{"Deadline of article 5 is <> (null or NR or NI or ?)"}

DL5B -->|NO| C_NR_10["Compliance article 5=NR"]
C_NR_10 -.-> ID10(["09-10"])

DL5B -->|YES| DL5C{"Deadline of article 5 is before or equal to reporting reference year"}

DL5C -->|YES| C_NC_11["Compliance article 5=NC"]
C_NC_11 -.-> ID11(["09-11"])

DL5C -->|NO| C_PD_12["Compliance article 5=PD"]
C_PD_12 -.-> ID12(["09-12"])

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

class ROOT,ART5,RCA,MORE_STR,LOAD_DIS,DL5A,SUM_LOAD,COND_NC,COND_PD,COND_C,DL5B,DL5C decision;
class C_NC_13,C_NC_04,C_NC_06,C_NC_11 nc;
class C_C_02,C_C_08 compliance;
class C_NR_01,C_NR_03,C_NR_09,C_NR_10 nr;
class C_PD_05,C_PD_07,C_PD_12 pd;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
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