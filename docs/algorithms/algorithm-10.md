# Algorithm 10. Agglomeration: Overall Compliance

## Overview

Overall compliance of an agglomeration based on the compliance results of **Articles 3, 4, 5, and 6**.

This is a **hierarchical logic**, where certain conditions override others.

## Simplified Logic

### 1. Check for NULLs

* Raises error if any article compliance is **NULL**.

### 2. Check for unknown (?)

* → Overall compliance = **?**
* (`exit_leaf = 10-01`)

### 3. If any Article = NC

* → Overall compliance = **NC**
* (`exit_leaf = 10-02`)

### 4. If Article 3 = NR

* → Overall compliance = **NR**
* (`exit_leaf = 10-03`)

### 5. If Article 3 = PD

* → Overall compliance = **PD**
* (`exit_leaf = 10-04`)

### 6. If Article 3 not in (C, QC)

* → Overall compliance = **?**
* (`exit_leaf = 10-05`)

### 7. If `aggGenerated < 10,000` & at least one plant with appropriate treatment

* → **C**
* (`exit_leaf = 10-06`)

### 8. If Article 6 = C or PD

* → Overall compliance = **C**
* (`exit_leaf = 10-07`)

### 9. If Article 4 = C, PD, or NR

* → Overall compliance = **C**
* (`exit_leaf = 10-08`)

### 10. Otherwise

* → Overall compliance = **NR**
* (`exit_leaf = 10-09`)

## Decision Tree

```{mermaid}

```

## Pseudocode

```{dropdown} Show python code
```python
# Unknown compliance 
if "?" in (art3, art4, art5, art6): 
    return "?", "10-01" 

# If any NC 
if "NC" in (art3, art4, art5, art6): 
    return "NC", "10-02" 

# Hierarchical checks 
if art3 == "NR": 
    return "NR", "10-03" 
elif art3 == "PD": 
    return "PD", "10-04" 
elif art3 not in ("C", "QC"): 
    return "?", "10-05" 
elif aggGenerated < 10000 and np_treat_appropriate > 0: 
    return "C", "10-06" 
elif art6 in ("C", "PD"): 
    return "C", "10-07" 
elif art4 in ("C", "PD", "NR"): 
    return "C", "10-08" 
else: 
    return "NR", "10-09" 
```