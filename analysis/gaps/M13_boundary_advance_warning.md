# M13 — Proactive Advance Warning When Approaching System Boundary

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Traceability / Validation Gap) |
| **EU Reference** | UN R.171 S2 §5.3.5.5 |
| **CN Reference** | GB draft §4.3.4(a) |
| **Gap Type** | Traceability / documentation gap |

> CN GB contains an equivalent requirement. Gap is ADRS documentation and validation test evidence.

---

## EU Requirement (R.171 §5.3.5.5)

> When approaching a system boundary in active mode, the system shall inform the driver with sufficient lead time to respond before the boundary is reached.

The key: the warning must be proactive — issued *before* the ODD boundary is actually exceeded, giving the driver time to react.

---

## China L2GB Status

GB draft §4.3.4 requires:

> 系统的目标应是在激活状态下持续探测其所适用的ODD边界，且应符合以下要求：
> a) 当探测到正在接近系统或功能ODD边界时，在即将超出系统或功能ODD边界时发出提示信号；

Translation: The system's goal shall be to continuously detect its applicable ODD boundaries in the active state, and when the system detects it is approaching a system or function ODD boundary, it shall issue a prompt signal when the boundary is about to be exceeded.

Also, §4.3.2(b) requires the manufacturer to document:

> 在系统探测到已超出、即将超出或正在接近系统或功能ODD边界时提示驾驶员的策略说明。

**CN and EU are aligned** — both require advance notification when approaching ODD boundary. CN also requires the notification strategy to be documented.

---

## Key Nuance

EU §5.3.5.5 specifies "sufficient lead time to respond" — CN §4.3.4(a) says "即将超出" (about to exceed). The CN phrasing does not specify a minimum lead time. EU type approval may require evidence that the lead time is sufficient (e.g., tested at system maximum speed with the boundary notification lead time measured).

---

## Required Closure Actions

1. Confirm the G1.3 ADRS explicitly references GB §4.3.4(a) and specifies the advance warning strategy for approaching ODD boundaries
2. Document the "approaching boundary" detection logic: at what distance/time before the boundary is the warning triggered?
3. For EU type approval, demonstrate that the advance warning lead time is sufficient for the driver to respond — test at maximum DCAS speed and measure warning-to-boundary time
4. Confirm all ODD boundary types are covered (speed, road type, lane marking, weather, etc.)
