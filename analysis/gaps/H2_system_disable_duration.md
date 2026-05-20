# H2 — System Disable Duration: CN 30-Min vs EU Run-Cycle

| Field | Detail |
|---|---|
| **Risk Level** | **High** (confirmed regulatory conflict) |
| **EU Reference** | UN R.171 S2 §5.5.4.2.8.1 |
| **CN Reference** | GB draft §8.1 |
| **Gap Type** | Conflict (CN and EU impose different disable durations) |

---

## EU Requirement (R.171 §5.5.4.2.8.1)

> The manufacturer shall implement strategies to disable the activation of the system for the run cycle when prolonged insufficient engagement leads to more than one driver unavailability response.

Key aspects:
- **Trigger**: >1 driver unavailability response (i.e., more than one RMF event in the same run cycle)
- **Duration**: Disabled for the **run cycle** — i.e., until the next ignition cycle (power off and back on)
- **Principle-based**: EU does not specify a fixed timer; the entire remaining run cycle is the disable period

---

## China L2GB Status

GB draft §8.1 states:

> 在当前车辆上电/点火周期内（发动机自动启停除外），当由于驾驶员脱离导致发生以下任一情况时，退出本次激活状态后领航组合驾驶辅助系统、基础单车道组合驾驶辅助系统和基础多车道组合驾驶辅助系统应被禁用不少于30 min：
> a) 系统触发1次RMF；
> b) 若不具有RMF，系统持续发出10 s 升级的HOR 或DCA；
> c) 系统发出2次EOR升级后的DCA；
> d) 在任意的30 min内，系统发出3次升级的HOR或EOR。

Translation: Within the current ignition cycle, after exiting the active state, the system shall be disabled for **no less than 30 minutes** when any of the following occurs due to driver disengagement:
- a) System triggers 1 RMF
- b) Without RMF: 10s continuous escalated HOR or DCA
- c) 2 escalated DCAs after EOR
- d) 3 escalated HOR or EOR within any 30-min window

---

## Conflict Analysis

| Dimension | CN GB | EU R.171 | Conflict |
|---|---|---|---|
| **Trigger threshold** | 1 RMF event (stricter) | >1 RMF event (requires multiple) | CN triggers disable sooner |
| **Disable duration** | ≥30 min (minimum timer) | Rest of run cycle (duration-unspecified) | Conflict: see below |
| **Scope** | All three system types | Manufacturer implements strategies | Broadly equivalent |

### Duration Conflict

The core conflict is the disable duration:

**Scenario A — Short run cycle (<30 min):**
- CN: 30-min minimum extends BEYOND the current ignition cycle into the next run cycle
- EU: Disable for the run cycle only — if cycle is 20 min, system re-enables after power cycle

In this scenario, CN is MORE restrictive than EU (blocks re-enabling into the next cycle).

**Scenario B — Long run cycle (>30 min):**
- CN: Disable for 30 min, then ALLOW RE-ENABLING within the same run cycle
- EU: Disable for the ENTIRE remaining run cycle — system cannot be re-enabled until the next ignition

In this scenario, CN is LESS restrictive than EU. A driver who has triggered RMF could regain system access after 30 min within the same trip. EU prohibits this.

### The Critical Gap

For EU type approval, a G1.3 vehicle could have a 2-hour motorway trip. Under CN rules: trigger RMF → wait 30 min → system available again. Under EU rules: trigger RMF → system stays disabled for the remaining ~90 min of that trip.

This is the real compliance risk: **the 30-min reset within a long run cycle does not satisfy EU's run-cycle-disable intent**.

---

## Engineering Impact

The current G1.3 software implements a 30-min countdown timer. For EU compliance, this must be changed to:
- On trigger: set a flag "disabled for run cycle" 
- Clear flag only on: ignition off + ignition on (new run cycle)
- The 30-min timer is insufficient and does not satisfy EU §5.5.4.2.8.1

This is an **architectural software change**, not just a parameter adjustment.

---

## Trigger Threshold: CN is Stricter

One aspect where CN is stricter than EU: CN disables after **1 RMF** event; EU requires "more than one driver unavailability response." This means the EU variant could tolerate a first RMF without disabling, while CN does not.

For EU type approval, the manufacturer could argue that starting disable after 1 RMF is more conservative. However, the run-cycle duration of the disable period remains non-compliant.

---

## Required Closure Actions

1. **Software**: Replace 30-min countdown timer with run-cycle disable flag (cleared only on power cycle)
2. **HMI**: Ensure the driver is clearly informed that the system is disabled for the rest of the current trip (not just 30 minutes)
3. **ADRS**: Update the 系统禁用 ADRS to reflect run-cycle disable for the EU variant
4. **Validation**: Define and test: system triggers RMF → system disabled → long driving session → verify system remains disabled → power off → power on → verify system is available again

---

## Open Questions

1. Does the G1.3 system currently communicate to the driver HOW LONG the disable will last? If showing "30 min," this messaging must change for the EU variant.
2. Does GB §8.1's "在当前车辆上电/点火周期内" clause already carry the intent to limit to the current ignition cycle, and is the 30-min timer the minimum floor? If interpreted this way (30 min OR rest of cycle, whichever is longer), then the GB standard could be more aligned than it appears — but this interpretation requires legal/regulatory confirmation.
3. Does the EU variant require a separate system calibration/software build, or can a single build satisfy both CN (30-min timer) and EU (run-cycle) by implementing the stricter (run-cycle) version?
