import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Establish a connection
        connection = mysql.connector.connect(
            host='localhost',         # Replace with your MySQL server host
            user='root',     # Replace with your MySQL username
            password='xxxxxx', # Replace with your MySQL password
            database=''  # Replace with your database name (optional)
        )

        if connection.is_connected():
            print("Connected to MySQL database successfully!")
            # Fetch and print server information
            db_info = connection.get_server_info()
            print("MySQL Server version:", db_info)

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Call the function
connect_to_mysql()
