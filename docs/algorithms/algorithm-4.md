# Algorithm 4. Agglomeration: Article 3 Compliance

## Overview

This procedure checks whether an agglomeration ≥ 2000 p.e. has an adequate wastewater collection system by deadline date.

* If **<2000 p.e.** → not relevant (**NR**).
* If deadline not reached → pending (**PD**).
* If deadline reached → several branches:
  * Very small untreated load → compliant (**C**).
  * Too much untreated load → non-compliant (**NC**).
  * In-between → compliant but flagged with extra QC:
    * **QC** when a load is addressed by IAS (<=2% and <=1000 p.e.)
    * **AddQC** when significant load is addressed by IAS (>2% or >1000 p.e. of the generated load of the agglomeration)

## Simplified Logic

### 1. Low load case

* If **aggGenerated < 2000** →
  * compliance = **NR** for Art 3, 4, 5, 6
  * (`alg4_exit_leaf = 04-01`)

### 2. Agglomeration ≥ 2000

#### Deadline of Article 3 passed or unknown (`aggDateArt3 <= repSituationAt`)

1. If
   * (**wastewater not collected + wastewater treated in IAS**) ≤ 2000 p.e.
   * AND (**% not collected + % treated in IAS**) ≤ 2%  
     →
   * compliance = **C**
   * (`alg4_exit_leaf = 04 02`)

2. Else:
   * If (**% not collected > 2 OR sum not collected > 2000 p.e.**) →
     * compliance = **NC**
     * (`alg4_exit_leaf = 04-05`)

   * Else:
     * If (**wastewater treated in IAS > 2% OR sum treated in IAS > 1000 p.e.**) →
       * compliance = **C + AddQC**
       * (`alg4_exit_leaf = 04-06`)

     * Else →
       * compliance = **C + QC**
       * (`alg4_exit_leaf = 04-03`)

#### Deadline of Article 3 not yet passed

* compliance = **PD**
* (`alg4_exit_leaf = 04-04`)

## Pseudocode

```python
if aggGenerated < 2000: 
    setCompliance(agg_id, art3="NR", art4="NR", art5="NR", art6="NR", exit="04-01") 
 
else: 
    if aggDateArt3 <= repSituationAt: 
        # deadline reached 
        untreated_load = (aggGenerated * aggPercWithoutTreatment) / 100 
        ias_load = (aggGenerated * aggC2) / 100 
 
        if untreated_load + ias_load <= 2000 and (aggPercWithoutTreatment + aggC2) <= 2: 
            setCompliance(agg_id, art3="C", exit="04-02") 
 
        elif untreated_load > 2000 or aggPercWithoutTreatment > 2: 
            setCompliance(agg_id, art3="NC", exit="04-05") 
 
        else: 
            # borderline, check IAS 
            if aggC2 > 2 or ias_load > 1000: 
                setCompliance(agg_id, art3="C", add_art3="AddQC", exit="04-06") 
            else: 
                setCompliance(agg_id, art3="C", add_art3="QC", exit="04-03") 
 
    else: 
        # deadline not reached 
        setCompliance(agg_id, art3="PD", exit="04-04") 
```