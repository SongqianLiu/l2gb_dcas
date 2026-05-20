# M16 — Privacy Management Information in User Materials

| Field | Detail |
|---|---|
| **Risk Level** | Medium (Missing in CN) |
| **EU Reference** | UN R.171 S2 §5.6(h) |
| **CN Reference** | Not found in GB draft |
| **Gap Type** | Missing in CN |

---

## EU Requirement (R.171 §5.6(h))

> The owner's manual shall contain information about: (h) privacy management, including what data is collected, how long it is retained, and how it can be deleted.

EU §5.6 specifies a mandatory list of items that must appear in the owner's manual / user documentation, including a dedicated privacy management section covering:
- What personal and driving data is collected
- Retention periods for each data category
- How the user can request deletion of stored data

---

## China L2GB Status

The CN GB draft §4.1.9 specifies requirements for user information/manual content:

> 产品使用说明书应向驾驶员说明...系统的激活和停用方式，各种驾驶模式的转换方式，以及...

CN §4.1.9 covers activation/deactivation, mode transitions, and operational guidance, but does **not** include a requirement to document privacy management (data collection, retention, deletion rights).

Data privacy for Chinese vehicles is addressed by separate legislation (Personal Information Protection Law / PIPL, and GB/T 35273 personal information security), but these are not reflected as specific owner's manual content requirements within the L2GB DCAS standard.

**This requirement is missing from the CN GB draft.** It is an EU-specific documentation requirement driven by GDPR and ECE consumer protection frameworks.

---

## Risk Assessment

For EU type approval and market entry, the G1.3 owner's manual must include a privacy section meeting §5.6(h). This is a documentation deliverable, not a software change, but it requires:
1. Legal review of what data G1.3 DCAS collects and for how long
2. User-facing documentation describing data collection scope and deletion procedures
3. Alignment with GDPR Article 13/14 (information to be provided where personal data is collected)

---

## Required Closure Actions

1. Inventory all data collected by G1.3 DCAS: driving logs, DMS images, radar/camera data, event data records
2. Document retention periods for each data category (distinguish: on-vehicle storage vs. cloud)
3. Document the user's rights: how to access, export, or delete stored personal data
4. Add a privacy management section to the EU variant owner's manual covering items (1)–(3) above
5. Coordinate with NIO legal/privacy team to ensure GDPR compliance of the EU privacy statement
