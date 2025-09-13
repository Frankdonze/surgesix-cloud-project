
import mysql.connector

def get_connection():
    # Connect to the database
    return mysql.connector.connect(
        host="20.0.0.31",       # or IP of your DB server
        user="app.user",    # DB username
        password="Frankie0119#!",# DB password
        database="surgedb"    # DB name you created
    )

