import unittest
import json
import sqlite3
import app as main_app
import database

class FreelanceFlowTestCase(unittest.TestCase):

    def setUp(self):
        """Set up an isolated test environment before each test method runs."""
        # Use an isolated test database so production data remains intact
        database.DB_NAME = "test_freelance.db"
        database.init_db()

        # Configure Flask test client
        main_app.app.config["TESTING"] = True
        self.client = main_app.app.test_client()

    def tearDown(self):
        """Clean up the test database after each test method finishes."""
        import os
        if os.path.exists("test_freelance.db"):
            try:
                os.remove("test_freelance.db")
            except PermissionError:
                pass

    def test_home_page(self):
        """Ensure dashboard loads successfully."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_create_client_success(self):
        """Verify client creation endpoint with valid data."""
        payload = {
            "name": "Acme Agency",
            "email": "contact@acme.com",
            "phone": "123456789"
        }
        response = self.client.post(
            "/clients",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("client_id", data)

    def test_create_client_validation_error(self):
        """Verify 400 Bad Request when mandatory 'name' field is missing."""
        payload = {"email": "invalid@acme.com"}
        response = self.client.post(
            "/clients",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    def test_create_project_and_income_stats(self):
        """Test full lifecycle: add client, create completed project, verify income stats."""
        # 1. Add a client
        client_res = self.client.post(
            "/clients",
            data=json.dumps({"name": "Beta Corp", "email": "beta@corp.com"}),
            content_type="application/json"
        )
        client_id = client_res.get_json()["client_id"]

        # 2. Add a completed project with 2500 budget
        project_res = self.client.post(
            "/projects",
            data=json.dumps({
                "client_id": client_id,
                "title": "Backend Migration",
                "budget": 2500.0,
                "status": "completed",
                "deadline": "2026-12-01"
            }),
            content_type="application/json"
        )
        self.assertEqual(project_res.status_code, 201)

        # 3. Check income stats
        stats_res = self.client.get("/stats/income")
        self.assertEqual(stats_res.status_code, 200)
        stats = stats_res.get_json()
        self.assertEqual(stats["total_budget"], 2500.0)
        self.assertEqual(stats["realized_income"], 2500.0)

    def test_export_csv(self):
        """Ensure CSV export endpoint returns valid response with appropriate headers."""
        response = self.client.get("/projects/export/csv")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "text/csv; charset=utf-8")
        self.assertIn("freelanceflow_projects.csv", response.headers["Content-Disposition"])


if __name__ == "__main__":
    unittest.main()