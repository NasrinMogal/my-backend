from flask import Blueprint, request, jsonify
from models import db
from models.attendance import Attendance

attendance_bp = Blueprint('attendance_bp', __name__)

@attendance_bp.route("/", methods=["POST"])
def mark_attendance():
    data = request.json
    if not all(k in data for k in ("student_id", "date", "status")):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        new_record = Attendance(
            student_id=data['student_id'],
            date=data['date'],
            status=data['status']
        )
        db.session.add(new_record)
        db.session.commit()
        return jsonify({"message": "Attendance recorded"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@attendance_bp.route("/<int:student_id>", methods=["GET"])
def get_attendance(student_id):
    records = Attendance.query.filter_by(student_id=student_id).all()
    return jsonify({
        "student_id": student_id,
        "records": [{
            "id": r.id,
            "date": r.date.strftime("%Y-%m-%d"),
            "status": r.status
        } for r in records]
    })
