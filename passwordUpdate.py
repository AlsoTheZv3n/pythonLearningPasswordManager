import mysql.connector

class PasswordUpdater:
    def __init__(self, connection):
        self.connection = connection

    def update_password(self, user_id, old_password, new_password):
        try:
            cursor = self.connection.cursor()
            # Execute a query to update the password for the given user ID and old password
            cursor.execute("UPDATE user SET UserPassword = %s WHERE uid = %s AND UserPassword = %s",
                           (new_password, user_id, old_password))
            self.connection.commit()
            print("Password updated successfully")
        except mysql.connector.Error as e:
            print("Error updating password:", e)
