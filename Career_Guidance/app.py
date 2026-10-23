"""
AI-Based Smart Career Guidance and Skill Recommendation System
Main Flask Application Server
"""

import os
import json
import joblib
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort

import database
from roadmap_data import CAREER_PROFILES, analyze_skill_gap

# Initialize Flask Application
app = Flask(__name__)
app.secret_key = "career-ai-super-secret-key-change-in-prod"

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "career_model.pkl")
META_PATH = os.path.join(BASE_DIR, "models", "feature_meta.pkl")

# Global ML Artifacts
model = None
feature_meta = None


def load_ml_model():
    """Loads the serialized ML model and feature metadata, auto-training if missing."""
    global model, feature_meta
    if not os.path.exists(MODEL_PATH) or not os.path.exists(META_PATH):
        print("[*] Model files not found. Auto-training now...")
        import train_model
        train_model.train_and_evaluate()

    model = joblib.load(MODEL_PATH)
    feature_meta = joblib.load(META_PATH)
    print(f"[*] ML Model loaded successfully! Classes: {model.classes_}")


# Initialize Database & Model on startup
with app.app_context():
    database.init_db()
    load_ml_model()


# Mapping from form skill checkbox codes to human-friendly skill names
SKILL_MAP = {
    "skill_python": "Python",
    "skill_java": "Java",
    "skill_cpp": "C++",
    "skill_javascript": "JavaScript",
    "skill_sql": "SQL",
    "skill_html_css": "HTML5 / CSS3",
    "skill_machine_learning": "Machine Learning",
    "skill_data_analysis": "Data Analysis",
    "skill_network_security": "Network Security",
    "skill_linux_git": "Linux & Git",
    "skill_cloud_basics": "Cloud Basics"
}


# ============================================================================
# Web Routes
# ============================================================================

@app.route("/")
def index():
    """Landing Page displaying project overview and real-time database stats."""
    stats = database.get_summary_stats()
    return render_template("index.html", stats=stats)


@app.route("/assess", methods=["GET", "POST"])
def assess():
    """
    Assessment Form Handler:
    - GET: Renders the assessment questionnaire with demo presets.
    - POST: Validates inputs, feeds features to ML model, analyzes skill gap,
            persists to SQLite, and redirects to results dashboard.
    """
    if request.method == "GET":
        return render_template("assess.html")

    # Form Extraction & Validation
    student_name = request.form.get("student_name", "").strip()
    email = request.form.get("email", "").strip()
    education_level = request.form.get("education_level", "").strip()
    primary_interest = request.form.get("primary_interest", "").strip()

    if not student_name or not education_level or not primary_interest:
        flash("Please fill in all required fields (Name, Education, Primary Interest).", "danger")
        return redirect(url_for("assess"))

    try:
        def get_score(field_name, default=3):
            val = request.form.get(field_name, default)
            try:
                return max(1, min(5, int(val)))
            except (ValueError, TypeError):
                return default

        # 1. Academic Strengths
        math_score = get_score("math_score")
        programming_score = get_score("programming_score")
        data_structures_score = get_score("data_structures_score")
        networking_score = get_score("networking_score")
        web_technologies_score = get_score("web_technologies_score")
        cybersecurity_score = get_score("cybersecurity_score")
        database_score = get_score("database_score")

        # 2. Domain Interests
        interest_software = get_score("interest_software")
        interest_data = get_score("interest_data")
        interest_ai_ml = get_score("interest_ai_ml")
        interest_security = get_score("interest_security")
        interest_web = get_score("interest_web")

        # 3. Technical Skills
        selected_skills = request.form.getlist("skills")
        skill_python = 1 if "skill_python" in selected_skills else 0
        skill_java = 1 if "skill_java" in selected_skills else 0
        skill_cpp = 1 if "skill_cpp" in selected_skills else 0
        skill_javascript = 1 if "skill_javascript" in selected_skills else 0
        skill_sql = 1 if "skill_sql" in selected_skills else 0
        skill_html_css = 1 if "skill_html_css" in selected_skills else 0
        skill_machine_learning = 1 if "skill_machine_learning" in selected_skills else 0
        skill_data_analysis = 1 if "skill_data_analysis" in selected_skills else 0
        skill_network_security = 1 if "skill_network_security" in selected_skills else 0
        skill_linux_git = 1 if "skill_linux_git" in selected_skills else 0
        skill_cloud_basics = 1 if "skill_cloud_basics" in selected_skills else 0

        # 4. Aptitude & Soft Skills
        problem_solving_score = get_score("problem_solving_score")
        abstract_thinking_score = get_score("abstract_thinking_score")
        creative_design_score = get_score("creative_design_score")
        system_architecture_score = get_score("system_architecture_score")

        # Build feature dictionary matching trained model features
        feature_dict = {
            "math_score": math_score,
            "programming_score": programming_score,
            "data_structures_score": data_structures_score,
            "networking_score": networking_score,
            "web_technologies_score": web_technologies_score,
            "cybersecurity_score": cybersecurity_score,
            "database_score": database_score,
            "interest_software": interest_software,
            "interest_data": interest_data,
            "interest_ai_ml": interest_ai_ml,
            "interest_security": interest_security,
            "interest_web": interest_web,
            "skill_python": skill_python,
            "skill_java": skill_java,
            "skill_cpp": skill_cpp,
            "skill_javascript": skill_javascript,
            "skill_sql": skill_sql,
            "skill_html_css": skill_html_css,
            "skill_machine_learning": skill_machine_learning,
            "skill_data_analysis": skill_data_analysis,
            "skill_network_security": skill_network_security,
            "skill_linux_git": skill_linux_git,
            "skill_cloud_basics": skill_cloud_basics,
            "problem_solving_score": problem_solving_score,
            "abstract_thinking_score": abstract_thinking_score,
            "creative_design_score": creative_design_score,
            "system_architecture_score": system_architecture_score
        }

        # Vectorize via Pandas DataFrame
        input_df = pd.DataFrame([feature_dict])[feature_meta["feature_names"]]

        # Predict using real Machine Learning model
        probabilities = model.predict_proba(input_df)[0]
        classes = model.classes_

        # Map classes to percentages
        scores_dict = {
            cls: round(float(prob) * 100, 1)
            for cls, prob in zip(classes, probabilities)
        }

        # Identify top predicted career
        top_career = max(scores_dict, key=scores_dict.get)
        match_score = scores_dict[top_career]

        # Analyze Skill Gap against domain requirements
        human_readable_skills = [
            SKILL_MAP[s] for s in selected_skills if s in SKILL_MAP
        ]
        gap_results = analyze_skill_gap(top_career, human_readable_skills)

        # Persist Assessment in SQLite
        assessment_id = database.save_assessment(
            student_name=student_name,
            email=email,
            education_level=education_level,
            primary_interest=primary_interest,
            inputs_dict=feature_dict,
            predicted_career=top_career,
            match_score=match_score,
            all_scores_dict=scores_dict,
            owned_skills=gap_results["owned_skills"],
            missing_skills=gap_results["missing_skills"]
        )

        flash("Assessment analyzed successfully by Machine Learning model!", "success")
        return redirect(url_for("results", assessment_id=assessment_id))

    except Exception as e:
        flash(f"An error occurred while evaluating your profile: {str(e)}", "danger")
        return redirect(url_for("assess"))


@app.route("/results/<int:assessment_id>")
def results(assessment_id):
    """Results Dashboard displaying recommendations, scores, skill gap, and roadmap."""
    record = database.get_assessment_by_id(assessment_id)
    if not record:
        abort(404)

    predicted_career = record["predicted_career"]
    profile = CAREER_PROFILES.get(predicted_career, CAREER_PROFILES["Software Developer"])

    # Re-verify skill gap using stored owned/missing skills
    gap = {
        "owned_skills": record["owned_skills"],
        "missing_skills": record["missing_skills"],
        "total_required": len(profile["required_skills"]),
        "owned_count": len(record["owned_skills"]),
        "missing_count": len(record["missing_skills"])
    }
    total_req = gap["total_required"]
    pct = round((gap["owned_count"] / total_req) * 100) if total_req > 0 else 0
    if pct >= 75:
        gap["readiness_status"] = "Advanced Readiness — Minor gaps to close"
    elif pct >= 45:
        gap["readiness_status"] = "Moderate Foundation — Key technical skills needed"
    else:
        gap["readiness_status"] = "Early Explorer — Follow the 4-phase roadmap"

    # Sort all career scores descending for clean chart presentation
    sorted_scores = sorted(
        record["all_scores"].items(),
        key=lambda item: item[1],
        reverse=True
    )

    return render_template(
        "results.html",
        record=record,
        profile=profile,
        gap=gap,
        sorted_scores=sorted_scores
    )


@app.route("/history")
def history():
    """Historical Log of all student assessments stored in SQLite."""
    assessments_list = database.get_all_assessments(limit=100)
    return render_template("history.html", assessments=assessments_list)


@app.route("/about")
def about():
    """Technical Overview explaining ML algorithm, dataset, and system limitations."""
    return render_template("about.html", meta=feature_meta)


# ============================================================================
# RESTful API Endpoint
# ============================================================================

@app.route("/api/predict", methods=["POST"])
def api_predict():
    """
    JSON API endpoint for programmatic inference.
    Accepts JSON payload with 27 features and returns top career and probabilities.
    """
    try:
        data = request.get_json(force=True)
        input_df = pd.DataFrame([data])[feature_meta["feature_names"]]
        probabilities = model.predict_proba(input_df)[0]
        classes = model.classes_

        scores = {cls: round(float(prob) * 100, 2) for cls, prob in zip(classes, probabilities)}
        top_career = max(scores, key=scores.get)

        return jsonify({
            "status": "success",
            "recommended_career": top_career,
            "match_score": scores[top_career],
            "all_scores": scores
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


# ============================================================================
# Error Handlers
# ============================================================================

@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


# ============================================================================
# Entry Point
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 65)
    print("  AI-BASED CAREER GUIDANCE & SKILL RECOMMENDATION SYSTEM")
    print("  Server running on http://127.0.0.1:5000")
    print("  Press Ctrl+C to terminate server")
    print("=" * 65 + "\n")
    app.run(host="127.0.0.1", port=5000, debug=False)
