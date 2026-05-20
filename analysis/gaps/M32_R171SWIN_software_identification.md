# M32 — R171SWIN Software Identification Number

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing in CN — EU-specific regulatory mechanism) |
| **EU Reference** | UN R.171 S2 §10 |
| **CN Reference** | Not found in GB draft |
| **Gap Type** | Missing in CN (EU-specific) |

---

## EU Requirement (R.171 §10)

> The DCAS system software shall be identified by a unique R171SWIN (R.171 Software Identification Number). The R171SWIN shall:
> - Uniquely identify the approved DCAS software version
> - Be readable from a standardized diagnostic interface (OBD/OBD-II)
> - Be updated and re-submitted for TA notification whenever the software is updated in a way that affects DCAS function

The R171SWIN is analogous to RXSWIN in R.157 (ALKS). It allows enforcement authorities to verify that a vehicle carries type-approved DCAS software.

---

## China L2GB Status

The CN GB draft does not require an equivalent software identification number for L2GB DCAS. CN vehicle software management is addressed by separate standards (GB/T 39003 for OBD, GB/T 32960 for remote diagnostics) but without a DCAS-specific software identification requirement analogous to R171SWIN.

**This mechanism is not found in the CN L2GB standard.** It is an EU-specific regulatory traceability tool.

---

## Implementation Requirements

1. **Define SWIN scope**: determine which software components (sensor fusion, control logic, HMI, DMS) are within the R171SWIN scope
2. **Assign initial SWIN**: create a unique identifier for the approved G1.3 EU DCAS software configuration
3. **OBD readout**: implement the R171SWIN in the OBD/diagnostic identifier registers (readable via ISO 14229 / UDS service 0x22)
4. **Update procedure**: define the process for updating the SWIN when DCAS software changes require TA re-notification
5. **TA notification**: establish the procedure for notifying the EU TA of SWIN changes and determining whether re-approval is required

---

## Required Closure Actions

1. Define the G1.3 R171SWIN format and assign the initial identifier
2. Implement R171SWIN readout via OBD diagnostic interface
3. Document the SWIN management process (update triggers, TA notification thresholds)
4. Include R171SWIN in the EU type approval submission documentation
5. Train the homologation and software release teams on R171SWIN update obligations

---

## Open Questions

1. Does NIO already have an RXSWIN for R.157 (if G1.3 has ALKS features)? The R171SWIN can follow the same architecture
2. What is the versioning scheme: will the SWIN be updated for every DCAS OTA update, or only for changes affecting approved performance?
