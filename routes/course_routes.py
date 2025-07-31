from flask import Blueprint, request, jsonify
from models import db
from models.course import Course

Course_bp = Blueprint('course_bp', __name__)

@Course_bp.route("/", methods=["POST"])
def add_course():
    data = request.json

    # Input validation
    if not data.get('student_id') or not data.get('subject') or not data.get('marks'):
        return jsonify({"message": "Missing fields"}), 400

    # Create new Course entry
    course = Course(
        student_id=data['student_id'],
        subject=data['subject'],
        marks=data['marks']
    )

    try:
        db.session.add(course)
        db.session.commit()
        return jsonify({"message": "Course added successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to add course", "error": str(e)}), 500

@Course_bp.route("/<int:student_id>", methods=["GET"])
def get_course(student_id):
    try:
        courses = Course.query.filter_by(student_id=student_id).all()
        return jsonify([{
            "subject": g.subject,
            "marks": g.marks
        } for g in courses])
    except Exception as e:
        return jsonify({"message": "Failed to retrieve courses", "error": str(e)}), 500
