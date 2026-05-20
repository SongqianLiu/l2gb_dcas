# M9 — Multiple Short Gaze Aversion Strategy

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Traceability / Validation Gap) |
| **EU Reference** | UN R.171 S2 §5.5.4.2.5.3 |
| **CN Reference** | GB draft §4.8.3.2.2.5 |
| **Gap Type** | Traceability / documentation gap |

> CN GB contains an equivalent strategy. Gap is ADRS documentation and validation evidence.

---

## EU Requirement (R.171 §5.5.4.2.5.3)

> The system shall address multiple subsequent short aversions — for example, by requiring increased re-engagement time or by immediately issuing an EOR upon detecting a subsequent aversion.

This prevents a driver from "gaming" the system by alternating brief glances at the road with repeated short gaze aversions, thereby avoiding EOR timeout.

---

## China L2GB Status

GB draft §4.8.3.2.2.5 states:

> 系统的设计应在发出EOR或升级的EOR后，若系统按照4.8.3.2.2.4的要求检测到驾驶员不再视线脱离，但在随后的3 s内驾驶员再次视线脱离持续至少2 s，立即发出EOR。

Translation: After issuing an EOR or escalated EOR, if the system detects re-engagement per §4.8.3.2.2.4 but the driver again deviates visually for at least 2 s within the following 3 s, the system shall immediately issue an EOR.

**CN and EU are aligned** — CN implements the strategy by specifying immediate EOR re-issuance if the driver re-deviates within 3 s of confirmed re-engagement.

---

## Required Closure Actions

1. Confirm the G1.3 ADRS EOR section explicitly documents this short-gaze re-issue logic (re-engage → re-deviate within 3 s for ≥ 2 s → immediate EOR)
2. Confirm the DMS/ADRS software implements this state machine transition
3. Add a validation test: trigger EOR → driver briefly re-engages (≥ 200 ms) → immediately re-deviates → verify immediate EOR re-issuance without restart of the 5 s countdown
