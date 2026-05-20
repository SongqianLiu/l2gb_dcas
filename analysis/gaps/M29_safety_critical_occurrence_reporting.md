# M29 — Safety-Critical Occurrence Reporting

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing in CN — EU-specific regulatory obligation) |
| **EU Reference** | UN R.171 S2 §7.2.1 |
| **CN Reference** | Not found in GB draft |
| **Gap Type** | Missing in CN (EU-specific post-market surveillance) |

---

## EU Requirement (R.171 §7.2.1)

> The manufacturer shall report to the Type Approval Authority any safety-critical occurrences involving the DCAS system, including incidents leading to injury, death, or significant property damage attributable to DCAS system behavior. Reports shall be submitted within the timeframes specified by the TA.

This is a post-market surveillance obligation — it applies after type approval is granted and the vehicle is on the market.

---

## China L2GB Status

The CN GB draft does not contain an equivalent mandatory safety-critical occurrence reporting requirement for L2GB DCAS systems.

China has a separate automotive recall and defect reporting system under the **缺陷汽车产品召回管理条例** (Defective Motor Vehicle Recall Regulations), which covers field defects requiring recall. However, this is a general product safety law, not a DCAS-specific incident reporting obligation.

**This specific post-market DCAS incident reporting requirement is not found in the CN L2GB standard.** It is an EU-specific regulatory obligation that will apply to all vehicles receiving R.171 type approval.

---

## Required Closure Actions

1. Identify the EU Type Approval Authority that NIO will submit G1.3 to (likely a designated European technical service — e.g., TÜV, UTAC, Applus+)
2. Establish a DCAS incident monitoring and reporting process for EU-market G1.3 vehicles
3. Define "safety-critical occurrence" thresholds for reporting (injury, death, significant property damage involving DCAS)
4. Implement a data collection pipeline: identify which on-vehicle data (EDR, DCAS event log) will be preserved for incident investigation
5. Assign organizational responsibility for monitoring, investigating, and reporting incidents to the EU TA
6. Document the reporting process in the EU type approval submission (§7.2.1 compliance declaration)
