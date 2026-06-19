from flask import Flask, jsonify, request
from flask_cors import CORS
from PyPDF2 import PdfReader

import os
from dotenv import load_dotenv
import google.generativeai as genai
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)

load_dotenv()

# Gemini
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# MongoDB Atlas
client = MongoClient(
    os.getenv("MONGO_URI")
)

db = client["ai_resume_analyzer"]
analysis_collection = db["analysis_history"]

resume_text_global = ""


@app.route("/")
def home():
    return "AI Resume Analyzer Backend Running!"


@app.route("/test")
def test():
    return jsonify({
        "message": "Backend Connected Successfully",
        "status": "success"
    })


@app.route("/upload", methods=["POST"])
def upload_resume():

    global resume_text_global

    if "resume" not in request.files:
        return jsonify({
            "message": "No file uploaded"
        }), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({
            "message": "No file selected"
        }), 400

    os.makedirs("uploads", exist_ok=True)

    filepath = f"uploads/{file.filename}"
    file.save(filepath)

    reader = PdfReader(filepath)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    resume_text_global = text

    return jsonify({
        "message": "Resume Read Successfully",
        "resume_text": text[:3000]
    })


@app.route("/analyze", methods=["POST"])
def analyze_resume():

    global resume_text_global

    try:

        data = request.get_json()

        job_description = data.get(
            "jobDescription",
            ""
        )

        if not resume_text_global:
            return jsonify({
                "error":
                "Please upload a resume first."
            })

        if not job_description.strip():
            return jsonify({
                "error":
                "Please enter a job description."
            })

        prompt = f"""
You are an ATS Resume Analyzer.

Compare the resume with the job description.

Resume:
{resume_text_global}

Job Description:
{job_description}

Give output in this format:

1. ATS Match Score (%)

2. Missing Skills

3. Strengths

4. Suggestions

Keep response concise and professional.
"""

        model = genai.GenerativeModel(
            "models/gemini-2.5-flash"
        )

        response = model.generate_content(
            prompt
        )

        # Save Analysis to MongoDB Atlas
        analysis_collection.insert_one({
            "job_description": job_description,
            "analysis": response.text,
            "created_at": datetime.utcnow()
        })

        return jsonify({
            "analysis": response.text
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


@app.route("/history")
def get_history():

    try:

        history = []

        records = analysis_collection.find().sort(
            "created_at",
            -1
        )

        for item in records:

            history.append({
                "job_description":
                item.get("job_description", "")[:200],

                "analysis":
                item.get("analysis", "")[:500],

                "created_at":
                str(item.get("created_at"))
            })

        return jsonify(history)

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)