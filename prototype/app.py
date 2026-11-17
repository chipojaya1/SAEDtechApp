"""SAEDtechApp: Gradio role-view demonstration with fictional, non-sensitive records.

This is a visual discussion prototype only. It has no Kobo or Power BI
connection, no authentication and no real school submissions.
"""
from collections import Counter
import html
import json
from pathlib import Path

import gradio as gr

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "form_catalog.json"

# Fictional demonstration records. Do not replace these with identifiable
# children, staff, safeguarding details or unapproved operational exports.
DEMO_SCHOOLS = [
    {"id": "DEMO-001", "name": "Example School A", "office": "Demo North Office",
     "province": "Example Province", "report": "Submitted", "assessment": "Draft",
     "data_flag": "Missing location confirmation"},
    {"id": "DEMO-002", "name": "Example School B", "office": "Demo North Office",
     "province": "Example Province", "report": "Needs correction", "assessment": "Submitted",
     "data_flag": "School identifier to verify"},
    {"id": "DEMO-003", "name": "Example School C", "office": "Demo South Office",
     "province": "Example Province", "report": "Not started", "assessment": "Not started",
     "data_flag": "None"},
    {"id": "DEMO-004", "name": "Example School D", "office": "Demo South Office",
     "province": "Example Province", "report": "Submitted", "assessment": "Submitted",
     "data_flag": "None"},
]

def escape(value):
    return html.escape(str(value))

def markdown_table(columns, rows):
    def cell(x):
        return escape(x).replace("|", "&#124;")
    return ("| " + " | ".join(columns) + " |\n"
            + "| " + " | ".join("---" for _ in columns) + " |\n"
            + "".join("| " + " | ".join(cell(x) for x in row) + " |\n" for row in rows))

def school_view(name):
    rec = next(r for r in DEMO_SCHOOLS if r["name"] == name)
    todo = ("Confirm the flagged record detail" if rec["data_flag"] != "None"
            else "No flagged identifier in this fictional example")
    return (
        "### " + escape(rec["name"]) + "\n"
        "**School reference:** " + escape(rec["id"]) + " · "
        + escape(rec["office"]) + "\n\n"
        + markdown_table(["Item", "Illustrative status"], [
            ("School assessment", rec["assessment"]),
            ("Term report", rec["report"]),
            ("Data-quality prompt", todo),
        ])
        + "\n*In a real system the school would only see its authorized records. "
        "This is not a working submission form.*"
    )

def office_view(selection):
    rows = [r for r in DEMO_SCHOOLS if selection == "All fictional schools"
            or r["report"] != "Submitted" or r["data_flag"] != "None"]
    return (
        "### Sub-provincial review queue — synthetic examples\n"
        + markdown_table(["School", "Managing office", "Report", "Data issue"], [
            (r["name"], r["office"], r["report"], r["data_flag"]) for r in rows
        ])
        + "\n*Accept/return/approve controls are not implemented: "
        "authorized workflow and audit rules must be agreed first.*"
    )

def provincial_view():
    offices = sorted({r["office"] for r in DEMO_SCHOOLS})
    data = []
    for office in offices:
        records = [r for r in DEMO_SCHOOLS if r["office"] == office]
        submitted = sum(r["report"] == "Submitted" for r in records)
        data.append((office, len(records), submitted, len(records) - submitted))
    return (
        "### Example Province — illustrative reporting coverage\n"
        + markdown_table(["Office", "Assigned", "Submitted", "Outstanding"], data)
        + "\n*Denominators are fictional. The official school-to-office map "
        "has not been approved.*"
    )

def national_view():
    count = len(DEMO_SCHOOLS)
    submitted = sum(r["report"] == "Submitted" for r in DEMO_SCHOOLS)
    flagged = sum(r["data_flag"] != "None" for r in DEMO_SCHOOLS)
    return (
        "### National coordination — synthetic preview\n"
        + markdown_table(["Indicator", "Illustrative value"], [
            ("Schools in synthetic demo", count),
            ("Report submissions in demo", submitted),
            ("Schools with a demo data-quality issue", flagged),
            ("Provinces in synthetic demo", len({r["province"] for r in DEMO_SCHOOLS})),
        ])
        + "\n*These are four fictional rows, **not the DRC school register**. "
        "No approved national indicator, score or compliance conclusion is calculated.*"
    )

def instrument_view(form_id):
    info = next(f for f in json.loads(CATALOG_PATH.read_text(encoding="utf-8"))["forms"]
                if f["id"] == form_id)
    groups = "\n".join(
        f"- **{escape(item['name'])}:** {escape(item['topic'])}"
        for item in info["groups"]
    )
    return (
        f"### {escape(info['title'])}\n"
        f"**Status:** {escape(info['status'])}\n\n"
        f"{escape(info['purpose'])}\n\n"
        f"**Reviewed XLSForm:** \`{escape(info['source_workbook'])}\`\n\n"
        f"{groups}\n\n"
        + "\n".join(f"- Note: {escape(note)}" for note in info["notes"])
        + "\n\n*This is a form outline, not a data-entry or approval interface.*"
    )

CUSTOM_CSS = """
.gradio-container {max-width:1160px!important;margin:auto!important}
#demo-banner {padding:16px 20px;border-radius:10px;background:#fff5dd;border:1px solid #e8c97d}
footer {display:none!important}
"""

def create_demo():
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    options = [(f["title"], f["id"]) for f in catalog["forms"]]
    with gr.Blocks(title="SAEDtechApp | Four role prototype") as app:
        gr.Markdown("# SAEDtechApp — Education information, four views")
        gr.Markdown(
            "**DEMONSTRATION ONLY.** All school names, counts, submission statuses "
            "and office assignments below are fictional. No KoboToolbox, Power BI "
            "or school register connection, authentication, data storage or form "
            "submission is implemented.", elem_id="demo-banner"
        )
        with gr.Tab("1 · School"):
            select_school = gr.Dropdown(
                choices=[r["name"] for r in DEMO_SCHOOLS],
                value=DEMO_SCHOOLS[0]["name"], label="Select fictional school"
            )
            school_panel = gr.Markdown(school_view(DEMO_SCHOOLS[0]["name"]))
            select_school.change(school_view, inputs=select_school, outputs=school_panel)
        with gr.Tab("2 · Sub-provincial"):
            office_filter = gr.Radio(
                choices=["All fictional schools", "Needs follow-up"],
                value="All fictional schools", label="Filter the synthetic queue"
            )
            office_panel = gr.Markdown(office_view("All fictional schools"))
            office_filter.change(office_view, inputs=office_filter, outputs=office_panel)
        with gr.Tab("3 · Provincial"):
            gr.Markdown(provincial_view())
        with gr.Tab("4 · National"):
            gr.Markdown(national_view())
        with gr.Tab("Two assessment forms"):
            form_select = gr.Dropdown(
                choices=options, value=options[0][1],
                label="Choose an instrument (read-only outline)"
            )
            form_panel = gr.Markdown(instrument_view(options[0][1]))
            form_select.change(instrument_view, inputs=form_select, outputs=form_panel)
            gr.Markdown(
                "For structural XLSForm checking, use the separate **Colab Form Audit** "
                "notebook in this repository. Do not upload restricted school data to "
                "publicly shared demonstration apps."
            )
        gr.Markdown(
            "[Repository and handover](https://github.com/chipojaya1/SAEDtechApp) · "
            "[Existing HTML dashboard](https://github.com/chipojaya1/SAEDtechApp/blob/main/index.html)"
        )
    return app

if __name__ == "__main__":
    create_demo().launch()
