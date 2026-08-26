import frappe


def student_timeline(doctype, docname):
    return [
        {
            "creation": frappe.utils.now(),
            "template": "student_timeline",
            "template_data": {
                "message": "Hello from my custom Student timeline!"
            },
        }
    ]