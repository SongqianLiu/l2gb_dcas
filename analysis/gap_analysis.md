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
| 1.4 | No auto-transition to sustained L/L control after driver turns off | GB draft §4.8.1.1.4: "驾驶员...使系统进入关闭状态后应不自动激活任何部分驾驶辅助系统" | §5.5.2.2: when system switched to off, no automatic transition to any system providing continuous lon/lat movement | **Traceability / Validation Gap** | Med | CN and EU substantively aligned at regulation level. Remaining risk: ADRS traceability and software state machine validation. |
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
| 2.6 | DMS unavailability → no lane departure | GB draft §4.8.3.1.1.3: "若系统确认视线脱离检测处于不可用状态，则系统应不通过非车道巡航控制功能使车辆离开本车道" | §5.5.4.2.1.2: if visual disengagement detection temporarily unavailable, system shall not lead vehicle to leave current lane | **Traceability / Validation Gap** | Med | CN and EU substantively aligned at regulation level. Remaining risk: ADRS traceability, software implementation, and validation evidence. |
| 2.7 | DMS occlusion test | 9.4.9.6.4: occlusion test, EOR within 5s | R.171 §5.5.4.2: strategy documented and demonstrated; Annex 4 tests | Partial | Low | China has specific test; EU defers to manufacturer safety concept + Annex 4. Outcome-equivalent but documentation requirements differ. |

---

### 3. Driver Override

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 3.1 | Lateral override force limit | GB draft §4.8.2.7: ≤50 N applies to ALL driver lateral interventions (including minor corrections). CN is stricter than EU on scope. ADRS/EPS/software/test traceability not yet confirmed. | §5.5.3.4.1.4: ≤50 N applies to override only; minor corrections permitted without force constraint | **Traceability / Validation Gap** | Med | CN stricter: §4.8.2.7 bounds all interventions; EU only bounds full override. Satisfying CN automatically satisfies EU. Remaining risk: ADRS traceability, EPS calibration, software override logic, and physical test measurement. |
| 3.2 | Override: system may remain active | Implied (system stays active during temporary driver input) | §5.5.3.4.1: system may remain in active mode, priority given to driver input during overriding period | Aligned | Low | — |
| 3.3 | Longitudinal override: hard braking | Driver braking overrides longitudinal assist | §5.5.3.4.1.1: driver brake input > system deceleration overrides and suspends longitudinal control | Aligned | Low | — |
| 3.4 | Longitudinal resume after brake override | Resumes on driver action | §5.5.3.4.1.1.1: shall not resume lon. control without separate driver action; exception: speed reduction ≤30 km/h within 2s | **Partial** | Med | EU defines a specific exception (≤30 km/h / 2s) for minor brake inputs that allows auto-resume. China ADRS does not address this edge case. |
| 3.5 | Lateral override not to terminate during motoric disengagement | Not found in CN GB draft — GB §4.8.2.8 addresses override termination but does not constrain based on HOD state | §5.5.3.4.1.5: shall not terminate lateral control while driver is detected to be motorically disengaged (controllability during override) | **Missing** | High | Confirmed true regulatory gap. No CN equivalent found. EU prevents the dangerous scenario where override detection causes lateral control to suddenly stop while the driver's hands are off the wheel. |
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
| 4.11 | RMF lane change capability | GB draft §4.6.3.1.1: "若系统具有驾驶员确认的换道控制功能或系统触发的换道控制功能，则RMF应至少具有在A类道路环境下执行换道控制的能力。" Target areas include 应急车道/硬路肩 (§4.6.3.1.2) | §5.3.7.3.2: if system has driver-confirmed/system-initiated lane change, RMF shall be capable of lane changes to reach target stop area (emergency lane) on highway | **Traceability / Validation Gap** | Med | CN and EU substantively aligned. Remaining risk: confirm G1.3 RMF module actually implements lane change to emergency lane; confirm GB §9.4.10.2.2 test result is applicable to EU validation. |

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
| 6.1 | System disable after repeated disengagement | GB draft §8.1: "被禁用不少于30 min" within current ignition cycle, triggered by: 1 RMF, 2 escalated DCAs after EOR, 3 escalated HOR/EOR in 30 min, or 10s continuous escalated HOR/DCA | §5.5.4.2.8.1: manufacturer shall implement strategies to disable activation for the run cycle when prolonged insufficient engagement leads to >1 driver unavailability response | **Conflict** | High | Confirmed conflict: CN specifies ≥30-min timer, allowing system re-enable within the same run cycle for long trips. EU requires disable for the entire remaining run cycle. On a 2-hour motorway trip, CN allows re-enable after 30 min; EU does not. Requires software architecture change for EU variant. |
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
| 8.4 | No auto-resume after AEBS intervention standstill | GB draft §4.8.1.3.3: "若在应急辅助功能（例如，AEBS）介入控制后导致车辆静止，在没有驾驶员人工操作的情况下，系统应不恢复纵向运动控制" | §5.5.3.3.4: system shall not resume longitudinal control without driver input if vehicle comes to standstill following AEBS intervention | **Traceability / Validation Gap** | Med | CN and EU are directly equivalent. Remaining risk: ADRS traceability and software state machine validation. |
| 8.5 | Mandatory AEBS + LDWS/LDPS baseline | Not explicitly referenced | §5.1.5: DCAS-equipped vehicle shall have AEBS (R.131/R.152) and LDWS or LDPS (R.130/R.79) | **Partial** | Med | G1.3 likely has AEBS. EU type approval requires formal compliance declarations for all three underlying systems. |
| 8.6 | No AEBS suppression during DCAS active | ODC failsafe addresses | §5.2.1: DCAS shall not deactivate or suppress longitudinal functionality of AEBS while in active mode | Aligned | Low | — |
| 8.7 | Controllability of decel/accel during system actions | Not specified quantitatively | §5.3.6.3.1: deceleration and acceleration shall remain manageable for driver and surrounding traffic unless higher decel needed for safety | **Missing** | Med | EU requires controllability of longitudinal dynamics. China ADRS has no equivalent comfort/controllability constraint. |

---

### 9. Lane Change Behavior

| # | Topic | China L2GB | EU R.171 | Gap Type | Risk | Notes |
|---|---|---|---|---|---|---|
| 9.1 | Lateral acceleration during lane change | GB §4.6.2.2.1.8: total ≤ 3.5 m/s², jerk ≤ 5 m/s³; §4.6.2.2.1.9: straight-road ≤ 1.5 m/s²; §4.6.2.2.1.11: decel ≤ 2 m/s² | §6.2.3: lateral accel ≤ 1.5 m/s² (beyond curvature, all roads); total ≤ 3.5 m/s²; lateral jerk moving avg ≤ 5 m/s³ | **Partial** | Med | Straight-road values identical. Gap: EU §6.2.3's "beyond curvature" constraint applies on curved roads too (delta accel from lane change ≤ 1.5 m/s²), but CN §4.6.2.2.1.9 only constrains straight roads. Curved-road lane change delta-lateral-accel is only bounded by the 3.5 m/s² total in CN. |
| 9.2 | Direction indicator requirement | Not specified in ADRS | §6.2.6: system shall generate direction indicator signal; active throughout entire lane change; deactivated by system after | **Missing** | Med | EU mandates system-controlled direction indicator. China ADRS does not address this. |
| 9.3 | Indicator advance notice to other road users | Not specified | §6.2.7: lane change indicated to other road users at least 3s before start of manoeuvre | **Missing** | Med | 3-second advance indicator requirement. No China equivalent. |
| 9.4 | Target lane safety assessment | System checks target lane before lane change | §6.2.4: approaching vehicle shall not be forced to decelerate >3 m/s² at A seconds after start; specific formula with detection range | **Partial** | Med | China checks target lane is clear. EU defines specific quantitative safety criterion for approaching vehicle deceleration impact. |
| 9.5 | Max time from initiation to start of manoeuvre | Not specified | §6.2.9.5: only permitted to extend beyond 7s where not in violation of national traffic rules | **Missing** | Low | EU caps the waiting time for lane change initiation at 7s. China ADRS does not specify. |
| 9.6 | No lane change against opposing traffic | Implied | §6.2.2: lane change shall not be performed towards lane intended for traffic moving in opposite direction | Aligned | Low | — |
| 9.7 | Lane change suppression notification | Not specified | §6.2.8: if lane change suppressed by system, inform driver with optical + acoustic/haptic | **Missing** | Low | When system decides not to perform a requested lane change, EU requires explicit driver notification. |
| 9.8 | No lane change during disengagement warning | GB draft §6.x(e): "若系统正在发出驾驶员脱离提示或警告信号，不触发换道过程" | §5.3.7.2.1.3: manoeuvre shall not be initiated if disengagement warning is active | **Traceability / Validation Gap** | Med | CN and EU are equivalent. Remaining risk: ADRS traceability, software implementation, and test coverage. Note: RMF lane change is exempt (RMF operates specifically under driver unavailability). |
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

> **Note (2026-05-20 re-review):** After checking all gaps against the full CN GB draft text, original H1–H3, H5, H7–H9 were found to have substantively equivalent requirements in CN and reclassified to Medium (now M1–M7). Original H4 (no CN equivalent) and H6 (30-min vs. run-cycle conflict) remain High Risk, renumbered H1 and H2.

### High Risk (true regulatory gap or implementation conflict — must resolve before EU type approval)

| # | Gap | Relevant R.171 § | Status |
|---|---|---|---|
| **H1** | Lateral control shall not terminate while driver is motorically disengaged (during override) — no CN equivalent | §5.5.3.4.1.5 | Missing in CN |
| **H2** | System disable: CN ≥30 min timer (re-enableable within same run cycle); EU requires run-cycle disable — genuine conflict | §5.5.4.2.8.1 | Conflict |

### Medium Risk — Traceability / Validation Gaps (CN regulation aligned; implementation/evidence must be confirmed)

| # | Gap | Relevant R.171 § | CN Reference |
|---|---|---|---|
| **M1** | Lateral override force ≤ 50 N: ADRS/EPS/software/test traceability not confirmed (note: CN stricter — applies to all interventions) | §5.5.3.4.1.4 | GB §4.8.2.7 |
| **M2** | DMS unavailability → no lane departure: ADRS and validation evidence needed | §5.5.4.2.1.2 | GB §4.8.3.1.1.3 |
| **M3** | No auto-transition after driver turns off: ADRS and state machine validation needed | §5.5.2.2 | GB §4.8.1.1.4 |
| **M4** | RMF lane change capability: implementation and test evidence needed | §5.3.7.3.2 | GB §4.6.3.1.1 |
| **M5** | No auto-resume after AEBS standstill: ADRS and validation evidence needed | §5.5.3.3.4 | GB §4.8.1.3.3 |
| **M6** | Lane change blocked during disengagement warning: ADRS and test coverage needed | §5.3.7.2.1.3 | GB §6.x(e) |
| **M7** | Curved-road lane change: EU "beyond curvature" ≤ 1.5 m/s² not in CN for curved roads | §6.2.3 | GB §4.6.2.2.1.8/1.9 (straight-road only) |

### Medium Risk — Adaptation / Documentation Required

| # | Gap | Relevant R.171 § |
|---|---|---|
| **M8** | Re-engagement minimum duration (≥200 ms) not specified | §5.5.4.2.5.2.1 |
| **M9** | Multiple short gaze aversion strategy not defined | §5.5.4.2.5.3 |
| **M10** | Dashboard explicitly excluded from driving-task-relevant area | §5.5.4.2.5.2 |
| **M11** | Brake override auto-resume exception (≤30 km/h / 2s) | §5.5.3.4.1.1.1 |
| **M12** | Speed limit: driver cannot set default offset above detected limit | §5.3.7.4.9 |
| **M13** | Proactive advance warning when approaching system boundary | §5.3.5.5 |
| **M14** | Headway first-activation notification if set < 2s | §5.3.7.5.1.1.2 |
| **M15** | Hardware/software tampering prevention (cybersecurity) | §5.1.3 |
| **M16** | Privacy management content in user materials | §5.6(h) |
| **M17** | DCAS controls physically distinguishable | §5.5.2.4.1 |
| **M18** | Mode confusion prevention (HMI design principle) | §5.5.2.4 |
| **M19** | Partial-failure feature-level HMI indication | §5.4.4.1 |
| **M20** | Controllability of decel/accel (manageable for driver) | §5.3.6.3.1 |
| **M21** | Direction indicator system-generated and held throughout lane change | §6.2.6 |
| **M22** | 3-second advance indicator before lane change | §6.2.7 |
| **M23** | Quantitative target lane safety criterion for approaching vehicle | §6.2.4 |
| **M24** | Lane change suppression notification to driver | §6.2.8 |
| **M25** | 7-second max from lane change initiation to start | §6.2.9.5 |
| **M26** | VRU detection as precondition for lane change | §6.2.9.4 |
| **M27** | Deceleration during lane change ≤ 2 m/s² | §6.2.4.3 |
| **M28** | Feature-level partial failure continued operation strategy | §5.4.4 |
| **M29** | Post-market surveillance: safety-critical occurrence reporting | §7.2.1 |
| **M30** | Annual reporting to Type Approval Authority | §7.2.3 |
| **M31** | In-service monitoring program | §7.1 |
| **M32** | R171SWIN software identification | §10 |
| **M33** | Formal AEBS + LDWS/LDPS compliance declaration | §5.1.5 |

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

1. **Override Logic During Motoric Disengagement (H1 — True Gap)**: The DCAS software must not drop lateral control when override is detected while the driver's hands are still off the wheel. The override logic must require positive HOD confirmation before terminating lateral assistance. This is an architectural software change with no CN equivalent to guide from.

2. **System Disable: Run-Cycle vs. 30-Min (H2 — True Conflict)**: China's 30-min timer allows re-enable within the same run cycle. EU requires the system to stay disabled for the entire remaining run cycle. The EU variant requires a run-cycle disable flag (cleared only on power cycle), not a countdown timer.

3. **ADRS Traceability Chain (M1–M6)**: Many requirements exist in the CN GB draft but may not be explicitly cascaded into the ADRS. Before EU type approval, all six traceability gaps need to be verified: ADRS → software requirement → implementation → validation test → test result.

4. **Curved-Road Lane Change Control (M7)**: The lane change controller must limit the manoeuvre-induced lateral acceleration to ≤ 1.5 m/s² even on curved roads. A curvature-aware control strategy is needed. Straight-road lane change values are already aligned.

5. **Post-Market Surveillance Infrastructure**: EU R.171 requires an OEM-level monitoring program + annual reporting + DETA notifications. This is a product-lifecycle obligation, not just a type-approval one.

6. **ADRS Source vs. GB Standard**: The original ADRS Feishu summary pages do not fully reflect all requirements in the underlying GB standard. When reviewing compliance evidence, the full CN GB draft text should be the authoritative source, not the ADRS Feishu summaries alone.

---

*Analysis based on: CN L2GB ADRS Feishu wiki (11 topics), CN GB draft full text (智能网联汽车组合驾驶辅助系统安全要求，送审稿), UN R.171 S2 (ECE/TRANS/WP.29/2025/65), UN R.79 04 series S6.*  
*2026-05-20: All 9 original High Risk gaps re-examined against CN GB draft full text. Original H1–H3, H5, H7–H9 reclassified to Medium (now M1–M7). Original H4 and H6 confirmed High Risk, renumbered H1 and H2. All gaps renumbered: H1–H2 (high), M1–M33 (medium).*  
*Next step: Cross-reference with Euro NCAP Assisted Driving 2024/2025 protocol for NCAP-specific requirements beyond type approval.*
