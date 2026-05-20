# M28 — Partial Failure Continued Operation Strategy

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Traceability / Validation Gap) |
| **EU Reference** | UN R.171 S2 §5.4.4 |
| **CN Reference** | GB draft §4.7.4 |
| **Gap Type** | Traceability / documentation gap |

> CN GB contains an equivalent requirement. Gap is ADRS documentation and validation evidence.

---

## EU Requirement (R.171 §5.4.4)

> In the event of a partial failure, the system shall continue to provide the unaffected functions if safe to do so, and shall clearly indicate to the driver the degraded operating state.

The principle of graceful degradation: a camera failure affecting lane centering should not necessarily disable adaptive cruise control if ACC relies on radar only.

---

## China L2GB Status

GB draft §4.7.4 states:

> 若系统出现功能降级，系统应通过视觉信号和声音信号通知驾驶员，并向驾驶员提示降级的功能。在功能降级情况下，系统应继续提供其他未受影响的功能（如适用）。

Translation: If the system experiences functional degradation, it shall notify the driver via visual and auditory signals and indicate the degraded function(s). Under functional degradation, the system shall continue to provide other unaffected functions (where applicable).

**CN and EU are aligned** — both require graceful degradation with continued operation of unaffected functions plus clear driver notification. CN adds the "where applicable" qualifier, which allows the manufacturer to define which functions can continue independently.

---

## Required Closure Actions

1. Confirm the G1.3 ADRS includes a functional degradation strategy that maps each failure mode to its impact on individual DCAS sub-functions
2. Confirm the system architecture supports independent operation of ACC and lane centering (i.e., a single sensor failure does not cascade to all functions)
3. Document all partial failure scenarios and the expected continued operation behavior for each
4. Validate: simulate each sensor failure mode → verify correct subset of functions continues operating → verify correct degradation notification is displayed
