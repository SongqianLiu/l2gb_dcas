# R79-5 — HOD Check and Warning Within 3 s of Lane Change Initiation (Pending Phase)

| Field | Detail |
|---|---|
| **Risk Level** | Medium (R.79-specific requirement not in R.171 or CN) |
| **R.79 Reference** | UN R.79 04 S6 §5.6.4.5.6 |
| **R.171 Reference** | §5.5.4.2 (general HOD/DMS — not specific to lane change pending phase) |
| **CN Reference** | Not found for this specific phase |
| **Gap Type** | R.79 standalone — HOD requirement specific to lane change pending phase |

---

## R.79 Requirement (§5.6.4.5.6)

> The system shall provide a means of detecting that the driver is holding the steering control and shall warn the driver in accordance with the warning strategy below:
>
> If, after a period of **no longer than 3 s** after the initiation of the lane change procedure and **before the start of the lane change manoeuvre**, the driver is not holding the steering control, an optical warning signal shall be provided.
>
> The warning signal shall be active until the driver is holding the steering control, or until the system is deactivated, either manually or automatically.

This is a targeted HOD requirement for the **pending phase** of a lane change — the window between when the driver activates the direction indicator (procedure start) and when the lateral movement begins (manoeuvre start). During this window, the driver must be confirmed holding the steering wheel.

---

## R.171 / CN L2GB Status

**R.171 §5.5.4.2**: general HOD (motoric engagement) requirements covering the active driving state. The general HOR (Hands-On Request) timing applies during normal driving. However, R.171 does not have a specific provision targeting the lane change pending phase (post-indicator activation, pre-lateral movement).

**CN GB draft**: No equivalent requirement for HOD checking specifically in the lane change pending phase.

---

## Rationale

During the pending phase (indicator active, lateral movement not yet started), the driver has committed to a lane change. If the driver's hands are off the wheel at this moment, the system should not proceed with lateral movement without warning. This is safety-critical: the manoeuvre will happen in 3–5 s (per §5.6.4.6.4.1), and driver hands must be on the wheel before it does.

---

## Interaction with Suppression Conditions

R.79 §5.6.4.6.8 lists conditions under which the pending lane change shall be automatically suppressed:
> (d) The system has detected that the driver is not holding the steering control at the start of the lane change manoeuvre.

If the HOD warning is issued per §5.6.4.5.6 and the driver still does not grip the wheel by the time the manoeuvre would start, the lane change shall be cancelled per §5.6.4.6.8(d).

---

## Required Closure Actions

1. Confirm G1.3 current behavior: during the lane change pending phase (indicator active, lateral movement not started), is there an active HOD check?
2. If not: add a HOD monitoring state for the pending phase — if hands not detected within 3 s of indicator activation, issue optical warning
3. Confirm the lane change is automatically cancelled if driver does not grip wheel before lateral movement starts (links to §5.6.4.6.8(d) suppression condition)
4. Add ADRS requirement for EU variant: "During the lane change pending phase, if driver hands-on not detected within 3 s of procedure start, an optical warning shall be issued and the manoeuvre shall not begin until HOD is confirmed"
5. Validate: initiate lane change procedure with hands off wheel → confirm warning within 3 s → confirm manoeuvre does not start until HOD confirmed
