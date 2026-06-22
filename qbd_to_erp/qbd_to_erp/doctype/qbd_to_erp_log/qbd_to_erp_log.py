import frappe
from frappe.model.document import Document


class QBDToERPLog(Document):

    def validate(self):
        # Status check
        if self.status not in ("Success", "Failure"):
            frappe.throw(f"Status sirf 'Success' ya 'Failure' ho sakta hai — mila: {self.status}")

        # Title required
        if not self.title:
            frappe.throw("Title khali nahi ho sakta.")