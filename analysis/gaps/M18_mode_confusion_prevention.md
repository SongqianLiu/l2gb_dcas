# M18 — Mode Confusion Prevention

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Traceability / Validation Gap) |
| **EU Reference** | UN R.171 S2 §5.5.2.4 |
| **CN Reference** | GB draft §4.1.12 |
| **Gap Type** | Traceability / documentation gap |

> CN GB contains an equivalent requirement. Gap is ADRS documentation and validation evidence.

---

## EU Requirement (R.171 §5.5.2.4)

> The system shall be designed to minimize the risk of mode confusion — i.e., the driver inadvertently believing the system is active when it is not, or vice versa.

This is a general design principle supported by the specific sub-requirement §5.5.2.4.1 (distinguishable controls) and the HMI status display requirements. The system must make its operational state unambiguous at all times.

---

## China L2GB Status

GB draft §4.1.12 states:

> 系统状态的变化应通过声音和/或视觉信号传达给驾驶员，以最大限度减少驾驶员对系统状态的误解。

Translation: Changes in system state shall be communicated to the driver through auditory and/or visual signals to minimize the driver's misunderstanding of the system state.

**CN and EU are aligned** — both require that the system communicate state changes clearly to prevent mode confusion. CN achieves this through mandatory auditory/visual signals on every state transition.

---

## Required Closure Actions

1. Confirm the G1.3 ADRS references GB §4.1.12 and explicitly states that all DCAS state transitions (active, standby, off, fault) are signaled by auditory and/or visual means
2. Enumerate all DCAS state transitions and verify each has a corresponding HMI signal
3. Validate that the current DCAS state is continuously indicated on the instrument cluster (not only on transitions)
4. Add a validation test: for each state transition, verify the appropriate signal is issued within the required timing
