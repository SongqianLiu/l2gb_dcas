# H2 — DMS Unavailability → No Lane Departure Constraint

| Field | Detail |
|---|---|
| **Risk Level** | ~~High~~ → **Medium (Traceability / Validation Gap)** |
| **EU Reference** | UN R.171 S2 §5.5.4.2.1.2 |
| **CN Reference** | GB draft §4.8.3.1.1.3 |
| **Gap Type** | Traceability / implementation / validation gap |

> **Reclassified**: Originally assessed as "Missing in CN / High Risk." GB §4.8.3.1.1.3 contains a substantively equivalent requirement. The remaining risk is whether this is cascaded into the G1.3 ADRS and validated.

---

## EU Requirement (R.171 §5.5.4.2.1.2)

> If the visual disengagement detection is temporarily unavailable, the system shall not lead the vehicle to leave the current lane.

---

## China L2GB Status

GB draft §4.8.3.1.1.3 states:

> 若系统确认视线脱离检测处于不可用状态，则系统应不通过非车道巡航控制功能使车辆离开本车道。

Translation: If the system confirms that visual disengagement detection is in an unavailable state, the system shall not cause the vehicle to leave the current lane through non-lane-cruise-control functions.

Additionally, GB §6.x (lane change preconditions, item f) states:

> 若系统确认视线脱离检测处于不可用状态，不触发换道过程。

Translation: If the system confirms that visual disengagement detection is unavailable, do not trigger the lane change procedure.

**CN and EU are substantively aligned** at the regulatory level.

---

## Root Cause of Remaining Risk

The regulation is aligned, but the engineering evidence chain may still be incomplete:

| Layer | Current Evidence | Remaining Question |
|---|---|---|
| **Regulation** | CN GB draft §4.8.3.1.1.3 and EU R.171 §5.5.4.2.1.2 both require no lane departure when DMS unavailable | Aligned |
| **ADRS** | 可控性需求 ADRS summary does not explicitly mention this constraint | Does the detailed ADRS explicitly include this condition? |
| **Software** | No software requirement evidence reviewed | Does the DMS unavailability flag propagate to lateral control mode constraints? |
| **Validation** | GB §9.4.9.6.4 includes a sensor occlusion test with 10s timeout | Is the "lane departure constrained" behavior tested and documented for EU submission? |

---

## Affected Functions

| Function | How DMS Unavailability Affects It |
|---|---|
| **Lane Centering** | System must not initiate or continue lateral movements that could cause lane departure |
| **Lane Change execution** | System must not trigger lane change initiation if DMS is unavailable |
| **RMF execution** | This is a more complex case: RMF must still execute (safety function), but DMS failure + RMF interaction needs to be addressed in the safety concept |

---

## Required Closure Actions

1. Confirm that the G1.3 ADRS explicitly includes GB §4.8.3.1.1.3 as a system requirement
2. Confirm that the DMS-unavailability flag triggers a lateral constraint mode in the DCAS software
3. Confirm that GB §9.4.9.6.4 occlusion test is also performed for EU type approval (sensor occlusion → no lane departure)
4. Clarify RMF behavior when DMS is unavailable — does RMF override the no-lane-departure constraint?

---

## Open Questions

1. Does the G1.3 ADRS explicitly map GB §4.8.3.1.1.3 to a software-level constraint?
2. When the DMS camera is occluded or fails, does the system enter a "lane-constrained" mode vs. simply degrading to a warning?
3. GB test §9.4.9.6.4 measures response to occlusion — does it verify the no-lane-departure behavior, or only the EOR signal timing?
4. Is there an exception for RMF (since stopping in-lane requires continued lateral control)? If so, is the RMF exception explicitly documented in the safety concept?
