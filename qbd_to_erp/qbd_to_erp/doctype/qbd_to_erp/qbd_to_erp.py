# Copyright (c) 2026, Asad and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class QBDToERP(Document):
	pass
import frappe
import json
from frappe.model.document import Document
from frappe.utils.file_manager import get_file_path


class QBDToERP(Document):

    def validate(self):
        if self.attach_json_file:
            self.process_json_file()

    def process_json_file(self):
        try:
            file_path = get_file_path(self.attach_json_file)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, list):
                frappe.throw("JSON file mein array hona chahiye: [...]")

            # Purani log clear karo
            self.processing_log = []

            for row in data:
                status  = (row.get("status") or "").capitalize()
                if status not in ("Success", "Failure"):
                    status = "Failure"

                self.append("processing_log", {
                    "title":     row.get("name")      or row.get("title")  or "—",
                    "status":    status,
                    "qbd_field": row.get("qbd_field") or row.get("source") or "—",
                    "erp_field": row.get("erp_field") or row.get("target") or "—",
                    "message":   row.get("message")   or "",
                })

            frappe.msgprint(
                f"JSON process ho gaya — {len(data)} rows load hue.",
                title="Success",
                indicator="green"
            )

        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "QBD To ERP Error")
            frappe.throw(f"JSON process karne mein error: {str(e)}")