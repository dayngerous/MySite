CREATE TABLE songs (
  song_id SERIAL PRIMARY KEY,
  song_title VARCHAR NOT NULL,
  artist VARCHAR NOT NULL,
  description VARCHAR,
  producer VARCHAR,
  mix_eng VARCHAR,
  year INTEGER NOT NULL
);

INSERT INTO songs
  (song_title, artist, description, producer, mix_eng, year)
  VALUES ('SYD', 'Dayngerous', 'A song featuring Darnique', 'HotBoyDre', 'Dayngerous', 2017);

INSERT INTO songs
  (song_title, artist, description, mix_eng, year)
  VALUES ('Narcos', 'Xkusive', 'Dancehll song by Xklusive', 'Dayngerous', 2020);

SELECT * FROM songs;

SELECT song_title, artist FROM songs;

SELECT * FROM songs WHERE id = 1;

SELECT * FROM songs WHERE artist = 'Dayngerous';

could use boolean ops and conditionals

SELECT AVG(year) FROM songs WHERE artist = 'Dayngerous';

SELECT COUNT(*) FROM songs;

min

SELECT * FROM songs WHERE artist LIKE '%ay%s';

UPDATE songs
  SET year = 2021
  WHERE artist='Dayngerous'
  AND title='SYD';

DELETE FROM songs
  WHERE ______

SELECT * FROM songs ORDER BY year ASC LIMIT 2;
DESC

adminer.cs50.net

count for each
SELECT artist, COUNT(*) FROM songs GROUP BY artist;


SELECT artist, COUNT(*) FROM songs GROUP BY artist HAVING COUNT(*) > 1;

CREATE TABLE
column DATATYPE REFERENcES other table

SELECT songs othrt pother JOIN songs other ON table.column = table.column;

could do an INNER JOIN by default
LEFT JOIN all from LEFT
RIGHT JOIN

CREATE INDEX indexname column;

unsafe
SELECT * FROM users
  WHERE (username = username)
  AND (password = password)

transactions counter race conduditions
BEGIN
COMMIT
