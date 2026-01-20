# 🚀 ERPNext & Python Developer Journey

This repository documents my daily progress in mastering **Python** and the **Frappe Framework (ERPNext)**. My goal is to become a full-stack ERPNext Developer.

---

### 📂 [Day 1: Python Core & Data Management](Day%20-%201%20Python%20core/)
**Focus:** Building backend logic, database connectivity, and file handling.

**Projects & Modules Built:**
1.  **Store Management System:** A logic-based system to manage store operations.
2.  **Database Integration (`company.db`):** - Learned to connect Python with **SQLite/SQL**.
    - Performed CRUD operations (Create, Read, Update, Delete) on data.
3.  **Data Processing:** - Parsed and processed `employees.csv` and `users.csv` using Python's file handling.
    - Scripts: `Data_Read.py`, `Emp_Reading.py`.
4.  **Object-Oriented Programming (OOP):**
    - Designed `Employee.py` class models to structure data efficiently.
5.  **Utility Tools:** - Built `Find_City_and_ISP.py` (Likely involving API/Network requests or data lookup).

**Key Skills Demonstrated:** `SQL/SQLite`, `CSV Handling`, `OOPs (Classes & Objects)`, `Data Parsing`.

---

### 📂 [Day 2: ERPNext Hiring System](Day%20-%202%20ERPNext-Hiring-System/)
**Focus:** Building a complete **Candidate Onboarding Module** with Automation.

**Key Features Built:**
1.  **Duplicate Prevention (Client Script):** - JavaScript logic to stop duplicate Email/Phone entries instantly.
    - Shows dynamic error popups with existing IDs.
2.  **Workflow Automation:** - Created Custom Workflow: `Pending` → `Shortlisted` → `Joined`.
    - Configured logic so only specific roles can approve.
3.  **Server-Side Automation (Python):** - Wrote Server Script to **Auto-Create a Laptop Setup Task** for the IT team when a candidate joins.
    - Added validation to prevent duplicate task creation.
4.  **Security:** - Created `Talent Acquisition` Role with strict permission levels (No Delete access).

**Techniques Used:** `frappe.ui.form.on`, `frappe.get_doc`, `frappe.db.exists`, `Jinja Templating`.

---

## 🛠️ Tech Stack
- **Languages:** Python, JavaScript
- **Framework:** Frappe / ERPNext v15
- **Database:** MariaDB
- **Tools:** Git, VS Code, Postman

---

---
*Author: Shubham*X