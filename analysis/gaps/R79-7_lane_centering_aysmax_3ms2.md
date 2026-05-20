# R79-7 — Lane Centering Maximum Lateral Acceleration aysmax ≤ 3 m/s² (M1/N1)

| Field | Detail |
|---|---|
| **Risk Level** | Medium (R.79 stricter than CN L2GB for lane centering) |
| **R.79 Reference** | UN R.79 04 S6 §5.6.2.1.3 Table 1 |
| **R.171 Reference** | §6.2.3 (constrains lane change; does not set lane centering total limit) |
| **CN Reference** | GB draft §4.6.2.2.1.8 (total ≤ 3.5 m/s²) |
| **Gap Type** | R.79 stricter than L2GB for lane centering lateral acceleration ceiling |

---

## R.79 Requirement (§5.6.2.1.3 Table 1)

Table 1 specifies the maximum and minimum values for **aysmax** (the manufacturer-declared maximum lateral acceleration for ACSF operation) for M1/N1 vehicles:

| Speed Range | Maximum aysmax | Minimum aysmax |
|---|---|---|
| 10–60 km/h | **3 m/s²** | 0 m/s² |
| >60–100 km/h | **3 m/s²** | 0.5 m/s² |
| >100–130 km/h | **3 m/s²** | 0.8 m/s² |
| >130 km/h | **3 m/s²** | 0.3 m/s² |

The declared aysmax (total lateral acceleration during lane centering) shall not exceed **3 m/s²** at any speed for M1/N1 vehicles.

Additionally, §5.6.2.1.3 includes a transient exception:
> For time periods of not more than 2 s, the lateral acceleration may exceed aysmax by not more than 40%, while not exceeding the maximum value by more than 0.3 m/s².

So the transient hard ceiling is: 3 m/s² × 1.4 = 4.2 m/s², but also capped at 3 m/s² + 0.3 m/s² = 3.3 m/s². The effective transient ceiling is **3.3 m/s²** for ≤2 s.

---

## CN L2GB Status

**CN GB §4.6.2.2.1.8**: 

> 系统在M1、N1类车辆上进行的换道控制所产生的横向加速度不应超过3.5 m/s²

Translation: Total lateral acceleration during lane change on M1/N1 vehicles shall not exceed **3.5 m/s²**.

**CN allows 3.5 m/s² total** — 0.5 m/s² more than R.79's 3 m/s² cap for lane centering.

Note: §4.6.2.2.1.8 refers to lane changes specifically. R.79 Table 1 aysmax applies to the overall ACSF lateral acceleration envelope, which includes both lane centering (B1/B2) and lane change (Cat C) operations.

---

## Practical Implication

If G1.3 is currently tuned to allow up to 3.5 m/s² total lateral acceleration (matching CN §4.6.2.2.1.8), this would fail R.79 Table 1. The EU variant must limit total lateral acceleration to ≤3 m/s² for both lane centering and lane change manoeuvres.

Combined with R79-1 (≤1 m/s² beyond curvature for lane change), the EU lane change controller must satisfy:
- Total lateral acceleration ≤ 3.0 m/s² (R.79 Table 1)
- Beyond-curvature component ≤ 1.0 m/s² (R.79 §5.6.4.4)

---

## Required Closure Actions

1. Confirm G1.3 current aysmax tuning: what is the maximum lateral acceleration the lane centering controller commands?
2. If aysmax > 3 m/s²: retune the EU variant lateral acceleration limit to ≤3 m/s² steady-state, ≤3.3 m/s² transient (≤2 s)
3. Document the declared aysmax value per speed range for the R.79 type approval submission
4. Validate: measure peak lateral acceleration during lane centering at various speeds → confirm ≤3 m/s² (steady) / ≤3.3 m/s² (≤2 s transient)
5. Add ADRS requirement: "Lane centering (B1/B2) maximum lateral acceleration shall not exceed aysmax = 3 m/s² for M1/N1 (R.79 §5.6.2.1.3 Table 1)"
