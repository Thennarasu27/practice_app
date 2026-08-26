import frappe


def test_scheduler():
    frappe.log_error(
        title="Scheduler Test",
        message="Scheduler is working!"
    )

# import frappe

def send_hourly_email():
    frappe.sendmail(
        recipients=["thennarasum2705@gmail.com"],
        subject="Hourly Email",
        message="This email was sent automatically by Frappe."
    )