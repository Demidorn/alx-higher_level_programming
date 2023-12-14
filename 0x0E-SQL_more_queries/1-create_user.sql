-- This script creates user with password and all privileges in Mysql server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
