// Copyright (c) 2026, Thennarasu and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Practice Product", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Practice Product", {
    setup(frm)
    {
        frm.set_query('supplier',()=>
        {
            return{
                filters:{
                    'country':'India'
                }
            }
        })
    },
    //Task 1
	refresh(frm) {
        frm.add_custom_button("Calculate",()=>
        {
            let price = frm.doc.price;
            let discount = frm.doc.discount;
            let finalprice = price - (price*discount/100)
            frm.set_value('final_price',finalprice);
            frappe.msgprint("Done!!!")
        })
        frm.add_custom_button("Available",()=>
        {
            frm.set_value('available',1);
            frappe.msgprint("")
        })
        frm.toggle_display('price',frm.doc.available)
        if(frm.is_new())
        {
            frm.add_custom_button("New Product",()=>
            {})
        }
        else
        {
            frm.add_custom_button("Edit Product",()=>
            {})
        }
        if(!frm.doc.price)
        {
            frm.disable_save();
        }
        frm.add_custom_button("Remove",()=>
        {
            frm.remove_custom_button("Calculate")
        })
        frm.add_custom_button("Get Product Info",()=>
        {

        })
        frm.add_custom_button('Email',()=>
        {
            frm.email_doc;
        }),
        frm.add_custom_button('Reload',()=>
        {
            frm.reload_doc().then(()=>{
                frappe.msgprint("Reloaded!!")
            })
        })
        frm.add_custom_button('Apply Discount',()=>
        {
            let val = frm.doc.price;
            frm.set_value('price',val-(val*10/100))
            frm.refresh_field(price)
        })
        
	},
    available(frm) {
    frm.toggle_display('price', frm.doc.available);
    },
    price(frm)
    {
        frm.toggle_reqd('discount',frm.doc.price>10000)
        if(frm.doc.price>50000){
        frm.set_intro('Premium-Product', 'blue');}
        else{
        frm.set_intro('Product', 'blue');}
        if(frm.doc.price>0)
        {
            frm.enable_save();
        }
        else
        {
            frm.disable_save();
        }

    },
    before_save(frm)
    {
        //dont use variable for checking use price
        if(!frm.doc.discount)
        {
            frm.set_value('discount',0);
        }
    },
    after_save(frm)
    {
        frappe.msgprint("Done !! Successfully Saved!!")
    }

    
});


