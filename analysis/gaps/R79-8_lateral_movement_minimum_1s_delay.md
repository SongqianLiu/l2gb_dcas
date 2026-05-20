# R79-8 — Lateral Movement Minimum 1-Second Delay After Procedure Start

| Field | Detail |
|---|---|
| **Risk Level** | Low-Medium (Timing constraint likely already met; needs confirmation) |
| **R.79 Reference** | UN R.79 04 S6 §5.6.4.6.4 |
| **R.171 Reference** | §6.2.7 (≥3 s indicator advance — implies ≥3 s delay; stricter than 1 s) |
| **CN Reference** | Not explicitly found in GB draft |
| **Gap Type** | R.79 explicit minimum delay — effectively subsumed by R.171/R79-2's ≥3 s requirement |

> Note: If R.171 §6.2.7 (M22) and R79-2 (3–5 s automatic initiation window) are both complied with, the 1 s minimum delay of §5.6.4.6.4 is automatically satisfied. This gap is included for completeness and for manual/second-deliberate-action mode, where the 3 s advance indicator does not apply.

---

## R.79 Requirement (§5.6.4.6.4)

> The lateral movement of the vehicle towards the intended lane shall **not start earlier than 1.0 second** after the start of the lane change procedure.
>
> Additionally, the lateral movement to approach the lane marking and the lateral movement necessary to complete the lane change manoeuvre shall be completed as one continuous movement.

The 1 s minimum delay between procedure start and lateral movement start ensures the direction indicator has been active for at least 1 s before any lateral displacement — a minimum warning to surrounding traffic.

The "one continuous movement" requirement prohibits pausing mid-lane-change: once lateral movement starts, it must complete without interruption (unless suppressed per §5.6.4.6.8).

---

## R.171 / CN L2GB Status

**R.171 §6.2.7**: requires ≥3 s advance indicator before lateral movement — this automatically satisfies the 1 s minimum delay of §5.6.4.6.4.

**For automatic initiation (R79-2)**: the 3–5 s window further ensures ≥3 s delay, making the 1 s minimum trivially satisfied.

**For second-deliberate-action initiation**: where the driver gives a second input to confirm the lane change (not automatic), the 3 s advance indicator rule still applies per R.171 §6.2.7, so again the 1 s minimum is satisfied.

**CN GB draft**: No equivalent minimum delay found, but CN §4.6.2.2.1.7 (direction indicator activated before lane change) implies a non-zero delay.

---

## "One Continuous Movement" Requirement

This is the more operationally significant aspect of §5.6.4.6.4: once the lateral phase starts, it must complete as a single continuous movement. The system must not:
- Begin crossing the lane marking, then pause
- Return to the original lane partway through before completing the change

If the suppression conditions (§5.6.4.6.8) are met after lateral movement has already started, the system must decide whether to: (a) complete the manoeuvre, or (b) immediately abort and return to original lane. The "continuous" requirement suggests (a) is the expected behavior unless safety demands otherwise.

---

## Required Closure Actions

1. Confirm G1.3 lane change controller: once lateral movement begins, is it designed to complete in one continuous movement?
2. Verify the minimum delay from procedure start to lateral movement start is ≥1 s across all lane change modes
3. Document the "one continuous movement" design principle in the ADRS
4. Add validation test: verify no lane change manoeuvre pauses mid-lane during normal operation
