// Copyright (c) 2026, Thennarasu and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Employee Check", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Employee Check", {
    checkout(frm)
    {
        if(!frm.doc.checkin)
            {
                frappe.throw("Check-In")
            }
        frappe.call({
            method: "practice_app.api.caltime",
            args:{
                checkin:frm.doc.checkin,
                checkout:frm.doc.checkout
            },
            callback: function(r) {
                let hours=r.message
                let status
                if(hours>4){
                    status="present"
                }
                let row = frm.add_child('attendance', {
                    item_code: 'Tennis Racket',
                    qty: 2
                });

frm.refresh_field('attendance');

            }});
        

        


        
       
    }
})
        
        // let c_in=frm.doc.checkin;
        // let c_out=frm.doc.checkout;
        // let start=moment(c_in,"HH:mm:ss");
        // let end=moment(c_out,"")


       

    


