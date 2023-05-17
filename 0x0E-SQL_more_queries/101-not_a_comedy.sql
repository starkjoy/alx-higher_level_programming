-- Lists all shows without Comedy contained in hbtn_0d_tvshows
SELECT `tv_shows`.`title` FROM `tv_shows` WHERE `tv_shows`.`id` NOT IN (
	SELECT `tv_show_genres`.`show_id` FROM `tv_show_genres`
	INNER JOIN `tv_genres` ON `tv_shows_genres`.`genre_id` = `tv_genre`.`id`
	WHERE `tv_genres`.`name` = 'Comedy')
ORDER BY `tv_shows`.`title` ASC;
