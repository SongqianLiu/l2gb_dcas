# M24 — Lane Change Suppression Notification to Driver

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing in CN) |
| **EU Reference** | UN R.171 S2 §6.2.8 |
| **CN Reference** | Not found in GB draft |
| **Gap Type** | Missing in CN |

---

## EU Requirement (R.171 §6.2.8)

> If the system suppresses or cancels a lane change that was requested by the driver (due to safety conditions not being met), the system shall notify the driver that the lane change has been suppressed and the reason (if determinable).

The intent: if a driver initiates a lane change request (e.g., by pressing the lane change button) and the system rejects it because the safety criterion is not met, the driver must be informed that the request was denied and why.

---

## China L2GB Status

GB draft §4.6.2.2.1.4 and §4.6.2.2.1.5 address safety assessment before lane changes but focus on the safety evaluation logic itself. Neither these clauses nor other sections explicitly require notification to the driver when a lane change request is suppressed.

GB draft §4.6.2.2.2 covers the driver-confirmation lane change procedure but does not include a requirement to notify the driver if the system determines the lane change cannot be safely executed.

**This specific notification requirement is not found in the CN GB draft.** Drivers using G1.3 in China currently may not receive feedback when a lane change request is silently rejected, which is acceptable under CN regulations but would fail EU §6.2.8.

---

## Required Closure Actions

1. Review G1.3 current behavior: when the driver requests a lane change and the system determines it is unsafe, does the system provide any feedback?
2. If no feedback: add a notification for the EU variant — visual indicator (e.g., flashing lane change icon) and/or auditory signal when lane change is suppressed
3. If possible, indicate the reason: "Lane blocked — vehicle in target lane" or similar
4. Add ADRS requirement for EU variant: "If a driver-requested lane change is suppressed, the system shall notify the driver of the suppression"
5. Validate: request a lane change when target lane is occupied → verify suppression notification appears

---

## Open Questions

1. Does G1.3 current HMI show any indication when lane change is blocked (e.g., the requested-direction indicator flashes differently)?
2. Is there a time limit — if the lane change remains suppressed for X seconds, does the driver need to re-request?
