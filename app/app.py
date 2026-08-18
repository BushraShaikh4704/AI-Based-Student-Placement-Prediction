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
    ["CSE", "IT", "ECE", "EE", "ME", "CE", "Chemical"]
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
# Technical & Branch-Specific Skill Details
# ==========================================

st.subheader("💻 Technical & Skill Details")


# ==========================================
# Common Skills
# ==========================================

aptitude_score = st.slider(
    "Aptitude Score",
    min_value=20.0,
    max_value=100.0,
    value=65.0,
    step=1.0
)

communication_skills = st.slider(
    "Communication Skills",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)


# ==========================================
# Branch-Specific Skills
# ==========================================

if branch == "CSE":

    st.markdown("### 💻 Computer Science Skills")

    coding_skills = st.slider(
        "Coding Skills",
        0.0, 10.0, 5.0, 0.5
    )

    dsa_score = st.slider(
        "DSA Score",
        0.0, 10.0, 5.0, 0.5
    )

    ml_knowledge = st.slider(
        "Machine Learning Knowledge",
        0.0, 10.0, 5.0, 0.5
    )

    system_design = st.slider(
        "System Design Knowledge",
        0.0, 10.0, 5.0, 0.5
    )


elif branch == "IT":

    st.markdown("### 🖥️ Information Technology Skills")

    coding_skills = st.slider(
        "Coding Skills",
        0.0, 10.0, 5.0, 0.5
    )

    dsa_score = st.slider(
        "DSA Score",
        0.0, 10.0, 5.0, 0.5
    )

    database_knowledge = st.slider(
        "Database Knowledge",
        0.0, 10.0, 5.0, 0.5
    )

    cloud_knowledge = st.slider(
        "Cloud Computing Knowledge",
        0.0, 10.0, 5.0, 0.5
    )

    ml_knowledge = 5.0
    system_design = 5.0


elif branch == "ECE":

    st.markdown("### 📡 Electronics & Communication Skills")

    embedded_systems = st.slider(
        "Embedded Systems",
        0.0, 10.0, 5.0, 0.5
    )

    vlsi = st.slider(
        "VLSI Knowledge",
        0.0, 10.0, 5.0, 0.5
    )

    electronics = st.slider(
        "Electronics Knowledge",
        0.0, 10.0, 5.0, 0.5
    )

    communication_systems = st.slider(
        "Communication Systems",
        0.0, 10.0, 5.0, 0.5
    )

    coding_skills = 5.0
    dsa_score = 5.0
    ml_knowledge = 5.0
    system_design = 5.0


elif branch == "EE":

    st.markdown("### ⚡ Electrical Engineering Skills")

    electrical_systems = st.slider(
        "Electrical Systems",
        0.0, 10.0, 5.0, 0.5
    )

    power_systems = st.slider(
        "Power Systems",
        0.0, 10.0, 5.0, 0.5
    )

    control_systems = st.slider(
        "Control Systems",
        0.0, 10.0, 5.0, 0.5
    )

    electrical_design = st.slider(
        "Electrical Design",
        0.0, 10.0, 5.0, 0.5
    )

    coding_skills = 5.0
    dsa_score = 5.0
    ml_knowledge = 5.0
    system_design = 5.0


elif branch == "ME":

    st.markdown("### ⚙️ Mechanical Engineering Skills")

    cad_design = st.slider(
        "CAD Design",
        0.0, 10.0, 5.0, 0.5
    )

    mechanical_design = st.slider(
        "Mechanical Design",
        0.0, 10.0, 5.0, 0.5
    )

    manufacturing = st.slider(
        "Manufacturing Knowledge",
        0.0, 10.0, 5.0, 0.5
    )

    production = st.slider(
        "Production Knowledge",
        0.0, 10.0, 5.0, 0.5
    )

    coding_skills = 5.0
    dsa_score = 5.0
    ml_knowledge = 5.0
    system_design = 5.0


elif branch == "CE":

    st.markdown("### 🏗️ Civil Engineering Skills")

    structural_design = st.slider(
        "Structural Design",
        0.0, 10.0, 5.0, 0.5
    )

    cad_design = st.slider(
        "CAD / AutoCAD",
        0.0, 10.0, 5.0, 0.5
    )

    construction = st.slider(
        "Construction Knowledge",
        0.0, 10.0, 5.0, 0.5
    )

    surveying = st.slider(
        "Surveying",
        0.0, 10.0, 5.0, 0.5
    )

    coding_skills = 5.0
    dsa_score = 5.0
    ml_knowledge = 5.0
    system_design = 5.0


elif branch == "Chemical":

    st.markdown("### 🧪 Chemical Engineering Skills")

    chemical_processes = st.slider(
        "Chemical Processes",
        0.0, 10.0, 5.0, 0.5
    )

    process_design = st.slider(
        "Process Design",
        0.0, 10.0, 5.0, 0.5
    )

    plant_operations = st.slider(
        "Plant Operations",
        0.0, 10.0, 5.0, 0.5
    )

    quality_control = st.slider(
        "Quality Control",
        0.0, 10.0, 5.0, 0.5
    )

    coding_skills = 5.0
    dsa_score = 5.0
    ml_knowledge = 5.0
    system_design = 5.0




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
    # Branch-Aware Career Recommendation
    # ==========================================

    branch_career_pools = {

        "CSE": [
            "Software Developer",
            "Data Analyst",
            "Data Scientist",
            "Machine Learning Engineer"
        ],

        "IT": [
            "Software Developer",
            "Data Analyst",
            "Data Scientist",
            "Machine Learning Engineer"
        ],

        "ECE": [
            "Embedded Systems Engineer",
            "VLSI Engineer",
            "Electronics Engineer",
            "Software Developer"
        ],

        "EE": [
            "Electrical Engineer",
            "Power Systems Engineer",
            "Embedded Systems Engineer",
            "Control Systems Engineer"
        ],

        "ME": [
            "Mechanical Design Engineer",
            "Manufacturing Engineer",
            "CAD Engineer",
            "Production Engineer"
        ],

        "CE": [
            "Civil Engineer",
            "Structural Engineer",
            "Construction Engineer",
            "Project Engineer"
        ],

        "Chemical": [
            "Chemical Engineer",
            "Process Engineer",
            "Production Engineer",
            "Quality Engineer"
        ]
    }

    career_weights = {

        "Software Developer": {
            "coding_skills": 0.30,
            "dsa_score": 0.25,
            "projects_count": 0.20,
            "internships": 0.10,
            "cgpa": 0.10,
            "communication_skills": 0.05
        },

        "Data Analyst": {
            "aptitude_score": 0.30,
            "communication_skills": 0.25,
            "coding_skills": 0.10,
            "projects_count": 0.15,
            "internships": 0.10,
            "cgpa": 0.10
        },

        "Data Scientist": {
            "ml_knowledge": 0.30,
            "coding_skills": 0.20,
            "aptitude_score": 0.15,
            "projects_count": 0.15,
            "cgpa": 0.10,
            "internships": 0.10
        },

        "Machine Learning Engineer": {
            "ml_knowledge": 0.30,
            "coding_skills": 0.25,
            "dsa_score": 0.15,
            "projects_count": 0.15,
            "internships": 0.10,
            "cgpa": 0.05
        },

        "Embedded Systems Engineer": {
            "coding_skills": 0.25,
            "dsa_score": 0.15,
            "projects_count": 0.20,
            "internships": 0.15,
            "cgpa": 0.15,
            "communication_skills": 0.10
        },

        "VLSI Engineer": {
            "dsa_score": 0.10,
            "projects_count": 0.25,
            "internships": 0.20,
            "cgpa": 0.25,
            "aptitude_score": 0.10,
            "certifications": 0.10
        },

        "Electronics Engineer": {
            "projects_count": 0.25,
            "internships": 0.20,
            "cgpa": 0.20,
            "aptitude_score": 0.15,
            "communication_skills": 0.10,
            "certifications": 0.10
        },

        "Electrical Engineer": {
            "projects_count": 0.25,
            "internships": 0.20,
            "cgpa": 0.25,
            "aptitude_score": 0.15,
            "certifications": 0.15
        },

        "Power Systems Engineer": {
            "projects_count": 0.25,
            "internships": 0.25,
            "cgpa": 0.25,
            "aptitude_score": 0.15,
            "certifications": 0.10
        },

        "Control Systems Engineer": {
            "projects_count": 0.25,
            "internships": 0.20,
            "cgpa": 0.25,
            "aptitude_score": 0.15,
            "certifications": 0.15
        },

        "Mechanical Design Engineer": {
            "projects_count": 0.25,
            "internships": 0.20,
            "cgpa": 0.25,
            "aptitude_score": 0.15,
            "certifications": 0.15
        },

        "Manufacturing Engineer": {
            "projects_count": 0.25,
            "internships": 0.25,
            "cgpa": 0.20,
            "aptitude_score": 0.15,
            "certifications": 0.15
        },

        "CAD Engineer": {
            "projects_count": 0.30,
            "internships": 0.20,
            "cgpa": 0.20,
            "certifications": 0.20,
            "aptitude_score": 0.10
        },

        "Production Engineer": {
            "projects_count": 0.25,
            "internships": 0.25,
            "cgpa": 0.20,
            "aptitude_score": 0.15,
            "communication_skills": 0.15
        },

        "Civil Engineer": {
            "projects_count": 0.25,
            "internships": 0.25,
            "cgpa": 0.25,
            "aptitude_score": 0.15,
            "communication_skills": 0.10
        },

        "Structural Engineer": {
            "projects_count": 0.25,
            "internships": 0.20,
            "cgpa": 0.25,
            "aptitude_score": 0.15,
            "certifications": 0.15
        },

        "Construction Engineer": {
            "projects_count": 0.25,
            "internships": 0.30,
            "cgpa": 0.20,
            "aptitude_score": 0.15,
            "communication_skills": 0.10
        },

        "Project Engineer": {
            "projects_count": 0.25,
            "internships": 0.25,
            "communication_skills": 0.20,
            "cgpa": 0.20,
            "aptitude_score": 0.10
        },

        "Chemical Engineer": {
            "projects_count": 0.25,
            "internships": 0.25,
            "cgpa": 0.25,
            "aptitude_score": 0.15,
            "certifications": 0.10
        },

        "Process Engineer": {
            "projects_count": 0.25,
            "internships": 0.25,
            "cgpa": 0.20,
            "aptitude_score": 0.15,
            "certifications": 0.15
        },

        "Quality Engineer": {
            "projects_count": 0.20,
            "internships": 0.20,
            "cgpa": 0.20,
            "aptitude_score": 0.20,
            "communication_skills": 0.20
        }
    }

    # Normalize aptitude score to 0-10 scale

    normalized_aptitude_score = aptitude_score / 10

    career_features = {
        "cgpa": cgpa,
        "aptitude_score": normalized_aptitude_score,
        "communication_skills": communication_skills,
        "coding_skills": coding_skills,
        "dsa_score": dsa_score,
        "ml_knowledge": ml_knowledge,
        "projects_count": projects_count,
        "internships": internships,
        "certifications": certifications
    }

    available_careers = branch_career_pools[branch]

    career_scores = {}

    for career in available_careers:

        score = 0

        for feature, weight in career_weights[career].items():
            score += career_features[feature] * weight

        career_scores[career] = score

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