# Algorithm 1c. UWWTP: Treatment Required (Catchment of Sensitive Areas) 

## Overview 

Determine the nutrient requirements for a plant based on the nitrogen and phosphorus flags for the 
receiving area (Eutrophication: rcaANitro, rcaAPhos; Quality of water for drinking: rcaB)  

Inputs:
- rcaANitro → Does the primary receiving area demand Nitrogen? 
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

```

## Pseudocode

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