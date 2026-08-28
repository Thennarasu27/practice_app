import frappe


def execute(filters=None):
    columns = [
        {
            "label": "Product",
            "fieldname": "product_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Category",
            "fieldname": "category",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Price",
            "fieldname": "price",
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "label": "Final Price",
            "fieldname": "final_price",
            "fieldtype": "Currency",
            "width": 150
        }
    ]

    data = frappe.get_all(
        "Practice Product",
        fields=[
            "product_name",
            "category",
            "price",
            "final_price"
        ]
    )

    return columns, data