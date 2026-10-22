# AI-Based Smart Career Guidance and Skill Recommendation System

An end-to-end Machine Learning web application designed to evaluate a student's academic performance, domain passions, and current skill set to recommend high-confidence career trajectories among five major computer science fields:
1. **Software Developer**
2. **Data Analyst**
3. **AI/ML Engineer**
4. **Cybersecurity Analyst**
5. **Web Developer**

The system provides matching confidence scores, dynamic skill-gap analysis (skills owned vs. missing skills), an industry-standard 4-phase learning roadmap, and persistent assessment logs in an SQLite database.

---

## 🌟 Key Features

1. **Modern, Responsive Web Interface**: Glassmorphism aesthetic, clean typography, responsive mobile-first navigation, and accessible input controls.
2. **Real Machine Learning Model**: Trained on a 1,500-sample balanced dataset using Scikit-Learn's **Random Forest Classifier** achieving **98% test accuracy**.
3. **Calibrated Match Confidence**: Uses `predict_proba()` to compute probabilistic confidence rankings across all 5 career tracks.
4. **Automated Skill-Gap Analysis**: Immediately separates existing capabilities from critical industry prerequisites.
5. **Structured 24-Week Learning Roadmap**: A 4-phase sequential curriculum detailing topics, milestone projects, and curated free resources (Harvard CS50, freeCodeCamp, Kaggle, TryHackMe).
6. **SQLite Persistence**: Automatically saves student assessments, confidence percentages, and skill gaps to `instance/career_guidance.db`.
7. **One-Click Demo Presets**: Pre-configured student profiles on the assessment page (*AI/ML Engineer*, *Web Developer*, *Cybersecurity Analyst*, *Data Analyst*, *Software Developer*) for fast, flawless college viva demonstrations.
8. **Print & PDF Export**: Clean styling configured with CSS `@media print` rules for generating professional career recommendation reports.

---

## 🛠️ Technology Stack

| Component | Technology | Version | Purpose |
| :--- | :--- | :--- | :--- |
| **Backend Framework** | Python / Flask | 3.1+ | Routing, MVC controllers, and session handling |
| **Machine Learning** | Scikit-Learn | 1.9+ | Random Forest model, evaluation & metrics |
| **Data Processing** | Pandas & NumPy | 3.1+ / 2.5+ | Feature engineering, vectorization & matrix operations |
| **Persistence** | SQLite3 & Joblib | Built-in / 1.6+ | Relational storage & model serialization |
| **Frontend** | HTML5, CSS3, JS | Modern ES6 | Responsive UI, sliders, demo presets, search filter |

---

## 📁 Project Directory Structure

```
Career_Guidance/
├── app.py                     # Flask server with routes, validation, and prediction logic
├── train_model.py             # Model training, benchmarking (CV), and export script
├── database.py                # SQLite database helper functions
├── roadmap_data.py            # Domain knowledge base: skills, roadmaps, and resources
├── requirements.txt           # Project Python dependencies
├── README.md                  # Project documentation & college viva guide
├── data/
│   ├── generate_dataset.py    # Balanced dataset generator script
│   └── career_dataset.csv     # 1,500 balanced student profile records
├── models/
│   ├── career_model.pkl       # Serialized Random Forest model artifact
│   └── feature_meta.pkl       # Serialized feature names and evaluation metrics
├── instance/
│   └── career_guidance.db     # SQLite database (auto-created on first run)
├── static/
│   ├── css/
│   │   └── style.css          # Design system, cards, badges, timeline, print styles
│   └── js/
│       └── main.js            # Live slider display, demo presets, search filter
└── templates/
    ├── base.html              # Base layout with navbar and footer
    ├── index.html             # Landing page with stats and career showcase
    ├── assess.html            # Assessment form with demo presets
    ├── results.html           # Recommendation dashboard, skill gap, and roadmap
    ├── history.html           # Historical assessments table with search
    ├── about.html             # ML architecture, mathematical formulation & limitations
    ├── 404.html               # Custom 404 error page
    └── 500.html               # Custom 500 server error page
```

---

## 🚀 Quick Start Guide (Windows)

Follow these exact Windows commands in **PowerShell** or **Command Prompt**:

### Step 1: Clone or Navigate to Project Folder
```powershell
cd c:\Users\Arun\OneDrive\Desktop\Career_Guidance
```

### Step 2: Install Python Dependencies
```powershell
py -m pip install -r requirements.txt
```

### Step 3: (Optional) Re-generate Dataset & Re-train Model
*Note: The dataset and trained models are already pre-generated and ready.*
```powershell
py data/generate_dataset.py
py train_model.py
```

### Step 4: Run the Flask Web Application
```powershell
py app.py
```

### Step 5: Open in Your Browser
Visit your browser at:
```
http://127.0.0.1:5000
```

---

## 🧪 Testing the Application (Sample Student Profiles)

To test the application, navigate to `http://127.0.0.1:5000/assess`. You can click any of the **Quick Demo Presets** or manually input one of the test profiles below:

### Sample 1: The AI/ML Engineer Profile
- **Name**: Priya Sharma
- **Education**: Bachelor's in CS / IT
- **Curiosity Focus**: Artificial Intelligence & Deep Learning
- **Academic Strengths**: Math (5/5), Programming (5/5), DSA (4/5), Databases (4/5), Networks (2/5)
- **Domain Interests**: AI/ML (5/5), Data Science (5/5), Software (3/5)
- **Skills Selected**: Python, Machine Learning, Data Analytics, SQL, Linux & Git
- **Soft Skills**: Problem Solving (5/5), Abstract Thinking (5/5)
- **Expected Prediction**: **AI/ML Engineer** (~90%+ Confidence)

### Sample 2: The Cybersecurity Analyst Profile
- **Name**: Karan Mehta
- **Education**: Bachelor's in IT
- **Curiosity Focus**: Ethical Hacking & Network Security
- **Academic Strengths**: Networks (5/5), Cybersecurity (5/5), Programming (4/5), Math (3/5)
- **Domain Interests**: Security & Hacking (5/5), Software (3/5), Web (2/5)
- **Skills Selected**: Network Security, Linux & Git, Python, Cloud Basics
- **Soft Skills**: Problem Solving (5/5), Abstract Thinking (4/5)
- **Expected Prediction**: **Cybersecurity Analyst** (~85%+ Confidence)

### Sample 3: The Full-Stack Web Developer Profile
- **Name**: Rahul Verma
- **Education**: Bachelor's in Computer Science
- **Curiosity Focus**: Web Applications & Frontend Design
- **Academic Strengths**: Web Technologies (5/5), Programming (4/5), Databases (4/5)
- **Domain Interests**: Web Development (5/5), Software (4/5), AI/ML (2/5)
- **Skills Selected**: JavaScript, HTML/CSS, Python, SQL, Cloud Basics
- **Soft Skills**: Creative Design (5/5), Problem Solving (4/5)
- **Expected Prediction**: **Web Developer** (~88%+ Confidence)

---

## 🧠 Machine Learning Model Details

### 1. Algorithm Selection: Random Forest Classifier
Random Forest is an ensemble meta-estimator that fits multiple decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

- **Number of Estimators**: 150 Decision Trees (`n_estimators=150`)
- **Max Depth**: 12
- **Split Criterion**: Gini Impurity
- **Bootstrap Sampling**: True

### 2. Mathematical Split Formula (Gini Impurity)
\[
I_G(p) = 1 - \sum_{i=1}^{C} (p_i)^2
\]
Where \(C = 5\) target careers, and \(p_i\) is the probability of an element being classified to class \(i\).

### 3. Model Benchmark Results (5-Fold Cross Validation)
| Model | Cross-Validation Accuracy | Test Set Accuracy | Generalization |
| :--- | :---: | :---: | :--- |
| **Random Forest (Champion)** | **99.08%** | **98.00%** | Exceptional; low variance |
| **Logistic Regression** | 99.42% | 97.67% | Linear decision boundaries |
| **Decision Tree** | 93.75% | 93.33% | Prone to overfitting |

### 4. Top Feature Importances
From model training, the most influential features determining career placement are:
1. `interest_ai_ml` (11.36%)
2. `interest_web` (9.69%)
3. `interest_data` (9.01%)
4. `interest_security` (8.64%)
5. `interest_software` (7.27%)
6. `cybersecurity_score` (6.75%)
7. `creative_design_score` (6.16%)

---

## ⚠️ Real-World Limitations

1. **Self-Reporting Bias**: The assessment relies on self-reported ratings (1 to 5). Subjective differences in self-perception may affect input consistency.
2. **Static Snapshot of Industry Requirements**: Emerging tools and frameworks evolve quickly. The model and knowledge base should be retrained periodically.
3. **Advisory Decision Support**: The recommendation is intended as an informative guideline to assist students, not a rigid constraint on their potential.

---

## 🎓 College Mini-Project Viva Q&A Guide

Prepare these frequently asked questions for your project review:

### Q1: What is the core objective of this mini-project?
**Answer**: To bridge the gap between academic education and industry expectations by providing students with an automated, data-driven career counseling system. It uses machine learning to classify student competency profiles into suitable career tracks and provides personalized skill-gap roadmaps.

### Q2: Why did you choose Random Forest over a single Decision Tree?
**Answer**: A single Decision Tree is prone to high variance and overfitting because it creates deep, complex decision splits on specific training samples. Random Forest creates an ensemble of 150 diverse trees through bagging (bootstrap aggregating) and random feature subset selection. Aggregating their predictions cancels out individual errors, resulting in higher generalization and smoother `predict_proba()` probability outputs.

### Q3: How do you calculate the match percentage score?
**Answer**: The matching score is extracted directly from the model's `predict_proba()` method. It calculates the proportion of trees in the Random Forest ensemble that voted for that specific career class, multiplied by 100.

### Q4: How is the Skill Gap Analysis performed?
**Answer**: In `roadmap_data.py`, we maintain an industry-standard skill requirement list for each of the five career domains. When a career is predicted, the student's selected skills are compared against the required skills using set operations to identify matching ("Owned") skills and missing ("Gap") skills.

### Q5: How is user data stored and retrieved?
**Answer**: We use SQLite (`instance/career_guidance.db`) with an `assessments` table. When an assessment is submitted, the student demographics, raw input feature JSON, predicted career, match score, and skill gaps are inserted and indexed by an auto-incrementing ID.

### Q6: What steps did you take to prevent data leakage during training?
**Answer**: We separated features \(X\) from the target label \(y\), and performed a stratified 80/20 train-test split (`stratify=y`) before evaluating model performance. The test accuracy (98%) was evaluated exclusively on unseen test data.

---

## 📄 License & Attribution
Developed as an academic Mini-Project for Computer Science & Artificial Intelligence / Machine Learning coursework.
