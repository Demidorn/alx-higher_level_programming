-- a script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, COALESCE(tv_show_genres.genre_id , 'NULL')
FROM tv_show_genres
RIGHT INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
