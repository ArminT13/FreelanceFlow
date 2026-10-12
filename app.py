from flask import Flask, request, jsonify
from database import get_connection, init_db

app = Flask(__name__)

# Ensure tables exist on startup
init_db()

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to FreelanceFlow API!",
        "status": "running"
    })

# ----------------- CLIENT ENDPOINTS -----------------

@app.route("/clients", methods=["POST"])
def create_client():
    """Create a new client."""
    data = request.get_json()

    # Simple input validation
    if not data or not data.get("name"):
        return jsonify({"error": "Field 'name' is required"}), 400

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO clients (name, email, phone) VALUES (?, ?, ?)",
                (name, email, phone)
            )
            conn.commit()
            new_id = cursor.lastrowid

        return jsonify({
            "message": "Client created successfully",
            "client_id": new_id
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/clients", methods=["GET"])
def get_clients():
    """Retrieve all clients."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients ORDER BY created_at DESC")
        rows = cursor.fetchall()

        # Convert sqlite rows into a list of regular Python dicts
        clients_list = [dict(row) for row in rows]

    return jsonify(clients_list), 200

import sqlite3

# ----------------- PROJECT ENDPOINTS -----------------

@app.route("/projects", methods=["POST"])
def create_project():
    """Create a new project linked to a client."""
    data = request.get_json()

    if not data or not data.get("title") or not data.get("client_id"):
        return jsonify({"error": "Fields 'title' and 'client_id' are required"}), 400

    client_id = data.get("client_id")
    title = data.get("title")
    budget = data.get("budget", 0.0)
    status = data.get("status", "in_progress")
    deadline = data.get("deadline")

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO projects (client_id, title, budget, status, deadline)
                VALUES (?, ?, ?, ?, ?)
            """, (client_id, title, budget, status, deadline))
            conn.commit()
            project_id = cursor.lastrowid

        return jsonify({
            "message": "Project created successfully",
            "project_id": project_id
        }), 201

    except sqlite3.IntegrityError:
        # If client_id doesn't exist in clients table
        return jsonify({"error": "Invalid client_id. Client does not exist."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/projects", methods=["GET"])
def get_projects():
    """Retrieve all projects with their client information."""
    with get_connection() as conn:
        cursor = conn.cursor()
        # Using JOIN to fetch the client's name directly with the project
        cursor.execute("""
            SELECT 
                p.id, p.title, p.budget, p.status, p.deadline,
                c.id AS client_id, c.name AS client_name
            FROM projects p
            JOIN clients c ON p.client_id = c.id
            ORDER BY p.id DESC
        """)
        rows = cursor.fetchall()
        projects_list = [dict(row) for row in rows]

    return jsonify(projects_list), 200


# ----------------- STATS / INCOME ENDPOINT -----------------

@app.route("/stats/income", methods=["GET"])
def get_income_stats():
    """Calculate total expected budget and realized income from completed projects."""
    with get_connection() as conn:
        cursor = conn.cursor()

        # Total potential budget across all projects
        cursor.execute("SELECT COALESCE(SUM(budget), 0) AS total FROM projects")
        total_budget = cursor.fetchone()["total"]

        # Realized income (only completed projects)
        cursor.execute("SELECT COALESCE(SUM(budget), 0) AS realized FROM projects WHERE status = 'completed'")
        realized_income = cursor.fetchone()["realized"]

    return jsonify({
        "total_budget": total_budget,
        "realized_income": realized_income
    }), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)