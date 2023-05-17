-- Lists all showsnot linked to 'Dexter' contained in hbtn_0d_tvshows
SELECT `tv_genres`.`name` FROM `tv_genres` WHERE `tv_genres`.`id` NOT IN (
	SELECT `tv_show_genres`.`genre_id` FROM `tv_show_genres`
	INNER JOIN `tv_shows` ON `tv_shows_genres`.`show_id` = `tv_shows`.`id`
	WHERE `tv_shows`.`title` = 'Dexter')
ORDER BY `tv_genres`.`name` ASC;
