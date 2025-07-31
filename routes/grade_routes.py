from flask import Blueprint, request, jsonify
from models import db
from models.grades import Grade

grade_bp = Blueprint('grade_bp', __name__)

@grade_bp.route("/", methods=["POST"])
def add_grade():
    data = request.json

    # Input validation
    if not data.get('student_id') or not data.get('subject') or not data.get('marks'):
        return jsonify({"message": "Missing fields"}), 400

    grade = Grade(
        student_id=data['student_id'],
        subject=data['subject'],
        marks=data['marks']
    )

    try:
        db.session.add(grade)
        db.session.commit()
        return jsonify({"message": "Grade added successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to add grade", "error": str(e)}), 500

@grade_bp.route("/<int:student_id>", methods=["GET"])
def get_grades(student_id):
    try:
        grades = Grade.query.filter_by(student_id=student_id).all()
        return jsonify([{
            "subject": g.subject,
            "marks": g.marks
        } for g in grades])
    except Exception as e:
        return jsonify({"message": "Failed to retrieve grades", "error": str(e)}), 500
