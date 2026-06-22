# Copyright (c) 2026, Asad and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestQBDToERP(IntegrationTestCase):
	"""
	Integration tests for QBDToERP.
	Use this class for testing interactions between multiple components.
	"""

	pass


import json

# Apna JSON file path yahan dein
JSON_FILE = "qbd_data.json"

def render_mapping_table(data):
    print("\n=== QBD → ERP Mapping Table ===\n")
    print(f"{'#':<4} {'Name':<25} {'Status':<12} {'Mapping (QBD → ERP)'}")
    print("-" * 75)

    success = failure = 0

    for i, row in enumerate(data, 1):
        name    = row.get("name") or row.get("title") or "—"
        status  = (row.get("status") or "").lower()
        is_ok   = status in ("success", "ok", "pass")
        qbd     = row.get("qbd_field") or row.get("source") or "—"
        erp     = row.get("erp_field") or row.get("target") or "—"
        label   = "✅ Success" if is_ok else "❌ Failure"
        mapping = f"{qbd} → {erp}"

        if is_ok: success += 1
        else:     failure += 1

        print(f"{i:<4} {name:<25} {label:<12} {mapping}")

    print(f"\nTotal: {len(data)} | Success: {success} | Failure: {failure}")


# JSON file se load karein
with open(JSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

render_mapping_table(data)