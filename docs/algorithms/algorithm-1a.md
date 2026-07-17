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

A["SA, CSA, A54 and/or A58"]

A --> B["If biggest agglomeration generated load <=10000 p.e"]

B --- Y1((YES)) --- C["Check waterbody type"]
B --- N1((NO)) --- CSA["CSA"]

%% <=10000 p.e

C --- ES["ES, FW or LF"]
C --- LC["LC or CW"]

ES --- SEC1["Required = Secondary"]
SEC1 -.- ID1(["01-B-01"])

LC --- APP1["Required = Appropriate"]
APP1 -.- ID2(["01-B-02"])

%% CSA branch

CSA --- Y2((YES)) --- ALG["See separate algorithm 1c"]


CSA ------ N2((NO)) --- ART["Article 5(4) applies [cases 5(1)+5(4);5(8)+5(4)]"]

ART --- Y3((YES)) --- SEC2["Required = Secondary"]
SEC2 -.- ID3(["01-B-03"])

ART --- N4((NO)) --- ART2["[Article 5(4)+5(2,3)] or [Article 5(8)+5(4)+5(2,3)]"]
ART2 --- ART3["Required?"]
ART3 -.- ID4([01-B-04])

%%%%%%%%%%%%%%%%%%%%%%

ART --- N33((NO)) --- N111["Article 5(4)+5(2,3) applies"]

N111 --- N1_node["If receiving area demands Nitrogen (rcaParameterN) and starting date of application before or equal reporting reference year"]





%% LEFT SUBTREE

N1_node --- Y4((YES)) --- P2["If receiving area demands Phosphorus (rcaParameterP) and starting date of application before or equal reporting reference year"]
N1_node --- N5((NO)) --- P1["If receiving area demands Phosphorus (rcaParameterP) and starting date of application before or equal reporting reference year"]


%% N + P branch

P2 --- Y5((YES)) --- O3["If receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year"]
P2 --- N6((NO)) --- O4["If receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year"]

O3 --- Y6((YES)) --- NPO["Required = Nitrogen + Phosphorus + Other"]
O3 --- N7((NO)) --- NP["Required = Nitrogen + Phosphorus"]

NPO -.- ID12(["01-B-12"])
NP -.- ID11(["01-B-11"])

O4 --- Y7((YES)) --- NO1["Required = Nitrogen + Other"]
O4 --- N8((NO)) --- NONLY["Required = Nitrogen"]

NO1 -.- ID10(["01-B-10"])
NONLY -.- ID9(["01-B-09"])

%% branch 2

P1 --- Y8((YES)) --- O1["If receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year"]
P1 --- N9((NO)) --- O2["If receiving area demands Other (rcaParameterOther) and starting date of application before or equal reporting reference year"]

O1 --- Y9((YES)) --- PHO_OTHER1["Required = Phosphorus + Other"]
O1 --- N10((NO)) --- PHO1["Required = Phosphorus"]

PHO_OTHER1 -.- ID8(["01-B-08"])
PHO1 -.- ID7(["01-B-07"])

O2 --- Y10((YES)) --- OTHER1["Required = Other"]
O2 --- N11((NO)) --- SEC3["Required = Secondary"]

OTHER1 -.- ID6(["01-B-06"])
SEC3 -.- ID5(["01-B-05"])



%% RIGHT-SIDE SA BRANCH

ART --- N12((NO)) --- SA1["Article 5(4)+5(2,3) applies"]

SA1 --- SA["SA"]

SA --- N2_node["If receiving area demands Nitrogen (aN) and starting date of application before or equal reporting reference year"]

N2_node --- Y11((YES)) --- P3["If receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year"]
N2_node --- N13((NO)) --- N3["If receiving area demands Nitrogen (b) and starting date of application before or equal reporting reference year"]

%% aN + aP branch

P3 --- Y12((YES)) --- O5["If receiving area demands Other (c) and starting date of application before or equal reporting reference year"]

O5 --- Y13((YES)) --- NPOTHER["Required = Nitrogen & Phosphorus & Other (aN+aP+c)"]
O5 --- N14((NO)) --- NPONLY["Required = Nitrogen & Phosphorus (aN+aP)"]

NPOTHER -.- ID16(["01-B-16"])
NPONLY -.- ID15(["01-B-15"])

%% aN + c

P3 --- N15((NO)) --- O6["If receiving area demands Other (c) and starting date of application before or equal reporting reference year"]

O6 --- Y14((YES)) --- NOTHER["Required = Nitrogen & Other (aN+c)"]
O6 --- N16((NO)) --- NREQ["Required = Nitrogen (aN)"]

NOTHER -.- ID14(["01-B-14"])
NREQ -.- ID13(["01-B-13"])

%% Nitrogen b branch



N3 --- Y15((YES)) --- P4["If receiving area demands Other (c) and starting date of application before or equal reporting reference year"]
N3 --- N17((NO)) --- P5["If receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year"]

P4 --- Y16((YES)) --- P42["If receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year"]
P4 --- N18((NO)) --- P43["If receiving area demands Phosphorus (aP) and starting date of application before or equal reporting reference year"]

P42 --- Y17((YES)) --- NBO2["Required =  Phosphorus (aP+b) & Nitrogen(b) & Other (aP+b+c)"]
P42 --- N19((NO)) --- NBP2["Required = Nitrogen(b) & Other (b+c)"]

NBO2 -.- ID24(["01-B-24"])
NBP2 -.- ID23(["01-B-23"])


P43 --- Y18((YES)) --- NBO["Required = Nitrogen(b) & Phosphorus (aP+b)"]
P43 --- N20((NO)) --- NBP["Required = Nitrogen(b)"]

NBO -.- ID22(["01-B-22"])
NBP -.- ID21(["01-B-21"])





P5 --- Y19((YES)) --- P6["If receiving area demands Other (c) and starting date of application before or equal reporting reference year"]

P6 --- Y20((YES)) --- APO["Required = Phosphorus & Other (aP+c)"]
P6 --- N21((NO)) --- PREQ["Required = Phosphorus (aP)"]

APO -.- ID20(["01-B-20"])
PREQ -.- ID18(["01-B-18"])

P5 --- N22((NO)) --- O7["If receiving area demands Other (c) and starting date of application before or equal reporting reference year"]

O7 --- Y21((YES)) --- OREQ["Required = Other (c)"]
O7 --- N23((NO)) --- SEC4["Required = Secondary"]

OREQ -.- ID19(["01-B-19"])
SEC4 -.- ID17(["01-B-17"])

%% Styles
classDef reference stroke:#00a2ff,color:#00a2ff;
classDef yesBox fill:#4CAF50,color:white,stroke:#2E7D32;
classDef noBox fill:#F44336,color:white,stroke:#C62828;

%% Class Assignments
class ID1,ID2,ID3,ID4,ID5,ID6,ID7,ID8,ID9,ID10,ID11,ID12,ID13,ID14,ID15,ID16,ID17,ID18,ID19,ID20,ID21,ID22,ID23,ID24 reference;
class Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12,Y13,Y14,Y15,Y16,Y17,Y18,Y19,Y20,Y21 yesBox;
class N1,N2,N33,N4,N5,N6,N7,N8,N9,N10,N11,N12,N13,N14,N15,N16,N17,N18,N19,N20,N21,N22,N23 noBox;
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




