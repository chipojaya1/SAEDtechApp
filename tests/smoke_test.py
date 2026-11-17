"""SAEDtechApp static handover checks. Run: python tests/smoke_test.py"""
import json
import ast
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class HandoverSmokeTests(unittest.TestCase):
    def test_core_pages_exist(self):
        for name in ("index.html", "forms.html", "script.js", "styles.css"):
            self.assertTrue((ROOT / name).is_file(), name)

    def test_dashboard_is_clearly_illustrative(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("Illustrative concept", html)
        self.assertIn('href="forms.html"', html)
        for role in ("school", "office", "provincial", "national"):
            self.assertIn('id="view-' + role + '"', html)

    def test_form_page_has_both_instruments(self):
        html = (ROOT / "forms.html").read_text(encoding="utf-8")
        self.assertIn('id="assessment"', html)
        self.assertIn('id="evaluation"', html)
        self.assertIn("approval pending", html)
        self.assertIn("20261117a", html)
        self.assertIn("615-school dropdown", html)

    def test_schema_manifest_is_not_live_data(self):
        data = json.loads((ROOT / "data/form_catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(data["metadata"]["data_status"], "schema-only")
        ids = {form["id"] for form in data["forms"]}
        self.assertEqual(ids, {"school_assessment", "school_evaluation"})
        self.assertEqual(next(f for f in data["forms"] if f["id"] == "school_assessment")["structure"]["criteria"], 8)
        self.assertEqual(next(f for f in data["forms"] if f["id"] == "school_evaluation")["structure"]["conditions"], 14)

    def test_final_drc_v2_form_contract(self):
        manifest = json.loads((ROOT / "data/form_catalog.json").read_text(encoding="utf-8"))
        shared = manifest["metadata"]["shared_linkage"]
        self.assertEqual(shared["school_field"], "school_key")
        self.assertTrue(shared["identical_choices_in_both"])
        self.assertEqual(shared["school_choice_count"], 615)
        self.assertIn("not_mapped", shared["managing_office"])

        assessment = next(f for f in manifest["forms"] if f["id"] == "school_assessment")
        conditions = next(f for f in manifest["forms"] if f["id"] == "school_evaluation")
        self.assertEqual(assessment["form_id"], "sawso_school_assessment_consolidated_master")
        self.assertEqual(conditions["form_id"], "sawso_vf_abc_combined_v01")
        self.assertEqual(assessment["form_version"], "20261117a")
        self.assertEqual(conditions["form_version"], "20261117a")
        self.assertEqual(assessment["structure"]["question_fields"], 159)
        self.assertEqual(conditions["structure"]["question_fields"], 95)
        self.assertEqual(assessment["structure"]["weighted_total"]["maximum"], 100)
        self.assertEqual(sum(assessment["structure"]["weighted_total"]["weights"]), 25)
        self.assertIn("provisional", assessment["structure"]["weighted_total"]["status"])

    def test_python_demo_is_parseable_without_gradio_installed(self):
        source = (ROOT / "prototype/app.py").read_text(encoding="utf-8")
        ast.parse(source)
        self.assertIn("DEMO_SCHOOLS", source)
        self.assertIn("create_demo", source)
        self.assertIn("fictional", source.lower())
        notebook = json.loads((ROOT / "notebooks/SAEDtechApp_Colab_Python_App_Demo.ipynb").read_text(encoding="utf-8"))
        self.assertEqual(notebook["nbformat"], 4)
        combined = "\\n".join("".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "code")
        self.assertIn("create_demo", combined)

    def test_colab_notebook_is_valid_and_has_expected_workflow(self):
        notebook = json.loads((ROOT / "notebooks/SAEDtechApp_Colab_Form_Audit.ipynb").read_text(encoding="utf-8"))
        self.assertEqual(notebook["nbformat"], 4)
        code = "\n".join("".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "code")
        for text in ("files.upload()", "read_sheet(", "audit_xlsform(", "xlsform_audit.json", "form_field_catalog.csv"):
            self.assertIn(text, code)
        # Metadata-only workflow must not try to access private live Kobo APIs.
        self.assertNotIn("kf.kobotoolbox.org/api", code)


if __name__ == "__main__":
    unittest.main()
