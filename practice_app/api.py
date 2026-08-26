# http://127.0.0.1:8000/api/method/practice_app.api.hello
import frappe
@frappe.whitelist()
def hello():
    return "Hello"

@frappe.whitelist()
def custom_hello():
    return "Hi"


@frappe.whitelist()
def hookfunc(doc,method):
    frappe.msgprint("Hook executed!")
