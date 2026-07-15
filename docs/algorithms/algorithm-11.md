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

```

## Pseudocode

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