# Algorithm 5. Agglomeration: Article 4, 5, 6 Compliance Exclusion

## Overview

Filters agglomerations based on connected plants and their treatment compliance, setting Art. 4–6 compliance accordingly, and delegates further processing to Algorithm 6 if conditions are not conclusive.

It also calls **Algorithm 10** and **Algorithm 11** when all plants are NR/NI with required “Appropriate treatment”.

## Simplified Logic

### Some wastewater collected

* (**sum\_percent\_wastewater\_collected > 0**)

### 1. Checks if plants are connected

#### 2a. At least one plant connected

* Checks if all connected plants require **Appropriate treatment** and have compliance = **NR or NI**:
  * If yes:
    * Art. 4, 5, 6 compliance = **NR**
    * Calls **Algorithm 10** and **Algorithm 11** for additional processing

  * If not:
    * Checks if at least one plant has compliance = **"?"** and the rest are **C/NR/PD**:
      * If yes →
        * Art. 4, 5, 6 compliance = **"?" (unknown)**
        * `exit_leaf = 05-02`

      * Otherwise →
        * Calls **Algorithm 6** to continue processing

#### 2b. No plants connected

* Two sub-cases based on **aggGenerated**:

  * **aggGenerated > 10000** →
    * Art. 4 & 5 = **"?"**
    * Art. 6 = **NR**
    * `exit_leaf = 05-01`

  * **aggGenerated < 10000** →
    * Art. 4 = **"?"**
    * Art. 5 & 6 = **NR**
    * `exit_leaf = 05-03`

## Pseudocode

```python
if sum_wastewater_collected > 0: 
    if num_plants_connected > 0: 
        # Check if all connected plants are "Appropriate" & NR/NI 
        if num_plants_required_appropriate_nr_ni == num_plants_connected: 
            setCompliance(agg_id, art4="NR", art5="NR", art6="NR", exit="05-04") 
            algorithm10(agg_id) 
            algorithm11(agg_id) 
            logFinalResults(agg_id) 
        else: 
            # Check if at least one "?" and others C/NR/PD 
            if ( 
                num_plants_comp_int > 0 
                and (num_plants_comp_int + num_plants_comp_c_nr_pd) 
                == num_plants_connected 
            ): 
                setCompliance(agg_id, art4="?", art5="?", art6="?", exit="05-02") 
            else: 
                algorithm6(agg_id) 
    else: 
        # No plants connected 
        if aggGenerated > 10000: 
            setCompliance(agg_id, art4="?", art5="?", art6="NR", exit="05-01") 
        else: 
            setCompliance(agg_id, art4="?", art5="NR", art6="NR", exit="05-03") 
        algorithm6(agg_id) 
else: 
    # No wastewater collected 
    algorithm6(agg_id)
```