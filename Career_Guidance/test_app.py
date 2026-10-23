"""
Automated End-to-End Test Suite for Career Guidance System.
Verifies Model Inference, Database Operations, Roadmap Logic, and Flask Routes.
"""

import unittest
import json
from app import app
import database
from roadmap_data import analyze_skill_gap, CAREER_PROFILES


class TestCareerGuidanceSystem(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_01_roadmap_and_skill_gap(self):
        """Test skill gap logic against known careers."""
        user_skills = ["Python", "SQL", "Machine Learning"]
        gap = analyze_skill_gap("AI/ML Engineer", user_skills)
        
        self.assertIn("Python", [s.split()[0] for s in gap["owned_skills"]])
        self.assertGreater(gap["total_required"], 0)
        self.assertGreaterEqual(gap["match_percentage"], 0)
        self.assertIn("readiness_status", gap)
        print("  [PASS] Skill Gap Analysis Engine verified.")

    def test_02_database_operations(self):
        """Test SQLite database insertion and querying."""
        test_id = database.save_assessment(
            student_name="Unit Test Student",
            email="unittest@example.com",
            education_level="Bachelor's in CS / IT",
            primary_interest="AI & Machine Learning",
            inputs_dict={"test_feature": 1},
            predicted_career="AI/ML Engineer",
            match_score=94.5,
            all_scores_dict={"AI/ML Engineer": 94.5, "Data Analyst": 5.5},
            owned_skills=["Python", "SQL"],
            missing_skills=["Deep Learning"]
        )

        record = database.get_assessment_by_id(test_id)
        self.assertIsNotNone(record)
        self.assertEqual(record["student_name"], "Unit Test Student")
        self.assertEqual(record["predicted_career"], "AI/ML Engineer")
        self.assertEqual(record["match_score"], 94.5)

        stats = database.get_summary_stats()
        self.assertGreaterEqual(stats["total_assessments"], 1)
        print("  [PASS] SQLite Database persistence & retrieval verified.")

    def test_03_http_routes(self):
        """Test Flask HTTP routes."""
        # 1. Home route
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Discover Your Ideal Tech Career Path", res.data)

        # 2. Assess GET route
        res = self.client.get("/assess")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Comprehensive Student Assessment", res.data)

        # 3. Assess POST route (Simulate Student Submission)
        payload = {
            "student_name": "Karan Mehta",
            "email": "karan@example.com",
            "education_level": "Bachelor's in IT",
            "primary_interest": "Ethical Hacking & Network Security",
            "math_score": "3",
            "programming_score": "4",
            "data_structures_score": "3",
            "networking_score": "5",
            "web_technologies_score": "3",
            "cybersecurity_score": "5",
            "database_score": "3",
            "interest_software": "3",
            "interest_data": "2",
            "interest_ai_ml": "2",
            "interest_security": "5",
            "interest_web": "2",
            "skills": ["skill_network_security", "skill_linux_git", "skill_python"],
            "problem_solving_score": "5",
            "abstract_thinking_score": "4",
            "creative_design_score": "2",
            "system_architecture_score": "4"
        }
        res = self.client.post("/assess", data=payload, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        # Verify cybersecurity analyst was recommended
        self.assertIn(b"Cybersecurity Analyst", res.data)
        self.assertIn(b"Skill Gap Analysis", res.data)
        self.assertIn(b"Step-by-Step 4-Phase Learning Roadmap", res.data)

        # 4. History Route
        res = self.client.get("/history")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Karan Mehta", res.data)

        # 5. About Route
        res = self.client.get("/about")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Random Forest Classifier", res.data)

        # 6. 404 Route
        res = self.client.get("/non-existent-page-xyz")
        self.assertEqual(res.status_code, 404)
        self.assertIn(b"Page Not Found", res.data)

        print("  [PASS] All Flask HTTP Routes & Redirects verified.")

    def test_04_api_predict_route(self):
        """Test the RESTful JSON prediction API endpoint."""
        sample_features = {
            "math_score": 5,
            "programming_score": 5,
            "data_structures_score": 4,
            "networking_score": 2,
            "web_technologies_score": 2,
            "cybersecurity_score": 2,
            "database_score": 4,
            "interest_software": 3,
            "interest_data": 5,
            "interest_ai_ml": 5,
            "interest_security": 2,
            "interest_web": 2,
            "skill_python": 1,
            "skill_java": 0,
            "skill_cpp": 0,
            "skill_javascript": 0,
            "skill_sql": 1,
            "skill_html_css": 0,
            "skill_machine_learning": 1,
            "skill_data_analysis": 1,
            "skill_network_security": 0,
            "skill_linux_git": 1,
            "skill_cloud_basics": 0,
            "problem_solving_score": 5,
            "abstract_thinking_score": 5,
            "creative_design_score": 2,
            "system_architecture_score": 4
        }
        res = self.client.post(
            "/api/predict",
            data=json.dumps(sample_features),
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["recommended_career"], "AI/ML Engineer")
        self.assertGreater(data["match_score"], 50.0)
        print("  [PASS] RESTful JSON API prediction verified.")


if __name__ == "__main__":
    print("\n--- RUNNING AUTOMATED UNIT & INTEGRATION TESTS ---")
    unittest.main()
