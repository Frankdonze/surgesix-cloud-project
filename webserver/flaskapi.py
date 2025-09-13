from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_connection

app = Flask(__name__)

# User signup
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email, username, and password required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO Users (Username, Email, Password) VALUES (%s, %s, %s)",
            (username, email, generate_password_hash(password))
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()

    return jsonify({"message": "User created"}), 201

# User Login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = generate_password_hash(data.get("password"))

    if not username or not password:
        return jsonify({"error": "Email, username, and password required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("select * from Users where Username = %s", (username,))
    user = cursor.fetchone()

    if user:
        db_password = cursor.execute("select Password from Users where Username = (%s)", (username,))
        if db_password == password:
            return jsonify({"Success": "{username} is now logged in"}), 201
        else:
            return jsonify({"error": "Username and password dont match"}), 400

    else:
        return jsonify({"error": "Username and password dont match"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
