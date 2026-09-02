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



#assignment
# Assignment: python-api-documentation Assignment

@frappe.whitelist()
def func1():
    Book = frappe.qb.DocType("Book")
    Author = frappe.qb.DocType("Author")
    books = (
        frappe.qb.from_(Book)
        .join(Author)
        .on(Book.author == Author.name)
        .select(
            Book.title,
            Book.status,
            Author.author_name
        )
        .limit(3)
    )
    results = books.run(as_dict=True)
    return results

@frappe.whitelist()
def func2():
    doc = frappe.get_doc("Book", "1")
    doc.status = "Issued"
    doc.save()
    frappe.db.commit()
    return {
        "name": doc.name,
        "title": doc.title,
        "status": doc.status
    }

@frappe.whitelist()
def func3():
    books = frappe.get_all(
        "Book",
        fields=["name"]
    )
    for book in books:
        frappe.db.set_value(
            "Book",
            book.name,
            "status",
            "Available"
        )
        frappe.db.commit()
    return "Bulk updated - books updated"




#form-scripts Tasks

import frappe


@frappe.whitelist()
def create_sample_data():

    # Create Suppliers
    suppliers = [
        {
            "supplier_name": "ABC Supplies",
            "country": "India",
            "email": "abc@gmail.com"
        },
        {
            "supplier_name": "XYZ Traders",
            "country": "India",
            "email": "xyz@gmail.com"
        },
        {
            "supplier_name": "Global Tech",
            "country": "USA",
            "email": "global@gmail.com"
        },
        {
            "supplier_name": "London Store",
            "country": "UK",
            "email": "london@gmail.com"
        }
    ]

    supplier_names = {}

    for data in suppliers:
        supplier = frappe.get_doc({
            "doctype": "Practice Supplier",
            "supplier_name": data["supplier_name"],
            "country": data["country"],
            "email": data["email"]
        })

        supplier.insert()

        supplier_names[data["supplier_name"]] = supplier.name


    # Create Products
    products = [
        {
            "product_name": "Laptop",
            "category": "Electronics",
            "price": 60000,
            "discount": 10,
            "description": "Basic laptop",
            "available": 1,
            "supplier": supplier_names["ABC Supplies"]
        },
        {
            "product_name": "Phone",
            "category": "Electronics",
            "price": 30000,
            "discount": 5,
            "description": "Smartphone",
            "available": 1,
            "supplier": supplier_names["XYZ Traders"]
        },
        {
            "product_name": "Mouse",
            "category": "Accessories",
            "price": 800,
            "discount": 0,
            "description": "Wireless mouse",
            "available": 1,
            "supplier": supplier_names["ABC Supplies"]
        },
        {
            "product_name": "Keyboard",
            "category": "Accessories",
            "price": 2000,
            "discount": 10,
            "description": "USB keyboard",
            "available": 1,
            "supplier": supplier_names["XYZ Traders"]
        },
        {
            "product_name": "Monitor",
            "category": "Electronics",
            "price": 15000,
            "discount": 5,
            "description": "24 inch monitor",
            "available": 0,
            "supplier": supplier_names["Global Tech"]
        },
        {
            "product_name": "Tablet",
            "category": "Electronics",
            "price": 55000,
            "discount": 10,
            "description": "Android tablet",
            "available": 1,
            "supplier": supplier_names["Global Tech"]
        },
        {
            "product_name": "Headphones",
            "category": "Accessories",
            "price": 5000,
            "discount": 0,
            "description": "Bluetooth headphones",
            "available": 1,
            "supplier": supplier_names["London Store"]
        },
        {
            "product_name": "Camera",
            "category": "Electronics",
            "price": 70000,
            "discount": 15,
            "description": "Digital camera",
            "available": 0,
            "supplier": supplier_names["London Store"]
        }
    ]

    for data in products:
        frappe.get_doc({
            "doctype": "Practice Product",
            **data
        }).insert()

    frappe.db.commit()

    return "4 suppliers and 8 products created successfully"


# @frappe.whitelist()
# def getproduct(doc):
#     return 
from frappe.utils import time_diff
@frappe.whitelist()
	def caltime(checkin,checkout):
		checkin=frappe.utils.get_time(checkin)
		checkout=frappe.utils.get_time(checkout)
		seconds = (
        checkout.hour * 3600 + checkout.minute * 60 + checkout.second
        - checkin.hour * 3600 - checkin.minute * 60 - checkin.second
    )

    hours = seconds / 3600

    return hours

