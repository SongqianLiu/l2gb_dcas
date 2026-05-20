# R79-6 — Minimum Rear Detection Distance ≥ 55 m (Tested with Motorcycle)

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing in CN and R.171) |
| **R.79 Reference** | UN R.79 04 S6 §5.6.4.8.1.1 |
| **R.171 Reference** | §6.2.4 (target lane safety criterion — no absolute detection range) |
| **CN Reference** | Not found in GB draft |
| **Gap Type** | R.79 standalone — quantitative detection range with specific test target |

---

## R.79 Requirement (§5.6.4.8.1.1)

> The ACSF of Category C shall be able to detect vehicles approaching from the rear in an adjacent lane up to a distance **Srear** as specified below:
>
> The minimum distance Srear shall be **declared by the vehicle manufacturer**. The declared value shall not be less than **55 m**.
>
> The declared distance shall be tested according to the relevant test in Annex 8 **using a two-wheeled motor vehicle of Category L3** as the approaching vehicle.

This is a minimum sensor performance requirement with a specific, binding test methodology:
- Minimum declared Srear: **55 m**
- Test target: **motorcycle** (Category L3) — the most challenging detection target due to small radar cross-section
- Test procedure: Annex 8 test protocol

---

## R.171 / CN L2GB Status

**R.171 §6.2.4**: specifies a quantitative safety criterion for the target lane (approaching vehicle must not be forced to decelerate beyond threshold), but does not specify a minimum absolute sensor detection range.

**CN GB §4.6.2.2.1.4/1.5**: requires safety assessment of target lane with safety margin requirements, but does not specify a minimum detection distance or a required test methodology with motorcycles.

---

## Why Motorcycle Specifically

Motorcycles have a significantly smaller radar cross-section than passenger vehicles. A system calibrated to detect cars at 55 m may fail to detect a motorcycle approaching at the same distance. The R.79 test with a motorcycle ensures the system's safety assessment is valid for the most challenging lateral traffic scenario.

---

## Required Closure Actions

1. Confirm G1.3 declared Srear value: what is the manufacturer-declared rear detection range for the lane change function?
2. If Srear < 55 m: investigate whether this can be addressed through sensor fusion improvements or if the lane change ODD must be restricted
3. Perform R.79 Annex 8 rear detection test with a Category L3 motorcycle as the approaching vehicle at the declared Srear distance
4. Document Srear in the R.79 type approval submission (§5.6.4.10.1)
5. Add ADRS requirement: "The ACSF Cat C rear detection range (Srear) shall be ≥ 55 m and shall be validated with a motorcycle target per R.79 Annex 8"

---

## Open Questions

1. What is G1.3's current rear/lateral radar range specification for the lane change sensing zone?
2. Does the current system use radar-only or radar+camera fusion for rear target lane detection?
3. Is the 55 m sufficient at the maximum declared lane change speed? (At 130 km/h closing speed differential of 30 km/h, 55 m gives approximately 6.6 s — this should be cross-checked against the safety criterion in §6.2.4.)
