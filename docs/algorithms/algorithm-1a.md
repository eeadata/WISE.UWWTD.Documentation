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


### 2. Receiving area dependent cases

#### Receiving area in {SA, CSA, A54, A58, A58523, A523, A5854}

* Call **Algorithm 1b**


#### Receiving area = NA

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

####  Receiving area = LSA

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

A["Number of discharge points > 0 (except BG and HR in 2018) and at least one agglomeration is connected"]

A -->|YES| B["Biggest agglomeration generated load < 2000 p.e"]
A -->|NO| NR["Required = NR"]

linkStyle 0 stroke:green,color:green,stroke-width:1px
linkStyle 1 stroke:red,color:red,stroke-width:1px


B -->|YES| APP1["Required = Appropriate"] 
B ---->|NO| C["Check receiving area type:
If number of discharge points > 1 choose the most constraining
(SA, CSA, A58>NA>LSA),
if number of discharge points = 0, use NA of type FW"]

linkStyle 2 stroke:green,color:green,stroke-width:1px
linkStyle 3 stroke:red,color:red,stroke-width:1px


%% Receiving area types


C ---> NA["NA"]
C ---> SA["SA, CSA, A54 and/or A58"]
C ---> LSA["LSA"]


%% SA branch

SA --> SA1["See separate algorithms 1b and 1c"]

%% NA branch

NA --> NA1["Check waterbody type"]

NA1 --> ES1["ES, FW or LF"]
NA1 --> LC1["LC or CW"]

ES1 --> SEC1["Required = Secondary"]

LC1 --> D["Biggest agglomeration generated load < 10000 p.e"]

D -->|YES| APP2["Required = Appropriate"]
D -->|NO| SEC2["Required = Secondary"]

linkStyle 13 stroke:green,color:green,stroke-width:1px
linkStyle 14 stroke:red,color:red,stroke-width:1px

%% LSA branch

LSA --> LSA1["Check waterbody type"]

LSA1 --> ES2["ES or LF"]
LSA1 --> LC2["LC or CW"]

ES2 --> E["Biggest agglomeration generated load >= 2000 and <= 10000 p.e"]

E -->|YES| PRI1["Required = Primary"]
E -->|NO| SEC3["Required = Secondary"]

linkStyle 19 stroke:green,color:green,stroke-width:1px
linkStyle 20 stroke:red,color:red,stroke-width:1px

LC2 --> F["Biggest agglomeration generated load >= 15000 p.e"]

F -->|YES| SEC4["Required = Secondary"]

F -->|NO| G["Biggest agglomeration generated load >= 10000 p.e"]

G -->|YES| PRI2["Required = Primary"]
G -->|NO| APP3["Required = Appropriate"]

linkStyle 22 stroke:green,color:green,stroke-width:1px
linkStyle 23 stroke:red,color:red,stroke-width:1px
linkStyle 24 stroke:green,color:green,stroke-width:1px
linkStyle 25 stroke:red,color:red,stroke-width:1px


%% Reference identifiers
 
NR -.- ID1(["01-A-01"])
APP1 -.- ID2(["01-A-02"])
SEC1 -.- ID3(["01-A-03"])
APP2 -.- ID4(["01-A-04"])
SEC2 -.- ID5(["01-A-05"])
PRI1 -.- ID6(["01-A-06"])
SEC3 -.- ID7(["01-A-07"])
SEC4 -.- ID8(["01-A-08"])
PRI2 -.- ID9(["01-A-09"])
APP3 -.- ID10(["01-A-10"])

classDef reference stroke:#00a2ff,color:#00a2ff;
class ID1,ID2,ID3,ID4,ID5,ID6,ID7,ID8,ID9,ID10 reference;

classDef decision fill:#ffffff,stroke:#000000,stroke-width:1px;
```


## Pseudocode

```python
# Low load case 
elif load < 2000: 
    result_required = "Appropriate" 
    exit_leaf = "01-A-02" 
 
# Receiving area dependent cases 
else: 
    if receiving_area in {"SA", "CSA", "A54", "A58", "A58523", "A523", "A5854"}: 
        algorithm_1b()  # Call Algorithm 1b 
 
    elif receiving_area == "NA": 
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
 
    elif receiving_area == "LSA": 
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
