import streamlit as st
import joblib
import pandas as pd
import mysql.connector


# ==========================================
# Load ML Model and Preprocessor
# ==========================================

preprocessor = joblib.load("models/preprocessor.pkl")
best_model = joblib.load("models/best_model.pkl")


# ==========================================
# Streamlit Application
# ==========================================

st.title("🎓 AI-Based Student Placement Prediction")
st.subheader("Student Information")


# ==========================================
# Student Information
# ==========================================

student_name = st.text_input("Student Name")

branch = st.selectbox(
    "Branch",
    ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil", "Other"]
)

college_tier = st.selectbox(
    "College Tier",
    ["Tier-1", "Tier-2", "Tier-3"]
)


# ==========================================
# Academic Details
# ==========================================

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


# ==========================================
# Technical & Skill Details
# ==========================================

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


# ==========================================
# Experience & Activities
# ==========================================

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
# Predict & Recommend
# ==========================================

if st.button("🎯 Predict & Recommend"):

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


    # ==========================================
    # Prepare Student Data
    # ==========================================

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


    # ==========================================
    # Placement Prediction
    # ==========================================

    student_encoded = preprocessor.transform(student_df)

    prediction = best_model.predict(student_encoded)

    placement_status = (
        "Placed"
        if prediction[0] == 1
        else "Not Placed"
    )

    placement_probability = (
        best_model.predict_proba(student_encoded)[0][1] * 100
    )


    # ==========================================
    # Career Recommendation
    # ==========================================

    career_scores = {
        "Machine Learning Engineer": (
            ml_knowledge
            + coding_skills
            + dsa_score
            + system_design
        ) / 4,

        "Data Analyst": (
            aptitude_score
            + communication_skills
            + coding_skills
            + cgpa
        ) / 4,

        "Software Developer": (
            coding_skills
            + dsa_score
            + system_design
            + projects_count
        ) / 4,

        "Business Analyst": (
            aptitude_score
            + communication_skills
            + cgpa
            + projects_count
        ) / 4,

        "Data Scientist": (
            ml_knowledge
            + coding_skills
            + aptitude_score
            + cgpa
        ) / 4
    }

    sorted_careers = sorted(
        career_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    recommended_career = sorted_careers[0][0]

    career_suitability_score = sorted_careers[0][1]

    alternative_career = sorted_careers[1][0]


    # ==========================================
    # Display Placement Prediction
    # ==========================================

    st.subheader("📊 Placement Prediction")

    st.write(
        f"**Placement Status:** {placement_status}"
    )

    st.write(
        f"**Placement Probability:** "
        f"{placement_probability:.2f}%"
    )


    # ==========================================
    # Display Career Recommendation
    # ==========================================

    st.subheader("🎯 Career Recommendation")

    st.write(
        f"**Recommended Career:** "
        f"{recommended_career}"
    )

    st.write(
        f"**Career Suitability Score:** "
        f"{career_suitability_score:.2f}"
    )

    st.write(
        f"**Alternative Career:** "
        f"{alternative_career}"
    )


    # ==========================================
    # MySQL Database Connection
    # ==========================================

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shaikh@#12",
        database="placement_career_db"
    )

    cursor = connection.cursor()


    # ==========================================
    # Store Result in MySQL
    # ==========================================

    insert_query = """
    INSERT INTO students (
        student_name,
        branch,
        college_tier,
        cgpa,
        backlogs,
        coding_skills,
        dsa_score,
        aptitude_score,
        communication_skills,
        ml_knowledge,
        system_design,
        internships,
        projects_count,
        certifications,
        hackathons,
        open_source_contributions,
        extracurriculars,
        placement_status,
        placement_probability,
        recommended_career,
        career_suitability_score,
        alternative_career
    )
    VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
    """

    placement_status_db = int(prediction[0])

    student_record = (
        student_name,
        branch,
        college_tier,
        cgpa,
        backlogs,
        coding_skills,
        dsa_score,
        aptitude_score,
        communication_skills,
        ml_knowledge,
        system_design,
        internships,
        projects_count,
        certifications,
        hackathons,
        open_source_contributions,
        extracurriculars,
        placement_status_db,
        placement_probability,
        recommended_career,
        career_suitability_score,
        alternative_career
    )

    cursor.execute(
        insert_query,
        student_record
    )

    connection.commit()

    cursor.close()
    connection.close()


    # ==========================================
    # Success Message
    # ==========================================

    st.success(
        "✅ Prediction completed and student result "
        "stored successfully!"
    )