# M17 — DCAS Controls Physically Distinguishable from Non-DCAS Controls

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Partial — CN requires information, not physical distinction) |
| **EU Reference** | UN R.171 S2 §5.5.2.4.1 |
| **CN Reference** | GB draft §4.1.11 |
| **Gap Type** | Partial — CN addresses information display, EU requires physical/visual control distinction |

---

## EU Requirement (R.171 §5.5.2.4.1)

> The controls for activating, modifying, or deactivating the system shall be clearly distinguishable from controls for systems not forming part of the DCAS.

The requirement is about the physical controls themselves — steering wheel buttons, stalk controls, touchscreen icons — being visually or tactilely distinguishable from non-DCAS vehicle controls.

---

## China L2GB Status

GB draft §4.1.11 states:

> 系统应向驾驶员提供与系统相关的信息，包括：可供驾驶员操作和改变的系统设置（例如，车速、车道维持、车头时距等）相关信息，以及驾驶员可使用的其他操作界面...

Translation: The system shall provide information to the driver related to the system, including information about system settings that can be operated and changed by the driver (e.g., speed, lane keeping, headway), and other operator interfaces available to the driver.

**CN addresses information provision** about available controls. It does not contain an explicit requirement that the physical controls for DCAS must be visually or tactilely distinguishable from non-DCAS controls.

---

## Practical Implication

EU §5.5.2.4.1 targets the design of the steering wheel and instrument cluster controls. For example:
- DCAS activation button should not look identical to, say, the audio controls or phone buttons
- If DCAS and non-DCAS functions share the same physical button with mode-dependent behavior, this must be clearly communicated to the driver

For the EU variant, the G1.3 HMI/UX design review must verify that DCAS controls are clearly distinct from non-DCAS controls, both visually (labeling, color, icon) and functionally.

---

## Required Closure Actions

1. Conduct a G1.3 HMI review: identify all physical/touchscreen controls that activate, modify, or deactivate DCAS
2. For each DCAS control, verify it is clearly distinguishable from adjacent non-DCAS controls (by label, icon, color, or physical position)
3. If any controls are shared/dual-function, add clear mode-indication to the instrument cluster
4. Document in the EU type approval submission: DCAS control layout diagram with differentiation method described
5. Add ADRS requirement: "DCAS controls shall be clearly distinguishable from non-DCAS controls" (EU variant)
