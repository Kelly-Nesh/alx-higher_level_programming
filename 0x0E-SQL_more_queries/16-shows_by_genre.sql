-- lists all shows, and all genres linked to that show, from 
-- the database hbtn_0d_tvshows.
SELECT title, name FROM tv_show_genres RIGHT OUTER JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id ORDER BY title ASC, name ASC;
