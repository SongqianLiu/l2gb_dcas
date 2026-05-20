# M15 — Hardware/Software Tampering Prevention

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing at system level in CN) |
| **EU Reference** | UN R.171 S2 §5.1.3 |
| **CN Reference** | Not found at system level in GB draft |
| **Gap Type** | Missing in CN (system-level requirement) |

---

## EU Requirement (R.171 §5.1.3)

> The system shall be designed and constructed to resist tampering with its hardware and software components, such that performance cannot be degraded below the requirements of this Regulation by deliberate or accidental modification.

The requirement covers both hardware (physical access to ECUs, sensors) and software (unauthorized firmware changes) tampering.

---

## China L2GB Status

The CN GB draft does not contain an equivalent system-level anti-tampering requirement for the DCAS system itself.

CN does address related topics at the process level:
- **GB/T 38628** (network security): covers cybersecurity for connected vehicle communication
- **GB/T 44464** (data security): covers data protection requirements
- **GB/T 18232** (general type approval): may include general product integrity requirements

However, the GB draft for combined driving assistance (L2GB) does not include a dedicated clause requiring the system to resist deliberate or accidental tampering with its DCAS hardware/software components.

**This specific system-level requirement is missing from the CN L2GB standard.** The gap is that R.171 requires the DCAS type-approval submission to explicitly address tampering resistance, while CN does not impose this requirement within the DCAS standard.

---

## Risk Assessment

For EU type approval, the technical service will expect evidence that:
1. DCAS ECU hardware is protected against physical tampering (e.g., tamper-evident seals, secure enclosures)
2. DCAS software cannot be modified without detection (e.g., secure boot, code signing)
3. The system fails safe if tampering is detected

This is a documentation and architecture gap for the EU submission — G1.3 may already implement these measures for cybersecurity reasons, but they must be formally documented and linked to R.171 §5.1.3.

---

## Required Closure Actions

1. Review G1.3 cybersecurity architecture: what tampering-prevention mechanisms are already in place for DCAS ECU(s)?
2. Document anti-tampering measures in the EU type approval submission: secure boot, code signing, hardware security modules, physical access protection
3. Add ADRS requirement referencing R.171 §5.1.3 for the EU variant
4. Confirm alignment with UN R.155 (cybersecurity) — many EU OEMs satisfy R.171 §5.1.3 by referencing their R.155 CSMS (Cybersecurity Management System) approval

---

## Open Questions

1. Does G1.3 have an existing UN R.155 type approval or CSMS certification? If yes, that likely satisfies most of §5.1.3
2. Is there a separate Chinese cybersecurity standard (GB/T 38628) approval that covers equivalent content?
