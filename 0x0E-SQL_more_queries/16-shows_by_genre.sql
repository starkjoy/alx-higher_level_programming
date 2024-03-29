-- Lists all shows and all their genres contained in hbtn_0d_tvshows
SELECT `tv_shows`.`title`, `tv_genres`.`name` FROM `tv_shows`
LEFT JOIN `tv_shows_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
JOIN `tv_genres` ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
ORDER BY `tv_shows`.`title` ASC, `tv_genres`.`name` ASC;
