# M23 — Quantitative Target Lane Safety Criterion for Lane Changes

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Partial — CN and EU use different quantitative frameworks) |
| **EU Reference** | UN R.171 S2 §6.2.4 |
| **CN Reference** | GB draft §4.6.2.2.1.4, §4.6.2.2.1.5 |
| **Gap Type** | Partial — functionally equivalent intent, different quantitative metrics |

---

## EU Requirement (R.171 §6.2.4)

> Before initiating a lane change, the system shall verify that the target lane is safe. The minimum safety criterion is:
> - Rear distance to the rearmost object in the target lane ≥ the stopping distance of the target lane object approaching at the current host vehicle speed
> - Forward distance to the foremost object in the target lane ≥ sufficient to complete the maneuver

EU expresses the safety criterion in terms of stopping distance relationships between the host vehicle and surrounding vehicles in the target lane.

---

## China L2GB Status

GB draft §4.6.2.2.1.4 states:

> 在换道前，系统应对目标车道进行安全评估，仅当目标车道满足安全条件时方可执行换道。安全条件应至少包括：目标车道后方来车与本车后侧的相对距离和相对速度满足相应安全裕量要求。

Translation: Before a lane change, the system shall conduct a safety assessment of the target lane, and shall only execute the lane change when the target lane meets the safety conditions. Safety conditions shall at minimum include: the relative distance and relative velocity between the approaching vehicle from behind in the target lane and the rear of the host vehicle satisfy the corresponding safety margin requirements.

GB draft §4.6.2.2.1.5 additionally requires:

> 目标车道前方的相对距离和相对速度同样应满足安全裕量要求。

**CN and EU are aligned in principle** — both require a minimum safe distance/speed assessment in both the forward and rearward directions in the target lane before executing a lane change.

The difference is in how the safety criterion is expressed:
- **EU**: expressed in terms of stopping distance calculations (physics-based minimum)
- **CN**: expressed as "safety margin requirements" (安全裕量要求) without specifying the exact formula

CN delegates the specific quantitative safety margin to the manufacturer's design, while EU provides a minimum stopping-distance formula.

---

## Required Closure Actions

1. Document G1.3's actual target lane safety margin algorithm: what is the minimum accepted gap (in time-to-collision or distance) for the rearward and forward target lane scenarios?
2. For EU type approval: demonstrate that the safety margin meets or exceeds the EU stopping-distance criterion in §6.2.4
3. Provide test data: lane change scenarios with rearward approaching vehicle at various closing speeds → show minimum accepted gap ≥ EU stopping distance
4. Add ADRS requirement: for EU variant, explicitly state the safety margin formula and confirm it satisfies §6.2.4

---

## Open Questions

1. Does G1.3 use a TTC (time-to-collision) threshold or a physical distance threshold for lane change safety?
2. What is the current minimum TTC/distance accepted by the system for rearward target lane vehicles?
