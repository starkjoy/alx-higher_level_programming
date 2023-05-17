-- Lists all shows contained in hbtn_0d_tvshows
-- displaying all genres of the show 'Dexter'
SELECT `tv_genres`.`name` FROM `tv_shows`
JOIN `tv_shows_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
JOIN `tv_genres` ON `tv_show_generes`.`genre_id` = `tv_genres`.`id`
WHERE `tv_shows`.`title` = 'Dexter'
ORDER BY `tv_genres`.`name` ASC;
