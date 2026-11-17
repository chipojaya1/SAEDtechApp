# Country-led decisions required before a real SAEDtechApp

| Decision | Why it matters | Suggested owner | Status |
|---|---|---|---|
| Confirm approved active-school list | Both final v2 forms contain the **same 615 choice rows and unique `school_key` values**; country team still needs to confirm active status | DRC school registry + programme | Open (technical consistency checked) |
| School-to-managing-office mapping | Determines role-level assignment and aggregates | Territorial education management | Open |
| Official hierarchy and terminology | Source of navigation and access permissions | Territorial management | Open |
| Who enters, reviews, returns and approves submissions | Workflow and audit history | Schools + sub-provincial offices | Open |
| First-round schools and assessment cadence | Correct denominators and time-series comparisons | Programme leadership | Open |
| Approve implemented provisional weights (4,1,4,4,3,3,4,2) and ratings | The v2 Assessment calculates `weighted_total` out of 100; it is not a policy-approved performance measure | Programme / technical experts | Open |
| Resolve C3/C7 rules including fee-free schools | Source hints present 1–3 cutoffs within a 1–4 rating system | Programme / country leadership | Open |
| Country-specific VF standards and legal interpretations | Evaluation sample is not a compliance ruling | Country legal/education authorities | Open |
| Evidence and privacy classification, safeguarding access | Avoid exposure of sensitive information | Safeguarding + IT owners | Open |
| Required vs optional questions, local languages and offline devices | Avoid excessive respondent burden | School assessors + field pilot team | Open |
| Data exports, integration, hosting and backups | Production reliability and maintenance | Local technical developers + SAWSO IT | Open |

**No automatic decisions are made by this demo.** These items should be resolved through consultation and recorded in an approved decision log rather than inferred from illustrative data.

## Verified as of 17 November 2026

The uploaded School Assessment and Conditions workbooks have identical `school` lists (615 rows; no duplicate school keys), a matching province → level → school cascade, and version `20261117a`. **Every `managing_office` value is `not_mapped`**. No local office-level dashboards or permission decisions should proceed until that information is supplied and signed off.

Earlier Kobo test submissions may contain renamed fields. Assign responsibility for preserving, documenting and reconciling those versioned exports before field launch.
