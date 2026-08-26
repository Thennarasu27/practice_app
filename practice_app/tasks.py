import frappe

def daily_maintenance():
    frappe.log_error(
        title="Daily",
        message="Scheduler Events"
    )
