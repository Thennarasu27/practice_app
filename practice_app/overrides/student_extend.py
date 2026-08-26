import frappe
from practice_app.practice_app.doctype.student.student import student
class CustomStudent(student):
    def on_update(self):
        frappe.msgprint("Student updated using CustomStudent! - Extended")
