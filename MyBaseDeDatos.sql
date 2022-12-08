/*
	Creamos la base de datos
*/
drop database EDA_BD;
create database if not exists EDA_BD;
use EDA_BD;

/*
	Visualizamos las tablas creadas desde las funciones
*/

select * from datos LIMIT 10;

select * from datos;
select * from casting;
select * from generos;

select count(type_of) as num from datos;
select count(actor) as num from casting;
select count(genero) as num from generos;

select * from datos
where title = 'BELLATOR MMA: Davis vs. Nemkov'; # Máxima duración = 19


/*
	QUERY: Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: 
		   get_max_duration(año, plataforma, [min o season]) -> 13
*/

# the house that jack built
select * from datos;

SELECT title, time_of
FROM datos
WHERE time_of = (SELECT MAX(time_of) FROM datos WHERE release_year = 2018 and plataf = 'Hulu') and min_season = 'min' and release_year = 2018 and plataf = 'Hulu';

SELECT title, time_of FROM datos WHERE time_of = (SELECT MAX(time_of) FROM datos WHERE release_year = 2018 and plataf = 'Hulu') and min_season = 'min' and release_year = 2018 and plataf = 'Hulu';

/*
	QUERY: Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)
*/
select count(plataf)  from datos where plataf = 'Amazon' and min_season = 'min'; # Cantidad de películas Amazon = 7814

select count(plataf)  from datos
where plataf = 'Amazon' and min_season = 'season'; # Cantidad de películas Amazon = 1854

/*
	QUERY: Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')
		   Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.
*/
select * from generos;

select genero, count(genero) as Cant_veces, plataforma from generos where Plataforma = 'Amazon' and genero = 'Comedy' group by genero order by Cant_veces desc;

select genero, count(genero) as Cant_veces
from generos
where Plataforma = 'Amazon' and genero = 'Documentaries'
group by genero
order by Cant_veces desc; # -> 2099

select genero, count(genero) as Cant_veces
from generos
where Plataforma = 'Netflix' and genero = 'Documentaries'
group by genero
order by Cant_veces desc; # -> 0

select genero, count(genero) as Cant_veces
from generos
where Plataforma = 'Hulu' and genero = 'Comedy'
group by genero
order by Cant_veces desc; # -> 667

/*
	QUERY: Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)
*/
select actor, anio, count(actor) as Cant_veces
from casting
where actor <> 'Unknown' and plataforma = 'Amazon' and Anio = 2009
group by actor
order by Cant_veces desc; # Actor que más se repite según plataforma y año = Gary Oldman, 3

select actor, anio, count(actor) as Cant_veces from casting where actor <> 'Unknown' and plataforma = 'Amazon' and Anio = 2009 group by actor order by Cant_veces desc;


