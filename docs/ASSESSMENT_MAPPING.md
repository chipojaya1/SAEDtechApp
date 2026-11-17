# Form-to-dashboard mapping (concept only)

## Core distinction

The **School Assessment** documents school conditions, needs and eight provisional ratings. The **School Evaluation** covers 14 VF conditions within three sections and is **not** itself an approved compliance decision. The two instruments should share a verified school key *only after* the local programme approves the registry and permissions. Keep separate record dates, versions, evidentiary standards and review states.

## School Assessment: eight criteria

| Criterion | Intended evidence (from reviewed XLSForm) | Possible role-level use | Do not infer |
|---|---|---|---|
| 1. Infrastructure | Classroom availability, roof/wall/floor/window condition, toilets and water | School: update issues; Office: review defect descriptions; Province/National: coverage and trends | Certified building safety or approved score |
| 2. Equipment and materials | Category-level inventory totals, usable/repairable/unrepairable counts, instructional materials | School: record resources; Office: check arithmetic; Province: needs summary | Verified physical inventory or procurement approval |
| 3. Enrolment/capacity | Counts, attendance, capacity, trends | School/office trends; aggregate only if denominator validated | True attendance rate without approved period/definition |
| 4. Access and alternatives | Nearby schools, distance/walking time and context | Local access planning | Quality ranking of neighboring schools |
| 5. Governance | Administrative roles and records | Identify missing management information | Legal compliance |
| 6. Community involvement | Committee and family participation | School / office support planning | Representativeness without further review |
| 7. School fees | Fee policy and payment information | Contextual sustainability review | Household wealth, hardship or sanctions |
| 8. External support | Assistance sources and observations | Planning and coordination | Complete verified funding dataset |

All eight provisional ratings are **human assessor entries**; weighted rollups remain unapproved.

## School Evaluation: 14 VF conditions

| Section | Covered areas | Intended role-level use |
|---|---|---|
| A. Governance and Compliance | Legal registration, minimum standards, governance structure, financial stability | Restricted review with evidence provenance; local standards must be approved |
| B. Monitoring and Protection | THQ monitoring, trained personnel, child protection, effectiveness measurement, risk management | Restricted authorized workflow; do not surface sensitive case details on dashboards |
| C. Mission and Faith Integration | Faith-based orientation, spiritual care, institutional integration, family proximity, vulnerable populations | Appropriate institution-level review with explicit access policies |

The XLSForm is marked **SAMPLE / NOT APPROVED**. Do not label responses as approved compliance determinations or combine them mechanically with the eight Criterion 1–8 ratings.

## One shared record, four views — data flow concept

```text
Approved School Register (stable internal school ID)
       │
       ├── School Assessment (eight criteria; repeat inventories)
       │
       └── School Evaluation (14 conditions; restricted review as needed)
       │
   Submission provenance + version + authorized review trail
       │
       ├── School: own tasks and records
       ├── Sub-provincial office: assigned schools and corrections
       ├── Province: aggregate completeness and support needs
       └── National: aggregated coverage / quality, no sensitive person-level details
```

## Rules before any metrics appear

- Define numerator, denominator, reporting period and the meaning of missing / zero / unknown.
- Keep preliminary, returned, approved and overdue states separate.
- Never describe a prototype's example numbers as current observations.
- Do not publish exact information that can identify a child or safeguarding case.
- Require documented approval for score weights, severity thresholds and access by role.
