--  lists all genres from hbtn_0d_tvshows and displays the number of shows 
-- linked to each.
SELECT name, count(title) AS number_of_shows FROM tv_show_genres JOIN
 tv_genres JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id AND tv_genres.id=tv_show_genres.genre_id GROUP BY name ORDER BY number_of_shows DESC;
