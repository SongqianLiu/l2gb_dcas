# H7 — No Auto-Resume Longitudinal Control After AEBS Stops Vehicle

| Field | Detail |
|---|---|
| **Risk Level** | ~~High~~ → **Medium (Traceability / Validation Gap)** |
| **EU Reference** | UN R.171 S2 §5.5.3.3.4 |
| **CN Reference** | GB draft §4.8.1.3.3 |
| **Gap Type** | Traceability / implementation / validation gap |

> **Reclassified**: Originally assessed as "Missing in CN / High Risk." GB §4.8.1.3.3 contains a directly equivalent requirement. Remaining risk is ADRS traceability and validation.

---

## EU Requirement (R.171 §5.5.3.3.4)

> The system shall not resume longitudinal control without driver input if the vehicle comes to a standstill following an AEBS intervention.

The intent: after emergency braking brings the vehicle to a stop, the DCAS must not automatically start moving the vehicle again. The driver must explicitly command movement.

---

## China L2GB Status

GB draft §4.8.1.3.3 states:

> 若在应急辅助功能（例如，AEBS）介入控制后导致车辆静止，在没有驾驶员人工操作的情况下，系统应不恢复纵向运动控制。

Translation: If after an emergency assistance function (e.g., AEBS) intervention causes the vehicle to come to a standstill, the system shall not resume longitudinal motion control without driver manual operation.

**CN and EU are identical** in substance.

---

## Root Cause of Remaining Risk

| Layer | Current Evidence | Remaining Question |
|---|---|---|
| **Regulation** | GB §4.8.1.3.3 and EU R.171 §5.5.3.3.4 are equivalent | Aligned |
| **ADRS** | Not explicitly referenced in extracted ADRS summaries | Is this explicitly in the G1.3 ADRS? |
| **Software** | Not reviewed | Is the post-AEBS standstill state handled in the DCAS state machine? Does it require an explicit "resume" action? |
| **Validation** | GB verification table shows §4.8.1.3.3 with a document check (√) | What is the test method for EU R.171 compliance? |

---

## Affected Scenario

**Sequence of events:**
1. DCAS active (combined lat + lon control)
2. AEBS detects imminent collision → overrides DCAS → applies emergency braking
3. Vehicle comes to a standstill
4. AEBS intervention ends
5. **Prohibited**: DCAS automatically resumes longitudinal control (vehicle starts moving again)
6. **Required**: DCAS must wait for explicit driver action (accelerator press, system re-activation, etc.)

This is critical because the standstill may be in an emergency situation (e.g., stopped due to collision avoidance), and the driver must assess the scene before the vehicle moves again.

---

## Boundary Conditions

| Case | Expected Behavior |
|---|---|
| AEBS brakes → standstill | System shall not resume lon. control without driver input |
| AEBS applies minor braking → vehicle decelerates but does not stop | §5.5.3.3.4 / §4.8.1.3.3 do not apply (standstill condition not met) |
| Driver-initiated braking → standstill | Different clause (§4.8.2.3: driver brake override); resume requires driver action anyway |

---

## Required Closure Actions

1. Confirm the G1.3 ADRS explicitly references GB §4.8.1.3.3 / EU §5.5.3.3.4 as a DCAS system requirement
2. Confirm the DCAS software state machine: AEBS-intervention-standstill → explicit driver resume required
3. Define the "driver action" that constitutes a valid resume (accelerator press? System re-activation command?)
4. Add a validation test case: AEBS activation → standstill → verify DCAS does not auto-resume → driver presses accelerator → verify DCAS can resume

---

## Open Questions

1. Does the current G1.3 DCAS automatically exit to standby mode after AEBS intervention, or does it remain in active mode waiting for an auto-resume condition?
2. What happens to DCAS lateral control during and after AEBS intervention? Is lateral control also suspended?
3. Is the "driver manual operation" requirement satisfied by any input (accelerator, brake release) or only a specific re-activation command?
