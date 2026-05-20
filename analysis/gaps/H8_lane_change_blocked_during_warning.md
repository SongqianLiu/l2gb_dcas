# H8 — Lane Change Shall Not Be Initiated When Disengagement Warning Is Active

| Field | Detail |
|---|---|
| **Risk Level** | ~~High~~ → **Medium (Traceability / Validation Gap)** |
| **EU Reference** | UN R.171 S2 §5.3.7.2.1.3 |
| **CN Reference** | GB draft §6.x (lane change preconditions, item e) |
| **Gap Type** | Traceability / implementation / validation gap |

> **Reclassified**: Originally assessed as "Missing in CN / High Risk." GB draft contains a direct equivalent in the lane change preconditions. Remaining risk is ADRS traceability and validation.

---

## EU Requirement (R.171 §5.3.7.2.1.3)

> A manoeuvre shall not be initiated if a disengagement warning (HOR, EOR, DCA) is currently active.

This applies to ALL manoeuvres involving lateral movement — most importantly, lane change initiation.

---

## China L2GB Status

GB draft §6.x lane change preconditions, item e) states:

> 若系统正在发出驾驶员脱离提示或警告信号，不触发换道过程。

Translation: If the system is currently issuing a driver disengagement reminder or warning signal, do not trigger the lane change procedure.

This covers HOR, EOR, and DCA — all three disengagement signal types. **CN and EU are equivalent.**

Additionally, GB §4.8.3.1.1.3 / §6.x(f) also prohibits lane change when DMS is unavailable:
> 若系统确认视线脱离检测处于不可用状态，不触发换道过程。

---

## Root Cause of Remaining Risk

| Layer | Current Evidence | Remaining Question |
|---|---|---|
| **Regulation** | GB §6.x(e) and EU R.171 §5.3.7.2.1.3 are equivalent | Aligned |
| **ADRS** | Lane_Change ADRS page not fully reviewed for this precondition | Does the ADRS explicitly list "no disengagement warning active" as a lane change precondition? |
| **Software** | Not reviewed | Is the HOR/EOR/DCA flag checked before lane change initiation in the DCAS software? |
| **Validation** | Not confirmed | Is there a test case for: system in lane change mode + HOR issued → lane change blocked? |

---

## Safety Rationale

The prohibition exists because:
1. If the driver is not paying attention (which is why HOR/EOR is active), initiating a lane change adds lateral risk
2. A lane change requires the driver to be able to assess the target lane — a disengaged driver cannot do this
3. Initiating a lane change while also issuing warnings creates conflicting demands on the driver's attention

This prohibition also interacts with H2: when DMS is unavailable, both no-lane-departure (H2) and no-lane-change-trigger (H8) apply.

---

## Scope

This requirement applies to:

| Lane Change Type | Applies? |
|---|---|
| Driver-triggered lane change | Yes — do not start the lane change if warning is active |
| Driver-confirmed lane change | Yes — do not request/present the lane change option if warning is active |
| System-triggered lane change | Yes — do not initiate |
| RMF lane change | Possibly excepted — RMF operates BECAUSE driver is unavailable; its lane changes are safety-critical and must not be blocked by the disengagement warning (RMF IS the response to disengagement) |

The RMF exception is architecturally important: RMF lane changes in §4.6.3 (GB) and §5.3.7.3.2 (R.171) operate precisely when the driver is unavailable, so the §6.x(e) prohibition should not apply to RMF lane changes.

---

## Required Closure Actions

1. Confirm the G1.3 Lane Change ADRS explicitly lists GB §6.x(e) / EU §5.3.7.2.1.3 as a lane change gate condition
2. Confirm the software checks the HOR/EOR/DCA flag before any lane change initiation (driver-triggered, driver-confirmed, system-triggered)
3. Confirm the RMF lane change is explicitly exempt from this gate (RMF operates under driver unavailability by design)
4. Add a validation test: DCAS active, driver-confirmed lane change mode, system issues HOR → verify lane change is not triggered

---

## Open Questions

1. Is there a race condition risk: system initiates lane change, THEN HOR is triggered mid-preparation — what happens? (GB §4.6.2.3.1.2 / §4.6.2.3.1.3 address ongoing lane change conditions, but not the reverse.)
2. Does the system re-attempt the lane change after the warning is cleared (driver responds to HOR and places hands back on wheel)?
3. Is the RMF lane change exempt from the §6.x(e) gate in the current software implementation?
