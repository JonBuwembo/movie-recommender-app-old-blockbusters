# Connects to postgres 
# Creates and manages a connection between backend and PostgreSQL database
import psycopg2
import os
from psycopg2 import RealDictCursor


# Read environment variables for database connection
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# Establish the database connection
def get_db_connection():

    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            cursor_factory=RealDictCursor
        )
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None



if __name__ == "__main__";
    connection = get_db_connection()
    print("Database connection successful!")
    connection.close()

