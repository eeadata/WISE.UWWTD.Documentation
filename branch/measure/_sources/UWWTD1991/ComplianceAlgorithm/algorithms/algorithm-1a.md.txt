# Algorithm 1a. UWWTP: Treatment required

## Overview

First decision step in determining what wastewater treatment level is legally “required” for a given plant, based on:

* How big the plant’s connected agglomerations are (population equivalent load)
* What type of water body the discharge goes into (e.g., freshwater, coastal, sensitive area)
* Special deadlines for compliance to one or more articles of the 1991 UWWTD (Articles 3, 4, 5)
* Whether the plant is active and connected to an agglomeration

***

## Simplified Logic

### 1. Low load case

* If **load < 2000** →
  * `result_required = Appropriate`
  * `exit_leaf = 01-A-02`


### 2. If receiving area dependent cases

#### If receiving area in {SA, CSA, A54, A58, A58523, A523, A5854}

* Call **Algorithm 1b**


#### If receiving area = NA

* If water in **{ES, FW, LF}** →
  * `result_required = Secondary`
  * `exit_leaf = 01-A-03`

* Else if water in **{LC, CW}** →
  * If **load < 10000** →
    * `result_required = Appropriate`
    * `exit_leaf = 01-A-04`
  * Else →
    * `result_required = Secondary`
    * `exit_leaf = 01-A-05`

####  If receiving area = LSA

* If water in **{ES, LF}** →
  * If **2000 ≤ load ≤ 10000** →
    * `result_required = Primary`
    * `exit_leaf = 01-A-06`
  * Else →
    * `result_required = Secondary`
    * `exit_leaf = 01-A-07`

* Else if water in **{LC, CW}** →
  * If **load ≥ 150000** →
    * `result_required = Secondary`
    * `exit_leaf = 01-A-08`
  * Else if **load ≥ 10000** →
    * `result_required = Primary`
    * `exit_leaf = 01-A-09`
  * Else →
    * `result_required = Appropriate`
    * `exit_leaf = 01-A-10`

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

ROOT{"If number of discharge points > 0 (except BG and HR in 2018) and at least one agglomeration is connected"}

ROOT -->|YES| B1{"If biggest agglomeration generated load < 2000p.e"}
ROOT -->|NO| B2["Required = NR"]
B2 -.-> ID01(["01-A-01"])

B1 -->|YES| C1["Required = Appropriate"]
C1 -.-> ID02(["01-A-02"])

B1 -->|NO| C2{"Check receiving area type: If number of discharge points > 1 choose the most constraining (SA, CSA, A58>NA>LSA), if number of discharge points =0, use NA of type FW"}

C2 --> TYPE1["SA, CSA, A54 and/or A58"]
C2 --> TYPE2["NA"]
C2 --> TYPE3["LSA"]

%% SA, CSA, A54 branch
TYPE1 --> ALG1["see separate algorithms 1b and 1c"]

%% NA branch
TYPE2 --> WB1{"Check waterbody type"}
WB1 --> WB1_1["ES, FW or LF"]
WB1 --> WB1_2["LC or CW"]

WB1_1 --> REQ1["Required = Secondary"]
REQ1 -.-> ID03(["01-A-03"])

WB1_2 --> LOAD1{"If biggest agglomeration generated load < 10000p.e"}
LOAD1 -->|YES| REQ2["Required = Appropriate"]
REQ2 -.-> ID04(["01-A-04"])
LOAD1 -->|NO| REQ3["Required = Secondary"]
REQ3 -.-> ID05(["01-A-05"])

%% LSA branch
TYPE3 --> WB2{"Check waterbody type"}
WB2 --> WB2_1["ES or LF"]
WB2 --> WB2_2["LC or CW"]

WB2_1 --> LOAD2{"If biggest agglomeration generated load >= 2000 and <= 10000p.e"}
LOAD2 -->|YES| REQ4["Required = Primary"]
REQ4 -.-> ID06(["01-A-06"])
LOAD2 -->|NO| REQ5["Required = Secondary"]
REQ5 -.-> ID07(["01-A-07"])

WB2_2 --> LOAD3{"If biggest agglomeration generated load >= 150 000p.e"}
LOAD3 -->|YES| REQ6["Required = Secondary"]
REQ6 -.-> ID08(["01-A-08"])
LOAD3 -->|NO| LOAD4{"If biggest agglomeration generated load >= 10000p.e"}

LOAD4 -->|YES| REQ7["Required = Primary"]
REQ7 -.-> ID09(["01-A-09"])
LOAD4 -->|NO| REQ8["Required = Appropriate"]
REQ8 -.-> ID10(["01-A-10"])

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

class ROOT,B1,C2,WB1,LOAD1,WB2,LOAD2,LOAD3,LOAD4 decision;
class B2 nr;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
```


## Pseudocode

```{dropdown} Show python code
```python
# Low load case 
elif load < 2000: 
    result_required = "Appropriate" 
    exit_leaf = "01-A-02" 
 
# If receiving area dependent cases 
else: 
    if If receiving_area in {"SA", "CSA", "A54", "A58", "A58523", "A523", "A5854"}: 
        algorithm_1b()  # Call Algorithm 1b 
 
    elif If receiving_area == "NA": 
        if water in {"ES", "FW", "LF"}: 
            result_required = "Secondary" 
            exit_leaf = "01-A-03" 
        elif water in {"LC", "CW"}: 
            if load < 10000: 
                result_required = "Appropriate" 
                exit_leaf = "01-A-04" 
            else: 
                result_required = "Secondary" 
                exit_leaf = "01-A-05" 
 
    elif If receiving_area == "LSA": 
        if water in {"ES", "LF"}: 
            if 2000 <= load <= 10000: 
                result_required = "Primary" 
                exit_leaf = "01-A-06" 
            else: 
                result_required = "Secondary" 
                exit_leaf = "01-A-07" 
        elif water in {"LC", "CW"}: 
            if load >= 150000: 
                result_required = "Secondary" 
                exit_leaf = "01-A-08" 
            elif load >= 10000: 
                result_required = "Primary" 
                exit_leaf = "01-A-09" 
            else: 
                result_required = "Appropriate" 
                exit_leaf = "01-A-10"
```




