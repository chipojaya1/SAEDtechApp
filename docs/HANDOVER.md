# SAEDtechApp — Technical and programme handover

**Date:** 17 November 2026  
**Prepared for:** SAWSO education programme and prospective local implementation team  
**Scope:** design demonstration and development handoff, **not** a production system

## 1. Why this work exists

The goal is to make Doug's proposed education information workflow visible enough for local territorial leadership, schools and developers to discuss. A shared school identity could connect an approved register to two distinct Kobo instruments, after which each authorized level sees the information it needs.

The current visual app is a **static four-role mockup**; it provides layout and workflow ideas. It does not submit forms, sync offline data, authenticate users or query real schools.

## 2. Current deliverables

| Deliverable | Evidence | Current status |
|---|---|---|
| Four-role interactive mockup | `index.html`, `styles.css`, `script.js` | Demonstration only; illustrative numbers |
| School Assessment design | `SAWSO_School_Assessment_Master_v0.5_Handover.xlsx` held outside this public repo | Working 8-criterion XLSForm; not field-validated |
| School Evaluation design | `SAWSO_VF_Combined_Sections_A_B_C_Overview.xlsx` held outside this public repo | 14-condition sample; not approved compliance instrument |
| Form catalogue | `forms.html`, `data/form_catalog.json` | Read-only source-schema overview |
| Colab quality-control notebook | `notebooks/SAEDtechApp_Colab_Form_Audit.ipynb` | Reads XLSForms, exports structural audit and field catalogue |
| Colab Python app demo | `notebooks/SAEDtechApp_Colab_Python_App_Demo.ipynb` + `prototype/app.py` | Runs a Gradio role-view concept using only fictional school records |
| Traceable decisions | `docs/DECISIONS_REQUIRED.md` | Open; requires local approval |

The School Assessment has two repeatable inventories: a category-level equipment/furniture entry and an instructional-material entry. Individual desks are **not** expected to be entered one at a time. Reports and provisional 1–4 criterion ratings are separate from any future weighted/approved score.

## 3. Roles and expected workflow (proposed, not approved)

1. **School:** view its own verified profile, complete approved Kobo forms, report corrections and see what is outstanding.
2. **Sub-provincial office:** review submissions from assigned schools, return corrections with reasons and track missing submissions without silently editing original figures.
3. **Provincial:** view aggregated coverage, patterns and priority follow-up, based on agreed school-to-office mapping.
4. **National:** see aggregate reporting, data-quality flags and support priorities subject to role-based permissions and denominator definitions.

A safe production workflow must define submitter, reviewer, approver, editable fields, review states and time stamps. The prototype displays possible states but does **not** enforce them.

## 4. Data model developers should validate

Recommended initial entities (not a final database design):

| Entity | Candidate key / fields | Key dependency |
|---|---|---|
| `School` | stable internal `school_id`, official name, level, province, relevant CONA/SECOPE identifiers | Approved master register; duplicate/missing ID resolution |
| `Office` | `office_id`, office level and approved name | Country management hierarchy |
| `SchoolOfficeAssignment` | `school_id`, `office_id`, validity period | School-to-office mapping and history |
| `SchoolAssessment` | `assessment_id`, `school_id`, assessment date, version, provisional criterion ratings | Approved questions, cadence, field pilot |
| `SchoolEvaluation` | `evaluation_id`, `school_id`, assessment date, version, separate VF conditions | Approved country standards; safeguarding/access rules |
| `SubmissionReview` | source form/record, submitter, reviewer, state, note, timestamps | Approval procedure and audit trail |

Do not join solely on school name or assume CONA/SECOPE values are complete and unique. Do not merge the Assessment's provisional ratings and Evaluation's VF conditions into one invented metric.

## 5. How to run the Colab notebook

1. Download both approved source XLSForms from controlled SAWSO project storage.
2. Open `notebooks/SAEDtechApp_Colab_Form_Audit.ipynb` in Google Colab.
3. Upload the **two workbooks** using the upload cell.
4. Run all cells; inspect structural issues.
5. Download `SAEDtechApp_Colab_Handover.zip`, containing `xlsform_audit.json`, `form_field_catalog.csv` and `HANDOVER_CHECKLIST.md`.
6. Review any potential inconsistencies with a human assessor, then import **test copies** into KoboToolbox.

The notebook does not make changes to source forms, authenticate with Kobo or write to this repository.

## 6. Run the optional Python app demonstration

1. Open `notebooks/SAEDtechApp_Colab_Python_App_Demo.ipynb` in Google Colab.
2. Run all cells. The notebook installs Gradio, clones the public repository, and launches a demonstration link.
3. Navigate the School, Sub-provincial, Provincial, National, and Forms tabs. The sample records are deliberately fictional.
4. Treat the temporary Gradio link as shareable/public to anyone who has it. **Never upload confidential data to this demo**.

The Python demo is separate from the read-only workbook audit. It does not receive data from the Kobo source forms.

## 7. Minimum tests before field use

- Test both XLSForms in KoboToolbox (valid import, preview, save, submit and export).
- Use realistic *fictional* cases for good, defective, unknown and incomplete school conditions.
- Check both equipment inventory repeats: at least one entry if "Yes", duplicate category handling, and total = usable + repairable + unrepairable.
- Test short and low-connectivity submissions on the devices actual users have.
- Check all required questions, unknown/zero distinctions and skip logic.
- Get explicit local approval of definitions, language, permissions, reporting cadence and school-to-office hierarchy.
- Reconcile the February 2024 assessment rubric before publishing any weighted score.
- Test that no unauthorized role can access or rewrite restricted details; document audit logs and retention.

## 8. Handover session agenda

**15–20 minutes suggested:**
- 3 min: show why consistent school identities and reduced respondent burden matter.
- 5 min: click through the four views and both form outlines.
- 4 min: run the Colab schema audit with two test forms.
- 5 min: review unresolved governance/data decisions.
- 3 min: assign owners and agree on a small, consented country-led pilot.

## 9. Explicit boundaries

- No live school data is connected.
- Sample figures in the dashboard are illustrative, not current national statistics.
- The project is not a registered legal-compliance engine.
- The current interface does **not** implement permission-controlled access, offline sync or field submissions.
- Deployment requires agreement by territorial leadership, school representatives and local implementers.
- Never place identifiable children, safeguarding reports, personal contacts, passwords, private workbook exports or unapproved registries into this public repository.

## 10. Immediate next owner actions

1. Designate an SAWSO programme owner and a local technical owner.
2. Confirm whether this concept matches Doug's intended decision-making chain.
3. Secure an approved school register and hierarchy map.
4. Approve the two Kobo instruments separately and perform field tests.
5. Decide privacy, access, review procedures, capacity and maintenance responsibilities.
6. Only then commission an API/reporting integration and pilot rollout.

See [ASSESSMENT_MAPPING.md](ASSESSMENT_MAPPING.md) and [DECISIONS_REQUIRED.md](DECISIONS_REQUIRED.md).