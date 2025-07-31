
import os
from dotenv import load_dotenv
from flask import Flask ,jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from config import Config
from extensions import db
from routes.student_routes import student_bp
from routes.course_routes import course_bp
from routes.auth_routes import auth_bp
from routes.attendance_routes import attendance_bp
from routes.grade_routes import grade_bp

load_dotenv()

def create_app():
    app= Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)
    CORS(app)

    app.register_blueprint(student_bp, url_prefix="/api/students")
    app.register_blueprint(course_bp, url_prefix="/api/courses")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(attendance_bp, url_prefix="/api/attendance")
    app.register_blueprint(grade_bp, url_prefix="/api/grades")

    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to Student Management System API!"}) 

    with app.app_context():
     from models.user_auth_model import User
     db.create_all()

    return app



