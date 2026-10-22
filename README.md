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




## 📄 License & Attribution
Developed as an academic Mini-Project for Computer Science & Artificial Intelligence / Machine Learning coursework.
