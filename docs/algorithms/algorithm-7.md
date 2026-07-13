# Algorithm 7. Agglomeration: Article 4 only

## Overview

Compliance of an agglomeration with **Article 4 of the 1991 urban wastewater treatment directive**.

The compliance depends on:

* the aggregation of compliance statuses of individual treatment plants, and
* the load discharged without treatment.

## Simplified Logic

### 1. No secondary/more stringent treatment required

* → **NR**
* (`exit_leaf = 07-01`)

### 2. Load discharged without treatment ≤ 2% and ≤ 2000 p.e.

* → check load entering stations and individual plant compliance

* Depending on:
  * deadlines, and
  * number of plants with **NC, PD, C**

→ set agglomeration compliance (**NC, PD, C**)

### 3. Load discharged without treatment > 2% or > 2000 p.e.

* → check Article 4 deadline vs reporting year
* → **NC or PD**

### 4. No station connected (`number_plants_connected = 0`) AND `aggPercWithoutTreatment > 2%`

* If **Article 4 deadline ≤ reporting reference year** →
  * compliance = **NC**
  * (`exit_leaf = 07-13`)

* If **Article 4 deadline > reporting reference year** →
  * compliance = **PD**
  * (`exit_leaf = 07-12`)

### 5. No plant satisfies conditions

* → fallback to **NR**

## Pseudocode

```python
if number_plants_connected = 0 and aggPercWithoutTreatment > 2%: 
 
    if deadline_article4 <= reporting_reference_year 
        # Deadline has passed → Non Compliant 
  return "NC", "07-13" 
 
    else: 
        # Deadline has not yet passed → Pending 
  return "PD", "07-12" 
 
else: 
 
# At least one station exists OR aggPercWithoutTreatment <= 2% 
A = (aggC1 * aggGenerated) * 0.01 
 
if np_treat_second_more_str > 0: 
    # At least one station requires secondary or more stringent treatment 
    if ( 
        aggPercWithoutTreatment <= 2.0 
        and (aggGenerated * aggPercWithoutTreatment) / 100 <= 2000 
    ): 
        # Load discharged without treatment is low 
        if ( 
            A - (sum_percent_wastewater_collected * aggGenerated) * 0.01 
        ) + sp_load_enter_treatNR_4NC <= A * 0.01 or ( 
            ( 
                aggC1 * aggGenerated * 0.01 
                - sum_percent_wastewater_collected * aggGenerated * 0.01 
            ) 
            + sp_load_enter_treatNR_4NC 
            < 2000 
        ): 
            if ( 
                np_4NC > 0 and sp_load_enter_4NC > A * 0.01 
            ) or sp_load_enter_4NC >= 2000: 
                # Deadline check for Article 4 
                if aggDateArt4 <= repSituationAt: 
                    return "NC", "07-04" 
                else: 
                    return "PD", "07-05" 
            else: 
                # Check PD or C plants 
                if np_4PD > 0 or aggDateArt4 > repSituationAt: 
                    return "PD", "07-06" 
                elif np_4C > 0: 
                    return "C", "07-07" 
                else: 
                    return "NR", "07-08" 
        else: 
            # Load condition not met → check deadlines 
            if aggDateArt4: 
                if aggDateArt4 <= repSituationAt: 
                    return "NC", "07-10" 
                else: 
                    return "PD", "07-11" 
            else:
                 return "NR", "07-09" 
    else: 
        # Load discharged without treatment > threshold → check deadline 
        if aggDateArt4 <= repSituationAt: 
            return "NC", "07-03" 
        else: 
            return "PD", "07-02" 
else: 
    # No secondary or more stringent treatment required 
    return "NR", "07-01" 
 
```