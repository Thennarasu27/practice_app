import frappe

def student_has_permission(doc, user=None, permission_type=None):
    frappe.msgprint(
        f"User: {user}<br>Permission: {permission_type}"
    )

    return True