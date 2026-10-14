# ⚡ FreelanceFlow

A lightweight, full-stack client and project management application built for freelancers to track deliverables, monitor deadlines, and analyze income. Built with **Python (Flask)**, **SQLite**, and **Tailwind CSS**.

🔗 **Live Demo:** [armint13.pythonanywhere.com](https://armint13.pythonanywhere.com/)

---

## 🚀 Features

- **Client Directory**: Store and manage client contact details.
- **Project Tracking**: Associate projects with specific clients, assign budgets, set deadlines, and track lifecycle statuses (`pending`, `in_progress`, `completed`).
- **Live Financial Analytics**: Real-time aggregation of total pipeline value versus realized income.
- **Smart Filtering**: Filter projects dynamically by status (`pending`, `in_progress`, `completed`).
- **Data Export**: One-click CSV export for offline accounting and reporting.
- **RESTful Endpoints**: Full CRUD architecture with relational data constraints.
- **Responsive Web Dashboard**: Single-page dark mode UI using asynchronous Fetch API calls and Tailwind CSS.
- **Automated Test Suite**: Built-in integration tests covering API behavior and business logic using `unittest`.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask
- **Database**: SQLite3 (Foreign key constraints with cascading deletes)
- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS (via CDN)
- **Testing**: Python `unittest`, Flask Test Client
- **Deployment**: PythonAnywhere
- **Version Control**: Git & GitHub

---

## 📁 Project Structure

```text
FreelanceFlow/
│
├── database.py          # SQLite connection and schema initializers
├── app.py               # Flask application and REST API endpoints
├── test_app.py          # Automated integration test suite
├── requirements.txt     # Python project dependencies
├── .gitignore           # Git ignore patterns (DB, environments, cache)
├── README.md            # Project documentation
│
└── templates/
    └── index.html       # Web dashboard interface
```

---

## ⚙️ Getting Started (Local Development)

### 1. Clone the repository
```bash
git clone [https://github.com/armint13/FreelanceFlow.git](https://github.com/armint13/FreelanceFlow.git)
cd FreelanceFlow
```

### 2. Set up a virtual environment
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

Open your browser and navigate to:
```text
[http://127.0.0.1:5000](http://127.0.0.1:5000)
```

---

## 🧪 Running Tests

Execute the automated test suite to verify endpoints and database behavior:

```bash
python -m unittest test_app.py
```

---

## 📡 API Reference

### Clients
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/clients` | Retrieve all clients |
| `POST` | `/clients` | Create a new client record |

### Projects
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/projects` | Retrieve all projects (Supports `?status=` query filter) |
| `POST` | `/projects` | Create a new project under a client |
| `PATCH` | `/projects/<id>` | Update status of an existing project |
| `DELETE` | `/projects/<id>` | Remove a project record |
| `GET` | `/projects/export/csv` | Download complete project list as a CSV spreadsheet |

### Financial Analytics
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/stats/income` | Calculate total budget and realized income |

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).