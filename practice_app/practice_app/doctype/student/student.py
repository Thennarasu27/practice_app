# Copyright (c) 2026, Thennarasu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class student(Document):
    pass


@frappe.whitelist()
def send_realtime():
    frappe.publish_realtime(
        "hello_event",
        {"message": "Hello from server!"}
    )

    frappe.publish_progress(
        25,
        title="Progress",
        description="25% completed"
    )

    

from frappe.realtime import realtime

@realtime.on("hello_server")
def hello_server(socket):
    print("Hello from browser!")