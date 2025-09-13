import requests

BASE_URL = "http://127.0.0.1:5000"

def signup():
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    response = requests.post(
        f"{BASE_URL}/signup",
        json={"username": username, "email": email, "password": password}
    )
    print("Signup response:", response.json())

def login():
    username = input("Enter your usernmae ")
    password = input("Enter your password: ")

    response = requests.post(
        f"{BASE_URL}/login",
        json={"username": username, "password": password}
    )
    print("Login response:", response.json())

def make_pick():
    user_id = input("Enter your user_id: ")
    game_id = input("Enter the game_id: ")
    winner = input("Enter your predicted winner: ")

    response = requests.post(
        f"{BASE_URL}/picks",
        json={"user_id": user_id, "game_id": game_id, "winner": winner}
    )
    print("Pick response:", response.json())

def view_picks():
    user_id = input("Enter your user_id: ")

    response = requests.get(f"{BASE_URL}/picks", params={"user_id": user_id})
    print("Your picks:", response.json())

# Simple terminal menu
while True:
    print("\nMenu:")
    print("1. Signup")
    print("2. Login")
    print("3. Make a Pick")
    print("4. View Picks")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        make_pick()
    elif choice == "4":
        view_picks()
    elif choice == "5":
        break
    else:
        print("Invalid option, try again.")
