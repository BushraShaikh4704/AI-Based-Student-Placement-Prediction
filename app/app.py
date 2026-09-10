from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from dotenv import load_dotenv

import mysql.connector
import pandas as pd
import joblib
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

def get_db_connection():

    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

@app.route("/")
def dashboard():
    session.pop("form_data", None)
    prediction_data = session.get("prediction_data")
    career_data = session.get("career_data")

    return render_template(
        "dashboard.html",
        prediction_data=prediction_data,
        career_data=career_data
    )

@app.route("/assessment")
def assessment():
    return render_template("assessment.html")

@app.route("/prediction")
def prediction_page():

    return render_template(
        "prediction.html",
        placement_status=None,
        placement_probability=None
    )

@app.route("/save_assessment", methods=["POST"])
def save_assessment():
    session["form_data"] = request.form.to_dict()
    session.pop("prediction_data", None)
    session.pop("career_data", None)
    return redirect(url_for("prediction_page"))

@app.route("/career")
def career():

    return render_template(
        "career.html",
        assessment_required=False,
        career_generated=False
    )

@app.route("/generate_career")
def generate_career():

    form_data = session.get("form_data")
    career_data = session.get("career_data")

    if not form_data:
        return render_template(
            "career.html",
            assessment_required=True,
            career_generated=False
        )

    if career_data:
        return render_template(
            "career.html",
            assessment_required=False,
            career_generated=True,
            recommended_career=career_data["recommended_career"],
            alternative_career=career_data["alternative_career"],
            career_suitability_score=career_data["career_suitability_score"],
            career_recommendations=career_data["sorted_careers"]
        )

    return redirect(url_for("prediction_page"))

@app.route("/skills")
def skills():

    return render_template(
        "skills.html",
        skill_generated=False,
        assessment_required=False
    )

@app.route("/generate_skills")
def generate_skills():

    form_data = session.get("form_data")
    prediction_data = session.get("prediction_data")

    if not form_data:

        return render_template(
            "skills.html",
            skill_generated=False,
            assessment_required=True
        )

    if prediction_data:

        return render_template(
            "skills.html",
            skill_generated=True,
            assessment_required=False,
            prediction_data=prediction_data
        )

    return redirect(url_for("prediction_page"))

@app.route("/history")
def history():

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM students
        ORDER BY student_id DESC
        LIMIT 10
    """)

    records = cursor.fetchall()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM students
    """)

    total_records = cursor.fetchone()["total"]

    cursor.execute("""
        SELECT COUNT(*) AS placed
        FROM students
        WHERE placement_status = 1
    """)

    placed_count = cursor.fetchone()["placed"]

    not_placed_count = (
        total_records - placed_count
    )

    cursor.close()
    connection.close()

    placement_rate = (
        round((placed_count / total_records) * 100, 1)
        if total_records > 0
        else 0
    )

    return render_template(
        "history.html",
        records=records,
        total_records=total_records,
        placed_count=placed_count,
        not_placed_count=not_placed_count,
        placement_rate=placement_rate
    )

@app.route("/save_history")
def save_history():

    insert_query = session.get("insert_query")
    student_record = session.get("student_record")

    if not student_record:
        flash("⚠ Result already saved.")
        return redirect(
            url_for("generate_skills") + "#save-message"
        )

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        insert_query,
        tuple(student_record)
    )

    connection.commit()

    cursor.close()
    connection.close()

    session.pop("student_record", None)

    flash("Result saved successfully!")
    return redirect(
        url_for("generate_skills") + "#save-message"
    )

@app.route("/predict", methods=["POST"])
def predict():

    preprocessor = joblib.load("models/preprocessor.pkl")
    best_model = joblib.load("models/best_model.pkl")

    form_data = session.get("form_data")
    if not form_data:
        return render_template(
            "prediction.html",
            assessment_required=True,
            placement_status=None,
            placement_probability=None
        )
    
    student_name = form_data["student_name"]
    cgpa = float(form_data["cgpa"])
    coding_skills = float(form_data["coding_skills"])
    branch = form_data["branch"]
    college_tier = form_data["college_tier"]
    backlogs = int(form_data["backlogs"])
    dsa_score = float(form_data["dsa_score"])
    aptitude_score = float(form_data["aptitude_score"]) * 10
    communication_skills = float(form_data["communication_skills"])
    ml_knowledge = float(form_data["ml_knowledge"])
    system_design = float(form_data["system_design"])
    internships = int(form_data["internships"])
    projects_count = int(form_data["projects_count"])
    certifications = int(form_data["certifications"])
    hackathons = int(form_data["hackathons"])
    open_source_contributions = int(form_data["open_source_contributions"])
    extracurriculars = int(form_data["extracurriculars"])
    database_knowledge = float(form_data.get("database_knowledge", 0))
    cloud_knowledge = float(form_data.get("cloud_knowledge", 0))

    embedded_systems = float(form_data.get("embedded_systems", 0))
    vlsi = float(form_data.get("vlsi", 0))
    electronics = float(form_data.get("electronics", 0))
    communication_systems = float(form_data.get("communication_systems", 0))

    electrical_systems = float(form_data.get("electrical_systems", 0))
    power_systems = float(form_data.get("power_systems", 0))
    control_systems = float(form_data.get("control_systems", 0))
    electrical_design = float(form_data.get("electrical_design", 0))

    cad_design = float(form_data.get("cad_design", 0))
    mechanical_design = float(form_data.get("mechanical_design", 0))
    manufacturing = float(form_data.get("manufacturing", 0))
    production = float(form_data.get("production", 0))

    structural_design = float(form_data.get("structural_design", 0))
    construction = float(form_data.get("construction", 0))
    surveying = float(form_data.get("surveying", 0))

    chemical_processes = float(form_data.get("chemical_processes", 0))
    process_design = float(form_data.get("process_design", 0))
    plant_operations = float(form_data.get("plant_operations", 0))
    quality_control = float(form_data.get("quality_control", 0))

    # ==========================================
    # Branch Skill Mapping For Placement Model
    # ==========================================

    if branch == "IT":

        ml_knowledge = database_knowledge
        system_design = cloud_knowledge

    elif branch == "ECE":

        coding_skills = embedded_systems
        dsa_score = vlsi
        ml_knowledge = electronics
        system_design = communication_systems

    elif branch == "EE":

        coding_skills = electrical_systems
        dsa_score = power_systems
        ml_knowledge = control_systems
        system_design = electrical_design

    elif branch == "ME":

        coding_skills = cad_design
        dsa_score = mechanical_design
        ml_knowledge = manufacturing
        system_design = production

    elif branch == "CE":

        coding_skills = structural_design
        dsa_score = construction
        ml_knowledge = surveying
        system_design = cad_design

    elif branch == "Chemical":

        coding_skills = chemical_processes
        dsa_score = process_design
        ml_knowledge = plant_operations
        system_design = quality_control

    technical_skill_score = (
        coding_skills +
        dsa_score +
        ml_knowledge +
        system_design
    ) / 4

    experience_score = (
        internships +
        projects_count +
        certifications +
        hackathons +
        open_source_contributions +
        extracurriculars
    )

    has_backlog = (
        1
        if backlogs > 0
        else 0
    )

    technical_skill_gap = (
        max(
            coding_skills,
            dsa_score,
            ml_knowledge,
            system_design
        )
        -
        min(
            coding_skills,
            dsa_score,
            ml_knowledge,
            system_design
        )
    )

    student_data = {
        "branch":branch,
        "college_tier":college_tier,
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
        "open_source_contributions":open_source_contributions,
        "extracurriculars": extracurriculars,
        "technical_skill_score": technical_skill_score,
        "has_backlog":has_backlog,
        "experience_score":experience_score,
        "technical_skill_gap":technical_skill_gap
    }

    student_df = pd.DataFrame([student_data])
    encoded_data = (preprocessor.transform(student_df))
    prediction = (best_model.predict(encoded_data)[0])
    probability = (best_model.predict_proba(encoded_data)[0][1] * 100)
    placement_status = ("Placed"
                    if prediction == 1
                    else "Not Placed"
        )
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

    strengths = []

    if branch in ["CSE", "IT"]:

        if coding_skills >= 7:
            strengths.append("Strong Coding Skills")

        if dsa_score >= 7:
            strengths.append("Good DSA Knowledge")

        if ml_knowledge >= 7:
            strengths.append("Excellent Technical Knowledge")

    elif branch == "ECE":

        if embedded_systems >= 7:
            strengths.append("Strong Embedded Systems Knowledge")

        if vlsi >= 7:
            strengths.append("Good VLSI Skills")

        if electronics >= 7:
            strengths.append("Excellent Electronics Fundamentals")

    elif branch == "EE":

        if electrical_systems >= 7:
            strengths.append("Strong Electrical Systems Knowledge")

        if power_systems >= 7:
            strengths.append("Good Power Systems Understanding")

        if control_systems >= 7:
            strengths.append("Strong Control Systems Skills")

    elif branch == "ME":

        if cad_design >= 7:
            strengths.append("Strong CAD Design Skills")

        if mechanical_design >= 7:
            strengths.append("Good Mechanical Design Knowledge")

        if manufacturing >= 7:
            strengths.append("Excellent Manufacturing Knowledge")

    elif branch == "CE":

        if structural_design >= 7:
            strengths.append("Strong Structural Design Skills")

        if construction >= 7:
            strengths.append("Good Construction Knowledge")

        if surveying >= 7:
            strengths.append("Strong Surveying Skills")

    elif branch == "Chemical":

        if chemical_processes >= 7:
            strengths.append("Strong Chemical Process Knowledge")

        if process_design >= 7:
            strengths.append("Good Process Design Skills")

        if quality_control >= 7:
            strengths.append("Strong Quality Control Knowledge")

    if projects_count >= 2:
        strengths.append("Good Project Experience")

    if certifications >= 2:
        strengths.append("Active in Certifications")

    if len(strengths) == 0:
        strengths.append("Keep improving your profile")

    improvements = []

    if communication_skills < 7:
        improvements.append("Communication Skills")

    if internships < 1:
        improvements.append("Internship Experience")

    if hackathons < 1:
        improvements.append("Hackathon Participation")

    if branch in ["CSE", "IT"]:

        if coding_skills < 7:
            improvements.append("Coding Skills")

        if dsa_score < 7:
            improvements.append("DSA Skills")

    elif branch == "ECE":

        if embedded_systems < 7:
            improvements.append("Embedded Systems")

        if vlsi < 7:
            improvements.append("VLSI Knowledge")

    elif branch == "EE":

        if electrical_systems < 7:
            improvements.append("Electrical Systems")

        if power_systems < 7:
            improvements.append("Power Systems")

    elif branch == "ME":

        if cad_design < 7:
            improvements.append("CAD Design")

        if manufacturing < 7:
            improvements.append("Manufacturing Knowledge")

    elif branch == "CE":

        if structural_design < 7:
            improvements.append("Structural Design")

        if construction < 7:
            improvements.append("Construction Knowledge")

    elif branch == "Chemical":

        if chemical_processes < 7:
            improvements.append("Chemical Processes")

        if process_design < 7:
            improvements.append("Process Design")

    if len(improvements) == 0:
        improvements.append("No major improvement areas detected")



# ==========================================
# Prepare Branch-Specific Database Values
# ==========================================

    database_knowledge_db = career_features.get("database_knowledge", 0)
    cloud_knowledge_db = career_features.get("cloud_knowledge", 0)
    embedded_systems_db = career_features.get("embedded_systems", 0)
    vlsi_db = career_features.get("vlsi", 0)
    electronics_db = career_features.get("electronics", 0)
    communication_systems_db = career_features.get("communication_systems", 0)
    electrical_systems_db = career_features.get("electrical_systems", 0)
    power_systems_db = career_features.get("power_systems", 0)
    control_systems_db = career_features.get("control_systems", 0)
    electrical_design_db = career_features.get("electrical_design", 0)
    cad_design_db = career_features.get("cad_design", 0)
    mechanical_design_db = career_features.get("mechanical_design", 0)
    manufacturing_db = career_features.get("manufacturing", 0)
    production_db = career_features.get("production", 0)
    structural_design_db = career_features.get("structural_design", 0)
    construction_db = career_features.get("construction", 0)
    surveying_db = career_features.get("surveying", 0)
    chemical_processes_db = career_features.get("chemical_processes", 0)
    process_design_db = career_features.get("process_design", 0)
    plant_operations_db = career_features.get("plant_operations", 0)
    quality_control_db = career_features.get("quality_control", 0)

# ==========================================
# Placement Status for Database
# ==========================================

    placement_status_db = (1
        if placement_status == "Placed"
        else 0
    )

    placement_probability = float(round(probability, 2))

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
    )"""

    session["insert_query"] = insert_query
    session["student_record"] = student_record
    star_rating = round(career_suitability_score / 2)

    session["career_data"] = {
        "recommended_career": recommended_career,
        "alternative_career": alternative_career,
        "career_suitability_score": career_suitability_score,
        "sorted_careers": sorted_careers,
        "star_rating": star_rating
    }

    session["prediction_data"] = {
        "student_name": student_name,
        "branch": branch,
        "college_tier": college_tier,
        "cgpa": cgpa,
        "backlogs": backlogs,

        "placement_status": placement_status,
        "placement_probability": placement_probability,
        "technical_skill_score": technical_skill_score,
        "experience_score": experience_score,
        "communication_skills": communication_skills,
        "aptitude_score": aptitude_score,
        "strengths": strengths,
        "improvements": improvements
    }

    print(session.get("career_data"))

    return render_template(
        "prediction.html",
        placement_status=placement_status,
        placement_probability=placement_probability,
        recommended_career=recommended_career,
        alternative_career=alternative_career,
        career_suitability_score=career_suitability_score,
        strengths=strengths,
        improvements=improvements
    )

if __name__ == "__main__":
    app.run(debug=True)