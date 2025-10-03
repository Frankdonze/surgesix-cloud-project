import requests

BASE_URL = "http://127.0.0.1:5000"
token = None

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
    global token
    token = response.json()["Token"]
    print("Login response:", response.json())

def make_picks():
    headers = { "Authorization": f"{token}" }
    response = requests.get(f"{BASE_URL}/games", headers=headers)
    gamelist = response.json()

    print("Request Headers:", response.request.headers)  # what you sent
    print("Response Headers:", response.headers) 
    
    if response.status_code != 200:
        print(gamelist)
    
    else:
        print("GAME ID  |  GAME TITLE\n")
    
        for game in gamelist:
            print(game[0], " |  ", game[1])

        for pick in range(6):
            gameid = input("Game ID for the Game you would like to select: ")
            teampicked = input("Pick the team that you think will win this game: ")

            print(repr(gameid))
            print(repr(teampicked))

            response = requests.post(
                f"{BASE_URL}/picks",
                json={"gameID": gameid, "userpick": teampicked},
                headers=headers
            )      

            print("pick Response:", response.json())

    

    #print("Games: ", response.json())
def view_picks():
    headers= { "Authorization": f"{token}" }
    response = requests.get(f"{BASE_URL}/userpicks", headers=headers)
    userpicks = response.json()

    if response.status_code != 200:
        print(userpicks)

    else:
        print(f"{'GAME TITLE':<35}  | {'YOUR PICK':<20}   | {'OUTCOME':<10}\n")

        for pick in userpicks:
            print(f"{pick[0]:<35}  |  {pick[1]:<20}  |  {str(pick[2]):<10}")
        
        #print("Success:", response.json())

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
