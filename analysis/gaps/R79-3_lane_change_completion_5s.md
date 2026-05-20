# R79-3 — Lane Change Completion Within 5 Seconds (M1/N1)

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing in R.171 and CN) |
| **R.79 Reference** | UN R.79 04 S6 §5.6.4.6.5 |
| **R.171 Reference** | Not found |
| **CN Reference** | Not found in GB draft |
| **Gap Type** | Missing in R.171 and CN — R.79 standalone requirement |

---

## R.79 Requirement (§5.6.4.6.5)

> The lane change manoeuvre shall be completed in less than:
> (a) **5 seconds** for M1, N1 vehicle categories;
> (b) 10 seconds for M2, M3, N2, N3 vehicle categories.

This is a maximum duration limit on the lateral manoeuvre itself — from the start of lateral movement to the completion of the lane change (vehicle stabilized in target lane with B1 lane centering resumed).

---

## R.171 / CN L2GB Status

**R.171**: No equivalent maximum lane change completion duration requirement. R.171 §6.2.9.5 sets a 7-second window from initiation to start of lateral movement (M25), but places no time limit on the lateral movement phase itself.

**CN GB draft**: No equivalent requirement found.

---

## Why This Matters

A lane change that drags out for 8–10 seconds occupies two lanes simultaneously for an extended period, increasing collision risk with vehicles in both the original and target lanes. The 5-second limit ensures the manoeuvre is executed decisively.

This is measured from start to completion of lateral movement, not including the pre-manoeuvre indicator activation period.

---

## Required Closure Actions

1. Measure G1.3 current lane change duration at various speeds and gap scenarios → confirm <5 s for M1/N1 category
2. If any scenario results in >5 s: investigate whether this is a controller tuning issue (lateral accel too low) or a sensor/safety hold condition
3. Add ADRS requirement for EU variant: "The lane change lateral manoeuvre shall be completed within 5 seconds from start of lateral movement (R.79 §5.6.4.6.5, M1/N1)"
4. Add to validation test protocol: lane change duration measurement as a pass/fail criterion ≤5 s

---

## Open Questions

1. How is "lane change completion" defined in the G1.3 system: first lane marking crossed, vehicle centre in target lane, or B1 resumption?
2. Does the completion time vary significantly with vehicle speed? (At high speed, the lateral distance to cross is the same but relative motion to lane marking is different.)
