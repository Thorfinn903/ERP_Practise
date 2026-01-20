frappe.ui.form.on('Candidate Onboarding', {
    // Ye function tab chalega jab user "Save" dabayega
    validate: function(frm) {
        
        // Check: Agar Salary 10,000 se kam hai
        if (frm.doc.expected_salary < 10000) {
            
            // 1. Error Message dikhao
            frappe.msgprint('Bhai, itni kam salary? Kam se kam 10,000 toh do!');
            
            // 2. Save hone se roko
            frappe.validated = false;
        }
    }
});