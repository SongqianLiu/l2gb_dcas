# M12 — Driver Cannot Set Default Speed Offset Above Detected Limit

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing in CN) |
| **EU Reference** | UN R.171 S2 §5.3.7.4.9 |
| **CN Reference** | Not found in GB draft |
| **Gap Type** | Missing in CN |

---

## EU Requirement (R.171 §5.3.7.4.9)

> The system shall not allow the driver to set a default speed offset above the system-determined speed limit.

In other words: a driver cannot configure the system to permanently drive, say, 10 km/h above the detected speed limit as a default cruise setting. The system-determined limit is an upper bound for the driver's default offset.

Note: this does not prohibit the driver from manually overriding speed upward in the moment (via accelerator); it constrains the **preset/default** offset setting.

---

## China L2GB Status

GB §4.5 (speed limit assistance) requires the system to:
- Determine and continuously display the current road speed limit (§4.5.1–4.5.2)
- Set cruise target speed via driver input OR system-determined limit (§4.5.3)

GB §4.1.5 prohibits the active vehicle speed from exceeding the ODC maximum speed limit while the system is active in Category A environments.

However, neither §4.5 nor §4.1.5 explicitly prohibits the driver from configuring a default offset (e.g., "+10 km/h above detected limit") in the system settings. **This specific prohibition is not found in the CN GB draft.**

---

## Risk

If G1.3 allows drivers to set a permanent "+X km/h" offset above the detected speed limit as a default profile, this would fail EU §5.3.7.4.9. This is a software/UX settings constraint that must be added for the EU variant.

---

## Required Closure Actions

1. Review G1.3 HMI/UX: does the system allow the user to set a speed offset relative to the detected speed limit in any settings menu?
2. If yes: for the EU variant, block this configuration option or cap the offset at 0 km/h (i.e., default cruise target ≤ detected limit)
3. Add ADRS requirement: "The system shall not allow the driver to configure a default cruise speed offset that exceeds the system-determined road speed limit"
4. Validate: in system settings, attempt to configure a speed offset above detected limit → verify this is rejected

---

## Open Questions

1. Does G1.3 currently have a "speed offset" setting at all (common in European market vehicles)?
2. Does the EU variant need to disable this feature entirely, or only cap the maximum offset at 0?
3. How does this interact with the driver's real-time ability to set a cruise speed above the detected limit during driving? (That is covered by §4.1.5 / §5.3.7.4 generally — active speed shall not exceed limit.)
