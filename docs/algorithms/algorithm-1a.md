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