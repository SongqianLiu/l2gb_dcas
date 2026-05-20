# M22 — 3-Second Advance Direction Indicator Before Lane Change Execution

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Partial — CN requires advance signal but no explicit 3 s minimum) |
| **EU Reference** | UN R.171 S2 §6.2.7 |
| **CN Reference** | GB draft §4.6.2.2.1.7 |
| **Gap Type** | Partial — CN aligned in principle, quantitative timing not specified |

---

## EU Requirement (R.171 §6.2.7)

> Before initiating a lane change, the direction indicator shall be activated for at least 3 s before any lateral movement begins.

The 3-second advance signaling provides trailing vehicles sufficient warning before the host vehicle begins moving laterally. This is a quantitative timing requirement — the indicator must precede the lateral movement by at least 3 seconds.

---

## China L2GB Status

GB draft §4.6.2.2.1.7 requires the system to activate the turn indicator during lane change execution and deactivate it afterward. The clause states:

> 若系统具有系统触发的换道控制功能，在执行换道过程中系统应自动激活目标方向的转向灯，并在换道完成后关闭。

The phrase "执行换道过程中" (during execution of the lane change) implies the indicator is active during the maneuver but does not specify a minimum pre-maneuver activation duration.

GB draft §4.6.2.2.1.6 addresses the advance notification to the driver but does not specify a 3-second indicator duration specifically.

**CN is aligned in principle** (indicator must be active during lane change) but does **not** specify the 3-second minimum advance activation requirement.

---

## Risk Assessment

If G1.3 activates the direction indicator simultaneously with the start of lateral movement (0-second advance), this satisfies CN but fails EU §6.2.7.

The 3-second advance is a safety-critical timing constraint because it ensures trailing vehicles have time to react before the lane change begins.

---

## Required Closure Actions

1. Confirm G1.3 current behavior: how long before lateral movement does the system activate the direction indicator?
2. If less than 3 seconds: update the EU variant software to activate the indicator ≥ 3 s before any lateral displacement begins
3. Add ADRS requirement for EU variant: "Direction indicator shall be activated at least 3 s before any lateral movement begins for system-initiated lane changes"
4. Validate: system-triggered lane change → measure time from indicator activation to first lateral displacement → verify ≥ 3 s
