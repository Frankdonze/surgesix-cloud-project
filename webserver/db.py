from dotenv import load_dotenv
import mysql.connector
import os



def get_connection():
    
    load_dotenv()

    # Connect to the database
    return mysql.connector.connect(
        host = os.getenv("HOST"),
        user = os.getenv("DBUSER"),
        password = os.getenv("PASSWORD"),
        database = os.getenv("DATABASE"),    
    )

