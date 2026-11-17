# Form-to-dashboard mapping (concept only)

## Core distinction

The **School Assessment** documents school conditions, needs and eight provisional ratings. The **School Conditions Questionnaire** covers 14 VF conditions within three sections and is **not** itself an approved compliance decision. The two final DRC v2 forms already carry the identical 615-row school list and the required field `school_key`. The **live app still needs an approved registry, office hierarchy, review permissions and secure ingest before joining submissions**. Keep separate record dates, versions, evidentiary standards and review states.

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

All eight provisional ratings are **required human assessor entries** in v2. A computed `weighted_total` out of 100 is now present (weights 4,1,4,4,3,3,4,2), but the method remains unapproved for official reporting. The top-three `priority_support` choices and `priority_action` are candidate fields for follow-up views.

## School Conditions Questionnaire: 14 VF conditions

| Section | Covered areas | Intended role-level use |
|---|---|---|
| A. Governance and Compliance | Legal registration, minimum standards, governance structure, financial stability | Restricted review with evidence provenance; local standards must be approved |
| B. Monitoring and Protection | THQ monitoring, trained personnel, child protection, effectiveness measurement, risk management | Restricted authorized workflow; do not surface sensitive case details on dashboards |
| C. Mission and Faith Integration | Faith-based orientation, spiritual care, institutional integration, family proximity, vulnerable populations | Appropriate institution-level review with explicit access policies |

The v2 Conditions XLSForm is a final **questionnaire design**, not an approved VF compliance determination. Do not label responses as approved compliance determinations or combine them mechanically with the eight Criterion 1–8 ratings.

## One shared record, four views — data flow concept

```text
Approved DRC school register (shared school_key; 615 common choices in final v2)
       │
       ├── School Assessment (eight criteria; repeat inventories)
       │
       └── School Conditions (14 VF conditions; restricted review as needed)
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

## Exact join and reporting contract for developers

| Dataset | Join field | Version/provenance | Implementation cautions |
|---|---|---|---|
| School register | `school_key` | Approved active school list | Exactly 615 identical choice rows in both submitted XLSForms; active roster must be confirmed by DRC |
| School Assessment | `school_key` | form `sawso_school_assessment_consolidated_master`, version `20261117a` | Eight required ratings, provisional weighted_total, two repeat groups, priority_support |
| School Conditions | `school_key` | form `sawso_vf_abc_combined_v01`, version `20261117a` | Fourteen VF conditions; land and operating documents separate; no compliance verdict |
| School-to-office mapping | `school_key` + `managing_office` | Not yet provided | All 615 workbook rows currently return `not_mapped`; no real sub-provincial assignments possible |

**Join at school + instrument submission granularity.** Multiple assessments, conditions submissions or equipment-repeat records can exist for one school. Do not combine two submission tables on `school_key` alone and then sum quantities; choose the approved period/version or aggregate each instrument separately first.

Only authorized aggregate indicators and accepted data definitions should reach the provincial and national views. Keep assessor contact details and child protection narratives out of public visualizations.

See [FORM_V2_RELEASE_NOTES.md](FORM_V2_RELEASE_NOTES.md) for exact form IDs, weights and migration rules.
