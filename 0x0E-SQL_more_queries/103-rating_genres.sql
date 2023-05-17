-- List all genres from hbtn_0d_tvshows_rate by rating
SELECT `tv_genres`.`name`, SUM(`hbtn_0d_tvshows_rate`.`rating`) AS `rating_sum`
FROM `tv_genres`
JOIN `hbtn_0d_tvshows` ON `tv_genres`.`id` = `hbtn_0d_tvshows_rate`.`genre_id`
JOIN `hbtn_0d_tvshows_rate` ON `hbtn_0d_tvshows`.`id` = `hbtn_0d_tvshows_rate`.`show_id`
GROUP BY `tv_genres`.`name`
ORDER BY `rating_sum` DESC;
