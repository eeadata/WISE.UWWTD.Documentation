# Algorithm 11. Agglomeration: Legal Compliance of Articles 4, 5, and 6

## Overview

Determine the legal compliance for **Articles 4, 5, and 6** at the agglomeration level, based on:

* Compliance of Article 3 (**result\_compliance\_art3**)
* Compliance of Articles 4, 5, and 6 (**result\_compliance\_art4/5/6**)
* Agglomeration characteristics (**aggGenerated, np\_54**)

## Simplified Logic

### 1. Check NULLs

* Raises error if any input compliance is **NULL**.

### 2. If Article 3 = NC

* Check Article 6:
  * If **Article 6 ≠ NR and ≠ PD** →
    * Art4 = **NR**, Art5 = **NR**, Art6 = **NC**
    * (`exit_leaf = 11-02`)

* Else check Article 4:
  * If **Article 4 ≠ NR and ≠ PD** → check Article 5:
    * If **Article 5 ≠ NR and ≠ PD** →
      * Art4 = **NC**, Art5 = **NC**, Art6 = **NR**
      * (`exit_leaf = 11-04`)

    * Else →
      * Art4 = **NC**, Art5 = **Article5**, Art6 = **NR**
      * (`exit_leaf = 11-05`)

  * Else →
    * No change (**Art4/5/6 stay same**)
    * (`exit_leaf = 11-03`)

### 3. If Article 3 ≠ NC

#### Check `np_54` (Article 5(4) applies)

* If **yes** → check `aggGenerated < 10000`:
  * If **yes** →
    * Art4 = **Compliance art4**
    * Art5 = **NR**
    * Art6 = **Compliance art6**
    * (`exit_leaf = 11-08`)

  * Else → check Article 4:
    * If **Article 4 = C** →
      * Art4 = **Compliance art4**
      * Art5 = **NR**
      * Art6 = **Compliance art6**
      * (`exit_leaf = 11-06`)

    * Else →
      * Art4 = **Compliance art4**
      * Art5 = **NC**
      * Art6 = **Compliance art6**
      * (`exit_leaf = 11-07`)

#### If `np_54` = no

* Check Article 4:
  * If **Article 4 = NC** → check Article 5:
    * If **Article 5 ≠ NR and ≠ PD** →
      * Art4 = **NC**, Art5 = **NC**, Art6 = **NR**
      * (`exit_leaf = 11-04`)

    * Else →
      * Art4 = **NC**, Art5 = **Article5**, Art6 = **NR**
      * (`exit_leaf = 11-05`)

  * Else →
    * No change
    * (`exit_leaf = 11-01`)

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

ROOT{"Compliance article 3 = NC"}

%% Left Branch
ROOT -->|NO| ART5{"Article 5(4) applies"}

ART5 -->|YES| AGG{"Agglomeration is <10.000pe"}

AGG -->|YES| LEG_1108_1["Legal compliance Article 4 = Compliance Article 4"]
LEG_1108_1 --- LEG_1108_2["Legal compliance Article 5 = NR"]
LEG_1108_2 --- LEG_1108_3["Legal Compliance Article 6 = Compliance Article 6"]
LEG_1108_3 -.-> ID11_08(["11-08"])

AGG -->|NO| COMP_4C{"Compliance Article 4= C"}

COMP_4C -->|YES| LEG_1106_1["Legal compliance Article 4 = Compliance Article 4"]
LEG_1106_1 --- LEG_1106_2["Legal compliance Article 5 = NR"]
LEG_1106_2 --- LEG_1106_3["Legal Compliance Article 6 = Compliance Article 6"]
LEG_1106_3 -.-> ID11_06(["11-06"])

COMP_4C -->|NO| LEG_1107_1["Legal compliance Article 4 = Compliance Article 4"]
LEG_1107_1 --- LEG_1107_2["Legal compliance Article 5 = NC"]
LEG_1107_2 --- LEG_1107_3["Legal Compliance Article 6 = Compliance Article 6"]
LEG_1107_3 -.-> ID11_07(["11-07"])

ART5 -->|NO| COMP_4NC{"Compliance article 4 = NC"}

COMP_4NC -->|NO| LEG_1101_1["Legal compliance Article 4 = Compliance Article 4"]
LEG_1101_1 --- LEG_1101_2["Legal compliance Article 5 = Compliance Article 5"]
LEG_1101_2 --- LEG_1101_3["Legal Compliance Article 6 = Compliance Article 6"]
LEG_1101_3 -.-> ID11_01(["11-01"])

COMP_4NC -->|YES| COMP_5{"Compliance article 5 ≠ NR OR ≠ PD"}

%% Right Branch
ROOT -->|YES| COMP_6{"Compliance article 6 ≠ NR OR ≠ PD"}



COMP_6 -->|NO| COMP_4{"Compliance article 4 ≠ NR OR ≠ PD"}

COMP_4 -->|YES| COMP_5

COMP_5 -->|YES| LEG_1104_1["Legal compliance Article 4 = NC"]
LEG_1104_1 --- LEG_1104_2["Legal Compliance Article 5 = NC"]
LEG_1104_2 --- LEG_1104_3["Legal compliance Article 6 = NR"]
LEG_1104_3 -.-> ID11_04(["11-04"])

COMP_5 -->|NO| LEG_1105_1["Legal compliance Article 4 = NC"]
LEG_1105_1 --- LEG_1105_2["Legal compliance Article 5 = Compliance Article 5"]
LEG_1105_2 --- LEG_1105_3["Legal compliance Article 6 = NR"]
LEG_1105_3 -.-> ID11_05(["11-05"])

COMP_4 -->|NO| LEG_1103_1["Legal compliance Article 4 = Compliance Article 4"]
LEG_1103_1 --- LEG_1103_2["Legal compliance Article 5 = Compliance Article 5"]
LEG_1103_2 --- LEG_1103_3["Legal compliance Article 6 = Compliance Article 6."]
LEG_1103_3 -.-> ID11_03(["11-03"])

COMP_6 -->|YES| LEG_1102_1["Legal Compliance Article 4 = NR"]
LEG_1102_1 --- LEG_1102_2["Legal compliance Article 5 = NR"]
LEG_1102_2 --- LEG_1102_3["Legal Compliance Article 6 = NC"]
LEG_1102_3 -.-> ID11_02(["11-02"])

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

class ROOT,ART5,AGG,COMP_4C,COMP_4NC,COMP_6,COMP_4,COMP_5 decision;
class LEG_1102_3,LEG_1104_1,LEG_1104_2,LEG_1105_1,LEG_1107_2 nc;
class LEG_1102_1,LEG_1102_2,LEG_1104_3,LEG_1105_3,LEG_1106_2,LEG_1108_2 nr;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
```

## Pseudocode

```{dropdown} Show python code
```python
# Article 3 = NC branch 
if art3 == "NC": 
    if art6 not in ("NR", "PD"): 
        return ("NR", "NR", "NC"), "11-02" 
    else: 
        if art4 not in ("NR", "PD"): 
            if art5 not in ("NR", "PD"): 
                return ("NC", "NC", "NR"), "11-04" 
            else: 
                return ("NC", art5, "NR"), "11-05" 
        else: 
            return (art4, art5, art6), "11-03" 
 
# Article 3 != NC branch 
else: 
    if np_54 > 0: 
        if aggGenerated < 10000: 
            return (art4, "NR", art6), "11-08" 
        else: 
            if art4 == "C": 
                return (art4, "NR", art6), "11-06" 
            else: 
                return (art4, "NC", art6), "11-07" 
    else: 
        if art4 == "NC": 
            if art5 not in ("NR", "PD"): 
                return ("NC", "NC", "NR"), "11-04" 
            else: 
                return ("NC", art5, "NR"), "11-05" 
        else: 
            return (art4, art5, art6), "11-01" 
```