# M14 — Headway Notification on First Activation If Set Below 2 s

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Partial — CN threshold differs) |
| **EU Reference** | UN R.171 S2 §5.3.7.5.1.1.2 |
| **CN Reference** | GB draft §4.6.1.11 |
| **Gap Type** | Partial — CN threshold covers subset of EU requirement |

---

## EU Requirement (R.171 §5.3.7.5.1.1.2)

> On first activation of the system if the headway setting is below 2 s, the system shall notify the driver of the current headway setting.

The intent: drivers should not unknowingly operate in a short-headway mode. A notification on first activation (when headway < 2 s) ensures informed consent about the current following distance setting.

---

## China L2GB Status

GB draft §4.6.1.11 states:

> 若车头时距的设置小于1 s，则系统应向驾驶员显示此时距，提醒驾驶员注意当前车头时距设置。

Translation: If the headway setting is less than 1 s, the system shall display this headway to the driver, alerting the driver to the current headway setting.

**CN and EU are partially aligned.** Both require headway notification when the setting is short, but the trigger threshold differs:
- **EU**: notification triggered when headway < **2 s**
- **CN**: notification triggered when headway < **1 s**

A system calibrated to the CN threshold (1 s) will not notify the driver for headway settings in the range [1 s, 2 s), which would fail EU §5.3.7.5.1.1.2.

---

## Required Closure Actions

1. Confirm G1.3 minimum headway range: what is the minimum allowed headway setting in the HMI?
2. If minimum headway ≥ 2 s: this gap is moot — EU notification never triggers
3. If minimum headway < 2 s: update the EU variant notification logic to trigger at headway < 2 s (not 1 s)
4. Add ADRS requirement: "On first activation, if the set headway is below 2 s, the system shall display the current headway setting to the driver" (for EU variant)
5. Validate: configure headway to 1.5 s → activate system → verify notification appears

---

## Open Questions

1. Does G1.3 allow headway settings below 2 s? Many OEMs set minimum headway at 1.5 s or even 2 s
2. Is the headway notification persistent (displayed for the entire trip) or only on first activation?
3. CN notification requirement for headway < 1 s: is this already in the G1.3 ADRS, or also a traceability gap?
