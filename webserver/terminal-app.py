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

def make_picks():
    response = requests.get(f"{BASE_URL}/games")
    gamelist = response.json()
    print("GAME ID  |  GAME TITLE\n")
    for game in gamelist:
        print(game[0], " |  ", game[1])

    for pick in 6:
        gameid = input("Game ID for the Game you would like to select: ")
        teampicked = input("Pick the team that you think will win this game: ")
        #store picks in database table need to create new table picks for this will need to releate tp table users

    

    #print("Games: ", response.json())
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
        make_picks()
    elif choice == "4":
        view_picks()
    elif choice == "5":
        break
    else:
        print("Invalid option, try again.")
