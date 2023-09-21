-- create the Mysql user user_0d_1 give it all privileges
-- password sbould be set to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhosf' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVIKEGES ON *.* TO 'user_0d_1'@'localhost';
