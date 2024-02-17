import mysql.connector

def connect_to_mysql(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None

def create_user_table(connection):
    try:
        cursor = connection.cursor()
        # Create a table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                uid INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """)
        connection.commit()
        print("User table created successfully")
    except mysql.connector.Error as e:
        print("Error creating user table:", e)

def register_user(connection, username, password):
    try:
        cursor = connection.cursor()
        # Insert username and password into the user table
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        print("User registered successfully")
    except mysql.connector.Error as e:
        print("Error registering user:", e)

# Get MySQL connection details from the user
host = input("Enter the host name (e.g., localhost): ")
user = input("Enter the user name: ")
password = input("Enter the password: ")
database = input("Enter the database name: ")

# Connect to MySQL
connection = connect_to_mysql(host, user, password, database)

# Create user table if it doesn't exist
if connection:
    create_user_table(connection)

    # Get username and password from user input
    print("Register")
    print("Please enter your username and password")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Register user
    register_user(connection, username, password)

    # Close connection
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")
