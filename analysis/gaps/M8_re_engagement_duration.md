# M8 — Re-engagement Minimum Duration (≥ 200 ms)

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Traceability / Validation Gap) |
| **EU Reference** | UN R.171 S2 §5.5.4.2.5.2.1 |
| **CN Reference** | GB draft §4.8.3.2.2.4 |
| **Gap Type** | Traceability / documentation gap |

> CN GB contains an equivalent requirement. Gap is ADRS documentation and validation evidence.

---

## EU Requirement (R.171 §5.5.4.2.5.2.1)

> Re-engagement shall require a continuous gaze toward the driving-task-relevant area of at least 200 ms before the system considers the driver visually re-engaged and cancels the EOR.

This prevents momentary glances from being counted as genuine re-engagement.

---

## China L2GB Status

GB draft §4.8.3.2.2.4 states:

> EOR 或升级的EOR 应持续到系统检测到驾驶员眼睛注视方向或头部姿态朝向至少200 ms 不再偏离驾驶任务相关区域。

Translation: EOR or escalated EOR shall continue until the system detects that the driver's eye gaze or head posture has been directed toward the driving-task-relevant area for at least 200 ms without deviation.

**CN and EU are aligned** — both specify 200 ms minimum re-engagement dwell time before cancelling EOR.

---

## Required Closure Actions

1. Confirm the G1.3 ADRS EOR section explicitly references the 200 ms re-engagement threshold
2. Confirm the DMS software uses ≥ 200 ms as the minimum dwell time before cancelling EOR
3. Validate in test: sensor unblocked → re-engagement detected → EOR cancels only after ≥ 200 ms of sustained gaze toward task-relevant area
