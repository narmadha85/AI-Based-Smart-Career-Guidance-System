"""
Domain Knowledge Base: Career Profiles, Required Skills, and Learning Roadmaps.
This module powers the Skill Gap Analysis and Structured Learning Roadmaps
for the AI-Based Career Guidance System.
"""

CAREER_PROFILES = {
    "Software Developer": {
        "title": "Software Developer / Engineer",
        "category": "Software Engineering & Systems",
        "tagline": "Design, build, and maintain robust, scalable software applications and system architectures.",
        "icon": "code-slash",
        "badge_color": "#2563eb",
        "overview": (
            "Software Developers apply computer science fundamentals, design patterns, and programming languages "
            "to build software products ranging from desktop programs and mobile applications to enterprise systems. "
            "They focus on algorithm efficiency, object-oriented principles, modularity, and clean code."
        ),
        "required_skills": [
            "Python",
            "Java",
            "Data Structures & Algorithms",
            "SQL & Relational Databases",
            "Git & Version Control",
            "Object-Oriented Programming",
            "Operating Systems & Linux Basics",
            "Software Testing & Debugging"
        ],
        "optional_skills": [
            "Docker / Containerization",
            "CI/CD Pipelines",
            "System Design Basics",
            "Cloud Fundamentals (AWS/Azure)",
            "C++"
        ],
        "typical_roles": [
            "Software Development Engineer (SDE I)",
            "Backend Developer",
            "Application Developer",
            "Systems Software Engineer"
        ],
        "market_demand": "Very High",
        "avg_salary_range": "$75,000 - $125,000 / year (₹6 - 15 LPA for freshers in India)",
        "roadmap": [
            {
                "phase": "Phase 1: Computer Science & Programming Fundamentals",
                "duration": "Weeks 1 - 6",
                "focus": "Master core programming concepts and algorithm design.",
                "topics": [
                    "Master one core language (Python, Java, or C++) thoroughly",
                    "Understand Memory Management, Pointers/References, and OOP Principles",
                    "Data Structures: Arrays, Linked Lists, Stacks, Queues, Hash Tables",
                    "Algorithms: Sorting, Searching, Recursion, Time & Space Complexity (Big-O)"
                ],
                "milestone_project": "Build an in-memory Console Application (e.g., Bank Management System or Inventory Manager) using OOP."
            },
            {
                "phase": "Phase 2: Database Systems & Version Control",
                "duration": "Weeks 7 - 12",
                "focus": "Persistent storage, database optimization, and team development workflows.",
                "topics": [
                    "Relational Database Management (RDBMS): PostgreSQL or MySQL",
                    "SQL queries: Joins, Indexing, Transactions (ACID properties), Normalization",
                    "Git workflows: Branching, Pull Requests, Merge Conflict Resolution",
                    "Basic Linux command line usage and shell scripting"
                ],
                "milestone_project": "Create a Database-Backed CRUD Application with an interactive CLI or desktop interface."
            },
            {
                "phase": "Phase 3: Architecture, APIs & Practical Development",
                "duration": "Weeks 13 - 18",
                "focus": "Build modular systems, RESTful APIs, and test suites.",
                "topics": [
                    "RESTful API design and JSON data transfer",
                    "Software Design Patterns (Factory, Singleton, Observer)",
                    "Unit Testing and Test-Driven Development (JUnit / PyTest)",
                    "Basic multi-threading and asynchronous programming"
                ],
                "milestone_project": "Develop a multi-tiered Microservice or REST API with authentication and automated test coverage."
            },
            {
                "phase": "Phase 4: Interview Prep, System Design & Portfolio",
                "duration": "Weeks 19 - 24",
                "focus": "Coding interview problem-solving and portfolio polish.",
                "topics": [
                    "Solve 100+ LeetCode / HackerRank problems (Medium difficulty)",
                    "High-Level System Design concepts: Caching, Load Balancing, Microservices",
                    "Deploy code on GitHub with comprehensive README documentation",
                    "Mock technical interviews and resume tailoring"
                ],
                "milestone_project": "Complete a capstone open-source contribution or full end-to-end deployed software system."
            }
        ],
        "free_resources": [
            {"title": "Harvard CS50: Introduction to Computer Science", "provider": "edX / Harvard", "url": "https://cs50.harvard.edu/x/"},
            {"title": "freeCodeCamp Python / JavaScript Algorithms Course", "provider": "freeCodeCamp", "url": "https://www.freecodecamp.org/"},
            {"title": "NeetCode / LeetCode Roadmap for DSA", "provider": "NeetCode.io", "url": "https://neetcode.io/roadmap"},
            {"title": "Pro Git Book (Official Free Guide)", "provider": "Git-SCM", "url": "https://git-scm.com/book/en/v2"}
        ]
    },

    "Data Analyst": {
        "title": "Data Analyst",
        "category": "Data Science & Business Intelligence",
        "tagline": "Transform raw numbers into strategic business insights through statistical analysis and visualization.",
        "icon": "graph-up",
        "badge_color": "#0891b2",
        "overview": (
            "Data Analysts inspect, clean, transform, and model data to uncover actionable trends, patterns, and insights. "
            "They bridge the gap between technical datasets and executive business decisions, crafting interactive dashboards "
            "and statistical reports that drive company strategy."
        ),
        "required_skills": [
            "SQL (Advanced Queries & Aggregations)",
            "Python (Pandas, NumPy)",
            "Data Cleaning & Wrangling",
            "Data Visualization (Matplotlib, Seaborn, Tableau/PowerBI)",
            "Applied Statistics & Probability",
            "Excel / Spreadsheets (Pivot Tables, VLOOKUP, Power Query)",
            "Business Communication & Storytelling"
        ],
        "optional_skills": [
            "R Programming",
            "Basic Machine Learning Regression",
            "ETL Pipelines",
            "Google Analytics / BigQuery",
            "A/B Testing Methodologies"
        ],
        "typical_roles": [
            "Junior Data Analyst",
            "Business Intelligence (BI) Analyst",
            "Marketing / Product Analyst",
            "Operations Data Specialist"
        ],
        "market_demand": "High",
        "avg_salary_range": "$65,000 - $105,000 / year (₹5 - 12 LPA for freshers in India)",
        "roadmap": [
            {
                "phase": "Phase 1: Advanced Excel & Descriptive Statistics",
                "duration": "Weeks 1 - 5",
                "focus": "Build intuition for quantitative metrics and spreadsheet mastery.",
                "topics": [
                    "Excel mastery: XLOOKUP, Nested IFs, Pivot Tables, Conditional Formatting",
                    "Measures of Central Tendency, Variance, Standard Deviation, Percentiles",
                    "Distributions, Normal Curve, Hypothesis Testing fundamentals",
                    "Data integrity, cleaning techniques, handling missing data"
                ],
                "milestone_project": "Build an executive financial/sales dashboard in Excel using interactive slicers."
            },
            {
                "phase": "Phase 2: Relational Databases & SQL Mastery",
                "duration": "Weeks 6 - 10",
                "focus": "Extract and manipulate enterprise relational data.",
                "topics": [
                    "Complex SQL queries: Inner/Outer/Self Joins, Subqueries, CTEs",
                    "Window Functions (ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD)",
                    "Data aggregation, GROUP BY, HAVING, Date/Time manipulation",
                    "Database schema analysis and Entity Relationship Diagrams (ERD)"
                ],
                "milestone_project": "Analyze a multi-table E-commerce database to identify customer churn and top revenue drivers."
            },
            {
                "phase": "Phase 3: Python for Data Analysis & Visualization",
                "duration": "Weeks 11 - 16",
                "focus": "Automate data cleaning and generate publication-quality visual insights.",
                "topics": [
                    "NumPy for fast vectorized operations",
                    "Pandas for DataFrame slicing, filtering, grouping, merging, and reshaping",
                    "Matplotlib and Seaborn for statistical chart generation",
                    "Exploratory Data Analysis (EDA) framework and outlier detection"
                ],
                "milestone_project": "Complete an end-to-end EDA notebook on a real Kaggle dataset (e.g., Airbnb pricing or Spotify trends)."
            },
            {
                "phase": "Phase 4: BI Dashboards, Storytelling & Portfolio",
                "duration": "Weeks 17 - 22",
                "focus": "Translate technical charts into business presentations and dashboards.",
                "topics": [
                    "Power BI or Tableau: Data modeling, calculated columns, DAX formulas",
                    "Dashboard UX: KPI cards, interactive drill-downs, color harmony",
                    "Data storytelling: Presenting findings clearly to non-technical stakeholders",
                    "Host interactive dashboards on Tableau Public / GitHub portfolio"
                ],
                "milestone_project": "Publish a live interactive Power BI / Tableau dashboard tracking regional healthcare or sales metrics."
            }
        ],
        "free_resources": [
            {"title": "Kaggle Learn: Python, Pandas, and Data Visualization", "provider": "Kaggle", "url": "https://www.kaggle.com/learn"},
            {"title": "Mode Analytics SQL Tutorial for Beginners", "provider": "Mode", "url": "https://mode.com/sql-tutorial/"},
            {"title": "freeCodeCamp Data Analysis with Python Course", "provider": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/data-analysis-with-python/"},
            {"title": "Power BI Guided Learning", "provider": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/power-bi/guided-learning/"}
        ]
    },

    "AI/ML Engineer": {
        "title": "AI / Machine Learning Engineer",
        "category": "Artificial Intelligence & Advanced Analytics",
        "tagline": "Build intelligent algorithms that learn from data to automate decisions, predict outcomes, and solve complex problems.",
        "icon": "cpu",
        "badge_color": "#7c3aed",
        "overview": (
            "AI and Machine Learning Engineers design mathematical models, neural networks, and self-learning pipelines. "
            "They bridge theoretical mathematics and high-performance software engineering to create systems capable of "
            "natural language processing, computer vision, recommendation engines, and predictive analytics."
        ),
        "required_skills": [
            "Python (NumPy, SciPy, Pandas)",
            "Scikit-Learn (Supervised & Unsupervised Learning)",
            "Linear Algebra, Multivariate Calculus & Probability",
            "Data Preprocessing & Feature Engineering",
            "Deep Learning Frameworks (TensorFlow or PyTorch)",
            "Model Evaluation (Confusion Matrix, ROC-AUC, F1, MSE)",
            "Model Deployment (Flask, FastAPI, ONNX, or Docker)"
        ],
        "optional_skills": [
            "Natural Language Processing (Transformers, Hugging Face, LLMs)",
            "Computer Vision (OpenCV, CNNs)",
            "MLOps (MLflow, Weights & Biases, DVC)",
            "Cloud ML Services (AWS SageMaker / GCP Vertex AI)",
            "CUDA / GPU Optimization"
        ],
        "typical_roles": [
            "Machine Learning Engineer",
            "Junior Data Scientist",
            "AI Research Engineer",
            "Computer Vision / NLP Specialist"
        ],
        "market_demand": "Very High",
        "avg_salary_range": "$90,000 - $145,000 / year (₹8 - 18 LPA for freshers in India)",
        "roadmap": [
            {
                "phase": "Phase 1: Mathematical Foundations & Python Scipy Stack",
                "duration": "Weeks 1 - 6",
                "focus": "Build intuition for vectors, gradients, matrices, and statistical inference.",
                "topics": [
                    "Linear Algebra: Vector spaces, Matrix multiplication, Eigenvalues/Eigenvectors, SVD",
                    "Calculus: Partial derivatives, Gradients, Gradient Descent optimization",
                    "Probability: Bayes Theorem, Probability density functions, Maximum Likelihood Estimation",
                    "Vectorized Python computation with NumPy and multidimensional arrays"
                ],
                "milestone_project": "Implement Linear Regression and Logistic Regression from scratch using only NumPy."
            },
            {
                "phase": "Phase 2: Classical Machine Learning & Feature Engineering",
                "duration": "Weeks 7 - 13",
                "focus": "Supervised and unsupervised algorithms with Scikit-Learn.",
                "topics": [
                    "Supervised Learning: Decision Trees, Random Forests, SVM, Gradient Boosting (XGBoost/LightGBM)",
                    "Unsupervised Learning: K-Means Clustering, PCA (Dimensionality Reduction)",
                    "Data preprocessing: Imputation, One-Hot Encoding, StandardScaler, Handling class imbalance (SMOTE)",
                    "Model evaluation: Cross-validation, Hyperparameter tuning (GridSearchCV), Precision-Recall trade-off"
                ],
                "milestone_project": "Build an end-to-end predictive pipeline (e.g., Credit Card Fraud Detection or House Price Predictor)."
            },
            {
                "phase": "Phase 3: Deep Learning, Neural Networks & Modern AI",
                "duration": "Weeks 14 - 20",
                "focus": "Multi-layer Perceptrons, Convolutional Networks, and Transfer Learning.",
                "topics": [
                    "Artificial Neural Networks (ANN): Forward/Backpropagation, Activation Functions (ReLU, Softmax)",
                    "PyTorch or TensorFlow/Keras basics: Tensors, Autograd, Dataset Loaders",
                    "Convolutional Neural Networks (CNN) for image classification",
                    "Introduction to Transformers, Attention Mechanisms, and Hugging Face pipelines"
                ],
                "milestone_project": "Train a Deep Learning image classifier or sentiment analysis model with PyTorch/TensorFlow."
            },
            {
                "phase": "Phase 4: MLOps, Model Deployment & Production",
                "duration": "Weeks 21 - 26",
                "focus": "Package models as scalable production web APIs.",
                "topics": [
                    "Serializing models with joblib / pickle / ONNX",
                    "Serving inference via REST APIs using FastAPI or Flask",
                    "Containerization with Docker for reproducible model environments",
                    "Monitoring data drift, model latency, and versioning models"
                ],
                "milestone_project": "Deploy an AI/ML web application (similar to this career recommendation system!) to the cloud."
            }
        ],
        "free_resources": [
            {"title": "Machine Learning Specialization by Andrew Ng", "provider": "Coursera / DeepLearning.AI", "url": "https://www.deeplearning.ai/courses/machine-learning-specialization/"},
            {"title": "Fast.ai: Practical Deep Learning for Coders", "provider": "Fast.ai", "url": "https://course.fast.ai/"},
            {"title": "Scikit-Learn Official User Guides and Examples", "provider": "Scikit-Learn Docs", "url": "https://scikit-learn.org/stable/user_guide.html"},
            {"title": "Hugging Face Deep Learning & NLP Course", "provider": "Hugging Face", "url": "https://huggingface.co/learn"}
        ]
    },

    "Cybersecurity Analyst": {
        "title": "Cybersecurity Analyst",
        "category": "Information Security & Infrastructure Defense",
        "tagline": "Protect digital infrastructure, investigate network threats, and defend systems against cyber attacks.",
        "icon": "shield-check",
        "badge_color": "#dc2626",
        "overview": (
            "Cybersecurity Analysts monitor computer networks, identify vulnerabilities, respond to security incidents, "
            "and establish defensive protocols. They understand attacker methodologies, audit code and systems for exploits, "
            "and ensure corporate systems comply with strict security standards."
        ),
        "required_skills": [
            "Computer Networking (TCP/IP, DNS, Subnetting, Firewalls)",
            "Linux Operating System & Bash Scripting",
            "Network Traffic Analysis (Wireshark, tcpdump)",
            "Vulnerability Assessment & Penetration Testing Basics (Nmap, Metasploit)",
            "Security Information & Event Management (SIEM)",
            "Cryptography Basics (Symmetric/Asymmetric, Hashing, SSL/TLS)",
            "Incident Response & Security Frameworks (NIST, MITRE ATT&CK)"
        ],
        "optional_skills": [
            "Python for Security Automation & Exploitation Scripts",
            "Cloud Security (AWS IAM, Security Groups)",
            "Web Application Security (OWASP Top 10, Burp Suite)",
            "Digital Forensics & Reverse Engineering",
            "Zero Trust Architecture"
        ],
        "typical_roles": [
            "SOC Analyst (Security Operations Center Tier 1/2)",
            "Junior Penetration Tester",
            "Information Security Specialist",
            "Network Security Administrator"
        ],
        "market_demand": "Extremely High",
        "avg_salary_range": "$70,000 - $120,000 / year (₹6 - 14 LPA for freshers in India)",
        "roadmap": [
            {
                "phase": "Phase 1: Networking & Operating System Fundamentals",
                "duration": "Weeks 1 - 6",
                "focus": "Understand how computers communicate and how operating systems operate under the hood.",
                "topics": [
                    "OSI 7-layer Model and TCP/IP protocol suite",
                    "Deep dive into DNS, DHCP, HTTP/HTTPS, SSH, FTP, and ARP",
                    "Linux command line: File permissions, process monitoring, systemd, SSH configuration",
                    "Windows administration and Active Directory concepts"
                ],
                "milestone_project": "Set up a virtual home lab (VirtualBox/VMware) with Kali Linux, Ubuntu Server, and a pfSense firewall."
            },
            {
                "phase": "Phase 2: Network Defense, Packet Analysis & SIEM",
                "duration": "Weeks 7 - 12",
                "focus": "Monitor traffic, identify malicious patterns, and inspect logs.",
                "topics": [
                    "Packet inspection with Wireshark: Filtering for SYN floods, ARP spoofing, cleartext credentials",
                    "Port scanning and host enumeration using Nmap",
                    "SIEM fundamentals: Splunk or Elastic Security log parsing and rule creation",
                    "Firewall rules, Intrusion Detection Systems (Snort / Suricata)"
                ],
                "milestone_project": "Analyze captured malicious PCAP files and write an incident triage report detailing the attack vector."
            },
            {
                "phase": "Phase 3: Web Security, Ethical Hacking & OWASP",
                "duration": "Weeks 13 - 18",
                "focus": "Learn attacker techniques to effectively defend against them.",
                "topics": [
                    "OWASP Top 10 vulnerabilities: SQL Injection, XSS, CSRF, IDOR, SSRF",
                    "Web proxy inspection using Burp Suite Community Edition",
                    "Authentication weaknesses, session hijacking, password cracking (Hashcat/John)",
                    "Bash and Python scripting for network reconnaissance and automated defense"
                ],
                "milestone_project": "Successfully complete 20+ Capture the Flag (CTF) challenges on TryHackMe or HackTheBox."
            },
            {
                "phase": "Phase 4: Incident Response, Certifications & Career Entry",
                "duration": "Weeks 19 - 24",
                "focus": "Master incident response playbooks and earn recognized credentials.",
                "topics": [
                    "Incident response lifecycle: Preparation, Detection, Containment, Eradication, Recovery",
                    "Study for entry certifications: CompTIA Security+, Cisco CCNA, or eJPT",
                    "Document home lab projects and CTF writeups on a technical blog/GitHub",
                    "Learn industry compliance standards (NIST CSF, ISO 27001)"
                ],
                "milestone_project": "Create a comprehensive incident response playbook for ransomware containment."
            }
        ],
        "free_resources": [
            {"title": "TryHackMe: Pre-Security & Complete Beginner Paths", "provider": "TryHackMe", "url": "https://tryhackme.com/"},
            {"title": "Professor Messer's CompTIA Security+ (SY0-701) Video Course", "provider": "YouTube", "url": "https://www.professormesser.com/"},
            {"title": "OverTheWire Wargames (Bandit for Linux Mastery)", "provider": "OverTheWire", "url": "https://overthewire.org/wargames/bandit/"},
            {"title": "PortSwigger Web Security Academy (Burp Suite)", "provider": "PortSwigger", "url": "https://portswigger.net/web-security"}
        ]
    },

    "Web Developer": {
        "title": "Full-Stack Web Developer",
        "category": "Web Technologies & Cloud Applications",
        "tagline": "Craft responsive user interfaces and scalable web services that power modern Internet experiences.",
        "icon": "globe2",
        "badge_color": "#059669",
        "overview": (
            "Web Developers engineer the client-facing frontends and backend servers that drive websites, web apps, "
            "and SaaS platforms. They combine visual design sensibilities, responsive layout engineering, RESTful API architecture, "
            "and database integration to build interactive digital products."
        ),
        "required_skills": [
            "HTML5, CSS3 & Responsive Web Design",
            "JavaScript (ES6+, DOM Manipulation, Async/Await)",
            "Backend Framework (Flask, Node.js/Express, or Django)",
            "RESTful API Development & JSON",
            "Relational Databases (SQLite / PostgreSQL) & ORM",
            "Version Control (Git & GitHub)",
            "Web Performance & Cross-Browser Compatibility"
        ],
        "optional_skills": [
            "Modern Frontend Frameworks (React, Vue, or Tailwind CSS)",
            "Authentication (JWT, OAuth2, Cookies/Sessions)",
            "Cloud Deployment (Render, Vercel, Netlify, Railway)",
            "WebSockets / Real-Time Communication",
            "TypeScript"
        ],
        "typical_roles": [
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Web Developer",
            "Web Application Specialist"
        ],
        "market_demand": "High",
        "avg_salary_range": "$65,000 - $115,000 / year (₹5 - 13 LPA for freshers in India)",
        "roadmap": [
            {
                "phase": "Phase 1: Modern HTML5, Responsive CSS3 & Design Basics",
                "duration": "Weeks 1 - 5",
                "focus": "Build pixel-perfect, accessible, mobile-first web layouts.",
                "topics": [
                    "Semantic HTML5 tags, accessibility (a11y), SEO meta tags",
                    "CSS3 Flexbox and CSS Grid layout systems",
                    "Responsive design: Media queries, mobile-first approach, fluid typography",
                    "Modern styling: CSS variables, animations, glassmorphism, UI components"
                ],
                "milestone_project": "Build a responsive modern multi-page portfolio website from scratch without frameworks."
            },
            {
                "phase": "Phase 2: Modern JavaScript (ES6+) & DOM Engineering",
                "duration": "Weeks 6 - 10",
                "focus": "Add interactivity, state management, and API connectivity to the browser.",
                "topics": [
                    "JavaScript core: Variables (let/const), Arrow functions, Array methods (map, filter, reduce)",
                    "DOM manipulation, Event listeners, Event delegation, Form validation",
                    "Asynchronous JS: Promises, async/await, Fetch API",
                    "Browser storage: localStorage, sessionStorage, Cookies"
                ],
                "milestone_project": "Develop an interactive task management dashboard with filtering, search, and local persistence."
            },
            {
                "phase": "Phase 3: Backend Development, Routing & Databases",
                "duration": "Weeks 11 - 16",
                "focus": "Build server-side logic, templating, and database integrations.",
                "topics": [
                    "Python Flask or Node.js Express server routing and middleware",
                    "Server-side templating (Jinja2) vs Single Page Application architectures",
                    "Database integration: SQLite, PostgreSQL, CRUD operations",
                    "User authentication, password hashing (bcrypt), and session security"
                ],
                "milestone_project": "Build a complete CRUD Web Application with user login, database storage, and REST endpoints."
            },
            {
                "phase": "Phase 4: Frontend Framework, Deployment & CI/CD",
                "duration": "Weeks 17 - 22",
                "focus": "Scale development with modern component frameworks and live deployment.",
                "topics": [
                    "Frontend component library (React or Tailwind CSS fundamentals)",
                    "Deployment to cloud platforms (Render, Vercel, Netlify)",
                    "Web security basics: CORS, XSS prevention, CSRF tokens, HTTPS",
                    "Lighthouse performance audits and SEO optimization"
                ],
                "milestone_project": "Deploy a full-stack SaaS product or community forum live on the web with custom domain."
            }
        ],
        "free_resources": [
            {"title": "freeCodeCamp Responsive Web Design & JavaScript Algorithms", "provider": "freeCodeCamp", "url": "https://www.freecodecamp.org/"},
            {"title": "The Odin Project (Full Stack Open Curriculum)", "provider": "The Odin Project", "url": "https://www.theodinproject.com/"},
            {"title": "MDN Web Docs (The Definitive Web Reference)", "provider": "Mozilla", "url": "https://developer.mozilla.org/"},
            {"title": "CS50's Web Programming with Python and JavaScript", "provider": "Harvard / edX", "url": "https://cs50.harvard.edu/web/"}
        ]
    }
}


def analyze_skill_gap(predicted_career: str, user_skills: list) -> dict:
    """
    Compares user's current skills against the target career requirements.
    Returns:
        dict containing:
        - owned_skills: list of matching skills
        - missing_skills: list of skills to acquire
        - match_percentage: percentage of required skills possessed
        - readiness_status: qualitative description (e.g., 'Strong Foundation', 'Moderate Gap')
    """
    profile = CAREER_PROFILES.get(predicted_career)
    if not profile:
        return {
            "owned_skills": [],
            "missing_skills": [],
            "match_percentage": 0,
            "readiness_status": "Unknown"
        }

    required = profile["required_skills"]
    user_skills_lower = {s.strip().lower() for s in user_skills if s}

    owned = []
    missing = []

    for req in required:
        # Check direct or partial match
        req_clean = req.lower()
        matched = False
        for u in user_skills_lower:
            if u in req_clean or req_clean in u:
                matched = True
                break
        if matched:
            owned.append(req)
        else:
            missing.append(req)

    total_req = len(required)
    pct = round((len(owned) / total_req) * 100) if total_req > 0 else 0

    if pct >= 75:
        status = "Advanced Readiness — Minor gaps to close"
    elif pct >= 45:
        status = "Moderate Foundation — Key technical skills needed"
    else:
        status = "Early Explorer — Follow the 4-phase roadmap"

    return {
        "owned_skills": owned,
        "missing_skills": missing,
        "match_percentage": pct,
        "readiness_status": status,
        "total_required": total_req,
        "owned_count": len(owned),
        "missing_count": len(missing)
    }
