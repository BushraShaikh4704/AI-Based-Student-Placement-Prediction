import streamlit as st
import joblib
import pandas as pd
import mysql.connector

st.set_page_config(
    page_title="CareerAI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("app/style.css", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "branch" not in st.session_state:
    st.session_state.branch = ""

if "college_tier" not in st.session_state:
    st.session_state.college_tier = ""

if "cgpa" not in st.session_state:
    st.session_state.cgpa = 0.0

if "backlogs" not in st.session_state:
    st.session_state.backlogs = 0

if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

if "placement_status" not in st.session_state:
    st.session_state.placement_status = "Not Available"

if "placement_probability" not in st.session_state:
    st.session_state.placement_probability = 0.0

if "technical_skill_score" not in st.session_state:
    st.session_state.technical_skill_score = 0.0

if "experience_score" not in st.session_state:
    st.session_state.experience_score = 0

with st.sidebar:

    st.markdown(
        """
        # 🎓 CareerAI
        Placement Predictor
        """
    )

    st.divider()

    if st.button("🏠 Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"

    if st.button("📋 Student Assessment", use_container_width=True):
        st.session_state.page = "Assessment"

    if st.button("📈 Prediction Result", use_container_width=True):
        st.session_state.page = "Prediction"

    if st.button("🎯 Career Recommendation", use_container_width=True):
        st.session_state.page = "Career"

    if st.button("📊 Skill Analysis", use_container_width=True):
        st.session_state.page = "Skills"

    if st.button("🕒 Prediction History", use_container_width=True):
        st.session_state.page = "History"


def dashboard_page():

    st.title(
        "🎓 AI-Based Student Placement & Career Recommendation System"
    )

    st.caption(
        "Predict your placement potential and discover your ideal career path"
    )

    st.markdown("---")

    st.subheader("👤 Student Profile Summary")

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.metric(
            "Name",
            st.session_state.student_name
            if st.session_state.student_name
            else "Not Provided"
        )

    with col2:
        st.metric(
            "Branch",
            st.session_state.branch
            if st.session_state.branch
            else "Not Selected"
        )

    with col3:
        st.metric(
            "College Tier",
            st.session_state.college_tier
            if st.session_state.college_tier
            else "Not Selected"
        )

    with col4:
        st.metric(
            "CGPA",
            st.session_state.cgpa
            if st.session_state.cgpa > 0
            else "-"
        )

    with col5:
        st.metric(
            "Backlogs",
            st.session_state.backlogs
        )

    st.markdown("---")

    left,right = st.columns([2,1])

    with left:

        st.subheader(
            "📈 Placement Prediction Result"
        )

        if st.session_state.prediction_done:
            st.metric(
                "Placement Status",
                 st.session_state.placement_status
                )

            st.metric(
                "Probability",
                f"{st.session_state.placement_probability}%"
            )

            st.progress(
                st.session_state.placement_probability / 100
            )

        else:

            st.info(
                "Run Prediction to view results"
            )

    with right:

        st.subheader(
            "💡 Quick Insights"
        )

        st.success(
            f"Technical Skills : {st.session_state.technical_skill_score}"
        )

        st.info(
            f"Experience Score : {st.session_state.experience_score}"
        )

        if "communication_skills" in st.session_state:

            st.warning(
                f"Communication : {st.session_state.communication_skills}"
            )

    st.markdown("---")

    left,right = st.columns([2,1])

    with left:

        st.subheader(
            "🎯 Career Recommendation"
        )

        if "recommended_career" in st.session_state:

            st.success(
                st.session_state.recommended_career
        )

        else:

            st.info(
                "Run Career Recommendation"
            )

    with right:

        st.subheader(
            "📌 Strengths"
        )

        if "strengths" in st.session_state:

            for item in st.session_state.strengths:
                st.write(f"✅ {item}")

        st.subheader(
            "⚠ Areas To Improve"
        )

        if "areas_to_improve" in st.session_state:

            for item in st.session_state.areas_to_improve:
                st.write(f"⚠ {item}")

    st.markdown("---")

    if st.button(
        "📝 Take Assessment",
        use_container_width=True
    ):

        st.session_state.page = "Assessment"
        st.rerun()


def assessment_page():

    st.title("📋 Student Assessment")

    st.subheader("Basic Information")

    student_name = st.text_input(
            "Full Name",
            value=st.session_state.student_name
        )

    col1,col2 = st.columns(2)

    with col1:
            branch = st.selectbox(
                "Branch",
                [
                    "CSE",
                    "IT",
                    "ECE",
                    "EE",
                    "ME",
                    "CE",
                    "Chemical"
                ]
            )

    with col2:
            college_tier = st.selectbox(
                "College Tier",
                [
                    "Tier-1",
                    "Tier-2",
                    "Tier-3"
                ]
            )

    col1,col2 = st.columns(2)

    with col1:
            cgpa = st.number_input(
                "CGPA",
                min_value=0.0,
                max_value=10.0,
                value=float(st.session_state.cgpa),
                step=0.1
            )

    with col2:
            backlogs = st.number_input(
                "Backlogs",
                min_value=0,
                max_value=20,
                value=int(st.session_state.backlogs)
            )

    st.divider()

    st.subheader("Technical Skills")

    aptitude_score = st.slider(
        "Aptitude Score",
        0.0,100.0,50.0
        )

    communication_skills = st.slider(
        "Communication Skills",
        0.0,10.0,5.0
        )

    if branch == "CSE":

            st.subheader("💻 Computer Science Skills")

            coding_skills = st.slider(
            "Coding Skills",
            0.0,10.0,5.0
            )

            dsa_score = st.slider(
            "DSA Score",
            0.0,10.0,5.0
            )

            ml_knowledge = st.slider(
            "Machine Learning Knowledge",
            0.0,10.0,5.0
            )

            system_design = st.slider(
            "System Design Knowledge",
            0.0,10.0,5.0
            )


    elif branch == "IT":

            st.subheader("🖥️ Information Technology Skills")

            coding_skills = st.slider(
            "Coding Skills",
            0.0,10.0,5.0
            )

            dsa_score = st.slider(
            "DSA Score",
            0.0,10.0,5.0
            )

            database_knowledge = st.slider(
            "Database Knowledge",
            0.0,10.0,5.0
            )

            cloud_knowledge = st.slider(
            "Cloud Computing Knowledge",
            0.0,10.0,5.0
            )

            ml_knowledge = 5.0
            system_design = 5.0

    elif branch == "ECE":

            st.subheader("📡 Electronics & Communication Skills")

            embedded_systems = st.slider(
            "Embedded Systems",
            0.0,10.0,5.0
            )

            vlsi = st.slider(
            "VLSI Knowledge",
            0.0,10.0,5.0
            )

            electronics = st.slider(
            "Electronics Knowledge",
            0.0,10.0,5.0
            )

            communication_systems = st.slider(
            "Communication Systems",
            0.0,10.0,5.0
            )

            coding_skills = 5.0
            dsa_score = 5.0
            ml_knowledge = 5.0
            system_design = 5.0

    elif branch == "EE":

            st.subheader("⚡ Electrical Engineering Skills")

            electrical_systems = st.slider(
            "Electrical Systems",
            0.0,10.0,5.0
            )

            power_systems = st.slider(
            "Power Systems",
            0.0,10.0,5.0
            )

            control_systems = st.slider(
            "Control Systems",
            0.0,10.0,5.0
            )

            electrical_design = st.slider(
            "Electrical Design",
            0.0,10.0,5.0
            )

            coding_skills = 5.0
            dsa_score = 5.0
            ml_knowledge = 5.0
            system_design = 5.0

    elif branch == "ME":

            st.subheader("⚙️ Mechanical Engineering Skills")

            cad_design = st.slider(
            "CAD Design",
            0.0,10.0,5.0
            )

            mechanical_design = st.slider(
            "Mechanical Design",
            0.0,10.0,5.0
            )

            manufacturing = st.slider(
            "Manufacturing Knowledge",
            0.0,10.0,5.0
            )

            production = st.slider(
            "Production Knowledge",
            0.0,10.0,5.0
            )

            coding_skills = 5.0
            dsa_score = 5.0
            ml_knowledge = 5.0
            system_design = 5.0

    elif branch == "CE":

            st.subheader("🏗️ Civil Engineering Skills")

            structural_design = st.slider(
            "Structural Design",
            0.0,10.0,5.0
            )

            cad_design = st.slider(
            "CAD / AutoCAD",
            0.0,10.0,5.0
            )

            construction = st.slider(
            "Construction Knowledge",
            0.0,10.0,5.0
            )

            surveying = st.slider(
            "Surveying",
            0.0,10.0,5.0
            )

            coding_skills = 5.0
            dsa_score = 5.0
            ml_knowledge = 5.0
            system_design = 5.0

    elif branch == "Chemical":
            
            st.subheader("🧪 Chemical Engineering Skills")

            chemical_processes = st.slider(
            "Chemical Processes",
            0.0,10.0,5.0
            )

            process_design = st.slider(
            "Process Design",
            0.0,10.0,5.0
            )

            plant_operations = st.slider(
            "Plant Operations",
            0.0,10.0,5.0
            )

            quality_control = st.slider(
            "Quality Control",
            0.0,10.0,5.0
            )

            coding_skills = 5.0
            dsa_score = 5.0
            ml_knowledge = 5.0
            system_design = 5.0

    st.divider()

    st.subheader("🏆 Experience & Activities")

    col1,col2,col3 = st.columns(3)

    with col1:
            internships = st.number_input(
                "Internships",
                min_value=0,
                value=0
            )

    with col2:
            projects_count = st.number_input(
                "Projects",
                min_value=0,
                value=0
            )

    with col3:
            certifications = st.number_input(
                "Certifications",
                min_value=0,
                value=0
            )

    col1,col2,col3 = st.columns(3)

    with col1:
            hackathons = st.number_input(
                "Hackathons",
                min_value=0,
                value=0
            )

    with col2:
            open_source_contributions = st.number_input(
                "Open Source",
                min_value=0,
                value=0
            )

    with col3:
            extracurriculars = st.number_input(
                "Extracurriculars",
                min_value=0,
                value=0
            )

    save_button = st.button(
        "🚀 Save Assessment",
        use_container_width=True
    )

    if save_button:

        st.session_state.student_name = student_name
        st.session_state.branch = branch
        st.session_state.college_tier = college_tier
        st.session_state.cgpa = cgpa
        st.session_state.backlogs = backlogs

        st.session_state.coding_skills = coding_skills
        st.session_state.dsa_score = dsa_score
        st.session_state.ml_knowledge = ml_knowledge
        st.session_state.system_design = system_design
        st.session_state.aptitude_score = aptitude_score
        st.session_state.communication_skills = communication_skills

        st.session_state.internships = internships
        st.session_state.projects_count = projects_count
        st.session_state.certifications = certifications
        st.session_state.hackathons = hackathons
        st.session_state.open_source_contributions = open_source_contributions
        st.session_state.extracurriculars = extracurriculars

        st.success(
            "Assessment saved successfully!"
        )

        if branch == "IT":

            st.session_state.database_knowledge = database_knowledge
            st.session_state.cloud_knowledge = cloud_knowledge

        elif branch == "ECE":

            st.session_state.embedded_systems = embedded_systems
            st.session_state.vlsi = vlsi
            st.session_state.electronics = electronics
            st.session_state.communication_systems = communication_systems

        elif branch == "EE":

            st.session_state.electrical_systems = electrical_systems
            st.session_state.power_systems = power_systems
            st.session_state.control_systems = control_systems
            st.session_state.electrical_design = electrical_design

        elif branch == "ME":

            st.session_state.cad_design = cad_design
            st.session_state.mechanical_design = mechanical_design
            st.session_state.manufacturing = manufacturing
            st.session_state.production = production

        elif branch == "CE":

            st.session_state.structural_design = structural_design
            st.session_state.cad_design = cad_design
            st.session_state.construction = construction
            st.session_state.surveying = surveying

        elif branch == "Chemical":

            st.session_state.chemical_processes = chemical_processes
            st.session_state.process_design = process_design
            st.session_state.plant_operations = plant_operations
            st.session_state.quality_control = quality_control

    st.markdown("---")

    if st.button(
        "➡ Proceed To Prediction",
        use_container_width=True
        ):

        st.session_state.page = "Prediction"

        st.rerun()

def prediction_page():

    st.title("📈 Placement Prediction")

    required_fields = [
        "coding_skills",
        "dsa_score",
        "ml_knowledge",
        "system_design",
        "aptitude_score",
        "communication_skills"
    ]

    if not all(
        key in st.session_state
        for key in required_fields
    ):
        st.warning(
            "Please complete Student Assessment first."
        )
        return

    if st.button(
        "🎯 Run Prediction",
        use_container_width=True
    ):

        try:

            preprocessor = joblib.load(
                "models/preprocessor.pkl"
            )

            best_model = joblib.load(
                "models/best_model.pkl"
            )

            technical_skill_score = (
                st.session_state.coding_skills +
                st.session_state.dsa_score +
                st.session_state.ml_knowledge +
                st.session_state.system_design
            ) / 4

            experience_score = (
                st.session_state.internships +
                st.session_state.projects_count +
                st.session_state.certifications +
                st.session_state.hackathons +
                st.session_state.open_source_contributions +
                st.session_state.extracurriculars
            )

            has_backlog = (
                1
                if st.session_state.backlogs > 0
                else 0
            )

            technical_skill_gap = (
                max(
                    st.session_state.coding_skills,
                    st.session_state.dsa_score,
                    st.session_state.ml_knowledge,
                    st.session_state.system_design
                )
                -
                min(
                    st.session_state.coding_skills,
                    st.session_state.dsa_score,
                    st.session_state.ml_knowledge,
                    st.session_state.system_design
                )
            )

            student_data = {
                "branch":
                st.session_state.branch,

                "college_tier":
                st.session_state.college_tier,

                "cgpa":
                st.session_state.cgpa,

                "backlogs":
                st.session_state.backlogs,

                "coding_skills":
                st.session_state.coding_skills,

                "dsa_score":
                st.session_state.dsa_score,

                "aptitude_score":
                st.session_state.aptitude_score,

                "communication_skills":
                st.session_state.communication_skills,

                "ml_knowledge":
                st.session_state.ml_knowledge,

                "system_design":
                st.session_state.system_design,

                "internships":
                st.session_state.internships,

                "projects_count":
                st.session_state.projects_count,

                "certifications":
                st.session_state.certifications,

                "hackathons":
                st.session_state.hackathons,

                "open_source_contributions":
                st.session_state.open_source_contributions,

                "extracurriculars":
                st.session_state.extracurriculars,

                "technical_skill_score":
                technical_skill_score,

                "has_backlog":
                has_backlog,

                "experience_score":
                experience_score,

                "technical_skill_gap":
                technical_skill_gap
            }

            student_df = pd.DataFrame(
                [student_data]
            )

            encoded_data = (
                preprocessor.transform(
                    student_df
                )
            )

            prediction = (
                best_model.predict(
                    encoded_data
                )[0]
            )

            probability = (
                best_model.predict_proba(
                    encoded_data
                )[0][1] * 100
            )

            placement_status = (
                "Placed"
                if prediction == 1
                else "Not Placed"
            )

            st.session_state.placement_status = (
                placement_status
            )

            st.session_state.placement_probability = (
                round(probability,2)
            )

            st.session_state.technical_skill_score = (
                round(
                    technical_skill_score,
                    2
                )
            )

            st.session_state.experience_score = (
                experience_score
            )

            st.session_state.prediction_done = True

            st.session_state.technical_skill_gap = (
                technical_skill_gap
            )

            st.session_state.has_backlog = (
                has_backlog
            )

            st.success(
                "Prediction Completed Successfully"
            )

        except Exception as e:

            st.error(
                f"Prediction Error : {e}"
            )

    if st.session_state.prediction_done:

        col1,col2 = st.columns(2)

        with col1:

            st.metric(
                "Placement Status",
                st.session_state.placement_status
            )

        with col2:

            st.metric(
                "Placement Probability",
                f"{st.session_state.placement_probability}%"
            )

        st.progress(
            st.session_state.placement_probability / 100
        )

    st.markdown("---")

    if st.session_state.prediction_done:

        if st.button(
            "🎯 View Career Recommendation",
            use_container_width=True
        ):

            st.session_state.page = "Career"

            st.rerun()

def career_page():

    branch = st.session_state.branch
    cgpa = st.session_state.cgpa

    aptitude_score = st.session_state.aptitude_score
    communication_skills = st.session_state.communication_skills

    projects_count = st.session_state.projects_count
    internships = st.session_state.internships
    certifications = st.session_state.certifications

    coding_skills = st.session_state.coding_skills
    dsa_score = st.session_state.dsa_score
    ml_knowledge = st.session_state.ml_knowledge
    system_design = st.session_state.system_design
    embedded_systems = st.session_state.get("embedded_systems", 0)
    vlsi = st.session_state.get("vlsi", 0)
    electronics = st.session_state.get("electronics", 0)
    communication_systems = st.session_state.get("communication_systems", 0)
    electrical_systems = st.session_state.get("electrical_systems", 0)
    power_systems = st.session_state.get("power_systems", 0)
    control_systems = st.session_state.get("control_systems", 0)
    electrical_design = st.session_state.get("electrical_design", 0)
    cad_design = st.session_state.get("cad_design", 0)
    mechanical_design = st.session_state.get("mechanical_design", 0)
    manufacturing = st.session_state.get("manufacturing", 0)
    production = st.session_state.get("production", 0)
    structural_design = st.session_state.get("structural_design", 0)
    construction = st.session_state.get("construction", 0)
    surveying = st.session_state.get("surveying", 0)
    chemical_processes = st.session_state.get("chemical_processes", 0)
    process_design = st.session_state.get("process_design", 0)
    plant_operations = st.session_state.get("plant_operations", 0)
    quality_control = st.session_state.get("quality_control", 0)
    database_knowledge = st.session_state.get("database_knowledge",0)
    cloud_knowledge = st.session_state.get("cloud_knowledge", 0)


    st.title("🎯 Career Recommendation")

    if not st.session_state.prediction_done:

        st.warning(
            "Please run Placement Prediction first."
        )

        return

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

    normalized_projects = min(projects_count, 10)
    normalized_internships = min(internships, 5) * 2
    normalized_certifications = min(certifications, 10)


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

        "projects_count": normalized_projects,
        "internships": normalized_internships,
        "certifications": normalized_certifications
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
    career_suitability_score = round(sorted_careers[0][1],2)
    alternative_career = sorted_careers[1][0]


    st.session_state.recommended_career = recommended_career

    st.session_state.career_score = (
        career_suitability_score
    )

    st.session_state.alternative_career = (
    alternative_career
)

    col1,col2 = st.columns(2)

    with col1:

        st.success(
            f"Recommended Career : {recommended_career}"
        )

        st.metric(
            "Suitability Score",
            f"{career_suitability_score:.2f}/10"
        )

    with col2:

        st.info(
            f"Alternative Career : {alternative_career}"
        )

    st.markdown("---")

    st.subheader("Other Career Options")

    options_df = pd.DataFrame(
        sorted_careers,
        columns=[
            "Career",
            "Score"
        ]
    )

    options_df["Score"] = (
        options_df["Score"]
        .round(2)
    )

    st.dataframe(
        options_df,
        use_container_width=True
    )

    st.markdown("---")

    if st.button(
        "📊 View Skill Analysis",
        use_container_width=True
    ):

        st.session_state.page = "Skills"

        st.rerun()


def skills_page():

    st.title("📊 Skill Analysis")

    if not st.session_state.prediction_done:

        st.warning(
            "Please run Placement Prediction first."
        )

        return

    technical_score = (
        st.session_state.technical_skill_score
    )

    experience_score = (
        st.session_state.experience_score
    )

    communication_score = (
        st.session_state.communication_skills
    )

    overall_score = (
        technical_score +
        communication_score +
        min(experience_score,10)
    ) / 3

    st.subheader("💡 Quick Insights")

    col1,col2 = st.columns(2)

    with col1:

        st.metric(
            "Technical Skills",
            f"{technical_score:.2f}/10"
        )

        st.metric(
            "Communication",
            f"{communication_score:.2f}/10"
        )

    with col2:

        st.metric(
            "Experience Score",
            experience_score
        )

        st.metric(
            "Overall Profile",
            f"{overall_score:.2f}/10"
        )

    st.markdown("---")

    st.subheader("✅ Top Strengths")

    strengths = []

    if st.session_state.coding_skills >= 7:
        strengths.append(
            "Strong Coding Skills"
        )

    if st.session_state.dsa_score >= 7:
        strengths.append(
            "Good DSA Knowledge"
        )

    if st.session_state.ml_knowledge >= 7:
        strengths.append(
            "Excellent ML Understanding"
        )

    if st.session_state.projects_count >= 2:
        strengths.append(
            "Good Project Experience"
        )

    if st.session_state.certifications >= 2:
        strengths.append(
            "Active in Certifications"
        )

    if len(strengths) == 0:
        strengths.append(
            "Keep improving your profile"
        )

    st.session_state.strengths = strengths

    for item in strengths:
        st.success(item)


    st.markdown("---")

    st.subheader("⚠ Areas To Improve")

    improvements = []

    if st.session_state.communication_skills < 7:
        improvements.append(
            "Communication Skills"
        )

    if st.session_state.system_design < 7:
        improvements.append(
            "System Design Knowledge"
        )

    if st.session_state.hackathons < 1:
        improvements.append(
            "Hackathon Participation"
        )

    if st.session_state.internships < 1:
        improvements.append(
            "Internship Experience"
        )

    if len(improvements) == 0:
        improvements.append(
            "No major improvement areas detected"
        )

    st.session_state.areas_to_improve = improvements

    for item in improvements:
        st.warning(item)

    st.markdown("---")

    col1,col2 = st.columns(2)

    with col1:

        if st.button(
            "🏠 Back To Dashboard",
            use_container_width=True
        ):

            st.session_state.page = "Dashboard"

            st.rerun()

    with col2:

        if st.button(
            "📜 View History",
            use_container_width=True
        ):

            st.session_state.page = "History"

            st.rerun()


def save_to_database():

    student_name = st.session_state.student_name
    branch = st.session_state.branch
    college_tier = st.session_state.college_tier
    cgpa = st.session_state.cgpa
    backlogs = st.session_state.backlogs
    coding_skills = st.session_state.coding_skills
    dsa_score = st.session_state.dsa_score
    aptitude_score = st.session_state.aptitude_score
    communication_skills = st.session_state.communication_skills
    ml_knowledge = st.session_state.ml_knowledge
    system_design = st.session_state.system_design

    internships = st.session_state.internships
    projects_count = st.session_state.projects_count
    certifications = st.session_state.certifications
    hackathons = st.session_state.hackathons
    open_source_contributions = st.session_state.open_source_contributions
    extracurriculars = st.session_state.extracurriculars

    technical_skill_score = st.session_state.technical_skill_score
    experience_score = st.session_state.experience_score
    technical_skill_gap = st.session_state.technical_skill_gap
    has_backlog = st.session_state.has_backlog

# ==========================================
# Prepare Branch-Specific Database Values
# ==========================================

    database_knowledge_db = st.session_state.get(
        "database_knowledge",
        0
    )

    cloud_knowledge_db = st.session_state.get(
        "cloud_knowledge",
        0
    )

    embedded_systems_db = st.session_state.get(
        "embedded_systems",
        0
    )

    vlsi_db = st.session_state.get(
        "vlsi",
        0
    )

    electronics_db = st.session_state.get(
        "electronics",
        0
    )

    communication_systems_db = st.session_state.get(
        "communication_systems",
        0
    )

    electrical_systems_db = st.session_state.get(
        "electrical_systems",
        0
    )

    power_systems_db = st.session_state.get(
        "power_systems",
        0
    )

    control_systems_db = st.session_state.get(
        "control_systems",
        0
    )

    electrical_design_db = st.session_state.get(
        "electrical_design",
        0
    )

    cad_design_db = st.session_state.get(
        "cad_design",
        0
    )

    mechanical_design_db = st.session_state.get(
        "mechanical_design",
        0
    )

    manufacturing_db = st.session_state.get(
        "manufacturing",
        0
    )

    production_db = st.session_state.get(
        "production",
        0
    )

    structural_design_db = st.session_state.get(
        "structural_design",
        0
    )

    construction_db = st.session_state.get(
        "construction",
        0
    )

    surveying_db = st.session_state.get(
        "surveying",
        0
    )

    chemical_processes_db = st.session_state.get(
        "chemical_processes",
        0
    )

    process_design_db = st.session_state.get(
        "process_design",
        0
    )

    plant_operations_db = st.session_state.get(
        "plant_operations",
        0
    )

    quality_control_db = st.session_state.get(
        "quality_control",
        0
    )


    # ==========================================
    # Placement Status for Database
    # ==========================================

    placement_status_db = (
        1
        if st.session_state.placement_status == "Placed"
        else 0
    )


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
        st.session_state.placement_probability,
        st.session_state.recommended_career,
        st.session_state.career_score,
        st.session_state.alternative_career,

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

def history_page():

    st.title("🕒 Prediction History")

    if not st.session_state.prediction_done:

        st.warning(
            "No prediction history available."
        )

        return

    history_df = pd.DataFrame(
        {
            "Name":[
                st.session_state.student_name
            ],
            "Branch":[
                st.session_state.branch
            ],
            "Placement Probability":[
                f"{st.session_state.placement_probability}%"
            ],
            "Status":[
                st.session_state.placement_status
            ]
        }
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

    if st.button(
        "💾 Save Result To Database",
        use_container_width=True
    ):
        save_to_database()


if st.session_state.page == "Dashboard":
    dashboard_page()

elif st.session_state.page == "Assessment":
    assessment_page()

elif st.session_state.page == "Prediction":
    prediction_page()

elif st.session_state.page == "Career":
    career_page()

elif st.session_state.page == "Skills":
    skills_page()

elif st.session_state.page == "History":
    history_page()
