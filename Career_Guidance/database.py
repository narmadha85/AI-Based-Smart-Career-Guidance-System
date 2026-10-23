"""
SQLite Database Layer for AI-Based Career Guidance System.
Handles schema initialization, persistence of student assessments,
and retrieval of historical recommendations.
"""

import os
import json
import sqlite3
from datetime import datetime

DB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "instance")
DB_PATH = os.path.join(DB_DIR, "career_guidance.db")


def get_db_connection():
    """Returns a SQLite connection with row access by column name."""
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes the database schema if tables do not exist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            email TEXT,
            education_level TEXT NOT NULL,
            primary_interest TEXT,
            inputs_json TEXT NOT NULL,
            predicted_career TEXT NOT NULL,
            match_score REAL NOT NULL,
            all_scores_json TEXT NOT NULL,
            owned_skills_json TEXT,
            missing_skills_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()


def save_assessment(
    student_name: str,
    email: str,
    education_level: str,
    primary_interest: str,
    inputs_dict: dict,
    predicted_career: str,
    match_score: float,
    all_scores_dict: dict,
    owned_skills: list,
    missing_skills: list
) -> int:
    """Inserts a new student assessment record and returns its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO assessments (
            student_name,
            email,
            education_level,
            primary_interest,
            inputs_json,
            predicted_career,
            match_score,
            all_scores_json,
            owned_skills_json,
            missing_skills_json,
            created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student_name.strip(),
        (email or "").strip(),
        education_level,
        primary_interest,
        json.dumps(inputs_dict),
        predicted_career,
        round(float(match_score), 1),
        json.dumps(all_scores_dict),
        json.dumps(owned_skills),
        json.dumps(missing_skills),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    assessment_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return assessment_id


def get_assessment_by_id(assessment_id: int):
    """Retrieves an assessment by its primary key ID, parsing JSON fields."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM assessments WHERE id = ?", (assessment_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    data = dict(row)
    data["inputs"] = json.loads(data["inputs_json"]) if data["inputs_json"] else {}
    data["all_scores"] = json.loads(data["all_scores_json"]) if data["all_scores_json"] else {}
    data["owned_skills"] = json.loads(data["owned_skills_json"]) if data["owned_skills_json"] else []
    data["missing_skills"] = json.loads(data["missing_skills_json"]) if data["missing_skills_json"] else []
    return data


def get_all_assessments(limit: int = 100):
    """Retrieves recent assessments for the history dashboard."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, student_name, education_level, primary_interest,
               predicted_career, match_score, created_at
        FROM assessments
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_summary_stats():
    """Computes high-level statistics for home and dashboard pages."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM assessments")
    total_count = cursor.fetchone()[0]

    cursor.execute("""
        SELECT predicted_career, COUNT(*) as career_count
        FROM assessments
        GROUP BY predicted_career
        ORDER BY career_count DESC
        LIMIT 1
    """)
    top_row = cursor.fetchone()
    top_career = top_row["predicted_career"] if top_row else "AI/ML Engineer"

    cursor.execute("SELECT AVG(match_score) FROM assessments")
    avg_score_row = cursor.fetchone()[0]
    avg_score = round(avg_score_row, 1) if avg_score_row else 87.5

    conn.close()

    return {
        "total_assessments": total_count,
        "top_career": top_career,
        "avg_match_score": avg_score
    }
