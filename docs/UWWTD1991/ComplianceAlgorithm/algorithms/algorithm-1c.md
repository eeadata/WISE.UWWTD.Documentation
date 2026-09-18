# Algorithm 1c. UWWTP: Treatment Required (Catchment of Sensitive Areas) 

## Overview 

Determine the nutrient requirements for a plant based on the nitrogen and phosphorus flags for the 
If receiving area (Eutrophication: rcaANitro, rcaAPhos; Quality of water for drinking: rcaB)  

Inputs:
- rcaANitro → Does the primary If receiving area demand Nitrogen? 
- rcaAPhos → Does it demand Phosphorus? 
- rcaB → Secondary Nitrogen demand.

## Simplified Logic

### 1. Check Article 5(4)

* If it applies, the result is automatically **"Secondary"** and exit leaf **"01-C-07"**.
* If it does not apply, we proceed to check nutrient demands.

### 2. Check primary Nitrogen (rcaANitro)

* If **rcaANitro = 1**:
  * If **rcaAPhos = 1**:
    * Required = **(aN+aP)**
    * Exit = **01-C-01**
  * Else:
    * Required = **(aN)**
    * Exit = **01-C-02**

* If **rcaANitro = 0**:
  * Use combinations of **rcaB** and **rcaAPhos** to determine:
    * **rcaB = 0 & rcaAPhos = 0** → Secondary, **01-C-03**
    * **rcaB = 0 & rcaAPhos = 1** → (aP), **01-C-04**
    * **rcaB = 1 & rcaAPhos = 0** → (b), **01-C-05**
    * **rcaB = 1 & rcaAPhos = 1** → (aP+b), **01-C-06**

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

CSA["CSA"] --> ART{"Article 5(4) applies"}

ART -->|YES| SEC["Required = Secondary"]
SEC -.-> ID07(["01-C-07"])

ART -->|NO| NAN{"If receiving area demands Nitrogen (aN)"}

NAN -->|YES| PAP1{"If receiving area demands Phosphorus (aP)"}
NAN -->|NO| NB{"If receiving area demands Nitrogen (b)"}

%% aN = YES branch
PAP1 -->|YES| NAP["Required = Nitrogen(a) & Phosphorus (aN + aP)"]
NAP -.-> ID01(["01-C-01"])

PAP1 -->|NO| NA["Required = Nitrogen(a) (aN)"]
NA -.-> ID02(["01-C-02"])

%% aN = NO branch (Nitrogen b)
NB -->|YES| PAP2{"If receiving area demands Phosphorus (aP)"}
NB -->|NO| PAP3{"If receiving area demands Phosphorus (aP)"}

%% Nitrogen b = YES branch
PAP2 -->|YES| NBP["Required = Nitrogen(b) & Phosphorus (b+aP)"]
NBP -.-> ID06(["01-C-06"])

PAP2 -->|NO| NBONLY["Required = Nitrogen (b)"]
NBONLY -.-> ID05(["01-C-05"])

%% Nitrogen b = NO branch
PAP3 -->|YES| PONLY["Required = Phosphorus (aP)"]
PONLY -.-> ID04(["01-C-04"])

PAP3 -->|NO| SEC2["Required = Secondary"]
SEC2 -.-> ID03(["01-C-03"])

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

class ART,NAN,PAP1,NB,PAP2,PAP3 decision;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
```



## Pseudocode

```{dropdown} Show python code
```python
if article_5_4_applies: 
    result_required = "Secondary" 
    exit_leaf = "01-C-07" 

else: 
    if rcaANitro == 1: 
        if rcaAPhos == 1: 
            result_required = "(aN+aP)" 
            exit_leaf = "01-C-01" 

        else: 
            result_required = "(aN)" 
            exit_leaf = "01-C-02" 
    else: 
        if rcaB == 0 and rcaAPhos == 0: 
            result_required = "Secondary" 
            exit_leaf = "01-C-03" 

        elif rcaB == 0 and rcaAPhos == 1: 
            result_required = "(aP)" 
            exit_leaf = "01-C-04" 
            
        elif rcaB == 1 and rcaAPhos == 0: 
            result_required = "(b)" 
            exit_leaf = "01-C-05" 
            
        elif rcaB == 1 and rcaAPhos == 1: 
            result_required = "(aP+b)" 
            exit_leaf = "01-C-06"
```