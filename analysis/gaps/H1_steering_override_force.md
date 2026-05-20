# H1 — Steering Override Force Limit (≤ 50 N)

| Field | Detail |
|---|---|
| **Risk Level** | High |
| **EU Reference** | UN R.171 S2 §5.5.3.4.1.4 |
| **CN ADRS Reference** | 可控性需求 ADRS |
| **Gap Type** | Missing in CN |

---

## EU Requirement (R.171 §5.5.3.4.1.4)

> A steering input by the driver shall override any feature associated with the lateral control assistance performed by the system. **The steering control effort necessary to override shall not exceed 50 N.** The system may allow for the driver to perform minor lateral corrections (e.g. to avoid a pothole).

---

## China L2GB Status

**可控性需求 ADRS** covers controllability through system-output constraints:

- Lateral acceleration ≤ 3 m/s² (manufacturer-declared max)
- Lateral jerk (0.5 s moving avg) ≤ 5 m/s³
- Longitudinal deceleration ≤ −8 m/s²
- System exit controllability for failures, ODD boundary, manoeuvre cancellation

**No requirement exists** for the force a driver must exert to override lateral control assistance. The GB draft (送审稿) records steering torque as a data field but specifies no limit value. The controllability test method (§9.4.2) explicitly instructs test personnel **not to intervene** in lateral control during tests — the driver override direction is untested.

---

## Root Cause of the Gap

China and EU approach controllability from opposite directions:

| Perspective | China 可控性需求 | EU R.171 §5.5.3.4.1.4 |
|---|---|---|
| **What is constrained** | System output (acceleration, jerk) | Driver input effort required to override |
| **Test method** | Passive observation — driver does not intervene | Active measurement — driver applies force to override |
| **Design focus** | System behaviour within ODD | Human-machine force interface |

These are **not equivalent**. A system can comply with all China acceleration limits and still require excessive driver effort to override, if the EPS servo strategy treats driver input as noise to be filtered out rather than a priority command.

---

## Affected Functions

| Function | Scenario | Why 50 N Matters |
|---|---|---|
| **Lane Centering** | System actively centres vehicle; driver attempts correction or emergency takeover | Primary case — system applies continuous torque; driver must be able to "push through" it |
| **Lane Change execution** | System executing lane change; driver spots hazard and steers to cancel | Driver must abort mid-manoeuvre with ≤ 50 N |
| **Curve negotiation** | System steering through a bend; driver disagrees with trajectory | Driver correction must not be blocked by EPS counter-torque |
| **RMF execution** | System executing risk mitigation; driver regains awareness and attempts takeover | Most safety-critical case — an incapacitated driver recovering must be able to override |

---

## Engineering Impact

50 N at the steering wheel rim translates to approximately:

```
Steering wheel radius ≈ 185 mm
50 N × 0.185 m ≈ 9.25 Nm at the steering column
```

This means that when DCAS is active, the net opposing torque the EPS presents to the driver's input must not exceed ~9.25 Nm. If the EPS calibration suppresses driver input (common in lane-centering systems optimised for comfort), actual override forces can significantly exceed this threshold.

**Verification requires:**

1. **EPS calibration layer** — Confirm that the DCAS torque control strategy yields ≤ 9.25 Nm net opposition at the steering wheel when the driver applies a counter-input
2. **Software override logic** — Confirm that upon detecting driver steering input, the system immediately yields priority (torque ramp-down speed and threshold)
3. **Test validation** — R.171 Annex 4 physical tests must include driver override force measurement; this must be added to the EU variant validation matrix

---

## CN ADRS Change Required

The **可控性需求 ADRS** needs a new requirement added for EU variant:

> When DCAS lateral control assistance is active, the steering input force required by the driver to override the lateral assistance shall not exceed **50 N** at any point during system operation, including during lane centering, lane change execution, and curve negotiation.

This requirement must cascade into:
- EPS system requirement (chassis/steering domain)
- DCAS software override detection threshold
- EU validation test case

---

## Open Questions

1. What is the current EPS torque opposition during lane centering on G1.3 domestic variant? Has this been measured?
2. Is there an existing override torque threshold in the EPS calibration, and what is its value?
3. Does the current DCAS software distinguish between "driver micro-correction" and "driver override intent"? (R.171 allows minor corrections without full override — the 50 N limit applies to full override, not micro-corrections.)
