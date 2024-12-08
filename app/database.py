
import os
import pyodbc
from dotenv import load_dotenv
load_dotenv()
Server = os.getenv("Server")
Database = os.getenv('Database')
Trusted_Connection = os.getenv('Trusted_Connections')

def get_connection():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={Server};DATABASE={Database};Trusted_Connection={Trusted_Connection}"
        )
        print("Database connection successful!")
        return conn
    except pyodbc.Error as e:
        print(f"Database connection error: {e}")
        return None
