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
graph TB
CSA["CSA"] --> ART["Article 5(4) applies"]

ART --- Y1((YES)) --- SEC["Required = Secondary"]
SEC -.- ID07(["01-C-07"])

ART --- N1((NO)) --- NAN["If receiving area demands Nitrogen (aN)"]

NAN --- Y2((YES)) --- PAP1["If receiving area demands Phosphorus (aP)"]
NAN --- N2((NO)) --- NB["If receiving area demands Nitrogen (b)"]

%% aN = YES branch
PAP1 --- Y3((YES)) --- NAP["Required = Nitrogen(a) & Phosphorus (aN + aP)"]
NAP -.- ID01(["01-C-01"])

PAP1 --- N3((NO)) --- NA["Required = Nitrogen(a) (aN)"]
NA -.- ID02(["01-C-02"])

%% aN = NO branch (Nitrogen b)
NB --- Y4((YES)) --- PAP2["If receiving area demands Phosphorus (aP)"]
NB --- N4((NO)) --- PAP3["If receiving area demands Phosphorus (aP)"]

%% Nitrogen b = YES branch
PAP2 --- Y5((YES)) --- NBP["Required = Nitrogen(b) & Phosphorus (b+aP)"]
NBP -.- ID06(["01-C-06"])

PAP2 --- N5((NO)) --- NBONLY["Required = Nitrogen (b)"]
NBONLY -.- ID05(["01-C-05"])

%% Nitrogen b = NO branch
PAP3 --- Y6((YES)) --- PONLY["Required = Phosphorus (aP)"]
PONLY -.- ID04(["01-C-04"])

PAP3 --- N6((NO)) --- SEC2["Required = Secondary"]
SEC2 -.- ID03(["01-C-03"])

classDef reference stroke:#00a2ff,color:#00a2ff;
class ID07,ID01,ID02,ID06,ID05,ID04,ID03 reference;

%% Styles
classDef reference stroke:#00a2ff,color:#00a2ff;
classDef yesBox fill:#4CAF50,color:white,stroke:#2E7D32;
classDef noBox fill:#F44336,color:white,stroke:#C62828;

%% Class Assignments
class ID07,ID01,ID02,ID06,ID05,ID04,ID03 reference;
class Y1,Y2,Y3,Y4,Y5,Y6 yesBox;
class N1,N2,N3,N4,N5,N6 noBox;
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