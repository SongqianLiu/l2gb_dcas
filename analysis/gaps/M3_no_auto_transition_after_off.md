# M3 — No Auto-Transition to Combined Control After Driver Turns Off System

| Field | Detail |
|---|---|
| **Risk Level** | ~~High~~ → **Medium (Traceability / Validation Gap)** |
| **EU Reference** | UN R.171 S2 §5.5.2.2 |
| **CN Reference** | GB draft §4.8.1.1.4 |
| **Gap Type** | Traceability / implementation / validation gap |

> **Reclassified**: Originally assessed as "Missing in CN / High Risk." GB §4.8.1.1.4 contains a substantively equivalent requirement. Remaining risk is ADRS traceability and validation.

---

## EU Requirement (R.171 §5.5.2.2)

> When the system is switched to the off mode, there shall be no automatic transition to any system providing continuous longitudinal and lateral movement control.

The intent is to prevent silent handoff: if the driver explicitly disables DCAS, the system must not automatically re-engage or hand over to another combined-control mode.

---

## China L2GB Status

GB draft §4.8.1.1.4 states:

> 驾驶员执行车辆制造商规定的操作方式使系统进入关闭状态后应不自动激活任何部分驾驶辅助系统。

Translation: After the driver uses the manufacturer-specified operation to put the system into the off state, the system shall not automatically activate any partial driving assistance system.

**CN and EU are substantively aligned** at the regulatory level.

Note: §4.8.1.1.3 also states:

> 车辆每次上电/点火后（发动机自动启停除外），系统应不处于激活状态。

Translation: Each time the vehicle is powered on/ignited (except engine auto start-stop), the system shall not be in the active state.

This adds the EU §5.5.3.1 requirement (system off at each new run cycle) as well.

---

## Root Cause of Remaining Risk

| Layer | Current Evidence | Remaining Question |
|---|---|---|
| **Regulation** | GB §4.8.1.1.4 and EU R.171 §5.5.2.2 are substantively aligned | Aligned |
| **ADRS** | Not explicitly referenced in extracted ADRS summaries | Does the G1.3 ADRS explicitly trace this prohibition? |
| **Software** | No evidence reviewed | Is the "no auto-activation after off" state enforced in the state machine? |
| **Validation** | GB §4.8.1.1.4 has a document check (√ in verification table) | What is the EU verification test for this? |

---

## Scope Clarification

Both EU §5.5.2.2 and CN §4.8.1.1.4 focus on combined (lateral + longitudinal) control systems. The prohibition applies specifically to:
- Systems providing **continuous** combined lat+lon control
- Not to individual component functions (e.g., ACC or LKAS in isolation)

For G1.3, this means: after the driver turns off the DCAS/领航 mode, neither lane centering nor adaptive cruise (as a combined DCAS mode) should re-engage automatically.

---

## Required Closure Actions

1. Confirm the G1.3 ADRS explicitly includes GB §4.8.1.1.4 / EU §5.5.2.2 prohibition
2. Confirm the software state machine enforces: OFF state → no automatic re-activation of any combined-control function
3. For EU type approval, document the test procedure verifying this behavior (document check per GB verification table is insufficient for R.171 Annex 4)

---

## Open Questions

1. Does the G1.3 system have any mode (e.g., a "resume" button) that could inadvertently re-activate combined control without explicit driver action? If so, does the ADRS define what constitutes a "deliberate driver action" for re-activation?
2. If the driver turns off DCAS and ACC independently remains active, does this violate either GB §4.8.1.1.4 or R.171 §5.5.2.2? (Probably not — they address combined control, not individual lon/lat.)
