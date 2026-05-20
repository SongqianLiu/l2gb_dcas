# R79-2 — Automatic Lane Change Initiation Window: 3 s to 5 s

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing in CN; R.171 partially covers) |
| **R.79 Reference** | UN R.79 04 S6 §5.6.4.6.4 + §5.6.4.6.4.1 |
| **R.171 Reference** | §6.2.7 (≥3 s advance indicator only) |
| **CN Reference** | Not found in GB draft |
| **Gap Type** | R.79 adds upper bound (≤5 s) not in R.171 or CN |

---

## R.79 Requirement (§5.6.4.6.4 + §5.6.4.6.4.1)

§5.6.4.6.4:
> The lateral movement of the vehicle towards the intended lane shall not start **earlier than 1.0 second** after the start of the lane change procedure.

§5.6.4.6.4.1 (automatic initiation):
> In case of an automatic initiation, the lane change manoeuvre shall commence **between 3.0 seconds and 5.0 seconds** after the manual activation of the procedure (driver activates direction indicator).

Two constraints work together:
1. **Minimum delay**: lateral movement cannot begin before 1.0 s after procedure start
2. **Automatic initiation window**: if the system automatically initiates the manoeuvre, it must do so within 3–5 s of the driver's direction indicator activation

The 3–5 s window ensures: (a) ≥3 s of advance indicator warning to surrounding traffic; (b) the system does not hold the pending state indefinitely — it must start or cancel within 5 s.

---

## R.171 / CN L2GB Status

**R.171 §6.2.7**: direction indicator shall be activated for at least 3 s before lateral movement — this sets the lower bound (≥3 s) but does NOT specify an upper bound (≤5 s for automatic start).

**R.171 §6.2.9.5**: the 7-second initiation timeout (M25 in our analysis) applies to the overall "approved to start" window — but this is a different concept from R.79's 3–5 s automatic initiation window.

**CN GB draft**: no equivalent timing window for automatic initiation found.

---

## Key Distinction from M25 (7-second timeout)

M25 (R.171 §6.2.9.5) addresses the overall window from "system approves lane change" to "manoeuvre must start or cancel" — capped at 7 s.

R79-2 (R.79 §5.6.4.6.4.1) specifically constrains **automatic initiation**: the system must start the lateral movement within 3–5 s of the driver activating the direction indicator. This is a tighter window (5 s max vs 7 s) and also sets a minimum delay (not before 3 s).

Both apply; the stricter 5 s upper bound from R.79 governs when automatic initiation is used.

---

## Required Closure Actions

1. Confirm G1.3 lane change mode: does the system automatically initiate lateral movement (automatic initiation per §5.6.4.6.4.1), or does it require a second deliberate driver action?
2. If automatic initiation: update the EU variant to enforce the 3–5 s window:
   - Lateral movement must not start before 3 s after indicator activation
   - Lateral movement must start (or manoeuvre must be cancelled) by 5 s after indicator activation
3. Confirm the 1 s minimum delay (§5.6.4.6.4) is implemented: no lateral movement within the first 1 s of procedure start
4. Add ADRS requirement for EU variant: "For automatic initiation, the lane change shall commence between 3.0 s and 5.0 s after indicator activation (R.79 §5.6.4.6.4.1)"
5. Validate: measure time from direction indicator activation to first lateral displacement for automatic initiation mode → confirm 3.0 s ≤ t ≤ 5.0 s
