# M25 — 7-Second Maximum from Lane Change Initiation to Execution Start

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing in CN) |
| **EU Reference** | UN R.171 S2 §6.2.9.5 |
| **CN Reference** | Not found in GB draft |
| **Gap Type** | Missing in CN |

---

## EU Requirement (R.171 §6.2.9.5)

> From the moment the system determines a lane change can be safely initiated, the lane change shall begin within 7 s, or the system shall cancel the maneuver and notify the driver.

The 7-second limit prevents the system from holding an "approved lane change pending" state indefinitely — if conditions remain safe for 7 s but no maneuver has started, the system must either start or cancel.

---

## China L2GB Status

GB draft §4.6.2.2.1 and §4.6.2.2.2 address lane change preconditions, safety assessment, and driver-confirmation procedures but do not specify any maximum duration between lane change approval and execution start.

CN allows the system to wait for safe conditions without a hard time limit before canceling the maneuver.

**This specific timing constraint is not found in the CN GB draft.**

---

## Risk Assessment

Without this constraint, a G1.3 on the EU market could approve a lane change, then wait an indeterminate time before executing, during which traffic conditions change. The 7-second limit ensures the safety assessment remains valid when the maneuver starts — a stale approval after a long wait creates risk.

---

## Required Closure Actions

1. Determine G1.3 current behavior: what is the maximum time between lane change approval and execution start?
2. If no time limit exists: add a 7-second cancellation timer for the EU variant
3. Add notification when the lane change is canceled due to timeout (links to M24)
4. Add ADRS requirement for EU variant: "If a lane change maneuver does not begin within 7 s of approval, the system shall cancel the maneuver and notify the driver"
5. Validate: create conditions where a lane change is approved but blocked from starting for >7 s → verify automatic cancellation and notification

---

## Open Questions

1. Does G1.3 already have a lane change approval timeout? If yes, what is the current value?
2. Does the timer reset if the driver re-requests the same lane change after cancellation?
