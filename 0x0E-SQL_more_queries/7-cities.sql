-- Creates a database 'hbtn_0d_usa' and table 'cities' on SQL server
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `htbn_0d_usa`.`cities` (
	`id` INT AUTO_INCREMENT NOT NULL,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`state_id`) REFERENCES `hbtn_0d_usa`.`states`(`id`));
