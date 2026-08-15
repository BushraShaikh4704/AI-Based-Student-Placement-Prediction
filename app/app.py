import streamlit as st
import joblib
import pandas as pd

# Load trained model and preprocessor
preprocessor = joblib.load("models/preprocessor.pkl")
best_model = joblib.load("models/best_model.pkl")


st.title("🎓 AI-Based Student Placement Prediction")
st.subheader("Student Information")

student_name = st.text_input("Student Name")

branch = st.selectbox(
    "Branch",
    ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil", "Other"]
)

college_tier = st.selectbox(
    "College Tier",
    ["Tier-1", "Tier-2", "Tier-3"]
)

st.subheader("📚 Academic Details")

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

backlogs = st.number_input(
    "Number of Backlogs",
    min_value=0,
    max_value=20,
    value=0,
    step=1
)

st.subheader("💻 Technical & Skill Details")

coding_skills = st.slider(
    "Coding Skills",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)

dsa_score = st.slider(
    "DSA Score",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)

aptitude_score = st.slider(
    "Aptitude Score",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)

communication_skills = st.slider(
    "Communication Skills",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)

ml_knowledge = st.slider(
    "Machine Learning Knowledge",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)

system_design = st.slider(
    "System Design Knowledge",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)

st.subheader("🏆 Experience & Activities")

internships = st.number_input(
    "Number of Internships",
    min_value=0,
    max_value=10,
    value=0,
    step=1
)

projects_count = st.number_input(
    "Number of Projects",
    min_value=0,
    max_value=20,
    value=0,
    step=1
)

certifications = st.number_input(
    "Number of Certifications",
    min_value=0,
    max_value=50,
    value=0,
    step=1
)

hackathons = st.number_input(
    "Number of Hackathons",
    min_value=0,
    max_value=50,
    value=0,
    step=1
)

open_source_contributions = st.number_input(
    "Open Source Contributions",
    min_value=0,
    max_value=100,
    value=0,
    step=1
)

extracurriculars = st.number_input(
    "Extracurricular Activities",
    min_value=0,
    max_value=50,
    value=0,
    step=1
)

# ==========================================
# Feature Engineering
# ==========================================

technical_skill_score = (
    coding_skills
    + dsa_score
    + ml_knowledge
    + system_design
) / 4

experience_score = (
    internships
    + projects_count
    + certifications
    + hackathons
    + open_source_contributions
    + extracurriculars
)

has_backlog = 1 if backlogs > 0 else 0

maximum_skill = max(
    coding_skills,
    dsa_score,
    ml_knowledge,
    system_design
)

minimum_skill = min(
    coding_skills,
    dsa_score,
    ml_knowledge,
    system_design
)

technical_skill_gap = maximum_skill - minimum_skill


student_data = {
    "branch": branch,
    "college_tier": college_tier,
    "cgpa": cgpa,
    "backlogs": backlogs,
    "coding_skills": coding_skills,
    "dsa_score": dsa_score,
    "aptitude_score": aptitude_score,
    "communication_skills": communication_skills,
    "ml_knowledge": ml_knowledge,
    "system_design": system_design,
    "internships": internships,
    "projects_count": projects_count,
    "certifications": certifications,
    "hackathons": hackathons,
    "open_source_contributions": open_source_contributions,
    "extracurriculars": extracurriculars,
    "technical_skill_score": technical_skill_score,
    "has_backlog": has_backlog,
    "experience_score": experience_score,
    "technical_skill_gap": technical_skill_gap
}

student_df = pd.DataFrame([student_data])


student_encoded = preprocessor.transform(student_df)
prediction = best_model.predict(student_encoded)
placement_status = "Placed" if prediction[0] == 1 else "Not Placed"

st.subheader("📊 Placement Prediction")
st.write(f"**Placement Status:** {placement_status}")

placement_probability = best_model.predict_proba(student_encoded)[0][1] * 100

st.subheader("📊 Placement Prediction")
st.write(f"**Placement Status:** {placement_status}")
st.write(f"**Placement Probability:** {placement_probability:.2f}%")


career_weights = {
    'Data Scientist': {
        'coding_skills': 0.2,
        'dsa_score': 0.1,
        'ml_knowledge': 0.25,
        'projects_count': 0.2,
        'internships': 0.1,
        'aptitude_score': 0.1,
        'communication_skills': 0.05
    },

    'Data Analyst': {
        'coding_skills': 0.1,
        'dsa_score': 0.05,
        'ml_knowledge': 0.1,
        'projects_count': 0.15,
        'internships': 0.1,
        'aptitude_score': 0.25,
        'communication_skills': 0.25
    },

    'Machine Learning Engineer': {
        'coding_skills': 0.25,
        'dsa_score': 0.15,
        'ml_knowledge': 0.3,
        'projects_count': 0.15,
        'internships': 0.05,
        'aptitude_score': 0.05,
        'communication_skills': 0.05
    },

    'Software Developer': {
        'coding_skills': 0.3,
        'dsa_score': 0.25,
        'ml_knowledge': 0.05,
        'projects_count': 0.2,
        'internships': 0.05,
        'aptitude_score': 0.1,
        'communication_skills': 0.05
    },

    'Business Analyst': {
        'coding_skills': 0.05,
        'dsa_score': 0.05,
        'ml_knowledge': 0.05,
        'projects_count': 0.15,
        'internships': 0.1,
        'aptitude_score': 0.3,
        'communication_skills': 0.3
    }
}


career_scores = {}

for career, weights in career_weights.items():
    score = 0

    for feature, weight in weights.items():
        score += student_data[feature] * weight

    career_scores[career] = score

ranked_careers = sorted(
    career_scores.items(),
    key=lambda x: x[1],
    reverse=True
)

recommended_career = ranked_careers[0][0]
career_suitability_score = ranked_careers[0][1]

alternative_career = ranked_careers[1][0]