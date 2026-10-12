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


if __name__ == "__main__":
    app.run(debug=True, port=5000)