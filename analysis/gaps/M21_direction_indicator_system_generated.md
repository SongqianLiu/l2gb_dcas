# M21 — Direction Indicator Shall Be System-Generated for Lane Changes

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Traceability / Validation Gap) |
| **EU Reference** | UN R.171 S2 §6.2.6 |
| **CN Reference** | GB draft §4.6.2.2.1.7 |
| **Gap Type** | Traceability / documentation gap |

> CN GB contains an equivalent requirement. Gap is ADRS documentation and validation evidence.

---

## EU Requirement (R.171 §6.2.6)

> For system-triggered lane changes, the direction indicator shall be operated by the system (not requiring manual driver activation) for the duration of the lane change maneuver.

This ensures that system-initiated lane changes are properly signaled to surrounding traffic without requiring the driver to manually activate the turn signal.

---

## China L2GB Status

GB draft §4.6.2.2.1.7 states:

> 若系统具有系统触发的换道控制功能，在执行换道过程中系统应自动激活目标方向的转向灯，并在换道完成后关闭。

Translation: If the system has a system-triggered lane change control function, during execution of a lane change the system shall automatically activate the turn indicator in the target direction and deactivate it after the lane change is complete.

**CN and EU are aligned** — both require the system to automatically activate and deactivate the direction indicator for system-triggered lane changes.

Note: For driver-confirmed lane changes (where the driver initiates via steering wheel input or button), both standards also require the direction indicator to be active during the maneuver.

---

## Required Closure Actions

1. Confirm the G1.3 ADRS references GB §4.6.2.2.1.7 and specifies that system-triggered lane changes automatically activate/deactivate the turn indicator
2. Confirm the turn indicator is activated BEFORE the lateral movement begins (advance indicator per M22)
3. Validate: trigger a system-initiated lane change → verify direction indicator activates automatically and deactivates on completion
4. Verify the indicator stays active for the entire maneuver duration, not just momentarily
