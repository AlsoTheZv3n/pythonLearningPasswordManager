import mysql.connector

class PasswordCreator:
    def __init__(self, connection):
        self.connection = connection

    def create_password(self, user_id, password):
        try:
            cursor = self.connection.cursor()
            # Execute a query to insert the new password for the given user ID
            cursor.execute("INSERT INTO PasswordManager (UID, UserPasswords) VALUES (%s, %s)", (user_id, password))
            self.connection.commit()
            print("Password created successfully")
        except mysql.connector.Error as e:
            print("Error creating password:", e)
