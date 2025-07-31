from flask import Blueprint, request, jsonify
from models import db
from backend.models.user_auth_model import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import models.user_auth_model
print(dir(models.user_auth_model))


auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "User already exists"}), 409

    hashed_pw = generate_password_hash(data['password'])
    new_user = User(username=data['username'], password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify({"token": access_token})
    return jsonify({"message": "Invalid credentials"}), 401




    