# M11 — Brake Override Auto-Resume Exception (≤ 30 km/h / 2 s)

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Traceability / Validation Gap) |
| **EU Reference** | UN R.171 S2 §5.5.3.4.1.1.1 |
| **CN Reference** | GB draft §4.8.2.4 |
| **Gap Type** | Traceability / documentation gap |

> CN GB contains an identical provision with the same threshold values. Gap is ADRS documentation and validation evidence.

---

## EU Requirement (R.171 §5.5.3.4.1.1.1)

> Exception to the no-auto-resume rule: if the driver brake input reduces speed by ≤ 30 km/h within 2 s, the system is permitted to automatically resume longitudinal control without a separate driver action.

The intent: light braking (e.g., to close a gap to a preceding vehicle) does not require the driver to explicitly re-activate ACC after releasing the brake.

---

## China L2GB Status

GB draft §4.8.2.4 states:

> 若驾驶员对车辆的纵向运动控制干预导致在2 s内车速的减少量不超过30 km/h，则准许系统在驾驶员未执行其他单独操作的情况下，恢复对车辆的纵向运动控制。

Translation: If the driver's longitudinal control intervention causes a speed reduction not exceeding 30 km/h within 2 s, the system is permitted to resume longitudinal control without a separate driver action.

**CN and EU are identical** — same threshold (30 km/h speed reduction within 2 s).

The counterpart clause §4.8.2.3 specifies the default: if braking reduces speed by more than this threshold, the system shall NOT auto-resume without a separate driver action.

---

## Required Closure Actions

1. Confirm the G1.3 ADRS explicitly references GB §4.8.2.4 with the 30 km/h / 2 s threshold
2. Confirm DCAS software distinguishes light braking (≤ 30 km/h in ≤ 2 s → auto-resume permitted) from heavy braking (> 30 km/h or > 2 s → driver action required)
3. Validate both paths: light braking → auto-resume; heavy braking → no auto-resume until driver re-commands
