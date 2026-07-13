# Algorithm 8. Agglomeration: Article 6 only

## Overview

Calculate compliance of an agglomeration with **Article 6** of the 1991 urban wastewater treatment directive.

Compliance depends on:

* treatment type at connected plants, and
* load entering plants.

## Simplified Logic

### 1. No primary treatment required

* → **NR**
* (`exit_leaf = 08-01`)

### 2. At least one primary treatment plant exists

* If any plant compliance = **NC** and load entering NC plants > 1% of collected load and ≥ 2000 p.e. →
  * **NC**
  * (`exit_leaf = 08-02`)

* Else, if any plant compliance = **PD** →
  * **PD**
  * (`exit_leaf = 08-03`)

* Else, if any plant compliance = **C** →
  * **C**
  * (`exit_leaf = 08-04`)

* Else →
  * **NR**
  * (`exit_leaf = 08-05`)

## Pseudocode

```python
A = (aggC1 * aggGenerated) * 0.01 
 
if np_treat_primary > 0: 
    # At least one primary treatment plant 
    if np_6NC > 0 and sp_load_enter_6NC > A*0.01 and sp_load_enter_6NC >= 2000: 
        return "NC", "08-02" 
    elif np_6PD > 0: 
        return "PD", "08-03" 
    elif np_6C > 0: 
        return "C", "08-04" 
    else: 
        return "NR", "08-05" 
else: 
    # No primary treatment plant 
    return "NR", "08-01" 
```