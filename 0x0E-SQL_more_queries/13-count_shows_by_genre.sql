-- Lists all shows contained in hbtn_0d_tvshows
-- displaying shows linked to each genre
SELECT `tv_shows_genres`.`genre` AS `genre`, COUNT(*)
AS `number_of_shows` FROM `tv_show_genres` GROUP BY `genre`
HAVING `number_of_shows` > 0 ORDER BY `number_of_shows` DESC;
