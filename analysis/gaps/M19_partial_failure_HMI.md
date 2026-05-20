# M19 — Partial-Failure Feature-Level HMI Indication

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Traceability / Validation Gap) |
| **EU Reference** | UN R.171 S2 §5.4.4.1 |
| **CN Reference** | GB draft §4.7.4 |
| **Gap Type** | Traceability / documentation gap |

> CN GB contains an equivalent requirement. Gap is ADRS documentation and validation evidence.

---

## EU Requirement (R.171 §5.4.4.1)

> In the event of a partial failure (where some but not all DCAS functions are affected), the system shall indicate to the driver which specific functions are unavailable.

The intent: when only the lane-centering sub-function fails but ACC remains operational, the driver must be told exactly which feature has failed — not just that "an error has occurred."

---

## China L2GB Status

GB draft §4.7.4 states:

> 若系统出现功能降级，系统应通过视觉信号和声音信号通知驾驶员，并向驾驶员提示降级的功能。

Translation: If the system experiences functional degradation, the system shall notify the driver via visual and auditory signals, and indicate to the driver the degraded function(s).

**CN and EU are aligned** — both require that the driver is notified of partial failures with function-level specificity. CN additionally requires both visual AND auditory signals for degradation events.

---

## Required Closure Actions

1. Confirm the G1.3 ADRS references GB §4.7.4 and specifies the exact set of DCAS sub-functions that can degrade independently
2. Confirm the HMI displays function-level degradation status — not just a generic fault indicator
3. List all partial-failure scenarios and their corresponding HMI messages (e.g., "Lane keeping unavailable", "Adaptive cruise control unavailable")
4. Validate: simulate each partial-failure condition → verify the correct function-specific message is displayed and auditory alert is issued
