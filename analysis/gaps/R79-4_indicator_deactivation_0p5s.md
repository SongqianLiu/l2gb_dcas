# R79-4 — Direction Indicator Deactivated ≤ 0.5 s After Lane Change Completion

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing timing specificity in R.171 and CN) |
| **R.79 Reference** | UN R.79 04 S6 §5.6.4.6.7 |
| **R.171 Reference** | §6.2.6 (deactivated by system after lane change — no timing specified) |
| **CN Reference** | GB draft §4.6.2.2.1.7 (deactivated after lane change — no timing) |
| **Gap Type** | R.79 adds quantitative timing not in R.171 or CN |

---

## R.79 Requirement (§5.6.4.6.7)

> The direction indicator shall remain active throughout the whole period of the lane change manoeuvre and shall be **automatically deactivated by the system no later than 0.5 seconds** after the resumption of ACSF of Category B1 lane keeping function.

The trigger for deactivation is the resumption of B1 (lane centering in the target lane), not just the end of lateral movement. The 0.5 s window prevents the indicator from staying on unnecessarily after the manoeuvre is complete.

Note: Automatic deactivation is required only if the lane change was automatically triggered. For driver-initiated manoeuvres where the driver manually activated the indicator, the system is not required to automatically deactivate it — but if the system did activate the indicator, it must deactivate it within 0.5 s.

---

## R.171 / CN L2GB Status

**R.171 §6.2.6**: direction indicator shall be deactivated by the system after lane change completion — no timing specified.

**CN GB §4.6.2.2.1.7**: system shall deactivate indicator after lane change completion — no timing specified.

Both R.171 and CN require deactivation but leave the timing unspecified. R.79 adds the ≤0.5 s constraint.

---

## Required Closure Actions

1. Confirm G1.3 current behavior: how long after lane change completion does the system maintain the direction indicator active?
2. Measure the delay from B1 resumption to indicator deactivation across multiple scenarios
3. If delay >0.5 s: update the indicator deactivation logic to trigger ≤0.5 s after B1 lane centering resumes in the target lane
4. Add ADRS requirement for EU variant: "The direction indicator shall be deactivated by the system no later than 0.5 s after B1 lane centering function resumes in the target lane (R.79 §5.6.4.6.7)"
5. Validate: trigger lane change → measure time from B1 resumption to indicator off → confirm ≤0.5 s
