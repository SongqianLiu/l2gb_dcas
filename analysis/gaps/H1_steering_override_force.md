# H1 — Steering Override Force Limit (≤ 50 N)

| Field | Detail |
|---|---|
| **Risk Level** | ~~High~~ → **Medium (Traceability / Validation Gap)** |
| **EU Reference** | UN R.171 S2 §5.5.3.4.1.4 |
| **CN Reference** | GB draft §4.8.2.7; 可控性需求 ADRS |
| **Gap Type** | Traceability / implementation / validation gap |

> **Reclassified**: Originally assessed as "Missing in CN / High Risk." GB §4.8.2.7 contains an equivalent (and in one respect stricter) requirement. The remaining risk is whether the ≤50 N constraint is cascaded into the G1.3 ADRS, EPS calibration, software override logic, and validated with measured test results.

---

## EU Requirement (R.171 §5.5.3.4.1.4)

> A steering input by the driver shall override any feature associated with the lateral control assistance performed by the system. **The steering control effort necessary to override shall not exceed 50 N.** The system may allow for the driver to perform minor lateral corrections (e.g. to avoid a pothole).

Key distinction: the 50 N limit applies specifically to **override** (full lateral takeover). Minor corrections — where the driver makes small inputs without terminating the system — are explicitly permitted and are not subject to the 50 N threshold under EU.

---

## China L2GB Status

GB draft §4.8.2.7 states:

> 系统应使驾驶员能够通过不大于50 N 的转向操纵力干预车辆的横向运动控制。

Translation: The system shall enable the driver to intervene in the vehicle's lateral motion control through a steering force not exceeding 50 N.

### CN is Stricter Than EU on Scope

GB §4.8.2.7 applies the ≤50 N limit to **all driver interventions** (干预), which includes both full overrides and minor corrections. EU §5.5.3.4.1.4 only binds the 50 N limit to **override** — minor corrections (without system termination) have no EU force constraint.

This means:
- If the G1.3 EPS satisfies CN §4.8.2.7 (≤50 N for any intervention), it automatically satisfies EU §5.5.3.4.1.4 (≤50 N for override only)
- **CN is the binding constraint** here — meeting CN compliance is sufficient for EU compliance on this specific limit

The minor-correction vs. override distinction is separately addressed in GB §4.8.2.8:
> 若驾驶员对车辆横向运动控制的干预发生在执行非车道巡航控制过程中，除驾驶员对转向控制的输入用来支持系统规划的控制或执行小幅转向控制纠正外，该非车道巡航控制应被终止。

This means: minor corrections (小幅转向控制纠正) do not terminate the system — matching EU's concept of minor corrections in §5.5.3.4.1.4.

### ADRS Gap

The extracted **可控性需求 ADRS** summary mainly covers system-output controllability constraints:

- Lateral acceleration ≤ 3 m/s² (manufacturer-declared max)
- Lateral jerk (0.5 s moving avg) ≤ 5 m/s³
- Longitudinal deceleration ≤ −8 m/s²
- System exit controllability for failures, ODD boundary, manoeuvre cancellation

The 50 N driver input force constraint is absent from the ADRS summary. The remaining risk is whether it is present in the full ADRS detail and whether it is explicitly traced to EPS calibration and software.

GB draft §9.4.9.1 includes steering wheel intervention tests for lane cruise and lane change. The evidence still needs to confirm whether the test setup physically measures steering control effort and demonstrates ≤50 N across all relevant operating modes.

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
4. Does the current DCAS software distinguish between "minor correction" (小幅转向控制纠正, system stays active) and "full override" (system terminates lateral control)? Both must be achievable within ≤50 N under CN §4.8.2.7. Under EU §5.5.3.4.1.4, only full override is bound to ≤50 N. CN is the stricter requirement here.
5. Do validation reports measure steering effort directly, or only verify that the vehicle eventually responds to steering intervention? Physical force measurement is required for R.171 Annex 4 compliance.
6. Does GB §9.4.9.1 (steering wheel intervention test) measure the actual steering force applied by the test driver, or only the outcome (vehicle deviates from lane)? If only outcome is measured, EU type approval requires adding force measurement instrumentation.
