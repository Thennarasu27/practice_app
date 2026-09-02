# Copyright (c) 2026, Thennarasu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import time_diff

# @frappe.whitelist()
# def caltime(time1,time2):
# 	diff = time_diff(time2, time1)
# 	return diff

class EmployeeCheck(Document):



	