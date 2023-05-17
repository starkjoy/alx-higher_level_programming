-- Lists all the cities of California in database
USE `hbtn_0d_usa`;
SELECT * FROM `cities` WHERE `state_id` = (
	SELECT `id` FROM `states` WHERE `name` = "California")
ORDER BY `id` ASC
