-- Creates a database 'hbtn_0d_2' and the user 'user_0d_2'
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
-- th
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- l
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- k
FLUSH PRIVILEGES;
