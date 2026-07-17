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