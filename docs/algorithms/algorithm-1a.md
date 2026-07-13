# Algorithm 1a - UWWTP Treatment Required

## Overview

First decision step in determining what wastewater treatment level is legally “required” for a given plant, based on:

- How big the plant’s connected agglomerations are (population equivalent load)  
- What type of water body the discharge goes into (e.g., freshwater, coastal, sensitive area)  
- Special deadlines for compliance to one or more articles of the 1991 UWWTD (Articles 3, 4, 5)  
- Whether the plant is active and connected to an agglomeration  


## Simplified Logic


```python
1. Low load case
    if load < 2000:
        result_required = Appropriate  
        exit_leaf = 01-A-02  

2. Receiving area dependent cases
    if Receiving area in {SA, CSA, A54, A58, A58523, A523, A5854}:
        Call Algorithm 1b  

    else if receiving area = NA:
        if water in {ES, FW, LF}:
            result_required = Secondary  
            exit_leaf = 01-A-03  

    else if water in {LC, CW}: 
        if load < 10000:
            result_required = Appropriate  
            exit_leaf = 01-A-04  
        else:
            result_required = Secondary  
            exit_leaf = 01-A-05  
```



3. Receiving area = LSA
    - If water in {ES, LF} →  
    - If 2000 ≤ load ≤ 10000 →  
        - result_required = Primary  
        - exit_leaf = 01-A-06  
    - Else →  
        - result_required = Secondary  
        - exit_leaf = 01-A-07  

    - Else if water in {LC, CW} →  
    - If load ≥ 150000 →  
        - result_required = Secondary  
        - exit_leaf = 01-A-08  
    - Else if load ≥ 10000 →  
        - result_required = Primary  
        - exit_leaf = 01-A-09  
    - Else →  
        - result_required = Appropriate  
        - exit_leaf = 01-A-10  


## Decision Tree
