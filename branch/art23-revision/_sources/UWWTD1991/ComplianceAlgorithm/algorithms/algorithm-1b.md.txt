# Algorithm 1b. UWWTP: Treatment required (Sensitive Areas)

## Overview

Algorithm 1b determines the required wastewater treatment level for a treatment plant when the most restrictive type of If receiving area (**TypeOfIf receivingArea**) is one of **SA**, **CSA**, **A54**, **A58**, or related codes. It considers:

* The size of the agglomeration (**biggestLoad**).
* The type of water body at the discharge point.
* Which articles apply (**articleApplies**).
* If receiving area parameters for Nitrogen, Phosphorus, and other treatments.
* Dates related to reporting and start of application.

***

## Simplified Logic

### 1. Check `article_applies`

* Only continues if **/A523/** appears in the string.
* Otherwise, nothing happens.

### 2. Check `dcp_type`

* If **CSA**, the algorithm delegates to **Algorithm 1c**.
* If **SA**, **A523**, or **A58523**, it processes **Algorithm 1b rules**.

### 3. Check Nitrogen Condition

* If **rca\_a\_nitro = 1** and **start date ≤ reporting date**:
  * Determines which combination of nutrients (**aN, aP, c**) is required.
  * Sets a **result string** and **exit leaf code** based on these combinations.

### 4. Secondary Conditions

* If the Nitrogen condition is not met:
  * Checks combinations of **rca\_b**, **rca\_a\_phos**, and **rca\_c** for “secondary” cases.
  * Assigns the corresponding **result string** and **exit leaf code**.

### 5. Update Plant Record

* Stores the calculated **result** and **exit\_leaf** using a placeholder function:
  * `update_algorithm_plant`

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

A["SA, CSA, A54 and/or A58"]

A --> B{"If biggest agglomeration generated load <=10000 p.e"}

B -->|YES| C{"Check waterbody type"}
B -->|NO| CSA{"CSA"}

%% <=10000 p.e

C --> ES["ES, FW or LF"]
C --> LC["LC or CW"]

ES --> SEC1["Required = Secondary"]
SEC1 -.-> ID1(["01-B-01"])

LC --> APP1["Required = Appropriate"]
APP1 -.-> ID2(["01-B-02"])

%% CSA branch

CSA -->|YES| ALG["See separate algorithm 1c"]

CSA -->|NO| ART{"Article 5(4) applies [cases 5(1)+5(4);5(8)+5(4)]"}

ART -->|YES| SEC2["Required = Secondary"]
SEC2 -.-> ID3(["01-B-03"])

ART -->|NO| ART2["[Article 5(4)+5(2,3)] or [Article 5(8)+5(4)+5(2,3)]"]
ART2 --> ART3["Required?"]
ART3 -.-> ID4(["01-B-04"])

%%%%%%%%%%%%%%%%%%%%%%

ART -->|NO| N111["Article 5(4)+5(2,3) applies"]

N111 --> N1_node{"If receiving area demands Nitrogen (rcaParameterN) and starting date of application before or equal reporting reference year"}

%% LEFT SUBTREE

N1_node -->|YES| P2{"If receiving area demands Phosphorus (rcaParameterP) and starting date of application before or equal reporting reference year"}
N1_node -->|NO| P1{"If receiving area demands Phosphorus (rcaParameterP) and starting date of application before or equal reporting reference year"}

%% N + P branch

P2 -->|YES| O3{"If receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year"}
P2 -->|NO| O4{"If receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year"}

O3 -->|YES| NPO["Required = Nitrogen + Phosphorus + Other"]
O3 -->|NO| NP["Required = Nitrogen + Phosphorus"]

NPO -.-> ID12(["01-B-12"])
NP -.-> ID11(["01-B-11"])

O4 -->|YES| NO1["Required = Nitrogen + Other"]
O4 -->|NO| NONLY["Required = Nitrogen"]

NO1 -.-> ID10(["01-B-10"])
NONLY -.-> ID9(["01-B-09"])

%% branch 2

P1 -->|YES| O1{"If receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year"}
P1 -->|NO| O2{"If receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year"}

O1 -->|YES| PHO_OTHER1["Required = Phosphorus + Other"]
O1 -->|NO| PHO1["Required = Phosphorus"]

PHO_OTHER1 -.-> ID8(["01-B-08"])
PHO1 -.-> ID7(["01-B-07"])

O2 -->|YES| OTHER1["Required = Other"]
O2 -->|NO| SEC3["Required = Secondary"]

OTHER1 -.-> ID6(["01-B-06"])
SEC3 -.-> ID5(["01-B-05"])

%% RIGHT-SIDE SA BRANCH

ART -->|NO| SA1["Article 5(4)+5(2,3) applies"]

SA1 --> SA["SA"]

SA --> N2_node{"If receiving area demands Nitrogen (aN) and starting date of application before or equal reporting reference year"}

N2_node -->|YES| P3{"If receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year"}
N2_node -->|NO| N3{"If receiving area demands Nitrogen (b) and starting date of application before or equal reporting reference year"}

%% aN + aP branch

P3 -->|YES| O5{"If receiving area demands Other (c) and starting date of application before or equal reporting reference year"}

O5 -->|YES| NPOTHER["Required = Nitrogen & Phosphorus & Other (aN+aP+c)"]
O5 -->|NO| NPONLY["Required = Nitrogen & Phosphorus (aN+aP)"]

NPOTHER -.-> ID16(["01-B-16"])
NPONLY -.-> ID15(["01-B-15"])

%% aN + c

P3 -->|NO| O6{"If receiving area demands Other (c) and starting date of application before or equal reporting reference year"}

O6 -->|YES| NOTHER["Required = Nitrogen & Other (aN+c)"]
O6 -->|NO| NREQ["Required = Nitrogen (aN)"]

NOTHER -.-> ID14(["01-B-14"])
NREQ -.-> ID13(["01-B-13"])

%% Nitrogen b branch

N3 -->|YES| P4{"If receiving area demands Other (c) and starting date of application before or equal reporting reference year"}
N3 -->|NO| P5{"If receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year"}

P4 -->|YES| P42{"If receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year"}
P4 -->|NO| P43{"If receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year"}

P42 -->|YES| NBO2["Required = Phosphorus (aP+b) & Nitrogen(b) & Other (aP+b+c)"]
P42 -->|NO| NBP2["Required = Nitrogen(b) & Other (b+c)"]

NBO2 -.-> ID24(["01-B-24"])
NBP2 -.-> ID23(["01-B-23"])

P43 -->|YES| NBO["Required = Nitrogen(b) & Phosphorus (aP+b)"]
P43 -->|NO| NBP["Required = Nitrogen(b)"]

NBO -.-> ID22(["01-B-22"])
NBP -.-> ID21(["01-B-21"])

P5 -->|YES| P6{"If receiving area demands Other (c) and starting date of application before or equal reporting reference year"}

P6 -->|YES| APO["Required = Phosphorus & Other (aP+c)"]
P6 -->|NO| PREQ["Required = Phosphorus (aP)"]

APO -.-> ID20(["01-B-20"])
PREQ -.-> ID18(["01-B-18"])

P5 -->|NO| O7{"If receiving area demands Other (c) and starting date of application before or equal reporting reference year"}

O7 -->|YES| OREQ["Required = Other (c)"]
O7 -->|NO| SEC4["Required = Secondary"]

OREQ -.-> ID19(["01-B-19"])
SEC4 -.-> ID17(["01-B-17"])

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

class B,C,CSA,ART,N1_node,P2,P1,O3,O4,O1,O2,N2_node,P3,O5,O6,N3,P4,P42,P43,P5,P6,O7 decision;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
```


## Pseudocode

```{dropdown} Show python code
```python
if biggestLoad <= 10000: 

    if dcpWaterBodyType in ('ES', 'FW', 'LF'): 
        result_required = "Secondary" 
        alg1_exit_leaf = "01-B-01" 

    elif dcpWaterBodyType in ('LC', 'CW'): 
        result_required = "Appropriate" 
        alg1_exit_leaf = "01-B-02" 

else:  # biggestLoad > 10000 

    if articleApplies contains '/A54/' or articleApplies contains '/A5854/': 
        result_required = "Secondary" 
        alg1_exit_leaf = "01-B-03" 

    elif articleApplies contains '/A54523/' or articleApplies contains '/A5854523/': 
        result_required = "" 
        alg1_exit_leaf = "01-B-04" 

    elif articleApplies contains '/A58523/': 

        # Determine result based on treatment parameters and dates 
        if not (rcaParameterN and rcaDateArt58 <= repSituationAt) and \ 
           not (rcaParameterP and rcaDateArt58 <= repSituationAt) and \ 
           not (rcaParameterOther and rcaDateArt58 <= repSituationAt): 
            result = "secondary" 
            alg1_exit_leaf = "01-B-05" 
 
        elif not (rcaParameterN and rcaDateArt58 <= repSituationAt) and \ 
             not (rcaParameterP and rcaDateArt58 <= repSituationAt) and \ 
             (rcaParameterOther and rcaDateArt58 <= repSituationAt): 
            result = "(other)" 
            alg1_exit_leaf = "01-B-06" 
 
        elif not (rcaParameterN and rcaDateArt58 <= repSituationAt) and \ 
             (rcaParameterP and rcaDateArt58 <= repSituationAt) and \ 
             not (rcaParameterOther and rcaDateArt58 <= repSituationAt): 
            result = "(phosphorus)" 
            alg1_exit_leaf = "01-B-07" 
 
        elif not (rcaParameterN and rcaDateArt58 <= repSituationAt) and \ 
             (rcaParameterP and rcaDateArt58 <= repSituationAt) and \ 
             (rcaParameterOther and rcaDateArt58 <= repSituationAt): 
            result = "(phosphorus+other)" 
            alg1_exit_leaf = "01-B-08" 
 
        elif (rcaParameterN and rcaDateArt58 <= repSituationAt) and \
             not (rcaParameterP and rcaDateArt58 <= repSituationAt) and \
             not (rcaParameterOther and rcaDateArt58 <= repSituationAt): 
            result = "(nitrogen)" 
            alg1_exit_leaf = "01-B-09" 
 
        elif (rcaParameterN and rcaDateArt58 <= repSituationAt) and \
             not (rcaParameterP and rcaDateArt58 <= repSituationAt) and \
             (rcaParameterOther and rcaDateArt58 <= repSituationAt): 
            result = "(nitrogen+other)" 
            alg1_exit_leaf = "01-B-10" 
 
        elif (rcaParameterN and rcaDateArt58 <= repSituationAt) and \
             (rcaParameterP and rcaDateArt58 <= repSituationAt) and \
             not (rcaParameterOther and rcaDateArt58 <= repSituationAt):
            result = "(nitrogen+phosphorus)" 
            alg1_exit_leaf = "01-B-11" 
 
        elif (rcaParameterN and rcaDateArt58 <= repSituationAt) and \
             (rcaParameterP and rcaDateArt58 <= repSituationAt) and \
             (rcaParameterOther and rcaDateArt58 <= repSituationAt): 
            result = "(nitrogen+phosphorus+other)" 
            alg1_exit_leaf = "01-B-12" 
 
        if "/A523/" in article_applies: 

            if dcp_type == "CSA": 
                goto: algorithm_1c(alg_plant_id) 

            elif dcp_type in ["SA", "A523", "A58523"]:

                if rca_a_nitro == 1 and rca_start_date <= rep_situation_at: 

                    if not (rca_a_phos == 1 and rca_start_date <= rep_situation_at) and \
                        not (rca_c == 1 and rca_start_date <= rep_situation_at): 
                            result = "(aN)" 
                            exit_leaf = "01-B-13" 

                    elif not (rca_a_phos == 1) and (rca_c == 1): 
                        result = "(aN+c)" 
                        exit_leaf = "01-B-14" 

                    elif (rca_a_phos == 1) and not (rca_c == 1): 
                        result = "(aN+aP)" 
                        exit_leaf = "01-B-15" 

                    else: 
                        result = "(aN+aP+c)" 
                        exit_leaf = "01-B-16" 
 
                else: 
                    if not (rca_b == 1 and rca_start_date <= rep_situation_at) and \
                       not (rca_c == 1 and rca_start_date <= rep_situation_at) and \ 
                       not (rca_a_phos == 1 and rca_start_date <= rep_situation_at): 
                        result = "Secondary" 
                        exit_leaf = "01-B-17" 

                    elif not rca_b and not rca_c and rca_a_phos: 
                        result = "(aP)" 
                        exit_leaf = "01-B-18" 

                    elif not rca_b and rca_c and not rca_a_phos: 
                        result = "(c)" 
                        exit_leaf = "01-B-19" 

                    elif not rca_b and rca_c and rca_a_phos: 
                        result = "(aP+c)" 
                        exit_leaf = "01-B-20" 

                    elif rca_b and not rca_c and not rca_a_phos: 
                        result = "(b)" 
                        exit_leaf = "01-B-21" 

                    elif rca_b and not rca_c and rca_a_phos: 
                        result = "(aP+b)" 
                        exit_leaf = "01-B-22" 

                    elif rca_b and rca_c and not rca_a_phos: 
                        result = "(b+c)" 
                        exit_leaf = "01-B-23" 
                        
                    else: 
                        result = "(aP+b+c)" 
                        exit_leaf = "01-B-24"
```