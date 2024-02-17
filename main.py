import mysql.connector

from login import login_user
from passwordCreate import PasswordCreator
from passwordDelete import PasswordDeleter
from passwordManager import connect_to_mysql, show_passwords
from passwordUpdate import PasswordUpdater
from register import register_user



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

            # Options to create, update, or delete password
            action = input("Enter 'create' to create a password, 'update' to update a password, or 'delete' to delete a password: ").lower()
            if action == 'create':
                new_password = input("Enter the new password: ")
                creator = PasswordCreator(connection)
                creator.create_password(user_id, new_password)
            elif action == 'update':
                old_password = input("Enter the old password: ")
                new_password = input("Enter the new password: ")
                updater = PasswordUpdater(connection)
                updater.update_password(user_id, old_password, new_password)
            elif action == 'delete':
                password_to_delete = input("Enter the password to delete: ")
                deleter = PasswordDeleter(connection)
                deleter.delete_password(user_id, password_to_delete)
            else:
                print("Invalid action")
except Exception as e:
    print("An error occurred:", e)
finally:
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection closed")
