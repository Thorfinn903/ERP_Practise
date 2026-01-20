frappe.ui.form.on('Candidate Onboarding', {
    // Ye tab chalega jab user 'hike_percent' wale box mein kuch likh ke hatega
    hike_: function(frm) {
        
        // 1. Current Salary aur Hike ki value uthao
        let current = frm.doc.current_ctc;
        let hike = frm.doc.hike_;
        
        // 2. Calculation karo (Basic Maths)
        let new_salary = current + (current * hike / 100);
        
        // 3. Result ko 'Expected Salary' wale box mein set kar do
        frm.set_value('expected_salary', new_salary);
        
    }
});