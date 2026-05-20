# China L2GB ADRS ↔ EU DCAS (UN R.171) Regulatory Gap Analysis

**Vehicle:** Firefly G1.3  
**China basis:** L2GB ADRS (Feishu wiki, as of May 2026)  
**EU basis:** UN Regulation No. 171 Supplement 2 (ECE/TRANS/WP.29/2025/65) + R79 04 series  
**Purpose:** Front-loaded technical assessment for G1.3 EU market entry  
**Date:** 2026-05-20  

---

## Regulatory Context

| Item | China | EU |
|---|---|---|
| Regulation | GB 44495（智能网联汽车组合驾驶辅助系统安全要求，送审稿） | UN R.171 S2 (DCAS) + UN R.79 §5.6.5 |
| Status | 强制标准，送审稿阶段 | R.171 issued; S2 = latest amendment (2025) |
| Scope | 组合驾驶辅助系统（L2 combined） | Driving Control Assistance System (L2 combined) |
| Key driver monitoring ref | DMS（直接视线检测或头部姿态） | §5.5.4.2.5: eye gaze primary, head posture supplemental |

---

## Gap Analysis by Dimension

### 1. System Activation / Exit

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 1.1 | System off at every ignition | Not explicitly required; current cycle context assumed | §5.5.3.1: system shall be in 'off' mode at each new engine start/run cycle | **Missing** | Med | China counts per power-on cycle but doesn't mandate off-state at start; EU requires explicit off-state reset |
| 1.2 | Activation preconditions | Speed ≥ Vsminset; road type (highway); lane marking detected | §5.5.3.2.2: driver in seat + belt fastened; DMS able to monitor; no active failure; within system boundary; safety systems functional | **Partial** | Med | China focuses on road/speed ODD; EU additionally mandates seatbelt check and DMS availability as hard preconditions |
| 1.3 | Driver-initiated activation only | Implied (driver activates) | §5.5.3.2.1: only upon deliberate driver action (off→on) | Aligned | Low | — |
| 1.4 | No auto-transition to sustained L/L control after driver turns off | Not explicitly addressed | §5.5.2.2: when system switched to off, no automatic transition to any system providing continuous lon/lat movement | **Missing** | High | Risk: after driver disables DCAS, system must not silently hand off to another combined-control mode. EU requires explicit prohibition. |
| 1.5 | Exit by driver at any time | System can be exited; RMF exception | §5.5.3.3.1: shall be possible to switch to 'off' at any time | Aligned | Low | — |
| 1.6 | Graceful exit when preconditions no longer met | Goes to standby/exits; HMI prompt | §5.5.3.3.3: terminate in safe and timely manner → standby or off | Aligned | Low | — |

---

### 2. Driver Monitoring / HOD (Hands-On Detection + Eyes-On Detection)

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 2.1 | Motoric disengagement definition | Hand-off detection (hands leave steering wheel) | §5.5.4.2.4.1: driver deemed motorically disengaged when hands removed from steering control | Aligned | Low | Same definition |
| 2.2 | Visual disengagement detection method | Eye-gaze primary; head posture if eye gaze unavailable | §5.5.4.2.5.1: eye gaze primary; head posture supplemental or if gaze temporarily unavailable | Aligned | Low | — |
| 2.3 | Visual disengagement definition | Eye gaze deviates from driving-relevant area | §5.5.4.2.5.2: eye gaze/head posture directed away from currently driving-task-relevant area; dashboard/instrument panel NOT a driving-task-relevant area | **Partial** | Med | EU explicitly excludes dashboard as driving-relevant area. China ADRS needs to confirm this exclusion is implemented. |
| 2.4 | Re-engagement duration threshold | Not specified in ADRS documents reviewed | §5.5.4.2.5.2.1: re-engagement requires ≥200ms of gaze towards task-relevant area | **Missing** | Med | EU defines a minimum re-engagement duration. China ADRS does not specify this threshold. |
| 2.5 | Multiple short gaze aversions handling | Not explicitly specified | §5.5.4.2.5.3: system shall address multiple subsequent short aversions (e.g., increased re-engagement time or immediate EOR) | **Missing** | Med | EU requires explicit strategy for "short blink" evasion. China ADRS silent on this. |
| 2.6 | DMS unavailability → no lane departure | Not explicitly addressed | §5.5.4.2.1.2: if visual disengagement detection temporarily unavailable, system shall not lead vehicle to leave current lane | **Missing** | High | Critical safety gap: EU requires that if DMS fails, lateral control must be constrained to prevent lane departure. |
| 2.7 | DMS occlusion test | 9.4.9.6.4: occlusion test, EOR within 5s | R.171 §5.5.4.2: strategy documented and demonstrated; Annex 4 tests | Partial | Low | China has specific test; EU defers to manufacturer safety concept + Annex 4. Outcome-equivalent but documentation requirements differ. |

---

### 3. Driver Override

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 3.1 | Lateral override force limit | Not specified | §5.5.3.4.1.4: steering override effort ≤ 50 N | **Missing** | High | EU sets a hard 50 N cap on the effort needed to override lateral control. China ADRS has no corresponding limit. This is a controllability/human factors requirement. |
| 3.2 | Override: system may remain active | Implied (system stays active during temporary driver input) | §5.5.3.4.1: system may remain in active mode, priority given to driver input during overriding period | Aligned | Low | — |
| 3.3 | Longitudinal override: hard braking | Driver braking overrides longitudinal assist | §5.5.3.4.1.1: driver brake input > system deceleration overrides and suspends longitudinal control | Aligned | Low | — |
| 3.4 | Longitudinal resume after brake override | Resumes on driver action | §5.5.3.4.1.1.1: shall not resume lon. control without separate driver action; exception: speed reduction ≤30 km/h within 2s | **Partial** | Med | EU defines a specific exception (≤30 km/h / 2s) for minor brake inputs that allows auto-resume. China ADRS does not address this edge case. |
| 3.5 | Lateral override not to terminate during motoric disengagement | Not addressed | §5.5.3.4.1.5: shall not terminate lateral control while driver is detected to be motorically disengaged (controllability during override) | **Missing** | High | EU prevents the dangerous scenario where override detection causes lateral control to suddenly stop while the driver's hands are off the wheel. |
| 3.6 | Acceleration override | Driver accelerator input overrides longitudinal assist | §5.5.3.4.1.3: accelerator input > system acceleration overrides longitudinal assist; system resumes on current max speed basis | Aligned | Low | — |

---

### 4. DCA / RMF (Driver Control Alert / Risk Mitigation Function)

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 4.1 | HOR timing | HOR issued when hand-off detected; timing per speed | §5.5.4.2.6.1.1: HOR latest when motorically disengaged >5s at speed >10 km/h; may be delayed up to 5s if visually engaged | Aligned | Low | Both require HOR within 5s; EU allows 5s delay if visually engaged (more nuanced) |
| 4.2 | HOR escalation timing | 3s after initial HOR (per EOR ADRS: within 5s, upgrade within 3s) | §5.5.4.2.6.1.2: escalated HOR latest 10s after initial HOR; escalated HOR adds acoustic/haptic | **Conflict** | Med | China: escalation within 3s. EU: escalation latest at 10s. EU is less strict on escalation speed but requires acoustic/haptic in escalated HOR. |
| 4.3 | EOR timing | EOR within 5s of visual disengagement at >10 km/h | §5.5.4.2.6.2.1: EOR latest when visually disengaged >5s at speed >10 km/h | Aligned | Low | Same 5s threshold |
| 4.4 | EOR escalation timing | EOR upgraded within 3s of initial EOR | §5.5.4.2.6.2.2: escalated EOR latest 3s after initial EOR; must include acoustic/haptic | Aligned | Low | Both require escalation within 3s; EU mandates acoustic/haptic in escalated EOR |
| 4.5 | DCA timing | DCA after EOR + further disengagement | §5.5.4.2.6.3.1: DCA at latest 5s after escalated EOR | Aligned | Low | — |
| 4.6 | RMF trigger timing | RMF triggered after DCA if driver remains unavailable | §5.5.4.2.6.4.1: driver unavailability response (RMF) at latest 10s after first escalated request or DCA | Aligned | Low | — |
| 4.7 | HOR signal requirements | Optical signal required | §5.5.4.2.3.1.1: HOR shall contain at least a continual (continuous or intermittent) visual information | Aligned | Low | — |
| 4.8 | EOR signal requirements | Optical + acoustic or tactile | §5.5.4.2.3.2.1: EOR = continual visual + at least one other modality (unless driver observed visual) | Aligned | Low | — |
| 4.9 | DCA signal requirements | Optical + acoustic or tactile, clear prompt for lateral takeover | §5.5.4.2.3.3.1: visual + at least one other modality; clearly instruct driver to resume at least lateral control | Aligned | Low | — |
| 4.10 | Manoeuvre inhibited during DDA warning | Not explicitly stated | §5.3.7.2.1.3: manoeuvre shall not be initiated if disengagement warning is active | **Missing** | Med | EU explicitly prohibits initiating any manoeuvre (e.g., lane change) while a disengagement warning is being issued. China ADRS silent. |
| 4.11 | RMF lane change capability | RMF defined; lane change as part of RMF not specified | §5.3.7.3.2: if system has driver-confirmed/system-initiated lane change, RMF shall be capable of lane changes to reach target stop area (emergency lane) on highway | **Missing** | High | EU requires that if the system has lane change capability, its RMF must also be able to perform lane changes to reach a safe stop area. This is architecturally significant. |

---

### 5. ODD / ODC Management

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 5.1 | Speed range | Vsminset (vehicle-specific); upper limit per road type | §5.3.7.4.3/4: assistance only within designed speed range; shall not exceed country's max speed limit | Aligned | Low | — |
| 5.2 | Speed limit compliance | Speed Limit function required; visual display of detected speed limit | §5.3.7.4.1–4.11: shall determine permitted speed; continuously display system-determined speed limit; auto-control to not exceed | **Partial** | Med | EU adds: shall not allow driver to set default offset above speed limit (§5.3.7.4.9). China ADRS does not have this prohibition. |
| 5.3 | Approaching system boundary notification | System exits/standby when ODD exceeded | §5.3.5.5: when approaching system boundary in active mode, inform driver with sufficient lead time to respond | **Partial** | Med | China addresses exit; EU additionally requires proactive advance warning before the boundary is reached. |
| 5.4 | Rapid oscillation between standby/active | Not addressed | §5.3.5.1.1: system shall aim to avoid rapid fluctuations between standby and active modes | **Missing** | Low | Stability of mode transitions not addressed in China ADRS. |
| 5.5 | Boundary detection transparency | Not specified | §5.3.5.3/5.4: manufacturer shall identify which boundaries are detectable; non-detectable boundaries must be justified | **Missing** | Med | EU requires documentation of which ODD boundaries the system can and cannot detect. Relevant for type approval documentation. |
| 5.6 | Road without lane marking | Not addressed (GB requires marked lanes) | §6.1.4: if designed for roads without lane markings, other info sources must be used for trajectory | **Partial** | Low | Not a gap for type approval if declared ODD excludes unmarked roads. Must be explicitly declared. |
| 5.7 | Emergency corridor formation | Not addressed | §6.1.3: if capable, system shall only leave lane where required/allowed by national traffic rules; return to original lane after | **Missing** | Low | Feature-specific. Only relevant if G1.3 EU implements emergency corridor. Declare as out-of-scope or implement per §6.1.3. |
| 5.8 | Headway assistance | Safe following distance maintained | §5.3.7.5: system shall support driver in complying with regulatorily defined headway; for M1/N1: permanently indicate headway setting, OR warn if headway <2s on first activation | **Partial** | Med | EU adds explicit first-activation headway notification if set <2s. China ADRS does not have this. |

---

### 6. Misuse Prevention

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 6.1 | System disable after repeated disengagement | 系统禁用 ADRS: disable for 30 min after: 1 RMF, or 2 escalated DCAs after EOR, or 3 escalated HOR/EOR in 30 min, or 10s continuous escalated HOR/DCA | §5.5.4.2.8.1: manufacturer shall implement strategies to disable activation for the run cycle when prolonged insufficient engagement leads to >1 driver unavailability response | **Conflict** | High | China: detailed quantitative triggers, 30-min disable. EU: principle-based — disable for run cycle after >1 RMF. EU does not specify 30 min; it requires run-cycle disable. China's 30-min may be shorter than EU's run-cycle requirement depending on context. |
| 6.2 | Disable HMI: instruction to read manual | 系统禁用 ADRS: HMI shall prompt driver to read and understand system usage instructions | §5.5.4.2.8.1: strategies to disable (no specific HMI requirement on content) | **More Strict in CN** | Low | China more explicit on HMI content post-disable. EU leaves to manufacturer. No negative gap. |
| 6.3 | Hardware/software tampering prevention | Not specified | §5.1.3: system shall guard against reasonably foreseeable misuse AND unauthorized modification of software/hardware | **Missing** | Med | EU requires explicit cybersecurity/tamper-resistance consideration for DCAS. China ADRS does not address this. |
| 6.4 | Driver information materials | Product description (产品说明 ADRS) | §5.6: mandatory content list including: driver responsibilities, system capabilities/limits, boundaries, modes, privacy management, override instructions, HMI details | **Partial** | Med | EU §5.6(h) requires Privacy Management explanation — China ADRS does not have this. Also EU requires content to not mislead about automation level. |

---

### 7. HMI Interaction

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 7.1 | Mode state machine | Active / standby / off (implied) | §5.5.1/5.5.2.1: off / on / standby / active — formal 4-state model; features may be in standby while system is in on | **Partial** | Med | EU defines a formal 4-state model (off/on/standby/active). China ADRS does not explicitly define all 4 states. Mode awareness documentation requirement for type approval. |
| 7.2 | System status display | Active state displayed; mode transitions signaled | §5.5.4.1.1: shall inform driver of: system status, ongoing manoeuvre, required driver action, reached/approaching boundary, failures, intended manoeuvres | Aligned | Low | Scope of status display aligned. |
| 7.3 | DCAS status distinguishable from ADS | Not addressed (no ADS on G1.3) | §5.5.4.1.7: system status shall be unambiguously distinguishable from ADS status indication | N/A | Low | Not applicable for G1.3 (no ADS). But must be addressed if future variants include ADS. |
| 7.4 | HMI control identification | Not specified | §5.5.2.4.1: DCAS controls shall be clearly identified and distinguishable (size, form, colour, type, action, spacing) | **Missing** | Med | EU requires physical/visual differentiation of DCAS controls. China ADRS does not specify this. |
| 7.5 | Mode confusion prevention | Not specified | §5.5.2.4: HMI shall be designed to not cause mode confusion with other vehicle systems | **Missing** | Med | Relevant for G1.3 which has multiple ADAS features coexisting. |
| 7.6 | Driver-confirmed manoeuvre HMI | Lane change: system proposes, driver confirms via turn signal | §5.5.4.1.8/5.3.7.2.3.2: system shall visually inform of proposed manoeuvre; driver given sufficient time to confirm; specific signal for confirmation request | Aligned | Low | — |
| 7.7 | System-initiated manoeuvre advance notice | Not specified for system-initiated | §5.5.4.1.9.1: information shall be provided at least 3s ahead of relevant intended manoeuvre where possible | **Missing** | Low | Only relevant if system-initiated lane changes are implemented. |
| 7.8 | Failure indication when not in off-mode | HMI fault display present | §5.4.2.2: failure shall be indicated with at least optical signal unless system is in off mode | Aligned | Low | — |
| 7.9 | Remaining features indication after partial failure | Not specified | §5.4.4.1: remaining available features (or absence thereof) shall be visually indicated in easily understandable manner | **Missing** | Med | EU requires partial-failure HMI showing which features remain. China ADRS does not specify this level of detail. |

---

### 8. Fallback / Failsafe

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 8.1 | Graceful degradation on failure | ODC failsafe: system safe stop on failure | §5.4.2: control assistance shall be terminated safely; shall gradually reduce if safe to do so | Aligned | Low | — |
| 8.2 | Whole-system failure → off mode | System deactivates on critical failure | §5.4.2.1: if failure affects entire system, switch to off mode upon termination; optical failure warning for appropriate duration | Aligned | Low | — |
| 8.3 | Partial failure: feature-level degradation | Not explicitly defined | §5.4.4: if failure only affects some features, system may continue with remaining features | **Missing** | Med | EU allows and defines partial-failure continued operation. China ADRS does not specify this feature-level resilience strategy. |
| 8.4 | No auto-resume after AEBS intervention standstill | Not specified | §5.5.3.3.4: system shall not resume longitudinal control without driver input if vehicle comes to standstill following AEBS intervention | **Missing** | High | After emergency braking brings vehicle to stop, EU prohibits automatic resumption of longitudinal control. China ADRS does not address this. |
| 8.5 | Mandatory AEBS + LDWS/LDPS baseline | Not explicitly referenced | §5.1.5: DCAS-equipped vehicle shall have AEBS (R.131/R.152) and LDWS or LDPS (R.130/R.79) | **Partial** | Med | G1.3 likely has AEBS. EU type approval requires formal compliance declarations for all three underlying systems. |
| 8.6 | No AEBS suppression during DCAS active | ODC failsafe addresses | §5.2.1: DCAS shall not deactivate or suppress longitudinal functionality of AEBS while in active mode | Aligned | Low | — |
| 8.7 | Controllability of decel/accel during system actions | Not specified quantitatively | §5.3.6.3.1: deceleration and acceleration shall remain manageable for driver and surrounding traffic unless higher decel needed for safety | **Missing** | Med | EU requires controllability of longitudinal dynamics. China ADRS has no equivalent comfort/controllability constraint. |

---

### 9. Lane Change Behavior

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 9.1 | Lateral acceleration during lane change | Not specified | §6.2.3: lateral accel ≤ 1.5 m/s² (beyond curvature); total ≤ 3.5 m/s²; lateral jerk moving avg ≤ 5 m/s³ | **Missing** | High | EU defines specific quantitative limits for lateral dynamics during lane change. China ADRS has no equivalent. |
| 9.2 | Direction indicator requirement | Not specified in ADRS | §6.2.6: system shall generate direction indicator signal; active throughout entire lane change; deactivated by system after | **Missing** | Med | EU mandates system-controlled direction indicator. China ADRS does not address this. |
| 9.3 | Indicator advance notice to other road users | Not specified | §6.2.7: lane change indicated to other road users at least 3s before start of manoeuvre | **Missing** | Med | 3-second advance indicator requirement. No China equivalent. |
| 9.4 | Target lane safety assessment | System checks target lane before lane change | §6.2.4: approaching vehicle shall not be forced to decelerate >3 m/s² at A seconds after start; specific formula with detection range | **Partial** | Med | China checks target lane is clear. EU defines specific quantitative safety criterion for approaching vehicle deceleration impact. |
| 9.5 | Max time from initiation to start of manoeuvre | Not specified | §6.2.9.5: only permitted to extend beyond 7s where not in violation of national traffic rules | **Missing** | Low | EU caps the waiting time for lane change initiation at 7s. China ADRS does not specify. |
| 9.6 | No lane change against opposing traffic | Implied | §6.2.2: lane change shall not be performed towards lane intended for traffic moving in opposite direction | Aligned | Low | — |
| 9.7 | Lane change suppression notification | Not specified | §6.2.8: if lane change suppressed by system, inform driver with optical + acoustic/haptic | **Missing** | Low | When system decides not to perform a requested lane change, EU requires explicit driver notification. |
| 9.8 | No lane change during disengagement warning | Not addressed | §5.3.7.2.1.3: manoeuvre shall not be initiated if disengagement warning is active | **Missing** | High | See also 4.10. Architecturally important: lane change must be blocked when any warning is active. |
| 9.9 | Lane change near pedestrians/cyclists | Not addressed | §6.2.9.4: only permitted if system able to avoid causing risk of collision with vulnerable road users | **Missing** | Med | China ADRS does not address VRU detection as precondition for lane change. |
| 9.10 | Deceleration during lane change limited | Not specified | §6.2.4.3: deceleration during lane change ≤ 2 m/s² (except for imminent collision avoidance) | **Missing** | Med | EU limits deceleration during lane change to protect trailing vehicles. |

---

### 10. Data Recording & Diagnostics

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 10.1 | Safety-critical occurrence notification to TA | Not in ADRS scope | §7.2.1.1: manufacturer shall notify Type Approval Authority as soon as practical about safety-critical occurrences when system was in 'on' mode or within last 5s | **Missing** | Med | EU requires OEM-to-type-approval-authority reporting chain. China ADRS does not address post-market surveillance reporting. |
| 10.2 | Periodic annual reporting | Not in ADRS scope | §7.2.3.1: annual report to TA including: safety-critical occurrences, active mode distance, RMF events, system-initiated deactivations, % distance with driver-set speed > system-determined speed | **Missing** | Med | Ongoing compliance obligation. No China equivalent in ADRS. |
| 10.3 | DCAS monitoring program | Not in ADRS scope | §7.1.2: manufacturer shall set up monitoring program for in-service safety performance | **Missing** | Med | Requires field monitoring infrastructure. |
| 10.4 | Software identification (R171SWIN) | Software version tracking (general) | §10: R171SWIN (specific software identification number for DCAS); means to read it shall be declared | **Missing** | Med | EU requires a dedicated DCAS software identification mechanism (R171SWIN), analogous to RXSWIN in R157. China ADRS has no equivalent. |
| 10.5 | DETA database upload | Not applicable | §7.2.2.2: Type Approval Authority uploads remedial action info to UNECE DETA database | N/A | Low | OEM action triggers TA action; not directly an OEM system requirement. |

---

## Summary: Risk-Ranked Gap List

### High Risk (must resolve before EU type approval)

| # | Gap | Relevant R.171 §|
|---|---|---|
| H1 | Lateral override force ≤ 50 N not implemented | §5.5.3.4.1.4 |
| H2 | DMS unavailability → no lane departure constraint missing | §5.5.4.2.1.2 |
| H3 | No auto-transition prohibition after driver turns off DCAS | §5.5.2.2 |
| H4 | Lateral control shall not terminate while driver is motorically disengaged (during override) | §5.5.3.4.1.5 |
| H5 | RMF must be capable of lane change if system has lane change feature | §5.3.7.3.2 |
| H6 | System disable: CN triggers 30 min disable; EU requires run-cycle disable (may be longer) | §5.5.4.2.8.1 |
| H7 | No auto-resume longitudinal control after AEBS stops vehicle | §5.5.3.3.4 |
| H8 | Lane change blocked when any disengagement warning is active | §5.3.7.2.1.3 |
| H9 | Quantitative lateral acceleration limits during lane change (1.5/3.5 m/s², 5 m/s³ jerk) | §6.2.3 |

### Medium Risk (requires adaptation or documentation)

| # | Gap | Relevant R.171 §|
|---|---|---|
| M1 | Re-engagement minimum duration (≥200ms) not specified | §5.5.4.2.5.2.1 |
| M2 | Multiple short gaze aversion strategy not defined | §5.5.4.2.5.3 |
| M3 | Dashboard explicitly excluded from driving-task-relevant area | §5.5.4.2.5.2 |
| M4 | Brake override auto-resume exception (≤30 km/h / 2s) | §5.5.3.4.1.1.1 |
| M5 | Speed limit: driver cannot set default offset above detected limit | §5.3.7.4.9 |
| M6 | Proactive advance warning when approaching system boundary | §5.3.5.5 |
| M7 | Headway first-activation notification if set < 2s | §5.3.7.5.1.1.2 |
| M8 | Hardware/software tampering prevention (cybersecurity) | §5.1.3 |
| M9 | Privacy management content in user materials | §5.6(h) |
| M10 | DCAS controls physically distinguishable | §5.5.2.4.1 |
| M11 | Mode confusion prevention (HMI design principle) | §5.5.2.4 |
| M12 | Partial-failure feature-level HMI indication | §5.4.4.1 |
| M13 | Controllability of decel/accel (manageable for driver) | §5.3.6.3.1 |
| M14 | Direction indicator system-generated and held throughout lane change | §6.2.6 |
| M15 | 3-second advance indicator before lane change | §6.2.7 |
| M16 | Quantitative target lane safety criterion for approaching vehicle | §6.2.4 |
| M17 | Lane change suppression notification to driver | §6.2.8 |
| M18 | 7-second max from lane change initiation to start | §6.2.9.5 |
| M19 | VRU detection as precondition for lane change | §6.2.9.4 |
| M20 | Deceleration during lane change ≤ 2 m/s² | §6.2.4.3 |
| M21 | Feature-level partial failure continued operation strategy | §5.4.4 |
| M22 | Post-market surveillance: safety-critical occurrence reporting | §7.2.1 |
| M23 | Annual reporting to Type Approval Authority | §7.2.3 |
| M24 | In-service monitoring program | §7.1 |
| M25 | R171SWIN software identification | §10 |
| M26 | Formal AEBS + LDWS/LDPS compliance declaration | §5.1.5 |

### Low Risk / Aligned / N/A

- System activation/deactivation logic: largely aligned
- HOR/EOR/DCA warning timing: aligned (minor escalation timing difference)
- Warning signal modalities: aligned
- RMF general trigger: aligned
- No lane change against opposing traffic: aligned
- AEBS non-suppression during active mode: aligned
- Graceful degradation on failure: aligned

---

## Key Architectural Implications for G1.3 EU Adaptation

1. **Driver Override Torque Limit**: Steering system must be validated to ensure override effort ≤ 50 N. This requires HW/SW-level torque control verification.

2. **DMS Failure → Lateral Constraint**: When eye-gaze detection fails, the system architecture must prevent lane departures (not just warn). This may require a mode that constrains lateral authority.

3. **RMF + Lane Change Integration**: If the EU variant includes driver-confirmed lane change, the RMF module must be extended to include autonomous lane changes towards emergency/slow lanes on highways.

4. **Disable Duration**: China's 30-min disable needs to be re-evaluated against EU's run-cycle requirement. If a run cycle is <30 min, the EU requirement is actually less strict; if >30 min, it is stricter.

5. **Post-Market Surveillance Infrastructure**: EU R.171 requires an OEM-level monitoring program + annual reporting + DETA notifications. This is a product-lifecycle obligation, not just a type-approval one.

6. **Lane Change Dynamics**: The quantitative limits (lateral accel, jerk, decel) require engineering validation and may require test track verification as part of Annex 4.

---

*Analysis based on: CN L2GB ADRS Feishu wiki (11 topics), UN R.171 S2 (ECE/TRANS/WP.29/2025/65), UN R.79 04 series S6.*  
*Next step: Cross-reference with Euro NCAP Assisted Driving 2024/2025 protocol for NCAP-specific requirements beyond type approval.*
