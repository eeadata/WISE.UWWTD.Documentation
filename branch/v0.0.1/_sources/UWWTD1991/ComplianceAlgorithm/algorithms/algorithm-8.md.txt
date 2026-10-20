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

ROOT{"At least one plant has treatment required = primary"}

ROOT -->|NO| C_NR_1["Compliance Article 6 = NR"]
C_NR_1 -.-> ID01(["08-01"])

ROOT -->|YES| COND_1{"At least one compliance for Article 6 = NC and (Sum of load entering for all plants with compliance for article 6 = NC) >1% and >= 2000p.e."}

COND_1 -->|YES| C_NC_1["Compliance article 6 = NC"]
C_NC_1 -.-> ID02(["08-02"])

COND_1 -->|NO| COND_2{"At least one compliance for Article 6 = PD"}

COND_2 -->|YES| C_PD_1["Compliance article 6 = PD"]
C_PD_1 -.-> ID03(["08-03"])

COND_2 -->|NO| COND_3{"At least one compliance for Article 6 = C"}

COND_3 -->|YES| C_C_1["Compliance article 6 = C"]
C_C_1 -.-> ID04(["08-04"])

COND_3 -->|NO| C_NR_2["Compliance article 6 = NR"]
C_NR_2 -.-> ID05(["08-05"])

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

class ROOT,COND_1,COND_2,COND_3 decision;
class C_NC_1 nc;
class C_C_1 compliance;
class C_NR_1,C_NR_2 nr;
class C_PD_1 pd;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
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