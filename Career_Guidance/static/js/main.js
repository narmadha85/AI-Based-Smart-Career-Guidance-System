/**
 * AI-Based Career Guidance System - Client Interactions & Demo Presets
 */

document.addEventListener("DOMContentLoaded", function () {
  // 1. Live Slider Value Display
  const rangeInputs = document.querySelectorAll('input[type="range"]');
  rangeInputs.forEach((input) => {
    const badge = document.getElementById(input.id + "_badge");
    if (badge) {
      input.addEventListener("input", function () {
        badge.textContent = this.value + " / 5";
      });
    }
  });

  // 2. Demo Presets Data (For effortless college viva demonstrations)
  const presets = {
    aiml: {
      student_name: "Priya Sharma",
      email: "priya.sharma@example.edu",
      education_level: "Bachelor's in CS / IT",
      primary_interest: "Artificial Intelligence & Deep Learning",
      math_score: 5,
      programming_score: 5,
      data_structures_score: 4,
      networking_score: 2,
      web_technologies_score: 2,
      cybersecurity_score: 2,
      database_score: 4,
      interest_software: 3,
      interest_data: 5,
      interest_ai_ml: 5,
      interest_security: 2,
      interest_web: 2,
      skills: ["skill_python", "skill_machine_learning", "skill_data_analysis", "skill_sql", "skill_linux_git"],
      problem_solving_score: 5,
      abstract_thinking_score: 5,
      creative_design_score: 2,
      system_architecture_score: 4
    },
    webdev: {
      student_name: "Rahul Verma",
      email: "rahul.verma@example.edu",
      education_level: "Bachelor's in Computer Science",
      primary_interest: "Web Applications & Frontend Design",
      math_score: 3,
      programming_score: 4,
      data_structures_score: 3,
      networking_score: 3,
      web_technologies_score: 5,
      cybersecurity_score: 2,
      database_score: 4,
      interest_software: 4,
      interest_data: 2,
      interest_ai_ml: 2,
      interest_security: 2,
      interest_web: 5,
      skills: ["skill_javascript", "skill_html_css", "skill_python", "skill_sql", "skill_cloud_basics"],
      problem_solving_score: 4,
      abstract_thinking_score: 3,
      creative_design_score: 5,
      system_architecture_score: 4
    },
    cybersecurity: {
      student_name: "Karan Mehta",
      email: "karan.mehta@example.edu",
      education_level: "Bachelor's in IT",
      primary_interest: "Ethical Hacking & Network Security",
      math_score: 3,
      programming_score: 4,
      data_structures_score: 3,
      networking_score: 5,
      web_technologies_score: 3,
      cybersecurity_score: 5,
      database_score: 3,
      interest_software: 3,
      interest_data: 2,
      interest_ai_ml: 2,
      interest_security: 5,
      interest_web: 2,
      skills: ["skill_network_security", "skill_linux_git", "skill_python", "skill_cloud_basics"],
      problem_solving_score: 5,
      abstract_thinking_score: 4,
      creative_design_score: 2,
      system_architecture_score: 4
    },
    data: {
      student_name: "Ananya Iyer",
      email: "ananya.iyer@example.edu",
      education_level: "Bachelor's in Statistics / Math",
      primary_interest: "Business Intelligence & Data Analytics",
      math_score: 5,
      programming_score: 3,
      data_structures_score: 3,
      networking_score: 2,
      web_technologies_score: 2,
      cybersecurity_score: 2,
      database_score: 5,
      interest_software: 2,
      interest_data: 5,
      interest_ai_ml: 3,
      interest_security: 2,
      interest_web: 2,
      skills: ["skill_sql", "skill_data_analysis", "skill_python"],
      problem_solving_score: 4,
      abstract_thinking_score: 4,
      creative_design_score: 4,
      system_architecture_score: 3
    },
    software: {
      student_name: "Amit Patel",
      email: "amit.patel@example.edu",
      education_level: "Bachelor's in CS / IT",
      primary_interest: "Backend Systems & Software Engineering",
      math_score: 4,
      programming_score: 5,
      data_structures_score: 5,
      networking_score: 3,
      web_technologies_score: 3,
      cybersecurity_score: 3,
      database_score: 4,
      interest_software: 5,
      interest_data: 3,
      interest_ai_ml: 3,
      interest_security: 3,
      interest_web: 3,
      skills: ["skill_java", "skill_python", "skill_cpp", "skill_sql", "skill_linux_git"],
      problem_solving_score: 5,
      abstract_thinking_score: 4,
      creative_design_score: 3,
      system_architecture_score: 5
    }
  };

  // 3. Preset Button Click Handler
  window.loadPreset = function (key) {
    const data = presets[key];
    if (!data) return;

    // Fill text inputs & selects
    if (document.getElementById("student_name")) document.getElementById("student_name").value = data.student_name;
    if (document.getElementById("email")) document.getElementById("email").value = data.email;
    if (document.getElementById("education_level")) document.getElementById("education_level").value = data.education_level;
    if (document.getElementById("primary_interest")) document.getElementById("primary_interest").value = data.primary_interest;

    // Fill sliders
    const sliderKeys = [
      "math_score", "programming_score", "data_structures_score", "networking_score",
      "web_technologies_score", "cybersecurity_score", "database_score",
      "interest_software", "interest_data", "interest_ai_ml", "interest_security", "interest_web",
      "problem_solving_score", "abstract_thinking_score", "creative_design_score", "system_architecture_score"
    ];

    sliderKeys.forEach((k) => {
      const el = document.getElementById(k);
      if (el && data[k] !== undefined) {
        el.value = data[k];
        const badge = document.getElementById(k + "_badge");
        if (badge) badge.textContent = data[k] + " / 5";
      }
    });

    // Reset and fill skills checkboxes
    const allSkillCheckboxes = document.querySelectorAll('input[name="skills"]');
    allSkillCheckboxes.forEach((cb) => {
      cb.checked = data.skills.includes(cb.value);
    });

    // Provide visual feedback
    const toast = document.createElement("div");
    toast.className = "flash-message flash-success";
    toast.style.position = "fixed";
    toast.style.bottom = "20px";
    toast.style.right = "20px";
    toast.style.zIndex = "9999";
    toast.style.boxShadow = "0 10px 25px rgba(0,0,0,0.15)";
    toast.innerHTML = `<span><strong>Preset Loaded:</strong> ${data.student_name} (${data.primary_interest})</span>`;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2500);
  };

  // 4. Print Report Trigger
  const printBtn = document.getElementById("printReportBtn");
  if (printBtn) {
    printBtn.addEventListener("click", function () {
      window.print();
    });
  }

  // 5. History Table Search Filter
  const searchInput = document.getElementById("historySearch");
  if (searchInput) {
    searchInput.addEventListener("keyup", function () {
      const filter = this.value.toLowerCase();
      const rows = document.querySelectorAll("#historyTableBody tr");
      rows.forEach((row) => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(filter) ? "" : "none";
      });
    });
  }
});
