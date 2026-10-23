"""
Dataset Generator for Career Guidance & Skill Recommendation System.
Generates a realistic, balanced, and statistically sound dataset (1,500 records)
across 5 career tracks with realistic correlations and natural noise.
"""

import os
import random
import csv

# Target career classes
CAREERS = [
    "Software Developer",
    "Data Analyst",
    "AI/ML Engineer",
    "Cybersecurity Analyst",
    "Web Developer"
]

# Feature definitions
FEATURE_COLUMNS = [
    # Academic & Subject Ratings (1-5)
    "math_score",
    "programming_score",
    "data_structures_score",
    "networking_score",
    "web_technologies_score",
    "cybersecurity_score",
    "database_score",
    # Domain Interests (1-5)
    "interest_software",
    "interest_data",
    "interest_ai_ml",
    "interest_security",
    "interest_web",
    # Technical Skills (0 or 1)
    "skill_python",
    "skill_java",
    "skill_cpp",
    "skill_javascript",
    "skill_sql",
    "skill_html_css",
    "skill_machine_learning",
    "skill_data_analysis",
    "skill_network_security",
    "skill_linux_git",
    "skill_cloud_basics",
    # Aptitude & Soft Skills (1-5)
    "problem_solving_score",
    "abstract_thinking_score",
    "creative_design_score",
    "system_architecture_score",
    # Target
    "career"
]


def clamp(val, min_val=1, max_val=5):
    """Clamps a rating between min_val and max_val."""
    return max(min_val, min(max_val, int(round(val))))


def sample_binary(prob):
    """Returns 1 with probability prob, else 0."""
    return 1 if random.random() < prob else 0


def generate_sample(career):
    """
    Generates a single student profile conditioned on their target career,
    incorporating realistic variations and occasional cross-domain skills.
    """
    row = {}

    if career == "Software Developer":
        # Strong programming, DSA, databases, OOP
        row["math_score"] = clamp(random.gauss(3.8, 0.7))
        row["programming_score"] = clamp(random.gauss(4.6, 0.5))
        row["data_structures_score"] = clamp(random.gauss(4.5, 0.5))
        row["networking_score"] = clamp(random.gauss(3.0, 0.9))
        row["web_technologies_score"] = clamp(random.gauss(3.2, 0.9))
        row["cybersecurity_score"] = clamp(random.gauss(2.7, 0.9))
        row["database_score"] = clamp(random.gauss(4.1, 0.7))

        row["interest_software"] = clamp(random.gauss(4.8, 0.4))
        row["interest_data"] = clamp(random.gauss(2.8, 0.9))
        row["interest_ai_ml"] = clamp(random.gauss(3.1, 0.9))
        row["interest_security"] = clamp(random.gauss(2.6, 0.8))
        row["interest_web"] = clamp(random.gauss(3.3, 0.9))

        row["skill_python"] = sample_binary(0.85)
        row["skill_java"] = sample_binary(0.80)
        row["skill_cpp"] = sample_binary(0.70)
        row["skill_javascript"] = sample_binary(0.40)
        row["skill_sql"] = sample_binary(0.85)
        row["skill_html_css"] = sample_binary(0.45)
        row["skill_machine_learning"] = sample_binary(0.20)
        row["skill_data_analysis"] = sample_binary(0.25)
        row["skill_network_security"] = sample_binary(0.15)
        row["skill_linux_git"] = sample_binary(0.85)
        row["skill_cloud_basics"] = sample_binary(0.50)

        row["problem_solving_score"] = clamp(random.gauss(4.5, 0.6))
        row["abstract_thinking_score"] = clamp(random.gauss(4.1, 0.7))
        row["creative_design_score"] = clamp(random.gauss(2.5, 0.8))
        row["system_architecture_score"] = clamp(random.gauss(4.4, 0.6))

    elif career == "Data Analyst":
        # Strong statistics/math, SQL, data analysis, spreadsheets
        row["math_score"] = clamp(random.gauss(4.4, 0.6))
        row["programming_score"] = clamp(random.gauss(3.5, 0.7))
        row["data_structures_score"] = clamp(random.gauss(2.9, 0.8))
        row["networking_score"] = clamp(random.gauss(2.2, 0.7))
        row["web_technologies_score"] = clamp(random.gauss(2.4, 0.8))
        row["cybersecurity_score"] = clamp(random.gauss(2.1, 0.7))
        row["database_score"] = clamp(random.gauss(4.7, 0.5))

        row["interest_software"] = clamp(random.gauss(2.7, 0.8))
        row["interest_data"] = clamp(random.gauss(4.8, 0.4))
        row["interest_ai_ml"] = clamp(random.gauss(3.4, 0.8))
        row["interest_security"] = clamp(random.gauss(2.0, 0.7))
        row["interest_web"] = clamp(random.gauss(2.5, 0.8))

        row["skill_python"] = sample_binary(0.80)
        row["skill_java"] = sample_binary(0.20)
        row["skill_cpp"] = sample_binary(0.15)
        row["skill_javascript"] = sample_binary(0.20)
        row["skill_sql"] = sample_binary(0.95)
        row["skill_html_css"] = sample_binary(0.25)
        row["skill_machine_learning"] = sample_binary(0.35)
        row["skill_data_analysis"] = sample_binary(0.95)
        row["skill_network_security"] = sample_binary(0.10)
        row["skill_linux_git"] = sample_binary(0.50)
        row["skill_cloud_basics"] = sample_binary(0.40)

        row["problem_solving_score"] = clamp(random.gauss(4.2, 0.6))
        row["abstract_thinking_score"] = clamp(random.gauss(3.8, 0.7))
        row["creative_design_score"] = clamp(random.gauss(3.6, 0.8))
        row["system_architecture_score"] = clamp(random.gauss(2.7, 0.8))

    elif career == "AI/ML Engineer":
        # Strong math, programming, ML algorithms, abstract thinking
        row["math_score"] = clamp(random.gauss(4.8, 0.4))
        row["programming_score"] = clamp(random.gauss(4.6, 0.5))
        row["data_structures_score"] = clamp(random.gauss(4.2, 0.6))
        row["networking_score"] = clamp(random.gauss(2.5, 0.8))
        row["web_technologies_score"] = clamp(random.gauss(2.6, 0.8))
        row["cybersecurity_score"] = clamp(random.gauss(2.4, 0.8))
        row["database_score"] = clamp(random.gauss(4.0, 0.7))

        row["interest_software"] = clamp(random.gauss(3.8, 0.7))
        row["interest_data"] = clamp(random.gauss(4.5, 0.6))
        row["interest_ai_ml"] = clamp(random.gauss(4.9, 0.3))
        row["interest_security"] = clamp(random.gauss(2.4, 0.8))
        row["interest_web"] = clamp(random.gauss(2.4, 0.8))

        row["skill_python"] = sample_binary(0.98)
        row["skill_java"] = sample_binary(0.35)
        row["skill_cpp"] = sample_binary(0.60)
        row["skill_javascript"] = sample_binary(0.20)
        row["skill_sql"] = sample_binary(0.85)
        row["skill_html_css"] = sample_binary(0.25)
        row["skill_machine_learning"] = sample_binary(0.95)
        row["skill_data_analysis"] = sample_binary(0.90)
        row["skill_network_security"] = sample_binary(0.12)
        row["skill_linux_git"] = sample_binary(0.85)
        row["skill_cloud_basics"] = sample_binary(0.60)

        row["problem_solving_score"] = clamp(random.gauss(4.7, 0.5))
        row["abstract_thinking_score"] = clamp(random.gauss(4.8, 0.4))
        row["creative_design_score"] = clamp(random.gauss(2.6, 0.8))
        row["system_architecture_score"] = clamp(random.gauss(4.1, 0.7))

    elif career == "Cybersecurity Analyst":
        # Strong networking, cybersecurity, linux, threat analysis
        row["math_score"] = clamp(random.gauss(3.3, 0.8))
        row["programming_score"] = clamp(random.gauss(3.7, 0.7))
        row["data_structures_score"] = clamp(random.gauss(3.2, 0.8))
        row["networking_score"] = clamp(random.gauss(4.8, 0.4))
        row["web_technologies_score"] = clamp(random.gauss(3.4, 0.8))
        row["cybersecurity_score"] = clamp(random.gauss(4.8, 0.4))
        row["database_score"] = clamp(random.gauss(3.4, 0.8))

        row["interest_software"] = clamp(random.gauss(3.0, 0.8))
        row["interest_data"] = clamp(random.gauss(2.3, 0.8))
        row["interest_ai_ml"] = clamp(random.gauss(2.7, 0.9))
        row["interest_security"] = clamp(random.gauss(4.9, 0.3))
        row["interest_web"] = clamp(random.gauss(2.8, 0.8))

        row["skill_python"] = sample_binary(0.80)
        row["skill_java"] = sample_binary(0.30)
        row["skill_cpp"] = sample_binary(0.55)
        row["skill_javascript"] = sample_binary(0.35)
        row["skill_sql"] = sample_binary(0.65)
        row["skill_html_css"] = sample_binary(0.35)
        row["skill_machine_learning"] = sample_binary(0.15)
        row["skill_data_analysis"] = sample_binary(0.25)
        row["skill_network_security"] = sample_binary(0.96)
        row["skill_linux_git"] = sample_binary(0.92)
        row["skill_cloud_basics"] = sample_binary(0.65)

        row["problem_solving_score"] = clamp(random.gauss(4.4, 0.6))
        row["abstract_thinking_score"] = clamp(random.gauss(3.9, 0.7))
        row["creative_design_score"] = clamp(random.gauss(2.2, 0.7))
        row["system_architecture_score"] = clamp(random.gauss(4.3, 0.6))

    elif career == "Web Developer":
        # Strong web tech, JS/HTML/CSS, visual design, databases
        row["math_score"] = clamp(random.gauss(3.0, 0.8))
        row["programming_score"] = clamp(random.gauss(4.1, 0.6))
        row["data_structures_score"] = clamp(random.gauss(3.3, 0.8))
        row["networking_score"] = clamp(random.gauss(3.1, 0.8))
        row["web_technologies_score"] = clamp(random.gauss(4.8, 0.4))
        row["cybersecurity_score"] = clamp(random.gauss(2.6, 0.8))
        row["database_score"] = clamp(random.gauss(3.9, 0.7))

        row["interest_software"] = clamp(random.gauss(3.8, 0.7))
        row["interest_data"] = clamp(random.gauss(2.3, 0.8))
        row["interest_ai_ml"] = clamp(random.gauss(2.4, 0.8))
        row["interest_security"] = clamp(random.gauss(2.5, 0.8))
        row["interest_web"] = clamp(random.gauss(4.9, 0.3))

        row["skill_python"] = sample_binary(0.60)
        row["skill_java"] = sample_binary(0.25)
        row["skill_cpp"] = sample_binary(0.15)
        row["skill_javascript"] = sample_binary(0.98)
        row["skill_sql"] = sample_binary(0.80)
        row["skill_html_css"] = sample_binary(0.99)
        row["skill_machine_learning"] = sample_binary(0.10)
        row["skill_data_analysis"] = sample_binary(0.18)
        row["skill_network_security"] = sample_binary(0.20)
        row["skill_linux_git"] = sample_binary(0.80)
        row["skill_cloud_basics"] = sample_binary(0.60)

        row["problem_solving_score"] = clamp(random.gauss(4.0, 0.6))
        row["abstract_thinking_score"] = clamp(random.gauss(3.4, 0.8))
        row["creative_design_score"] = clamp(random.gauss(4.7, 0.5))
        row["system_architecture_score"] = clamp(random.gauss(3.7, 0.7))

    row["career"] = career
    return row


def generate_dataset(total_records=1500, output_path="data/career_dataset.csv"):
    """Generates a balanced dataset and writes it to CSV."""
    random.seed(42)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    records_per_class = total_records // len(CAREERS)
    all_data = []

    for career in CAREERS:
        for _ in range(records_per_class):
            all_data.append(generate_sample(career))

    # Shuffle the dataset
    random.shuffle(all_data)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FEATURE_COLUMNS)
        writer.writeheader()
        writer.writerows(all_data)

    print(f"Successfully generated {len(all_data)} balanced records in: {output_path}")
    print(f"Careers: {CAREERS}")
    print(f"Records per career: {records_per_class}")
    return output_path


if __name__ == "__main__":
    generate_dataset()
