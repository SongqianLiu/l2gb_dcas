# M10 — Dashboard Excluded from Driving-Task-Relevant Area

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Traceability / Documentation Gap) |
| **EU Reference** | UN R.171 S2 §5.5.4.2.5.2 |
| **CN Reference** | GB draft §4.8.3.1.3.2 |
| **Gap Type** | Traceability / documentation gap |

> CN GB contains an equivalent geometric exclusion zone that covers the dashboard area. Gap is documentation for EU type approval submission.

---

## EU Requirement (R.171 §5.5.4.2.5.2)

> The dashboard/instrument panel is explicitly stated as NOT a driving-task-relevant area. A driver looking at the dashboard is considered visually disengaged.

This prevents a system from accepting dashboard glances as valid "road-directed" gaze, since instrument panel monitoring requires sustained attention away from the forward driving scene.

---

## China L2GB Status

GB draft §4.8.3.1.3.2 defines the exclusion zone geometrically:

> 在车辆内部由驾驶员基准眼点相对于车辆纵向基准面分别向左55°和向右55°所构成的两个垂直平面以及驾驶员基准眼点向下30°的平面以下围成的区域应不被视为驾驶任务相关区域。

Translation: The region bounded by ±55° laterally and below 30° downward from the driver's ocular reference point shall not be considered a driving-task-relevant area.

The instrument panel is located in the downward visual field (typically ≥ 15–25° below horizontal) from the driver's eye point, which falls within the CN-defined exclusion zone. **CN and EU are aligned in substance**, though CN uses a geometric definition rather than explicitly naming the dashboard.

---

## Key Documentation Requirement

EU explicitly names "dashboard/instrument panel" as non-driving-relevant. CN uses an angular zone. For EU type approval, the submission must demonstrate that the G1.3 vehicle geometry places the instrument panel within the CN-defined exclusion zone (below 30° from driver eye reference point).

---

## Required Closure Actions

1. Perform a vehicle geometry measurement: confirm instrument panel angular position relative to driver eye reference point is below 30° downward
2. Document this in the EU type approval submission: vehicle geometry diagram + DMS exclusion zone overlay
3. Confirm the DMS correctly triggers EOR when the driver looks at the instrument cluster
4. Add a validation test: driver looks at instrument panel → verify EOR is triggered within the standard timeout
