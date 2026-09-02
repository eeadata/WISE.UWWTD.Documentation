# Algorithm 5. Agglomeration: Article 4, 5, 6 Compliance Exclusion

## Overview

Filters agglomerations based on connected plants and their treatment compliance, setting Art. 4–6 compliance accordingly, and delegates further processing to Algorithm 6 if conditions are not conclusive.

It also calls **Algorithm 10** and **Algorithm 11** when all plants are NR/NI with required “Appropriate treatment”.

## Simplified Logic

### Some wastewater collected

* (**sum\_percent\_wastewater\_collected > 0**)

### 1. Checks if plants are connected

#### 2a. At least one plant connected

* Checks if all connected plants require **Appropriate treatment** and have compliance = **NR or NI**:
  * If yes:
    * Art. 4, 5, 6 compliance = **NR**
    * Calls **Algorithm 10** and **Algorithm 11** for additional processing

  * If not:
    * Checks if at least one plant has compliance = **"?"** and the rest are **C/NR/PD**:
      * If yes →
        * Art. 4, 5, 6 compliance = **"?" (unknown)**
        * `exit_leaf = 05-02`

      * Otherwise →
        * Calls **Algorithm 6** to continue processing

#### 2b. No plants connected

* Two sub-cases based on **aggGenerated**:

  * **aggGenerated > 10000** →
    * Art. 4 & 5 = **"?"**
    * Art. 6 = **NR**
    * `exit_leaf = 05-01`

  * **aggGenerated < 10000** →
    * Art. 4 = **"?"**
    * Art. 5 & 6 = **NR**
    * `exit_leaf = 05-03`

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

ROOT{"agglomeration: sum of wastewater collected in collecting system > 0%"}

ROOT -->|NO| ALG6_1["see algorithm n°6"]
ROOT -->|YES| CONN{"at least connected to one treatment plant"}

CONN -->|YES| ALL_PLANTS{"all plants have treatment required = appropriate & treatment compliance = NR OR NI"}
CONN -->|NO| CHECK_LOAD{"Check agglomeration generated load > 10000p.e"}

%% Left Subtree
ALL_PLANTS -->|YES| COMP_NR_1["Compliance Article 4 = NR Compliance Article 5 = NR Compliance Article 6 = NR"]
COMP_NR_1 --> ALG10["see algorithm n°10"]
ALG10 -.-> ID04(["05-04"])

ALL_PLANTS -->|NO| AT_LEAST{"at least one treatment plant compliance =? and all other treatment plants compliance = C or NR or PD"}

AT_LEAST -->|YES| COMP_Q_1["Compliance Article 4 = ? Compliance Article 5 = ? Compliance Article 6 = ?"]
COMP_Q_1 --> ALG6_2["see algorithm n°6"]
ALG6_2 -.-> ID02(["05-02"])

AT_LEAST -->|NO| ALG6_NO["see algorithm n°6"]
ALG6_NO -.-> ID03(["05-03"])

%% Right Subtree
CHECK_LOAD -->|NO| LOAD_NO_1["Compliance Article 4 = ?"]
LOAD_NO_1 --- LOAD_NO_2["Compliance Article 5 = NR Compliance Article 6 = NR"]
LOAD_NO_2 --> ALG6_3["see algorithm n°6"]
ALG6_3 -.-> ID03(["05-03"])

CHECK_LOAD -->|YES| LOAD_YES_1["Compliance Article 4 = ? Compliance Article 5 = ?"]
LOAD_YES_1 --- LOAD_YES_3["Compliance Article 6 = NR"]
LOAD_YES_3 --> ALG6_4["see algorithm n°6"]
ALG6_4 -.-> ID01(["05-01"])

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

class ROOT,CONN,ALL_PLANTS,AT_LEAST,CHECK_LOAD decision;
class COMP_NR_1,COMP_NR_2,COMP_NR_3,LOAD_NO_2,LOAD_NO_3,LOAD_YES_3 nr;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;

```

## Pseudocode

```{dropdown} Show python code
```python
if sum_wastewater_collected > 0: 
    if num_plants_connected > 0: 
        # Check if all connected plants are "Appropriate" & NR/NI 
        if num_plants_required_appropriate_nr_ni == num_plants_connected: 
            setCompliance(agg_id, art4="NR", art5="NR", art6="NR", exit="05-04") 
            algorithm10(agg_id) 
            algorithm11(agg_id) 
            logFinalResults(agg_id) 
        else: 
            # Check if at least one "?" and others C/NR/PD 
            if ( 
                num_plants_comp_int > 0 
                and (num_plants_comp_int + num_plants_comp_c_nr_pd) 
                == num_plants_connected 
            ): 
                setCompliance(agg_id, art4="?", art5="?", art6="?", exit="05-02") 
            else: 
                algorithm6(agg_id) 
    else: 
        # No plants connected 
        if aggGenerated > 10000: 
            setCompliance(agg_id, art4="?", art5="?", art6="NR", exit="05-01") 
        else: 
            setCompliance(agg_id, art4="?", art5="NR", art6="NR", exit="05-03") 
        algorithm6(agg_id) 
else: 
    # No wastewater collected 
    algorithm6(agg_id)
```