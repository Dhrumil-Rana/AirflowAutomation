Begin transaction;

create schema if not exists airflow;
create table airflow.players (
    player name varchar(255) primart key,
    team varchar(100),
    position varchar(20),
    birthdate date,
    shirt_name varchar(100),
    clib varchar(225),
    height int,
    weight int
)

create table airflow.movies (
    movie_id int primary key,
    title varchar(255),
    genre varchar(100)
)

create table airflow.ratings (
    userID int,
    movieId int,
    rating float,
    time datetime
)

commit;
End transaction;