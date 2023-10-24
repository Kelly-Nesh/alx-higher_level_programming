-- list only comedy shows
USE hbtn_0d_tvshows;
SELECT title FROM tv_show_genres JOIN tv_shows JOIN tv_genres ON tv_show_genres.show_id=tv_shows.id AND tv_show_genres.genre_id=tv_genres.id WHERE name="Comedy" ORDER BY title ASC;
