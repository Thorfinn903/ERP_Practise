# 1. Sirf tab chalo jab status 'Selected' ho
if doc.workflow_state == "Joined":

    # 2. CHECK: Kya is Candidate ka ToDo pehle se hai?
    # Hum Database se puch rahe hain: "ToDo table mein koi aisa task hai jo is Candidate se juda ho?"
    task_exists = frappe.db.exists("ToDo", {
        "reference_type": "Candidate Onboarding",
        "reference_name": doc.name
    })

    # 3. Agar Task nahi hai (Not Exists), tabhi naya banao
    if not task_exists:
        new_task = frappe.get_doc({
            "doctype": "ToDo",
            "description": f"Allocate Laptop for {doc.first_name}",
            "priority": "High",
            "status": "Open",

            # 👇 Ye 2 lines MAGIC hain (Linking)
            # Isse hum Task ko Candidate se jod rahe hain
            "reference_type": "Candidate Onboarding",
            "reference_name": doc.name
        })

        new_task.insert(ignore_permissions=True)
        frappe.msgprint("🎉 Laptop Task bana diya gaya!")

    else:
        # 4. Agar pehle se hai, toh shanti se baitho
        frappe.msgprint("⚠️ Task pehle se bana hua hai, tension mat lo.")