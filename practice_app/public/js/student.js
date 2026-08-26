frappe.ui.form.on("student", {
    refresh: function(frm) {
        console.log("Custom Student form script loaded!");
        frappe.msgprint("Override-formscripts")
    }
});