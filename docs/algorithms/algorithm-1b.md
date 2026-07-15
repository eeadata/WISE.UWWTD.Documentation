# Algorithm 1b. UWWTP: Treatment required (Sensitive Areas)

## Overview

Algorithm 1b determines the required wastewater treatment level for a treatment plant when the most restrictive type of receiving area (**TypeOfReceivingArea**) is one of **SA**, **CSA**, **A54**, **A58**, or related codes. It considers:

* The size of the agglomeration (**biggestLoad**).
* The type of water body at the discharge point.
* Which articles apply (**articleApplies**).
* Receiving area parameters for Nitrogen, Phosphorus, and other treatments.
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

```

## Pseudocode

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
        result_required = "?" 
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