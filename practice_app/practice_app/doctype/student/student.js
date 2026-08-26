// Copyright (c) 2026, Thennarasu and contributors
// For license information, please see license.txt

// frappe.ui.form.on("student", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("student", {
    refresh(frm) {
        frm.add_custom_button("Send Realtime", () => {
            frappe.call({
                method: "practice_app.practice_app.doctype.student.student.send_realtime",
                callback(r) {
                    console.log("Server method called");
                }
            });
        });
    }
});

frappe.realtime.on("hello_event", (data) => {
    console.log("Hello from realtime!");
    console.log(data);
});

frappe.realtime.on("student_hello_result", (data) => {
    console.log(data);
});
