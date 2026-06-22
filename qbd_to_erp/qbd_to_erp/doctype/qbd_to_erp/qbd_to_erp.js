// Copyright (c) 2026, Asad and contributors
// For license information, please see license.txt

// frappe.ui.form.on("QBD To ERP", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("QBD To ERP", {

    refresh(frm) {
        // Process button manually chalane ke liye
        frm.add_custom_button(__("Process JSON"), function () {
            if (!frm.doc.attach_json_file) {
                frappe.msgprint({
                    title: __("File Missing"),
                    message: __("Pehle JSON file attach karein."),
                    indicator: "red"
                });
                return;
            }

            frappe.confirm(
                __("JSON file process karein aur log update karein?"),
                function () {
                    frm.save().then(() => {
                        frappe.msgprint({
                            title: __("Done"),
                            message: __("Processing complete — log table check karein."),
                            indicator: "green"
                        });
                        frm.reload_doc();
                    });
                }
            );
        }, __("Actions"));
    },

    attach_json_file(frm) {
        if (frm.doc.attach_json_file) {
            frappe.show_alert({
                message: __("File attach ho gayi — save karein to process hogi."),
                indicator: "blue"
            });
        }
    }

});