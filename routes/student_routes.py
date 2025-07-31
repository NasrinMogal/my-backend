from flask import Blueprint, request, jsonify
from models import db
from models.student import Student

student_bp = Blueprint('student_bp', __name__)

@student_bp.route("/", methods=["GET"])
def get_students():
    try:
        students = Student.query.all()
        result = [{
            "id": s.id,
            "name": s.name,
            "email": s.email,
            "course": s.course,
            "photo": s.photo
        } for s in students]
        return jsonify(result)
    except Exception as e:
        return jsonify({"message": "Failed to fetch students", "error": str(e)}), 500

@student_bp.route("/", methods=["POST"])
def add_student():
    data = request.json

    # Basic input validation
    if not data.get('name') or not data.get('email') or not data.get('course'):
        return jsonify({"message": "Missing required fields"}), 400

    new_student = Student(
        name=data['name'],
        email=data['email'],
        course=data['course'],
        photo=data.get('photo', '')
    )

    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to add student", "error": str(e)}), 500

@student_bp.route("/<int:id>", methods=["DELETE"])
def delete_student(id):
    try:
        student = Student.query.get(id)
        if not student:
            return jsonify({"message": "Student not found"}), 404

        db.session.delete(student)
        db.session.commit()
        return jsonify({"message": "Student deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to delete student", "error": str(e)}), 500





