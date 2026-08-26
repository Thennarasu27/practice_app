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
