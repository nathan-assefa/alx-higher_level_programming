-- a script that lists all shows contained in hbtn_0d_tvshows
-- +that does not have genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_show_genres.show_id IS NULL OR tv_shows.title IS NULL ORDER BY tv_shows.title, tv_show_genres.genre_id;
