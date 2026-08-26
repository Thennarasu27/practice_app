import frappe

def after_insert_student(doc, method=None):
    frappe.msgprint(f"Student {doc.name} has been created!") 