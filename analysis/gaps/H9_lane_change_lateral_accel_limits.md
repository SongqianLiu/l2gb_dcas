# H9 — Lateral Acceleration Limits During Lane Change

| Field | Detail |
|---|---|
| **Risk Level** | ~~High~~ → **Medium (Partial alignment; curved-road gap remains)** |
| **EU Reference** | UN R.171 S2 §6.2.3, §6.2.4.3 |
| **CN Reference** | GB draft §4.6.2.2.1.8, §4.6.2.2.1.9, §4.6.2.2.1.11 |
| **Gap Type** | Partial — aligned for straight-road lane changes; gap remains for curved-road lane changes |

> **Reclassified**: Originally "Missing in CN / High Risk." CN GB draft contains quantitative limits. Straight-road values are identical to EU. A residual gap exists for curved-road lane changes where EU's "beyond-curvature" constraint is stricter.

---

## EU Requirements (R.171 §6.2.3 + §6.2.4.3)

| Parameter | EU Value |
|---|---|
| Lateral acceleration beyond curvature | ≤ 1.5 m/s² |
| Total lateral acceleration | ≤ 3.5 m/s² |
| Lateral jerk (0.5s moving avg) | ≤ 5 m/s³ |
| Deceleration during lane change | ≤ 2 m/s² (except imminent collision avoidance) |

The phrase "beyond curvature" means the component of lateral acceleration attributable to the lane change manoeuvre itself, excluding the centripetal acceleration already present due to road curvature. On straight roads, road curvature = 0, so "beyond curvature" = total lateral acceleration.

---

## China L2GB Status

### GB §4.6.2.2.1.8 (total limit, all roads)

> 对于M1类以及N1类汽车，换道执行阶段车辆的最大横向加速度应不大于3.5 m/s²，且横向加速度变化率在任意0.5 s内的平均值应不大于5 m/s³。

M1/N1 vehicles: maximum lateral acceleration ≤ 3.5 m/s² during lane change execution; lateral jerk ≤ 5 m/s³.

### GB §4.6.2.2.1.9 (straight-road specific)

> 在直道上的换道执行阶段，车辆横向加速度应不大于1.5 m/s²，且横向加速度变化率在任意0.5 s内的平均值应不大于5 m/s³。

On straight roads: lane change lateral accel ≤ 1.5 m/s²; jerk ≤ 5 m/s³.

### GB §4.6.2.2.1.11 (deceleration limit)

> 除为避免或减缓急迫的碰撞风险外，车辆的减速度应不大于2 m/s²。

Deceleration during lane change ≤ 2 m/s² (except imminent collision avoidance).

---

## Alignment and Gap

| Parameter | EU R.171 | CN GB | Status |
|---|---|---|---|
| Total lateral accel limit | ≤ 3.5 m/s² | ≤ 3.5 m/s² (§4.6.2.2.1.8) | ✅ Aligned |
| Lateral jerk (0.5s avg) | ≤ 5 m/s³ | ≤ 5 m/s³ (§4.6.2.2.1.8) | ✅ Aligned |
| Deceleration during LC | ≤ 2 m/s² | ≤ 2 m/s² (§4.6.2.2.1.11) | ✅ Aligned |
| Straight-road lane change | ≤ 1.5 m/s² beyond curvature (= total on straight) | ≤ 1.5 m/s² on straight roads (§4.6.2.2.1.9) | ✅ Aligned |
| **Curved-road lane change** | ≤ 1.5 m/s² **beyond curvature** (applies on ALL roads) | Only ≤ 3.5 m/s² total (§4.6.2.2.1.8); no "beyond curvature" sub-limit on curves | ⚠️ **Gap** |

### The Curved-Road Gap

On a curved road (e.g., a motorway bend with lateral accel 1.2 m/s² from curvature):
- **EU**: The lane change may add at most 1.5 m/s² beyond curvature → total ≤ 2.7 m/s²
- **CN**: Only the total 3.5 m/s² cap applies → lane change could add up to 2.3 m/s² beyond curvature → total ≤ 3.5 m/s²

The EU constraint is stricter on curved roads: it limits the delta lateral acceleration from the lane change itself, not just the total.

---

## Practical Impact

Curved-road lane changes are relatively uncommon on high-speed motorways (most are on straight sections), but they do occur in:
- Motorway curves with moderate radius
- Highway on-ramps/off-ramps
- Long sweeping bends

For EU type approval, the G1.3 lane change controller must be verified to limit the delta-lateral-acceleration (lane change contribution) to ≤ 1.5 m/s² on curved roads as well. This may require:
- A curvature-compensated control strategy that estimates road curvature and limits lane change lateral acceleration accordingly
- Or a conservative calibration that limits total lateral accel to ≤ curvature_component + 1.5 m/s²

---

## RMF Lane Change Dynamics

GB §4.6.3.2.10 separately specifies for RMF lane changes:
> 除由于弯道曲率产生的横向加速度外，RMF的目标应是避免由于换道控制额外产生大于1 m/s² 的车辆横向加速度。

RMF lane change: additional lateral accel beyond curvature ≤ 1 m/s². This is actually stricter than both the regular lane change limit (1.5 m/s²) and the EU §5.3.7.3.2 RMF requirement. This shows CN uses the "beyond curvature" concept for RMF lane changes.

---

## Required Closure Actions

1. Confirm the G1.3 lane change controller has a curvature-aware lateral acceleration control strategy
2. Verify that on curved roads, the control strategy limits the lane-change-induced lateral accel to ≤ 1.5 m/s² beyond curvature (EU requirement)
3. Add a curved-road lane change test to the EU validation matrix: curved road lane change → measure lateral accel components → verify lane-change component ≤ 1.5 m/s²
4. For the RMF lane change: verify the ≤ 1 m/s² beyond-curvature constraint (already in GB §4.6.3.2.10) is implemented and validated

---

## Open Questions

1. Does the current G1.3 lane change controller compute road curvature independently and use it as a feedforward signal for lateral acceleration budget?
2. What is the typical curvature-induced lateral accel on the targeted highway curves in validation tests?
3. Is the RMF lane change currently validated against the ≤ 1 m/s² beyond-curvature constraint?
4. Are there test track data showing lane change lateral accel decomposition (curvature component vs. manoeuvre component) for curved-road scenarios?
