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
graph TB
ROOT["If number of discharge points > 0 (except BG and HR in 2018) and at least one agglomeration is connected"]

ROOT --> Y1((YES)) --- B1["If biggest agglomeration generated load < 2000p.e"]
ROOT --> N1((NO)) --- B2["Required = NR"]
B2 -.- ID01(["01-A-01"])

B1 --- Y2((YES)) --- C1["Required = Appropriate"]
C1 -.- ID02(["01-A-02"])

B1 --- N2((NO)) --- C2["Check receiving area type: If number of discharge points > 1 choose the most constraining (SA, CSA, A58>NA>LSA), if number of discharge points =0, use NA of type FW"]

C2 --- TYPE1["SA, CSA, A54 and/or A58"]
C2 --- TYPE2["NA"]
C2 --- TYPE3["LSA"]

%% SA, CSA, A54 branch
TYPE1 --- ALG1["see separate algorithms 1b and 1c"]

%% NA branch
TYPE2 --- WB1["Check waterbody type"]
WB1 --- WB1_1["ES, FW or LF"]
WB1 --- WB1_2["LC or CW"]

WB1_1 --- REQ1["Required = Secondary"]
REQ1 -.- ID03(["01-A-03"])

WB1_2 --- LOAD1["If biggest agglomeration generated load < 10000p.e"]
LOAD1 --- Y3((YES)) --- REQ2["Required = Appropriate"]
REQ2 -.- ID04(["01-A-04"])
LOAD1 --- N3((NO)) --- REQ3["Required = Secondary"]
REQ3 -.- ID05(["01-A-05"])

%% LSA branch
TYPE3 --- WB2["Check waterbody type"]
WB2 --- WB2_1["ES or LF"]
WB2 --- WB2_2["LC or CW"]

WB2_1 --- LOAD2["If biggest agglomeration generated load >= 2000 and <= 10000p.e"]
LOAD2 --- Y4((YES)) --- REQ4["Required = Primary"]
REQ4 -.- ID06(["01-A-06"])
LOAD2 --- N4((NO)) --- REQ5["Required = Secondary"]
REQ5 -.- ID07(["01-A-07"])

WB2_2 --- LOAD3["If biggest agglomeration generated load >= 150 000p.e"]
LOAD3 --- Y5((YES)) --- REQ6["Required = Secondary"]
REQ6 -.- ID08(["01-A-08"])
LOAD3 --- N5((NO)) --- LOAD4["If biggest agglomeration generated load >= 10000p.e"]

LOAD4 --- Y6((YES)) --- REQ7["Required = Primary"]
REQ7 -.- ID09(["01-A-09"])
LOAD4 --- N6((NO)) --- REQ8["Required = Appropriate"]
REQ8 -.- ID10(["01-A-10"])

%% Styles
classDef reference stroke:#00a2ff,color:#00a2ff;
classDef yesBox fill:#4CAF50,color:white,stroke:#2E7D32;
classDef noBox fill:#F44336,color:white,stroke:#C62828;

%% Class Assignments
class ID01,ID02,ID03,ID04,ID05,ID06,ID07,ID08,ID09,ID10 reference;
class Y1,Y2,Y3,Y4,Y5,Y6 yesBox;
class N1,N2,N3,N4,N5,N6 noBox;
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




