# M26 — VRU Detection as Precondition for Lane Change

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Partial / Missing — CN does not explicitly list VRU as precondition) |
| **EU Reference** | UN R.171 S2 §6.2.9.4 |
| **CN Reference** | GB draft §4.6.2.2.1.4 (partial coverage) |
| **Gap Type** | Partial — CN safety assessment clause may not explicitly require VRU detection |

---

## EU Requirement (R.171 §6.2.9.4)

> The system shall not initiate a lane change if a vulnerable road user (pedestrian, cyclist, motorcyclist) is detected in or approaching the target lane.

VRU detection is an explicit precondition for lane change execution — not just other vehicles. The system must detect and account for pedestrians, cyclists, and powered two-wheelers in the target lane.

---

## China L2GB Status

GB draft §4.6.2.2.1.4 requires a safety assessment before lane changes:

> 在换道前，系统应对目标车道进行安全评估，仅当目标车道满足安全条件时方可执行换道。安全条件应至少包括：目标车道后方来车与本车后侧的相对距离和相对速度满足相应安全裕量要求。

The safety assessment requirement uses the phrase "后方来车" (vehicles approaching from behind) which typically refers to motor vehicles. The clause does not explicitly name pedestrians, cyclists, or other VRUs as objects that must be detected and accounted for.

GB draft §4.2.1 (object detection) lists the objects the system shall detect and may include VRUs, but the explicit VRU-as-lane-change-precondition linkage is not clearly established in the CN text.

**CN is partially aligned** — the general safety assessment clause could be interpreted to include VRUs, but the EU requirement is explicit. For EU type approval, explicit VRU coverage must be demonstrated.

---

## Required Closure Actions

1. Review G1.3 perception system: does the target lane safety assessment explicitly include VRU detection (pedestrians, cyclists, PTW)?
2. If VRU detection is not explicitly included: update the EU variant lane change precondition logic to block lane change when VRUs are detected in the target lane
3. Add ADRS requirement for EU variant: "The lane change safety assessment shall include detection of VRUs (pedestrians, cyclists, powered two-wheelers) in the target lane"
4. Validate: approach scenario where a cyclist is present in target lane → verify lane change is blocked
5. Confirm minimum detection range for VRUs in the lateral/rear zone sufficient for lane change safety

---

## Open Questions

1. Does G1.3 radar/camera system currently detect and classify VRUs in the side/rear sensing zone?
2. What is the G1.3 object classification taxonomy for the lane change precondition check?
