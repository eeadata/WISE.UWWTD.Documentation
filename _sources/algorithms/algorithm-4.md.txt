(algorithm4)=
# Algorithm 4. Agglomeration: Article 3 Compliance

## Overview

This procedure checks whether an agglomeration ≥ 2000 p.e. has an adequate wastewater collection system by deadline date.

* If **<2000 p.e.** → not relevant (**NR**).
* If deadline not reached → pending (**PD**).
* If deadline reached → several branches:
  * Very small untreated load → compliant (**C**).
  * Too much untreated load → non-compliant (**NC**).
  * In-between → compliant but flagged with extra QC:
    * **QC** when a load is addressed by IAS (<=2% and <=1000 p.e.)
    * **AddQC** when significant load is addressed by IAS (>2% or >1000 p.e. of the generated load of the agglomeration)

## Simplified Logic

### 1. Low load case

* If **aggGenerated < 2000** →
  * compliance = **NR** for Art 3, 4, 5, 6
  * (`alg4_exit_leaf = 04-01`)

### 2. Agglomeration ≥ 2000

#### Deadline of Article 3 passed or unknown (`aggDateArt3 <= repSituationAt`)

1. If
   * (**wastewater not collected + wastewater treated in IAS**) ≤ 2000 p.e.
   * AND (**% not collected + % treated in IAS**) ≤ 2%  
     →
   * compliance = **C**
   * (`alg4_exit_leaf = 04 02`)

2. Else:
   * If (**% not collected > 2 OR sum not collected > 2000 p.e.**) →
     * compliance = **NC**
     * (`alg4_exit_leaf = 04-05`)

   * Else:
     * If (**wastewater treated in IAS > 2% OR sum treated in IAS > 1000 p.e.**) →
       * compliance = **C + AddQC**
       * (`alg4_exit_leaf = 04-06`)

     * Else →
       * compliance = **C + QC**
       * (`alg4_exit_leaf = 04-03`)

#### Deadline of Article 3 not yet passed

* compliance = **PD**
* (`alg4_exit_leaf = 04-04`)

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

ROOT{"Check agglomeration generated load"}

ROOT -->|< 2000p.e| LT2000_1["Compliance art3 = NR Compliance art4 = NR Compliance art5 = NR Compliance art6 = NR"]

LT2000_1 -.-> ID01(["04-01"])

ROOT -->|>= 2000p.e| GE2000{"Deadline of Article 3 is before or equal to reporting reference date"}

GE2000 -->|NO| ART3_PD["Compliance art3 = PD"]
ART3_PD -.-> ID04(["04-04"])

GE2000 -->|YES| COND1{"If ((sum of wastewater not collected in collecting system and not addressed by IAS) + sum of wastewater treated in IAS) <= 2000p.e AND ((% of wastewater not collected in collecting system and not addressed by IAS) + % of wastewater treated in IAS) <= 2%"}

COND1 -->|YES| ART3_C["Compliance art3 = C"]
ART3_C -.-> ID02(["04-02"])

COND1 -->|NO| COND2{"If (sum of wastewater not collected in collecting system and not addressed by IAS) > 2000p.e OR (% of wastewater not collected in collecting system and not addressed by IAS) > 2%"}

COND2 -->|YES| ART3_NC["Compliance art3 = NC"]
ART3_NC -.-> ID05(["04-05"])

COND2 -->|NO| COND3{"If addressed by IAS >2% or >1000pe"}

COND3 -->|YES| ART3_C_ADDQC["Compliance art3 = C Additionnal compliance art3: AddQC"]
ART3_C_ADDQC -.-> ID06(["04-06"])

COND3 -->|NO| ART3_C_QC["Compliance art3 = C Additionnal compliance art3= QC"]
ART3_C_QC -.-> ID03(["04-03"])

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

class ROOT,GE2000,COND1,COND2,COND3 decision;
class ART3_NC nc;
class ART3_C,ART3_C_ADDQC,ART3_C_QC compliance;
class LT2000_1,LT2000_2,LT2000_3,LT2000_4 nr;
class ART3_PD pd;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
```

## Pseudocode

```{dropdown} Show python code
```python
if aggGenerated < 2000: 
    setCompliance(agg_id, art3="NR", art4="NR", art5="NR", art6="NR", exit="04-01") 
 
else: 
    if aggDateArt3 <= repSituationAt: 
        # deadline reached 
        untreated_load = (aggGenerated * aggPercWithoutTreatment) / 100 
        ias_load = (aggGenerated * aggC2) / 100 
 
        if untreated_load + ias_load <= 2000 and (aggPercWithoutTreatment + aggC2) <= 2: 
            setCompliance(agg_id, art3="C", exit="04-02") 
 
        elif untreated_load > 2000 or aggPercWithoutTreatment > 2: 
            setCompliance(agg_id, art3="NC", exit="04-05") 
 
        else: 
            # borderline, check IAS 
            if aggC2 > 2 or ias_load > 1000: 
                setCompliance(agg_id, art3="C", add_art3="AddQC", exit="04-06") 
            else: 
                setCompliance(agg_id, art3="C", add_art3="QC", exit="04-03") 
 
    else: 
        # deadline not reached 
        setCompliance(agg_id, art3="PD", exit="04-04") 
```