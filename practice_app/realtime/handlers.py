import frappe
from frappe.realtime import Socket, realtime


@realtime.on("student_hello")
def student_hello(socket: Socket):
    socket.emit(
        "student_hello_result",
        {"message": "Hello from Python Realtime!"}
    )