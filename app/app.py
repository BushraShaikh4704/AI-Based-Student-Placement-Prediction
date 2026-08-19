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


    # ==========================================
    # Branch-Aware Career Weights
    # ==========================================

    branch_career_weights = {

        "CSE": {

            "Software Developer": {
                "coding_skills": 0.30,
                "dsa_score": 0.25,
                "projects_count": 0.20,
                "internships": 0.10,
                "cgpa": 0.10,
                "communication_skills": 0.05
            },

            "Data Analyst": {
                "aptitude_score": 0.20,
                "communication_skills": 0.20,
                "coding_skills": 0.15,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.20
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
            }
        },

        "IT": {

            "Software Developer": {
                "coding_skills": 0.25,
                "dsa_score": 0.20,
                "database_knowledge": 0.15,
                "cloud_knowledge": 0.15,
                "projects_count": 0.15,
                "internships": 0.05,
                "cgpa": 0.05
            },

            "Data Analyst": {
                "database_knowledge": 0.20,
                "aptitude_score": 0.20,
                "communication_skills": 0.15,
                "coding_skills": 0.10,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.10
            },

            "Data Scientist": {
                "coding_skills": 0.20,
                "database_knowledge": 0.15,
                "aptitude_score": 0.15,
                "projects_count": 0.20,
                "internships": 0.10,
                "cgpa": 0.20
            },

            "Machine Learning Engineer": {
                "coding_skills": 0.25,
                "dsa_score": 0.15,
                "cloud_knowledge": 0.15,
                "projects_count": 0.20,
                "internships": 0.10,
                "cgpa": 0.15
            }
        },

        "ECE": {

            "Embedded Systems Engineer": {
                "embedded_systems": 0.30,
                "electronics": 0.20,
                "communication_systems": 0.15,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.10
            },

            "VLSI Engineer": {
                "vlsi": 0.35,
                "electronics": 0.25,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.10,
                "certifications": 0.05
            },

            "Electronics Engineer": {
                "electronics": 0.35,
                "communication_systems": 0.20,
                "embedded_systems": 0.15,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.05
            },

            "Software Developer": {
                "coding_skills": 0.30,
                "dsa_score": 0.20,
                "projects_count": 0.20,
                "internships": 0.10,
                "cgpa": 0.10,
                "communication_skills": 0.10
            }
        },

        "EE": {

            "Electrical Engineer": {
                "electrical_systems": 0.35,
                "electrical_design": 0.20,
                "projects_count": 0.20,
                "internships": 0.10,
                "cgpa": 0.10,
                "certifications": 0.05
            },

            "Power Systems Engineer": {
                "power_systems": 0.35,
                "electrical_systems": 0.25,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.10,
                "certifications": 0.05
            },

            "Embedded Systems Engineer": {
                "control_systems": 0.20,
                "electrical_systems": 0.25,
                "electrical_design": 0.20,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.10
            },

            "Control Systems Engineer": {
                "control_systems": 0.35,
                "electrical_systems": 0.20,
                "electrical_design": 0.20,
                "projects_count": 0.15,
                "internships": 0.05,
                "cgpa": 0.05
            }
        },

        "ME": {

            "Mechanical Design Engineer": {
                "mechanical_design": 0.35,
                "cad_design": 0.30,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.10
            },

            "Manufacturing Engineer": {
                "manufacturing": 0.35,
                "mechanical_design": 0.20,
                "projects_count": 0.15,
                "internships": 0.20,
                "cgpa": 0.10
            },

            "CAD Engineer": {
                "cad_design": 0.40,
                "mechanical_design": 0.25,
                "projects_count": 0.15,
                "certifications": 0.10,
                "cgpa": 0.10
            },

            "Production Engineer": {
                "production": 0.35,
                "manufacturing": 0.25,
                "projects_count": 0.15,
                "internships": 0.15,
                "cgpa": 0.10
            }
        },

        "CE": {

            "Civil Engineer": {
                "construction": 0.30,
                "surveying": 0.20,
                "structural_design": 0.15,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.10
            },

            "Structural Engineer": {
                "structural_design": 0.40,
                "cad_design": 0.20,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.10,
                "certifications": 0.05
            },

            "Construction Engineer": {
                "construction": 0.40,
                "surveying": 0.15,
                "projects_count": 0.15,
                "internships": 0.20,
                "cgpa": 0.10
            },

            "Project Engineer": {
                "construction": 0.25,
                "projects_count": 0.20,
                "internships": 0.20,
                "communication_skills": 0.15,
                "cgpa": 0.10,
                "surveying": 0.10
            }
        },

        "Chemical": {

            "Chemical Engineer": {
                "chemical_processes": 0.35,
                "process_design": 0.25,
                "projects_count": 0.15,
                "internships": 0.10,
                "cgpa": 0.10,
                "certifications": 0.05
            },

            "Process Engineer": {
                "process_design": 0.35,
                "chemical_processes": 0.25,
                "plant_operations": 0.20,
                "projects_count": 0.10,
                "internships": 0.10
            },

            "Production Engineer": {
                "plant_operations": 0.30,
                "chemical_processes": 0.25,
                "process_design": 0.20,
                "projects_count": 0.10,
                "internships": 0.10,
                "cgpa": 0.05
            },

            "Quality Engineer": {
                "quality_control": 0.35,
                "chemical_processes": 0.20,
                "communication_skills": 0.15,
                "projects_count": 0.10,
                "internships": 0.10,
                "certifications": 0.10
            }
        }
    }


    # ==========================================
    # Career Features
    # ==========================================

    normalized_aptitude_score = aptitude_score / 10

    career_features = {
        "cgpa": cgpa,
        "aptitude_score": normalized_aptitude_score,
        "communication_skills": communication_skills,

        "coding_skills": coding_skills,
        "dsa_score": dsa_score,
        "ml_knowledge": ml_knowledge,

        "database_knowledge": (
            database_knowledge
            if branch == "IT"
            else 0
        ),

        "cloud_knowledge": (
            cloud_knowledge
            if branch == "IT"
            else 0
        ),

        "embedded_systems": (
            embedded_systems
            if branch == "ECE"
            else 0
        ),

        "vlsi": (
            vlsi
            if branch == "ECE"
            else 0
        ),

        "electronics": (
            electronics
            if branch == "ECE"
            else 0
        ),

        "communication_systems": (
            communication_systems
            if branch == "ECE"
            else 0
        ),

        "electrical_systems": (
            electrical_systems
            if branch == "EE"
            else 0
        ),

        "power_systems": (
            power_systems
            if branch == "EE"
            else 0
        ),

        "control_systems": (
            control_systems
            if branch == "EE"
            else 0
        ),

        "electrical_design": (
            electrical_design
            if branch == "EE"
            else 0
        ),

        "cad_design": (
            cad_design
            if branch in ["ME", "CE"]
            else 0
        ),

        "mechanical_design": (
            mechanical_design
            if branch == "ME"
            else 0
        ),

        "manufacturing": (
            manufacturing
            if branch == "ME"
            else 0
        ),

        "production": (
            production
            if branch == "ME"
            else 0
        ),

        "structural_design": (
            structural_design
            if branch == "CE"
            else 0
        ),

        "construction": (
            construction
            if branch == "CE"
            else 0
        ),

        "surveying": (
            surveying
            if branch == "CE"
            else 0
        ),

        "chemical_processes": (
            chemical_processes
            if branch == "Chemical"
            else 0
        ),

        "process_design": (
            process_design
            if branch == "Chemical"
            else 0
        ),

        "plant_operations": (
            plant_operations
            if branch == "Chemical"
            else 0
        ),

        "quality_control": (
            quality_control
            if branch == "Chemical"
            else 0
        ),

        "projects_count": projects_count,
        "internships": internships,
        "certifications": certifications
    }


    # ==========================================
    # Calculate Career Scores
    # ==========================================

    available_careers = branch_career_pools[branch]

    career_scores = {}

    for career in available_careers:

        score = 0

        for feature, weight in branch_career_weights[branch][career].items():
            score += career_features[feature] * weight

        career_scores[career] = score


    # ==========================================
    # Rank Careers
    # ==========================================

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
    # Prepare Branch-Specific Database Values
    # ==========================================

    database_knowledge_db = (
        database_knowledge
        if branch == "IT"
        else 0
    )

    cloud_knowledge_db = (
        cloud_knowledge
        if branch == "IT"
        else 0
    )

    embedded_systems_db = (
        embedded_systems
        if branch == "ECE"
        else 0
    )

    vlsi_db = (
        vlsi
        if branch == "ECE"
        else 0
    )

    electronics_db = (
        electronics
        if branch == "ECE"
        else 0
    )

    communication_systems_db = (
        communication_systems
        if branch == "ECE"
        else 0
    )

    electrical_systems_db = (
        electrical_systems
        if branch == "EE"
        else 0
    )

    power_systems_db = (
        power_systems
        if branch == "EE"
        else 0
    )

    control_systems_db = (
        control_systems
        if branch == "EE"
        else 0
    )

    electrical_design_db = (
        electrical_design
        if branch == "EE"
        else 0
    )

    cad_design_db = (
        cad_design
        if branch in ["ME", "CE"]
        else 0
    )

    mechanical_design_db = (
        mechanical_design
        if branch == "ME"
        else 0
    )

    manufacturing_db = (
        manufacturing
        if branch == "ME"
        else 0
    )

    production_db = (
        production
        if branch == "ME"
        else 0
    )

    structural_design_db = (
        structural_design
        if branch == "CE"
        else 0
    )

    construction_db = (
        construction
        if branch == "CE"
        else 0
    )

    surveying_db = (
        surveying
        if branch == "CE"
        else 0
    )

    chemical_processes_db = (
        chemical_processes
        if branch == "Chemical"
        else 0
    )

    process_design_db = (
        process_design
        if branch == "Chemical"
        else 0
    )

    plant_operations_db = (
        plant_operations
        if branch == "Chemical"
        else 0
    )

    quality_control_db = (
        quality_control
        if branch == "Chemical"
        else 0
    )


    # ==========================================
    # Placement Status for Database
    # ==========================================

    placement_status_db = int(prediction[0])


    # ==========================================
    # Prepare Complete Student Record
    # ==========================================

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

        technical_skill_score,
        has_backlog,
        experience_score,
        technical_skill_gap,

        placement_status_db,
        placement_probability,
        recommended_career,
        career_suitability_score,
        alternative_career,

        database_knowledge_db,
        cloud_knowledge_db,

        embedded_systems_db,
        vlsi_db,
        electronics_db,
        communication_systems_db,

        electrical_systems_db,
        power_systems_db,
        control_systems_db,
        electrical_design_db,

        cad_design_db,
        mechanical_design_db,
        manufacturing_db,
        production_db,

        structural_design_db,
        construction_db,
        surveying_db,

        chemical_processes_db,
        process_design_db,
        plant_operations_db,
        quality_control_db
    )


    # ==========================================
    # MySQL Insert Query
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

        technical_skill_score,
        has_backlog,
        experience_score,
        technical_skill_gap,

        placement_status,
        placement_probability,
        recommended_career,
        career_suitability_score,
        alternative_career,

        database_knowledge,
        cloud_knowledge,

        embedded_systems,
        vlsi,
        electronics,
        communication_systems,

        electrical_systems,
        power_systems,
        control_systems,
        electrical_design,

        cad_design,
        mechanical_design,
        manufacturing,
        production,

        structural_design,
        construction,
        surveying,

        chemical_processes,
        process_design,
        plant_operations,
        quality_control
    )
    VALUES (
        %s, %s, %s, %s, %s,

        %s, %s, %s, %s, %s, %s,

        %s, %s, %s, %s, %s, %s,

        %s, %s, %s, %s,

        %s, %s, %s, %s, %s,

        %s, %s,

        %s, %s, %s, %s,

        %s, %s, %s, %s,

        %s, %s, %s, %s,

        %s, %s, %s,

        %s, %s, %s, %s
    )
    """


    # ==========================================
    # Connect to MySQL
    # ==========================================

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shaikh@#12",
        database="placement_career_db"
    )

    cursor = connection.cursor()


    # ==========================================
    # Insert Complete Student Record
    # ==========================================

    cursor.execute(
        insert_query,
        student_record
    )

    connection.commit()


    # ==========================================
    # Close Database Connection
    # ==========================================

    cursor.close()
    connection.close()


    # ==========================================
    # Success Message
    # ==========================================

    st.success(
        "✅ Prediction completed and student result "
        "stored successfully!"
    )
