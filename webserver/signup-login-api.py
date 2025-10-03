from flask import Flask, request, jsonify
import datetime
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_connection
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET")

def create_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except:
        return None

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
            "INSERT INTO users (Username, Email, Password) VALUES (%s, %s, %s)",
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
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Email, username, and password required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("select * from users where Username = %s", (username,))
    user = cursor.fetchone()

    if user:
        cursor.execute("select Password from users where Username = (%s)", (username,))
        row = cursor.fetchone()
        db_password = row[0]


        if check_password_hash(db_password, password):
            token = create_token(user[0])
            return jsonify({"Token": token}), 201

        else:
            return jsonify({"error": "Username and password dont match"}), 400

    else:
        return jsonify({"error": "Username and password dont match"}), 400

# List Games
@app.route("/games", methods=["GET"])
def games():
    token = request.headers.get("Authorization")
    user_id = verify_token(token)
    
    print(token)
    print(user_id)

    if not user_id:
        return jsonify({"error": "You have been logged out please log back in to make picks"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select id, game from games where date = \"2025-08-09\";")
    gamelist = cursor.fetchall()
    return gamelist

#pick winners of games
@app.route("/picks", methods=["POST"])
def picks():

    token = request.headers.get("Authorization")
    user_id = verify_token(token)

    if not user_id:
        return jsonify({"error": "You have been logged out please log back in to make picks"})

    data = request.json
    print(data)
    game_id = data.get("gameID")
    pick = data.get("userpick")

    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO picks (userID, gameID, userpick) VALUES (%s, %s, %s)",
            (user_id, game_id, pick)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        conn.close()

    return jsonify({"Success": "Pick was saved. You feeling lucky?"})

#display user picks
@app.route("/userpicks", methods=["GET"])
def userpicks():

    token = request.headers.get("Authorization")
    user_id = verify_token(token)

    if not user_id:
        return jsonify({"error": "You have been logged out please log back in to make picks"})

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select game, userpick, outcome from picks join games on picks.gameID = games.id where userid = (%s)", (user_id,))
    userpicks = cursor.fetchall()
    return userpicks

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
