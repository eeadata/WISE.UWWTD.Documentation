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
%%{init: {
  "theme": "base",
  "flowchart": {
    "curve": "basis",
    "nodeSpacing": 35,
    "rankSpacing": 55,
    "padding": 15
  }
}}%%

graph TB

%% ============================================================
%% DECISION TREE
%% ============================================================

ROOT{"Compliance Article 3 = ? or <br>Compliance Article 4 = ? or <br>Compliance Article 5 = ? or <br>Compliance Article 6 = ?"}

ROOT -->|YES| C_Q1["Compliance agglomeration =?"]
C_Q1 -.-> ID01(["10-01"])

ROOT -->|NO| COND_NC{"Compliance Article 3 = NC or <br>Compliance Article 4 = NC or <br>Compliance Article 5 = NC or <br>Compliance Article 6 = NC"}

COND_NC -->|YES| C_NC["Compliance agglomeration = NC"]
C_NC -.-> ID02(["10-02"])

COND_NC -->|NO| COND_NR{"(Compliance Article 3 = NR and <br>Compliance Article 4 = NR and <br>Compliance Article 5 = NR and <br>Compliance Article 6 = NR) or <br>Compliance Article 3 =NR"}

COND_NR -->|YES| C_NR1["Compliance agglomeration = NR"]
C_NR1 -.-> ID03(["10-03"])

COND_NR -->|NO| COND_PD{"Compliance Article 3 = PD"}

COND_PD -->|YES| C_PD["Compliance agglomeration = PD"]
C_PD -.-> ID04(["10-04"])

COND_PD -->|NO| COND_CQC{"Compliance Article 3 = C or QC"}

COND_CQC -->|NO| C_Q2["Compliance agglomeration = ?"]
C_Q2 -.-> ID05(["10-05"])

COND_CQC -->|YES| COND_LOAD{"Agglomeration generated load < 10,000p.e <br>and treatment required = appropriate"}

COND_LOAD -->|YES| C_C1["Compliance agglomeration = C"]
C_C1 -.-> ID06(["10-06"])

COND_LOAD -->|NO| COND_ART6{"Compliance Article 6 = C or PD"}

COND_ART6 -->|YES| C_C2["Compliance agglomeration = C"]
C_C2 -.-> ID07(["10-07"])

COND_ART6 -->|NO| COND_ART4{"Compliance Article 4 = C or PD or NR"}

COND_ART4 -->|YES| C_C3["Compliance agglomeration = C"]
C_C3 -.-> ID08(["10-08"])

COND_ART4 -->|NO| C_NR2["Compliance agglomeration = NR"]
C_NR2 -.-> ID09(["10-09"])

%% ============================================================
%% DECISION STYLE
%% ============================================================

classDef decision fill:#FFF7E6,stroke:#D97706,stroke-width:2px,color:#1E293B;

%% ============================================================
%% COMPLIANCE OUTCOME STYLES
%% ============================================================

%% NC = RED
classDef nc fill:#FEE2E2,stroke:#DC2626,stroke-width:2px,color:#991B1B;

%% C = GREEN
classDef compliance fill:#DCFCE7,stroke:#16A34A,stroke-width:2px,color:#166534;

%% NR = BLUE
classDef nr fill:#DBEAFE,stroke:#2563EB,stroke-width:2px,color:#1E40AF;

%% PD = GREY
classDef pd fill:#E5E7EB,stroke:#6B7280,stroke-width:2px,color:#374151;

%% ============================================================
%% APPLY STYLES
%% ============================================================

class ROOT,COND_NC,COND_NR,COND_PD,COND_CQC,COND_LOAD,COND_ART6,COND_ART4 decision;
class C_NC nc;
class C_C1,C_C2,C_C3 compliance;
class C_NR1,C_NR2 nr;
class C_PD pd;

%% ============================================================
%% EDGES
%% ============================================================

linkStyle default stroke:#64748B,stroke-width:1.5px;
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