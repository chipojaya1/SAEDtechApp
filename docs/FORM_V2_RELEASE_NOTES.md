# Final DRC Kobo forms v2 — release notes

**Reviewed files (user-supplied 17 November 2026)**

| Instrument | Working upload filename | Kobo `id_string` | Version |
|---|---|---|---|
| School Assessment | `SAWSO_School_Assessment.xlsx` | `sawso_school_assessment_consolidated_master` | `20261117a` |
| School Conditions Questionnaire | `SAWSO_School_Conditions.xlsx` | `sawso_vf_abc_combined_v01` | `20261117a` |

**Source verification:** Checked the `survey`, `choices` and `settings` sheets in these exact uploaded files. The agent who prepared them reports successful pyxform 4.5.0 and ODK Validate conversion. That conversion was **not independently repeated here**, and the files have not been tested in a live Kobo deployment within this handover.

## 1. Shared DRC school record and join contract

The `school` choice list in both workbooks contains **615 identical rows** and **615 distinct `name` identifiers**. The shared `school_key` is a required `select_one school` in both, filtered by:

```text
province=${province} and level_key=${reg_level}
```

The data collection key is **`school_key`**, not the text of the school name.

Both instruments contain the same required assessor/selection block: `assessment_date`, calculated `academic_year` (academic year starts in September), `assessor_name`, `assessor_role`, optional email/telephone with confirmations, `territory = 'drc'`, `province`, `reg_level`, `school_key`, and calculated `school_name`, `cona_id`, `secope_id`, `municipality`, `education_level` and `managing_office`.

The school record can flag missing SECOPE/address information and request an officer's correction. **It is not an automatically approved registry change.**

**Critical outstanding limitation:** All 615 school-choice rows have `managing_office = 'not_mapped'`. Therefore the static sub-provincial / provincial reporting examples are **not operational aggregation logic**. Territorial leadership must supply the validated school-to-office mapping.

This public repository stores **no actual school list**, full form workbook or submitted answers. Use the approved, controlled workbook copies.

## 2. Final School Assessment structure

- **Eight criteria**; 230 survey rows including groups/calculations; **159 response fields** (including fields hidden conditionally and fields in two repeat groups).
- Two inventory repeats (equipment/furniture; instructional materials). One entry per *category or material item*, not per physical desk.
- All eight `c1_rating` … `c8_rating` fields are **required** (`select_one rating`).
- An explanation is mandatory only when the relevant rating is `1`.
- A provisional `weighted_total` is calculated:

```text
4*c1_rating + 1*c2_rating + 4*c3_rating + 4*c4_rating +
3*c5_rating + 3*c6_rating + 4*c7_rating + 2*c8_rating
```

Weights total **25**: a rating of 1 on every criterion produces **25**, and a rating of 4 on every criterion produces **100**. This is a **25–100 point provisional index, not a literal 0–100% performance percentage**. The formula is an implemented draft method, not an SAWSO-approved score.

- `priority_support` allows no more than three selected categories or `none`; `priority_action` captures a follow-up.
- `assessment_date` must not be in the future; year labels are derived from the date.
- Fee-free schools can be recorded separately; interpretation of Criterion 7 ratings still requires approval.
- Criteria 3 and 7 hints preserve source guide cutoffs using **1–3**, while the general ratings include **1–4**. This should be reconciled with the programme owner before interpreting scores.

## 3. Final School Conditions Questionnaire structure

- **14 VF conditions** (A1–A4; B1–B5; C1–C5) in **three sections**; 168 survey rows including groups/calculations; **95 response fields**.
- A1 separates the school's land-use documentation from operating authorisation, including approval decree, micro-plan or provisional authorisation.
- A2 avoids re-asking the building condition, furniture and latrine inventory already included in the School Assessment. Classroom shortfalls are requested when standards are *not* met.
- A4 shows the shortfall explanation when income is insufficient or the government subsidy is insufficient.
- Many “which ones?” fields now use multi-select choices rather than long typed descriptions.
- The form is **not** an approved compliance certification. Restrictions for safeguarding information must be configured in a real system; narrative fields should describe institutional systems, never individual child protection incidents.

## 4. Consequences for the app

The four views should eventually use the **same `school_key`** as the two Kobo forms, while keeping separate instrument ID, form version, date, submission ID, reviewer and approval status. The Assessment's provisional `weighted_total` should never silently be presented as an official performance grade, and VF Conditions answers should never be merged into that score.

The current app and the Python Gradio version remain **fictional/illustrative**. No live Kobo sync or privileged data access exists. Do not substitute sample dashboard numbers for DRC submissions.

### Suggested future joins

```text
MasterSchool.school_key
     1 ──── *  SchoolAssessment.school_key   [form: sawso_school_assessment_consolidated_master]
     1 ──── *  SchoolConditions.school_key   [form: sawso_vf_abc_combined_v01]
     1 ──── *  SchoolOfficeAssignment.school_key  [to be provided and approved]
```

Separate repeat-group tables from the Assessment should retain the parent submission identifier; simply joining repeat records directly to the Conditions table will multiply rows and distort percentages.

## 5. Migration and handover safety

**Both `id_string` values were retained**, so updating a corresponding Kobo project can supersede its draft form design. However, some question names changed, so **old test submissions will not necessarily align with the current CSV columns**. Retain and document form version and submitter date; do not rewrite previous records in place or silently concatenate different schema versions.

Before rollout:
1. Back up the existing drafts and test submissions.
2. Import/test each **v2 XLSForm** in a separate staging Kobo project.
3. Run fictional school scenarios: good, damaged, unavailable information, fee-free, inventory repeat, missing ID, conditional required rationale.
4. Test whether school-to-office assignment and territorial review reflect approved organisational structures.
5. Approve eight weighted criteria, fee-free treatment, C3/C7 rating anchor rules and VF evaluation standards.
6. Agree roles, access control, safeguarding restrictions and offline/low-bandwidth devices.
7. Build a version-aware ETL from **approved exports** only after validation.

**Result:** A strong, cross-form common school identity and a plausible field pilot foundation—not yet a production information system.
