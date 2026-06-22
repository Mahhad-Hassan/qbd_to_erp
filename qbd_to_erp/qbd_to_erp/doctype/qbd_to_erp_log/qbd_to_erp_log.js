frappe.ui.form.on("QBD To ERP Log", {

    status(frm, cdt, cdn) {
        const row = locals[cdt][cdn];

        if (row.status === "Failure") {
            frappe.show_alert({
                message: __(`"${row.title}" — Failure status hai, message zaroor likhein.`),
                indicator: "red"
            });
        }

        if (row.status === "Success") {
            frappe.show_alert({
                message: __(`"${row.title}" — Successfully mapped.`),
                indicator: "green"
            });
        }
    }

});