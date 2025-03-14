import mysql.connector

def connect_db():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="tracker_user",
            password="4612552aA",
            database="expense_tracker"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None
