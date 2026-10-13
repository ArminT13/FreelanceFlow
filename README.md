# ⚡ FreelanceFlow

A lightweight, full-stack project and client management tool designed for freelancers. Built with **Python (Flask)**, **SQLite**, and styled with **Tailwind CSS**.

---

## 🚀 Features

- **Client Directory**: Track clients with direct contact information.
- **Project Tracking**: Manage deadlines, budgets, and project statuses (`pending`, `in_progress`, `completed`).
- **Financial Analytics**: Real-time calculation of total project pipeline and realized income.
- **RESTful Architecture**: Clean, modular API endpoints supporting standard CRUD operations.
- **Modern Dashboard**: Responsive, dark-mode single-page dashboard communicating asynchronously via the Fetch API.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask
- **Database**: SQLite3 (Relational schema with foreign keys and cascade rules)
- **Frontend**: HTML5, Vanilla JavaScript (Async/Await), Tailwind CSS

---

## 📁 Project Structure

```text
FreelanceFlow/
│
├── database.py       # SQLite connection setup and schema initialization
├── app.py            # Flask application routes, REST API, and view handler
├── templates/
│   └── index.html    # Single-page dashboard UI (Tailwind CSS)
├── requirements.txt  # Project dependencies
├── .gitignore        # Ignored files (virtual environments, database binaries)
└── README.md         # Project documentation

1. Clone the repository
Bash
git clone [https://github.com/](https://github.com/)<YOUR-USERNAME>/FreelanceFlow.git
cd FreelanceFlow

2. Create and activate a virtual environment
Bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
Bash
pip install -r requirements.txt

4. Run the application
Bash
python app.py

Open your browser and navigate to:

Plaintext
[http://127.0.0.1:5000](http://127.0.0.1:5000)

📄 License
This project is open-source and available under the MIT License.