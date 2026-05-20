# H4 — Lateral Control Must Not Terminate While Driver is Motorically Disengaged During Override

| Field | Detail |
|---|---|
| **Risk Level** | **High** (confirmed true regulatory gap) |
| **EU Reference** | UN R.171 S2 §5.5.3.4.1.5 |
| **CN Reference** | Not found in GB draft |
| **Gap Type** | Missing in CN |

> **Confirmed High**: No equivalent requirement found in the CN GB draft. This remains a true regulatory gap.

---

## EU Requirement (R.171 §5.5.3.4.1.5)

> The system shall not terminate lateral control while the driver is detected to be motorically disengaged.

The context: §5.5.3.4.1 permits the system to remain in active mode while the driver overrides it. §5.5.3.4.1.5 adds a specific safety constraint: if, at the moment of lateral override detection, the driver is still motorically disengaged (hands off the steering wheel), the system must NOT drop lateral control.

---

## Why This Matters

The scenario this protects against:

1. Driver's hands are off the steering wheel (system has been issued HOR)
2. Driver makes a small steering input — system detects this as an "override event"
3. System, interpreting the override, terminates lateral control
4. Driver is left without lateral assistance while hands are only partially on the wheel

This creates a dangerous situation: the driver has not yet fully taken over, but the system has already handed back full lateral authority. If the driver cannot immediately regain steering control (e.g., in a fast lane change or curve), the vehicle could deviate.

The EU requirement means: during an override, lateral control continues until the driver is positively detected as motorically engaged again.

---

## China L2GB Status

### What CN GB Does Address

GB §4.8.2.1 permits the system to remain active during driver override:
> 在驾驶员执行运动控制干预期间，系统可保持激活状态。

GB §4.8.2.8 terminates non-lane-cruise-control on override (with exceptions for supportive inputs and minor corrections):
> 若驾驶员对车辆横向运动控制的干预发生在执行非车道巡航控制过程中，除驾驶员对转向控制的输入用来支持系统规划的控制或执行小幅转向控制纠正外，该非车道巡航控制应被终止。

GB lane change §6.x(g) similarly terminates lane change on override (with the same exceptions).

### What CN GB Does NOT Address

Neither §4.8.2.1, §4.8.2.8, nor any other GB clause found contains an equivalent to R.171 §5.5.3.4.1.5: **the explicit prohibition on terminating lateral control while the driver's hands remain off the wheel**.

The GB provisions deal with WHAT HAPPENS when the override is detected — they do not constrain WHEN lateral control may be terminated based on the driver's motoric engagement state.

---

## Affected Functions

| Function | Scenario |
|---|---|
| **Lane Centering** | Driver's hands are off → HOR issued → driver makes small steering nudge → system must not drop lane centering while hands still off |
| **Lane Change execution** | Mid-lane-change, hands-off detected → driver makes a correction input → system must maintain lateral authority until hands are confirmed back on wheel |
| **RMF execution** | Most critical: driver recovering from incapacitation, reaching for wheel → small touch detected as override → system must not drop lateral control before hands are properly on wheel |

---

## Engineering Impact

This requirement constrains the software logic for override detection:

```
Current likely logic:
  detect steering torque > threshold → terminate lateral control (or enter override mode)

Required logic per R.171:
  detect steering torque > threshold AND driver motorically engaged (HOD detected)
  → enter override mode
  
  if steering torque > threshold BUT driver NOT motorically engaged:
  → do NOT terminate lateral control
  → continue lateral control with driver priority (§5.5.3.4.1 allows system to stay active)
```

The EPS must also be designed to yield priority to driver input during this mode WITHOUT dropping lateral control assistance.

---

## Required Closure Actions

1. **ADRS**: Add an explicit requirement: "Lateral control shall not be terminated in response to a driver override input while the driver is detected as motorically disengaged."
2. **Software**: Modify override detection logic — termination of lateral control should require positive confirmation of motoric engagement, not just presence of steering torque.
3. **EPS interface**: Confirm that the system can maintain lateral assistance while also yielding to driver torque input (dual-path control: system assists + driver can push through).
4. **Validation**: Add a specific test case — hands-off driving, DMS issues HOR, driver makes small steering input → verify lateral control is maintained.

---

## Open Questions

1. Does the current G1.3 DCAS software terminate lane centering immediately upon detecting steering torque above a threshold, regardless of HOD state?
2. Does the EPS architecture support a "follow + yield" mode where the system maintains lateral trajectory while also allowing driver to push through?
3. How does the current system handle the transition from HOR-issued (hands-off) + driver touch → does it ramp down torque or cut immediately?
4. Is the "small correction" exception in GB §4.8.2.8 related to this gap? (R.171 §5.5.3.4.1 similarly allows minor corrections — but §5.5.3.4.1.5 still prohibits terminating lateral control while motorically disengaged.)
