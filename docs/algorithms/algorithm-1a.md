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

A["SA, CSA, A54 and/or A58"]

A --> B["If biggest agglomeration generated load <=10000 p.e"]

B -->|YES| C["Check waterbody type"]
B -->|NO| CSA["CSA"]

%% <=10000 p.e

C --> ES["ES, FW or LF"]
C --> LC["LC or CW"]

ES --> SEC1["Required = Secondary"]
SEC1 -.- ID1(["01-B-01"])

LC --> APP1["Required = Appropriate"]
APP1 -.- ID2(["01-B-02"])

%% CSA branch

CSA -->|YES| ALG["See separate algorithm 1c"]


CSA ----->|NO| ART["Article 5(4) applies [cases 5(1)+5(4);5(8)+5(4)]"]

ART -->|YES| SEC2["Required = Secondary"]
SEC2 -.- ID3(["01-B-03"])

ART -->|NO| N111["Article 5(4)+5(2,3) applies"]

N111 --> N1["Receiving area demands Nitrogen (rcaParameterN) and starting date of application before or equal reporting reference year?"]


ART -->|NO| ART2["[Article 5(4)+5(2,3)] or [Article 5(8)+5(4)+5(2,3)]"]
ART2 --> ART3["Required?"]
ART3 -.- ID4([01-B-04])


%% LEFT SUBTREE

N1 -->|YES| P2["Receiving area demands Phosphorus (rcaParameterP) and starting date of application before or equal reporting reference year?"]
N1 -->|NO| P1["Receiving area demands Phosphorus (rcaParameterP) and starting date of application before or equal reporting reference year?"]


%% N + P branch

P2 -->|YES| O3["Receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year?"]
P2 -->|NO| O4["Receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year?"]

O3 -->|YES| NPO["Required = Nitrogen + Phosphorus + Other"]
O3 -->|NO| NP["Required = Nitrogen + Phosphorus"]

NPO -.- ID12(["01-B-12"])
NP -.- ID11(["01-B-11"])

O4 -->|YES| NO1["Required = Nitrogen + Other"]
O4 -->|NO| NONLY["Required = Nitrogen"]

NO1 -.- ID10(["01-B-10"])
NONLY -.- ID9(["01-B-09"])

%% branch 2

P1 -->|YES| O1["Receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year?"]
P1 -->|NO| O2["Receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year?"]

O1 -->|YES| PHO_OTHER1["Required = Phosphorus + Other"]
O1 -->|NO| PHO1["Required = Phosphorus"]

PHO_OTHER1 -.- ID8(["01-B-08"])
PHO1 -.- ID7(["01-B-07"])

O2 -->|YES| OTHER1["Required = Other"]
O2 -->|NO| SEC3["Required = Secondary"]

OTHER1 -.- ID6(["01-B-06"])
SEC3 -.- ID5(["01-B-05"])



%% RIGHT-SIDE SA BRANCH

ART -->|NO| SA1["Article 5(4)+5(2,3) applies"]

SA1 --> SA["SA"]

SA --> N2["Receiving area demands Nitrogen (aN) and starting date of application before or equal reporting reference year?"]

N2 -->|YES| P3["Receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year?"]
N2 -->|NO| N3["Receiving area demands Nitrogen (b) and starting date of application before or equal reporting reference year?"]

%% aN + aP branch

P3 -->|YES| O5["Receiving area demands Other (c) and starting date of application before or equal reporting reference year?"]

O5 -->|YES| NPOTHER["Required = Nitrogen & Phosphorus & Other (aN+aP+c)"]
O5 -->|NO| NPONLY["Required = Nitrogen & Phosphorus (aN+aP)"]

NPOTHER -.- ID16(["01-B-16"])
NPONLY -.- ID15(["01-B-15"])

%% aN + c

P3 -->|NO| O6["Receiving area demands Other (c) and starting date of application before or equal reporting reference year?"]

O6 -->|YES| NOTHER["Required = Nitrogen & Other (aN+c)"]
O6 -->|NO| NREQ["Required = Nitrogen (aN)"]

NOTHER -.- ID14(["01-B-14"])
NREQ -.- ID13(["01-B-13"])

%% Nitrogen b branch



N3 -->|YES| P4["Receiving area demands Other (c) and starting date of application before or equal reporting reference year?"]
N3 -->|NO| P5["Receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year?"]

P4 -->|YES| P42["Receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year?"]
P4 -->|NO| P43["Receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year?"]

P42 -->|YES| NBO2["Required =  Phosphorus (aP+b) & Nitrogen(b) & Other (aP+b+c)"]
P42 -->|NO| NBP2["Required = Nitrogen(b) & Other (b+c)"]

NBO2 -.- ID24(["01-B-24"])
NBP2 -.- ID23(["01-B-23"])


P43 -->|YES| NBO["Required = Nitrogen(b) & Phosphorus (aP+b)"]
P43 -->|NO| NBP["Required = Nitrogen(b)"]

NBO -.- ID22(["01-B-22"])
NBP -.- ID21(["01-B-21"])





P5 -->|YES| P6["Receiving area demands Other (c) and starting date of application before or equal reporting reference year?"]

P6 -->|YES| APO["Required = Phosphorus & Other (aP+c)"]
P6 -->|NO| PREQ["Required = Phosphorus (aP)"]

APO -.- ID20(["01-B-20"])
PREQ -.- ID18(["01-B-18"])

P5 -->|NO| O7["Receiving area demands Other (c) and starting date of application before or equal reporting reference year?"]

O7 -->|YES| OREQ["Required = Other (c)"]
O7 -->|NO| SEC4["Required = Secondary"]

OREQ -.- ID19(["01-B-19"])
SEC4 -.- ID17(["01-B-17"])

classDef reference stroke:#00a2ff,color:#00a2ff;
class ID1,ID2,ID3,ID4,ID5,ID6,ID7,ID8,ID9,ID10,ID11,ID12,ID13,ID14,ID15,ID16,ID17,ID18,ID19,ID20,ID21,ID22,ID23,ID24 reference;

linkStyle 1 stroke:green,color:green,stroke-width:1px
linkStyle 2 stroke:red,color:red,stroke-width:1px
linkStyle 9 stroke:green,color:green,stroke-width:1px
linkStyle 10 stroke:red,color:red,stroke-width:1px
linkStyle 11 stroke:green,color:green,stroke-width:1px
linkStyle 15 stroke:red,color:red,stroke-width:1px
linkStyle 18 stroke:green,color:green,stroke-width:1px
linkStyle 20 stroke:green,color:green,stroke-width:1px
linkStyle 21 stroke:red,color:red,stroke-width:1px
linkStyle 22 stroke:green,color:green,stroke-width:1px
linkStyle 23 stroke:red,color:red,stroke-width:1px
linkStyle 26 stroke:green,color:green,stroke-width:1px
linkStyle 27 stroke:red,color:red,stroke-width:1px
linkStyle 19 stroke:red,color:red,stroke-width:1px

linkStyle 30 stroke:green,color:green,stroke-width:1px
linkStyle 31 stroke:red,color:red,stroke-width:1px

linkStyle 32 stroke:green,color:green,stroke-width:1px
linkStyle 33 stroke:red,color:red,stroke-width:1px

linkStyle 36 stroke:green,color:green,stroke-width:1px
linkStyle 37 stroke:red,color:red,stroke-width:1px

linkStyle 43 stroke:green,color:green,stroke-width:1px
linkStyle 44 stroke:red,color:red,stroke-width:1px
linkStyle 45 stroke:green,color:green,stroke-width:1px

linkStyle 46 stroke:green,color:green,stroke-width:1px
linkStyle 47 stroke:red,color:red,stroke-width:1px

linkStyle 50 stroke:red,color:red,stroke-width:1px
linkStyle 51 stroke:green,color:green,stroke-width:1px
linkStyle 52 stroke:red,color:red,stroke-width:1px

linkStyle 55 stroke:green,color:green,stroke-width:1px
linkStyle 56 stroke:red,color:red,stroke-width:1px
linkStyle 57 stroke:red,color:red,stroke-width:1px

linkStyle 58 stroke:red,color:red,stroke-width:1px
linkStyle 59 stroke:green,color:green,stroke-width:1px
linkStyle 60 stroke:red,color:red,stroke-width:1px

linkStyle 63 stroke:green,color:green,stroke-width:1px
linkStyle 64 stroke:red,color:red,stroke-width:1px

linkStyle 65 stroke:red,color:red,stroke-width:1px

linkStyle 67 stroke:green,color:green,stroke-width:1px

linkStyle 68 stroke:green,color:green,stroke-width:1px
linkStyle 69 stroke:red,color:red,stroke-width:1px

linkStyle 72 stroke:red,color:red,stroke-width:1px

linkStyle 73 stroke:green,color:green,stroke-width:1px
linkStyle 74 stroke:red,color:red,stroke-width:1px
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