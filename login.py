import mysql.connector
from hashlib import sha256


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


def register_user(connection, username, password):
    try:
        cursor = connection.cursor()
        # Hash the password before storing
        hashed_password = sha256(password.encode()).hexdigest()
        # Insert username and hashed password into the users table
        cursor.execute("INSERT INTO User (UserName, UserPassword) VALUES (%s, %s)", (username, hashed_password))
        connection.commit()
        print("User registered successfully")
    except mysql.connector.Error as e:
        print("Error registering user:", e)


def login_user(connection, username, password):
    try:
        cursor = connection.cursor()
        # Execute a query to retrieve the hashed password for the given username
        cursor.execute("SELECT UserPassword FROM User WHERE UserName = %s", (username,))
        hashed_password = cursor.fetchone()
        if hashed_password:
            hashed_password = hashed_password[0]
            # Hash the input password and compare with the hashed password from the database
            if hashed_password == sha256(password.encode()).hexdigest():
                print("Login successful")
            else:
                print("Invalid password")
        else:
            print("Invalid username")
    except mysql.connector.Error as e:
        print("Error logging in:", e)


try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Benutzername für die Datenbankverbindung
        password="12345678910",  # Passwort für die Datenbankverbindung
        database="pythonLearning"  # Name der Datenbank
    )
    if connection.is_connected():
        print("Connected to MySQL database")

except mysql.connector.Error as e:
    print("Error connecting to MySQL database:", e)
    connection = None

if connection:
    # Register or login user based on user input
    action = input("Enter 'register' to register or 'login' to login: ").lower()
    if action == 'register':
        username = input("Enter username: ")
        password = input("Enter password: ")
        register_user(connection, username, password)
    elif action == 'login':
        username = input("Enter username: ")
        password = input("Enter password: ")
        login_user(connection, username, password)
    else:
        print("Invalid action")

    # Close connection
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")
