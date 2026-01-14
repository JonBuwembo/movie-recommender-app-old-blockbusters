-- tables created for movie recommendation application
-- particular database script can be run in dbeaver.
-- does not need to be in script folder

-- movies table improved.
DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    overview TEXT,
    poster_url VARCHAR(255),
    release_year INT,
    rating_avg FLOAT
);

-- genres table
drop table if exists genres;
CREATE TABLE Genres (
    genre_id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
)

-- connects both tables. no need for foreign keys in the above tables.
drop table if exists moviesgenres;
CREATE TABLE MoviesGenres (
    movie_id INT REFERENCES Movies(movie_id),
    genre_id INT REFERENCES Genres(genre_id),
    PRIMARY KEY (movie_id, genre_id)
)

