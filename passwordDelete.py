import mysql.connector
from hashlib import sha256

class PasswordDeleter:
    def __init__(self, connection):
        self.connection = connection

    def delete_password(self, user_id, password):
        try:
            cursor = self.connection.cursor()
            # Hash the password before deleting
            hashed_password = sha256(password.encode()).hexdigest()
            # Execute a query to delete the password for the given user ID and hashed password
            cursor.execute("DELETE FROM PasswordManager WHERE UID = %s AND UserPasswords = %s", (user_id, hashed_password))
            self.connection.commit()
            print("Password deleted successfully")
        except mysql.connector.Error as e:
            print("Error deleting password:", e)
