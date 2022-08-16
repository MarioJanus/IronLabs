use applestore;
select distinct prime_genre from applestore;

select distinct prime_genre, max(rating_count_tot) from `applestore`;

SELECT prime_genre, count(prime_genre) FROM `apple`.`applestore` 
GROUP by prime_genre
order by count(prime_genre) desc
limit 1;

SELECT prime_genre, count(prime_genre) FROM `applestore` 
GROUP by prime_genre
order by count(prime_genre) asc
limit 1;

select distinct track_name, rating_count_tot, prime_genre from `applestore`
GROUP by track_name
order by rating_count_tot desc
limit 10;

select distinct track_name, user_rating, prime_genre from `applestore`
GROUP by track_name
order by user_rating desc
limit 10;

select track_name, user_rating, rating_count_tot from applestore 
GROUP by track_name
order by user_rating desc, rating_count_tot desc
limit 3;


select track_name, price, user_rating, rating_count_tot from applestore 
GROUP by track_name
order by rating_count_tot, price
limit 10;

select track_name, price, user_rating, rating_count_tot from applestore 
GROUP by track_name
order by rating_count_tot desc, price desc
limit 10;
