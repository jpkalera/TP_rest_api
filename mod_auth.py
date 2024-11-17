from flask import jsonify
from flask_jwt_extended import create_access_token

def authenticate(request):
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")

    if username == "admin" and password == "password":
        access_token = create_access_token(identity={"username": username})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
