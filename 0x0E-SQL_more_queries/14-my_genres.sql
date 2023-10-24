--  lists all genres of the show Dexter
SELECT name FROM tv_show_genres JOIN tv_genres JOIN tv_shows ON tv_show_genres.genre_id=tv_genres.id AND tv_shows.id=tv_show_genres.show_id WHERE title="Dexter" ORDER BY title ASC;
