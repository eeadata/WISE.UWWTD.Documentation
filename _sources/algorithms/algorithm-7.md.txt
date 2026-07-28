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

## Decision Tree

```{mermaid}
graph TB
ROOT["There is no station and aggPercWithoutTreatment>2%"]

ROOT --> Y1((YES)) --- DL_A["Deadline of article 4 is before or equal to reporting reference year"]
DL_A --- Y2((YES)) --- C_NC_1["Compliance article 4=NC"]
DL_A --- N1((NO)) --- C_PD_1["Compliance article 4=PD"]

ROOT --> N2((NO)) --- AT_LEAST["At least one station has treatment required = secondary or more stringent"]

AT_LEAST --- N3((NO)) --- C_NR_1["Compliance Article 4 = NR"]
AT_LEAST ---- Y3((YES)) --- LOAD_DIS["Load discharged without treatment <=2% of generated load and <=2000p.e"]

LOAD_DIS --- N4((NO)) --- DL_B["Deadline of article 4 is before or equal to reporting reference year"]
DL_B --- Y4((YES)) --- C_NC_2["Compliance article 4=NC"]
DL_B --- N5((NO)) --- C_PD_2["Compliance article 4=PD"]

LOAD_DIS --- Y5((YES)) --- BIG_COND["([(load collected in collecting system-sum of load entering the treatment plants)] + (Sum of load entering for all stations with treatment in place = primary or NI or compliance for article 4 = NC)) <=1% OR < 2000p.e"]

BIG_COND --- N6((NO)) --- DL_C["Deadline of article 4 is <> (null or NR or NI or ?)"]
DL_C --- N7((NO)) --- C_NR_2["Compliance article 4=NR"]
DL_C --- Y6((YES)) --- DL_D["Deadline of article 4 is before or equal to reporting reference year"]
DL_D --- Y7((YES)) --- C_NC_3["Compliance article 4=NC"]
DL_D --- N8((NO)) --- C_PD_3["Compliance article 4=PD"]

BIG_COND --- Y8((YES)) --- COND_NC["At least one compliance for Article 4 = NC AND Sum of load entering for all stations with compliance for article 4 = NC) >1% or >=2000p.e."]

COND_NC --- Y9((YES)) --- DL_E["Deadline of article 4 is before or equal to reporting reference year"]
DL_E --- Y10((YES)) --- C_NC_4["Compliance article 4 = NC"]
DL_E --- N9((NO)) --- C_PD_4["Compliance article 4 = PD"]

COND_NC --- N10((NO)) --- COND_PD["At least one compliance for Article 4 = PD OR agglomeration deadline article 4 is after reporting reference year"]

COND_PD --- Y11((YES)) --- C_PD_5["Compliance article 4 = PD"]
COND_PD --- N11((NO)) --- COND_C["At least one compliance for Article 4 = C"]

COND_C --- Y12((YES)) --- C_C_1["Compliance article 4 = C"]
COND_C --- N12((NO)) --- C_NR_3["Compliance article 4 = NR"]

%% Styles
classDef yesBox fill:#4CAF50,color:white,stroke:#2E7D32;
classDef noBox fill:#F44336,color:white,stroke:#C62828;

%% Class Assignments
class Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12 yesBox;
class N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11,N12 noBox;
```

## Pseudocode

```{dropdown} Show python code
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