# app.py
from flask import Flask, request, jsonify
from utils import optimize_resume
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.get_json()
    resume = data.get("resume", "")
    job_description = data.get("job_description", "")

    if not resume or not job_description:
        return jsonify({"error": "Missing resume or job description"}), 400

    try:
        optimized = optimize_resume(resume, job_description)
        return jsonify({"optimized_resume": optimized})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
