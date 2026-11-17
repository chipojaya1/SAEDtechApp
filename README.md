# SAEDtechApp — SAWSO Education Data System (concept prototype)

> **Status: handover prototype, not a deployed application.** This repository demonstrates how information from a shared school register, a School Assessment and a separate School Conditions Questionnaire *could* support four levels of decision-making. The dashboard currently uses illustrative figures and static HTML/CSS/JavaScript. It does not connect to KoboToolbox, Power BI, or live submissions. **The two final DRC v2 XLSForms already share a verified 615-row school choice list and a stable `school_key`; the app does not yet ingest it.**

## Quick start

- **Dashboard:** open [index.html](index.html) in a browser, then explore the School, Sub-provincial, Provincial and National tabs.
- **Two-form overview:** open [forms.html](forms.html).
- **Google Colab — Python app:** [Run the four-role Gradio demonstration](https://colab.research.google.com/github/chipojaya1/SAEDtechApp/blob/main/notebooks/SAEDtechApp_Colab_Python_App_Demo.ipynb) with fictional records only.
- **Google Colab — form audit:** [Run the XLSForm audit notebook](https://colab.research.google.com/github/chipojaya1/SAEDtechApp/blob/main/notebooks/SAEDtechApp_Colab_Form_Audit.ipynb) to inspect two private workbooks without publishing them.
- **Handover:** [docs/HANDOVER.md](docs/HANDOVER.md).
- **Form-to-dashboard mapping:** [docs/ASSESSMENT_MAPPING.md](docs/ASSESSMENT_MAPPING.md).
- **Final DRC form release notes and migration guidance:** [docs/FORM_V2_RELEASE_NOTES.md](docs/FORM_V2_RELEASE_NOTES.md).
- **Project decisions still required:** [docs/DECISIONS_REQUIRED.md](docs/DECISIONS_REQUIRED.md).

## What exists

| Component | Current state | What it does |
|---|---|---|
| Four-role dashboard | Static demonstration | Shows a possible division of information and responsibilities by role |
| Python/Gradio demo | Fictional data only | Runnable four-role prototype with an interactive school selector, office filter and read-only two-form overview |
| School Assessment (DRC v2) | Final design XLSForm, **not hosted in this public repository** | Eight required criterion ratings, provisional weighted total out of 100, two inventory repeats, and top-three priority-support areas |
| School Conditions Questionnaire (DRC v2) | Final design XLSForm, **not hosted in this public repository** | Fourteen VF conditions across A–C, separate land/operating documents and reduced overlap; **not an approved compliance decision** |
| [Forms catalogue](forms.html) | Static reference | Explains form purposes and responsibilities without exposing school responses |
| [Google Colab notebook](notebooks/SAEDtechApp_Colab_Form_Audit.ipynb) | Runnable read-only workflow | Upload two XLSForms, check their basic structure, export a CSV field catalogue and audit/handover ZIP |
| [Schema-only manifest](data/form_catalog.json) | Source metadata only | Documents field and group counts from the two reviewed workbooks |

### Form versions reviewed

- **School Assessment:** `SAWSO_School_Assessment.xlsx` — form ID `sawso_school_assessment_consolidated_master`; version `20261117a`; 8 **required** 1–4 ratings; 2 repeat inventories; **159 possible response fields**; a **provisional** weighted total using weights 4,1,4,4,3,3,4,2.
- **School Conditions:** `SAWSO_School_Conditions.xlsx` — form ID `sawso_vf_abc_combined_v01`; version `20261117a`; 14 VF conditions across A–C; **95 possible response fields**; no certification or automatic compliance verdict.

Counts describe possible XLSForm response fields, **not** the number of questions every respondent sees. **Both form choice sheets contain exactly the same 615 schools with 615 unique `school_key` values.** Province → school level → school selection is aligned across the two forms. Every school is currently assigned `managing_office = not_mapped`, so reporting by managing office and any permissions dependent on that hierarchy are pending. Both workbooks remain subject to staging import, field testing and programme sign-off.

## Repository structure

```text
index.html                                # existing four-role visual concept
styles.css
script.js
forms.html                                # instruments and proposed workflow
data/form_catalog.json                   # metadata only; no actual submissions
notebooks/SAEDtechApp_Colab_Form_Audit.ipynb
notebooks/SAEDtechApp_Colab_Python_App_Demo.ipynb
prototype/app.py                          # Gradio demo; synthetic schools only
docs/HANDOVER.md
docs/ASSESSMENT_MAPPING.md
docs/FORM_V2_RELEASE_NOTES.md
docs/DECISIONS_REQUIRED.md
tests/smoke_test.py
```

## How to run locally

This is a static website; no backend setup is needed. Opening `index.html` or `forms.html` in a browser is enough. For a local HTTP preview, run:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`. The site must be treated as a **demonstration** even when served over HTTP.

Run the lightweight static checks with:

```bash
python tests/smoke_test.py
```

## Run the Python demo locally (optional)

```bash
python -m pip install -r requirements-demo.txt
python -m prototype.app
```

This launches a **fictional Gradio interface** on your local computer. It does not accept or store live school data, and it has no authentication.

## Colab: run the Python app demo

1. Open the [Python app notebook](https://colab.research.google.com/github/chipojaya1/SAEDtechApp/blob/main/notebooks/SAEDtechApp_Colab_Python_App_Demo.ipynb).
2. Run all cells to install Gradio, fetch this public repository and launch the demo.
3. Select fictional schools and switch between School, Sub-provincial, Provincial, National and the two-form overview.
4. The temporary Gradio sharing link is public to people with the URL, so **never add confidential workbooks or real learner data** to this demo.

The Gradio app uses fictional records and displays **no actual Kobo submissions**, regardless of whether the other notebook has inspected your form files.

## Colab: update the form audit

1. Open the notebook in Google Colab.
2. Upload **both** XLSForm files from the approved working copies.
3. Run **Runtime → Run all**.
4. Download the generated `SAEDtechApp_Colab_Handover.zip` (audit JSON, field catalogue CSV and a checklist).
5. Review warnings and test a separate copy in KoboToolbox. **Do not interpret a clean structural audit as a field-validated form.**

The notebook is read-only and intentionally does not publish the XLSForm files or school submissions to this public repository.

## Design principles

1. **One school, stable key:** match records using an approved internal key, never school name alone.
2. **Different tools, different meanings:** condition ratings are *not* compliance approvals.
3. **Role-level views:** school staff correct their own information; authorized offices can review and return submissions, not silently rewrite a school's answers.
4. **Low respondent burden:** click/count first, require explanation only for important problems.
5. **Transparency:** a provisional weighted score is *calculated in the final XLSForm*, but it is not yet approved for performance or compliance decisions; uncertain denominators and missing office assignments stay visible.
6. **Safety and privacy:** no learner records, safeguarding cases, salaries, personal contacts or credentials should enter the public repository.

## What is **not** implemented

Authentication or authorization; live data ingestion; approved office hierarchy; live register-linked submissions; offline data sync; audit trail; school-to-office mapping; **approved** weighted scoring; VF/legal compliance decisions; operational reporting; production hosting or backups.

**Next owner:** review [the handover guide](docs/HANDOVER.md) and [open decisions](docs/DECISIONS_REQUIRED.md) with SAWSO, the DRC territorial offices, schools and local developers before committing to a development specification.

## Related design work

The companion education-data-system planning repository documents the Kobo/design work: [chipojaya1/sawso-education-data-system](https://github.com/chipojaya1/sawso-education-data-system). Keep any private workbook distributions in approved storage, not in either public demo page.
