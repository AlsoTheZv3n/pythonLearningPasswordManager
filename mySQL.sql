import mysql.connector

-- User
-- UID
-- UserName
-- UserPassword
-- forgeinkey to passwordmanager id
-- auto increment

-- Create User table
CREATE TABLE IF NOT EXISTS User (
    UID INT AUTO_INCREMENT PRIMARY KEY,
    UserName VARCHAR(255) NOT NULL,
    UserPassword VARCHAR(255) NOT NULL
);



-- PasswordManager
-- Pid
-- forkein uid
-- userpasswords

-- Create PasswordManager table
CREATE TABLE IF NOT EXISTS PasswordManager (
    Pid INT AUTO_INCREMENT PRIMARY KEY,
    UID INT,
    UserPasswords VARCHAR(255) NOT NULL,
    FOREIGN KEY (UID) REFERENCES User(UID)
);