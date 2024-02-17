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
        cursor.execute("INSERT INTO user (UserName, UserPassword) VALUES (%s, %s)", (username, hashed_password))
        connection.commit()
        print("User registered successfully")
    except mysql.connector.Error as e:
        print("Error registering user:", e)

def login_user(connection, username, password):
    try:
        cursor = connection.cursor()
        # Execute a query to retrieve the user ID for the given username and password
        cursor.execute("SELECT uid FROM user WHERE UserName = %s AND UserPassword = %s", (username, sha256(password.encode()).hexdigest()))
        user_id = cursor.fetchone()
        if user_id:
            print("Login successful")
            return user_id[0]  # Return the user ID
        else:
            print("Invalid username or password")
            return None
    except mysql.connector.Error as e:
        print("Error logging in:", e)
        return None

def show_passwords(connection, user_id):
    try:
        cursor = connection.cursor()
        # Execute a query to retrieve passwords for the given user ID
        cursor.execute("SELECT UserPasswords FROM passwordmanager WHERE uid = %s", (user_id,))
        passwords = cursor.fetchall()
        if passwords:
            print("Passwords for user:")
            for password in passwords:
                print(password[0])
        else:
            print("No passwords found for the user")
    except mysql.connector.Error as e:
        print("Error retrieving passwords:", e)

try:
    connection = connect_to_mysql(
        host="localhost",
        user="root",
        password="12345678910",
        database="pythonLearning"
    )
    if connection:
        # Login user
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_id = login_user(connection, username, password)
        if user_id is not None:
            # Show passwords for the logged-in user
            show_passwords(connection, user_id)
except Exception as e:
    print("An error occurred:", e)
finally:
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection closed")
