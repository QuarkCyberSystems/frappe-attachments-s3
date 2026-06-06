// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("S3 File Attachment", {
	//refresh(frm) {
	//},
	migrate_existing_files(frm) {
		frappe.msgprint("Local files getting migrated", "S3 Migration");
		frappe.call({
			method: "frappe_s3_attachment.controller.migrate_existing_files",
			callback: function (data) {
				if (data.message) {
					frappe.msgprint("Upload Successful");
					location.reload(true);
				} else {
					frappe.msgprint("Retry");
				}
			},
		});
	},
});
