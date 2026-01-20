frappe.ui.form.on('Candidate Onboarding', {
    
    // 1. Refresh Event (Duplicate Entry pakdne ke liye)
    refresh: function(frm) {
        // Agar Form Naya hai, toh dono check karo
        if (frm.is_new()) {
            if (frm.doc.email_address) frm.trigger('email_address');
            if (frm.doc.phone_no)  frm.trigger('phone_no'); // Phone check trigger
        }
    },

    // 2. Email Check Logic (Pehle wala hi hai)
    email_address: function(frm) {
        if (!frm.doc.email_address) return;

        frappe.call({
            method: "frappe.client.get_value",
            args: {
                doctype: "Candidate Onboarding",
                filters: {
                    "email_address": frm.doc.email_address,
                    "name": ["!=", frm.doc.name]
                },
                fieldname: "name"
            },
            callback: function(r) {
                if (r.message && r.message.name) {
                    frappe.msgprint("🚫 Ye Email ID pehle se Candidate " + r.message.name + " ke paas hai!");
                    frm.set_value('email_address', '');
                }
            }
        });
    },

    // 3. 👇 NAYA PART: Phone Number Check Logic
    phone_no: function(frm) {
        // Agar khali hai toh return jao
        if (!frm.doc.phone_no) return;

        frappe.call({
            method: "frappe.client.get_value", // Wahi same function call
            args: {
                doctype: "Candidate Onboarding", // Tera DocType
                filters: {
                    "phone_no": frm.doc.phone_no, // Filter: Phone Number match karo
                    "name": ["!=", frm.doc.name] // Khud ko chhod ke
                },
                fieldname: "name"
            },
            callback: function(r) {
                if (r.message && r.message.name) {
                    // Agar mil gaya duplicate
                    frappe.msgprint("🚫 Arre! Ye Phone Number pehle se Candidate " + r.message.name + " ka hai!");
                    
                    // Number uda do
                    frm.set_value('phone_no', '');
                }
            }
        });
    }
});