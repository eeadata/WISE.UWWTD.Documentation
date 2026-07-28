# Algorithm 11. Agglomeration: Legal Compliance of Articles 4, 5, and 6

## Overview

Determine the legal compliance for **Articles 4, 5, and 6** at the agglomeration level, based on:

* Compliance of Article 3 (**result\_compliance\_art3**)
* Compliance of Articles 4, 5, and 6 (**result\_compliance\_art4/5/6**)
* Agglomeration characteristics (**aggGenerated, np\_54**)

## Simplified Logic

### 1. Check NULLs

* Raises error if any input compliance is **NULL**.

### 2. If Article 3 = NC

* Check Article 6:
  * If **Article 6 ≠ NR and ≠ PD** →
    * Art4 = **NR**, Art5 = **NR**, Art6 = **NC**
    * (`exit_leaf = 11-02`)

* Else check Article 4:
  * If **Article 4 ≠ NR and ≠ PD** → check Article 5:
    * If **Article 5 ≠ NR and ≠ PD** →
      * Art4 = **NC**, Art5 = **NC**, Art6 = **NR**
      * (`exit_leaf = 11-04`)

    * Else →
      * Art4 = **NC**, Art5 = **Article5**, Art6 = **NR**
      * (`exit_leaf = 11-05`)

  * Else →
    * No change (**Art4/5/6 stay same**)
    * (`exit_leaf = 11-03`)

### 3. If Article 3 ≠ NC

#### Check `np_54` (Article 5(4) applies)

* If **yes** → check `aggGenerated < 10000`:
  * If **yes** →
    * Art4 = **Compliance art4**
    * Art5 = **NR**
    * Art6 = **Compliance art6**
    * (`exit_leaf = 11-08`)

  * Else → check Article 4:
    * If **Article 4 = C** →
      * Art4 = **Compliance art4**
      * Art5 = **NR**
      * Art6 = **Compliance art6**
      * (`exit_leaf = 11-06`)

    * Else →
      * Art4 = **Compliance art4**
      * Art5 = **NC**
      * Art6 = **Compliance art6**
      * (`exit_leaf = 11-07`)

#### If `np_54` = no

* Check Article 4:
  * If **Article 4 = NC** → check Article 5:
    * If **Article 5 ≠ NR and ≠ PD** →
      * Art4 = **NC**, Art5 = **NC**, Art6 = **NR**
      * (`exit_leaf = 11-04`)

    * Else →
      * Art4 = **NC**, Art5 = **Article5**, Art6 = **NR**
      * (`exit_leaf = 11-05`)

  * Else →
    * No change
    * (`exit_leaf = 11-01`)

## Decision Tree

```{mermaid}
graph TB
ROOT["Compliance article 3 = NC"]

%% Left Branch
ROOT --> N1((NO)) --- ART5["Article 5(4) applies"]

ART5 --- Y2((YES)) --- AGG["Agglomeration is <10.000pe"]

AGG --- Y3((YES)) --- LEG_1108["Legal compliance Article 4 = Compliance Article 4<br>Legal compliance Article 5 = NR<br>Legal Compliance Article 6 = Compliance Article 6"]
LEG_1108 -.- ID11_08(["11-08"])

AGG --- N3((NO)) --- COMP_4C["Compliance Article 4= C"]

COMP_4C --- Y4((YES)) --- LEG_1106["Legal compliance Article 4 = Compliance Article 4<br>Legal compliance Article 5 = NR<br>Legal Compliance Article 6 = Compliance Article 6"]
LEG_1106 -.- ID11_06(["11-06"])

COMP_4C --- N4((NO)) --- LEG_1107["Legal compliance Article 4 = Compliance Article 4<br>Legal compliance Article 5 = NC<br>Legal Compliance Article 6 = Compliance Article 6"]
LEG_1107 -.- ID11_07(["11-07"])

ART5 --- N2((NO)) --- COMP_4NC["Compliance article 4 = NC"]

COMP_4NC --- N5((NO)) --- LEG_1101["Legal compliance Article 4 = Compliance Article 4<br>Legal compliance Article 5 = Compliance Article 5<br>Legal Compliance Article 6 = Compliance Article 6"]
LEG_1101 -.- ID11_01(["11-01"])

COMP_4NC --- Y6((YES))
COMP_4NC --- N8((YES))

%% Right Branch
ROOT --> Y1((YES)) --- COMP_6["Compliance article 6 ≠ NR OR ≠ PD"]

COMP_6 --- Y5((YES)) --- LEG_1102["Legal Compliance Article 4 = NR<br>Legal compliance Article 5 = NR<br>Legal Compliance article 6 = NC"]
LEG_1102 -.- ID11_02(["11-02"])

COMP_6 --- N6((NO)) --- COMP_4["Compliance article 4 ≠ NR OR ≠ PD"]


COMP_4 --- Y6((YES)) --- COMP_5["Compliance article 5 ≠ NR OR ≠ PD"]
COMP_4 --- N5((YES))


COMP_5 --- Y7((YES)) --- LEG_1104["Legal compliance Article 4 = NC<br>Legal Compliance Article 5 = NC<br>Legal compliance Article 6 = NR"]
LEG_1104 -.- ID11_04(["11-04"])

COMP_5 --- N7((NO)) --- LEG_1105["Legal compliance Article 4 = NC<br>Legal Compliance Article 5 = Compliance Article 5<br>Legal compliance Article 6 = NR"]
LEG_1105 -.- ID11_05(["11-05"])

COMP_4 --- N8((NO)) --- LEG_1103["Legal compliance Article 4 = Compliance Article 4<br>Legal compliance Article 5 = Compliance Article 5<br>Legal compliance Article 6 = Compliance Article 6."]
LEG_1103 -.- ID11_03(["11-03"])

%% Styles
classDef reference stroke:#00a2ff,color:#00a2ff;
classDef yesBox fill:#4CAF50,color:white,stroke:#2E7D32;
classDef noBox fill:#F44336,color:white,stroke:#C62828;

%% Class Assignments
class ID11_01,ID11_02,ID11_03,ID11_04,ID11_05,ID11_06,ID11_07,ID11_08 reference;
class Y1,Y2,Y3,Y4,Y5,Y6,Y7 yesBox;
class N1,N2,N3,N4,N5,N6,N7,N8 noBox;
```

## Pseudocode

```{dropdown} Show python code
```python
# Article 3 = NC branch 
if art3 == "NC": 
    if art6 not in ("NR", "PD"): 
        return ("NR", "NR", "NC"), "11-02" 
    else: 
        if art4 not in ("NR", "PD"): 
            if art5 not in ("NR", "PD"): 
                return ("NC", "NC", "NR"), "11-04" 
            else: 
                return ("NC", art5, "NR"), "11-05" 
        else: 
            return (art4, art5, art6), "11-03" 
 
# Article 3 != NC branch 
else: 
    if np_54 > 0: 
        if aggGenerated < 10000: 
            return (art4, "NR", art6), "11-08" 
        else: 
            if art4 == "C": 
                return (art4, "NR", art6), "11-06" 
            else: 
                return (art4, "NC", art6), "11-07" 
    else: 
        if art4 == "NC": 
            if art5 not in ("NR", "PD"): 
                return ("NC", "NC", "NR"), "11-04" 
            else: 
                return ("NC", art5, "NR"), "11-05" 
        else: 
            return (art4, art5, art6), "11-01" 
```