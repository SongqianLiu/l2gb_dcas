# H1 — Steering Override Force Limit (≤ 50 N)

| Field | Detail |
|---|---|
| **Risk Level** | High |
| **EU Reference** | UN R.171 S2 §5.5.3.4.1.4 |
| **CN Reference** | GB draft §4.8.2.7; 可控性需求 ADRS |
| **Gap Type** | Traceability / implementation / validation gap |

---

## EU Requirement (R.171 §5.5.3.4.1.4)

> A steering input by the driver shall override any feature associated with the lateral control assistance performed by the system. **The steering control effort necessary to override shall not exceed 50 N.** The system may allow for the driver to perform minor lateral corrections (e.g. to avoid a pothole).

---

## China L2GB Status

The **China GB draft** already contains an aligned 50 N requirement:

> 系统应使驾驶员能够通过不大于50 N 的转向操纵力干预车辆的横向运动控制。

This is substantively aligned with UN R.171 S2 §5.5.3.4.1.4.

However, the extracted **可控性需求 ADRS** summary mainly covers controllability through system-output constraints:

- Lateral acceleration ≤ 3 m/s² (manufacturer-declared max)
- Lateral jerk (0.5 s moving avg) ≤ 5 m/s³
- Longitudinal deceleration ≤ −8 m/s²
- System exit controllability for failures, ODD boundary, manoeuvre cancellation

The current project evidence therefore does **not** show a China-vs-EU regulatory gap on the 50 N limit itself. The remaining risk is whether the 50 N requirement is fully cascaded into the G1.3 ADRS, EPS/software implementation, and validation evidence.

GB draft §9.4.9.1 includes steering wheel intervention tests for lane cruise and lane change. The evidence still needs to confirm whether the test setup measures the actual steering control effort and demonstrates ≤50 N across all relevant operating modes.

---

## Root Cause of the Remaining Risk

The regulatory requirement is aligned, but the engineering evidence chain may still be incomplete:

| Layer | Current Evidence | Remaining Question |
|---|---|---|
| **Regulation** | CN GB draft §4.8.2.7 and EU R.171 §5.5.3.4.1.4 both specify ≤50 N | Aligned |
| **ADRS** | Extracted 可控性需求 ADRS summary emphasizes acceleration, jerk, warning, exit behavior | Does the detailed ADRS explicitly include ≤50 N? |
| **Software** | No software requirement evidence reviewed yet | Does AD control yield priority to driver steering input under all lateral-control features? |
| **EPS calibration** | No calibration evidence reviewed yet | Is opposing torque limited so steering effort stays ≤50 N? |
| **Validation** | GB includes steering wheel intervention tests | Is steering effort physically measured and reported for EU type approval? |

A vehicle can be compliant on paper with the GB/R.171 clause but still fail approval if the implementation or validation evidence does not prove that the driver can override lateral assistance within the 50 N limit.

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

## Required Closure Action

The **可控性需求 ADRS** and EU variant evidence package should explicitly include:

> When DCAS lateral control assistance is active, the steering input force required by the driver to override the lateral assistance shall not exceed **50 N** at any point during system operation, including during lane centering, lane change execution, and curve negotiation.

This requirement should be traced to:
- EPS system requirement (chassis/steering domain)
- DCAS software override detection threshold
- Minor-correction vs. override-intent handling
- EU validation test case
- Measured steering effort results

---

## Open Questions

1. Does the detailed G1.3 可控性需求 ADRS explicitly include GB draft §4.8.2.7 / ≤50 N, or was it omitted from the extracted summary?
2. What is the current EPS torque opposition during lane centering on G1.3 domestic variant? Has this been measured?
3. Is there an existing override torque threshold in the EPS calibration, and what is its value?
4. Does the current DCAS software distinguish between "driver micro-correction" and "driver override intent"? (R.171 allows minor corrections without full override — the 50 N limit applies to full override, not micro-corrections.)
5. Do validation reports measure steering effort directly, or only verify that the vehicle eventually responds to steering intervention?
