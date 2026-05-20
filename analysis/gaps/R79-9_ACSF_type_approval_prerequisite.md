# R79-9 — R.79 ACSF Type Approval as Separate Prerequisite

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Administrative / process gap — prerequisite for R.171 DCAS approval) |
| **R.79 Reference** | UN R.79 04 S6 §5.6 + Annex 8 |
| **R.171 Reference** | §5.1 (DCAS shall incorporate ACSF functions complying with R.79) |
| **CN Reference** | No equivalent type approval framework in L2GB |
| **Gap Type** | Missing in CN (EU-specific regulatory approval structure) |

---

## R.79 Requirement

Under the EU regulatory framework, the ACSF functions in G1.3 require separate type approval under R.79, in addition to DCAS approval under R.171:

**Cat B1 (Lane Centering — low speed)**: R.79 §5.6.2 — required as a prerequisite for Cat C
**Cat B2 (Lane Centering — higher speed)**: R.79 §5.6.2 — applies when B1 operational envelope is extended
**Cat C (Driver-confirmed Lane Change)**: R.79 §5.6.4 — standalone approval with Annex 8 tests

R.79 §5.6.4.1.1 explicitly states:
> A power-driven vehicle equipped with an ACSF of Category C shall also be equipped with an ACSF of Category B1.

R.171 §5.1 requires that the DCAS "incorporates the [ACSF] functions" and that those functions "comply with the technical requirements and transitional provisions of UN R.79."

This creates a two-level approval structure:
```
R.79 ACSF approval (Cat B1 + Cat C)   ←— prerequisite
         ↓
R.171 DCAS system approval
```

---

## CN L2GB Status

The CN L2GB regulatory framework treats the combined driving assistance system as a single unit. There is no separate "steering function" type approval analogous to R.79. The GB 44495 standard covers the entire L2GB system in one approval process.

This means G1.3's lateral control functions (lane centering + lane change) may never have been evaluated against R.79-specific test procedures (Annex 8), even if they comply with the equivalent CN functional requirements.

---

## R.79 Annex 8 Test Requirements (Cat C)

Annex 8 specifies dedicated test procedures for ACSF Cat C, including:
- Lane change performance tests (lateral acceleration measurement)
- Safety assessment tests (approaching vehicle scenarios)
- **Rear detection test with motorcycle** (per §5.6.4.8.1.1 — see R79-6)
- Direction indicator timing tests
- HOD functionality tests during lane change procedure
- Suppression condition verification tests

These tests are separate from R.171 system-level tests and must be passed to obtain R.79 Cat C type approval.

---

## Required Closure Actions

1. Initiate a dedicated R.79 ACSF type approval project for G1.3 EU:
   - Cat B1 (lane centering, low speed)
   - Cat B2 (lane centering, highway speed) if applicable
   - Cat C (driver-confirmed lane change)
2. Select an EU Technical Service authorized for R.79 ACSF testing (same TS as R.171 DCAS is recommended for efficiency)
3. Prepare an R.79 technical documentation package: aysmax declarations, HOD strategy, suppression conditions, Srear declaration
4. Execute Annex 8 tests, including motorcycle rear detection test (R79-6)
5. Obtain R.79 ACSF type approval certificate before submitting R.171 DCAS type approval application
6. Include R.79 ACSF approval certificate in the R.171 DCAS type approval dossier

---

## Timeline Note

R.79 ACSF type approval typically requires 3–6 months of test preparation and execution. This should be planned as a critical-path item in the G1.3 EU type approval programme — it must complete before R.171 DCAS approval can be granted.
