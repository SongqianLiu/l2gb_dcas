# H5 — RMF Must Be Capable of Lane Change If System Has Lane Change Feature

| Field | Detail |
|---|---|
| **Risk Level** | ~~High~~ → **Medium (Traceability / Validation Gap)** |
| **EU Reference** | UN R.171 S2 §5.3.7.3.2 |
| **CN Reference** | GB draft §4.6.3.1.1 |
| **Gap Type** | Traceability / implementation / validation gap |

> **Reclassified**: Originally assessed as "Missing in CN / High Risk." GB §4.6.3.1.1 contains a substantively equivalent requirement. Remaining risk is implementation and validation evidence.

---

## EU Requirement (R.171 §5.3.7.3.2)

> If the system has driver-confirmed or system-initiated lane change functionality, its risk mitigation function (RMF) shall be capable of performing lane changes to reach the target stop area (e.g., emergency lane) on highway-type roads.

---

## China L2GB Status

GB draft §4.6.3.1.1 states:

> 若系统具有驾驶员确认的换道控制功能或系统触发的换道控制功能，则RMF 应至少具有在A类道路环境下执行换道控制的能力。

Translation: If the system has driver-confirmed lane change control or system-triggered lane change control, the RMF shall at least have the capability to execute lane change control in Category A road environments.

Additionally, GB §4.6.3.1.2:

> 系统的设计应根据系统能力和当前情况（例如，交通流情况、道路设施情况）选择适当的目标停车区域以降低安全风险。
> 注：目标停车区域包括本车道、本车道的右侧车道、应急车道、硬路肩等。

This explicitly includes "应急车道" (emergency lane) and "硬路肩" (hard shoulder) as possible target stop areas — consistent with EU R.171's intent.

**CN and EU are substantively aligned** at the regulatory level. Both require:
1. RMF must have lane change capability IF the base system has lane change
2. Target stop areas include the emergency lane / hard shoulder

---

## Root Cause of Remaining Risk

| Layer | Current Evidence | Remaining Question |
|---|---|---|
| **Regulation** | GB §4.6.3.1.1 and EU §5.3.7.3.2 aligned | Aligned |
| **ADRS** | Not explicitly confirmed in extracted ADRS summaries | Is RMF lane change capability explicitly defined in ADRS? |
| **Software** | Not reviewed | Does the G1.3 RMF module actually execute lane changes to emergency lane? Under what traffic conditions? |
| **Validation** | GB §9.4.10 includes RMF tests; §9.4.10.2.2 specifically for RMF lane change | Is this validated? Is test coverage complete? |

---

## Affected Scope

This gap is **conditional** on G1.3 having lane change capability:

| System Type | Lane Change Capability | RMF Lane Change Required? |
|---|---|---|
| 基础单车道 (lane keeping only) | No | No |
| 基础多车道 (driver-triggered lane change) | Yes | Yes — must implement |
| 领航 (system-triggered lane change) | Yes | Yes — must implement |

G1.3 likely has at least 基础多车道 or 领航 capability. If so, the RMF lane change capability is mandatory under both GB and EU.

---

## Key Validation Test

GB §9.4.10.2.2 tests RMF lane change capability. This test must be:
1. Performed and passed for CN type approval
2. Adapted for EU type approval context (highway scenario, emergency lane / hard shoulder as target)

---

## Required Closure Actions

1. Confirm G1.3 system type (does it have driver-confirmed or system-triggered lane change?)
2. If yes: confirm the ADRS explicitly maps GB §4.6.3.1.1 → RMF software requirement
3. Confirm the RMF module's lane change logic covers emergency lane / hard shoulder targeting
4. Ensure GB §9.4.10.2.2 test evidence is also applicable to EU R.171 Annex 4 RMF test requirements

---

## Open Questions

1. Does the G1.3 RMF currently execute lane changes in practice, or does it only perform in-lane stopping?
2. If the RMF encounters dense traffic in the target lane, does it have a fallback (stay in current lane, decelerate to stop)?
3. Does the RMF lane change comply with the same lateral dynamics constraints (§4.6.3.2.10: ≤1 m/s² additional lateral accel during RMF lane change, beyond curvature)?
4. What is the GB test result for §9.4.10.2.2? Any known failures?
