USE SAKILA;

DESCRIBE actor;

SELECT* FROM actor;

-- 1a
SELECT first_name, last_name FROM actor;

-- 1b
SELECT concat_ws('  ',first_name, last_name)
 AS 'Actor Name'
 FROM actor;
 
 -- 2a
 SELECT actor_id, first_name, last_name
 FROM actor
 WHERE first_name = 'JOE';
 
 -- 2b
 SELECT* FROM actor
 WHERE last_name 
 LIKE '%GEN%';
 
 -- 2c
SELECT* FROM actor 
WHERE last_name 
LIKE '%LI%'
ORDER BY last_name;

-- 2d
SELECT* FROM country;

SELECT country_id, country 
FROM country
WHERE country IN('Afghanistan', 'Bangladesh','China');

-- 3a
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(20)
AFTER first_name;

-- SELECT*FROM actor;  To See the updated table

-- 3b 
ALTER TABLE actor
MODIFY COLUMN middle_name BLOB;

-- 3c
ALTER TABLE actor
DROP COLUMN middle_name;

-- SELECT*FROM actor;  To See the updated table

-- 4a 
SELECT last_name, COUNT(*)
FROM actor
GROUP BY last_name;

-- 4b
SELECT last_name, COUNT(*)
FROM actor
GROUP BY last_name
HAVING COUNT(*) > 1;

-- 4c
UPDATE ACTOR
SET first_name= 'HARPO'
WHERE first_name= 'GROUCHO' AND last_name='WILLIAMS';

-- 4d
SELECT first_name , actor_id 
FROM actor 
WHERE first_name = 'HARPO';

UPDATE actor
SET first_name =
   CASE

       WHEN first_name='HARPO' 
       THEN 'GROUCHO'
       ELSE 'MUCHO GROUCHO'
   END
   
WHERE actor_id= 172;

-- 5a 
SHOW COLUMNS FROM sakila.address; 
SHOW CREATE TABLE sakila.address;

-- 6a
select*FROM address;
SELECT*FROM staff;

SELECT staff.first_name, staff.last_name, address,address
FROM staff
Inner JOIN address ON staff.address_id = address.address_id;

-- 6b
SELECT*FROM payment;
SELECT staff.staff_id, first_name, last_name, SUM(amount) AS 'TOTAL AMOUNT'
FROM staff
Inner JOIN payment 
ON staff.staff_id = payment.staff_id
GROUP BY staff.staff_id;

-- 6c
SELECT*FROM film;
SELECT*FROM film_actor;
SELECT title AS 'Film Name', COUNT(actor_id) AS 'Number Of Actors'
FROM film_actor
INNER JOIN film ON film.film_id = film_actor.film_id
GROUP BY title;

-- 6d
SELECT title AS 'Film Name', COUNT(inventory_id) AS 'Number Of Copies' 
FROM inventory
INNER JOIN film ON film.film_id = inventory.film_id
GROUP BY title
HAVING title = 'Hunchback Impossible'; 

-- 6e
SELECT payment.customer_id, first_name, last_name, sum(amount) AS 'Total Payment'
FROM customer
INNER JOIN payment ON customer.customer_id = payment.customer_id
GROUP BY payment.customer_id
ORDER BY last_name;  

-- 7a 
SELECT*FROM film;
SELECT*FROM language;


SELECT title FROM film
WHERE language_id IN 
(SELECT language_id 
FROM language
WHERE name = 'English')
AND (title LIKE '%K%') OR (title LIKE '%Q%'); 

-- 7b
SELECT*FROM film_actor;

SELECT*FROM actor;

SELECT first_name, last_name 
FROM actor 
WHERE actor_id IN
(SELECT actor_id 
FROM film_actor
WHERE film_id IN
( SELECT film_id FROM film WHERE title = 'ALONE TRIP'));

-- 7c
SELECT*FROM customer;
SELECT*FROM country;
SELECT*FROM address;
SELECT*FROM city;

SELECT customer.first_name, customer.last_name, customer.email, country.country
FROM customer
INNER JOIN address ON customer.address_id = address.address_id
INNER JOIN city ON address.city_id = city.city_id
INNER JOIN country ON city.country_id = country.country_id
WHERE country = 'Canada';  

-- 7d 
SELECT*FROM film;
SELECT*FROM category;
SELECT*FROM film_category;

SELECT title AS 'FAMILY MOVIES' 
FROM film 
WHERE film_id IN
(SELECT film_id FROM film_category
WHERE category_id IN
(SELECT category_id from category
WHERE name = 'family'));

-- 7e
SELECT*FROM inventory;
SELECT*FROM rental;


SELECT title AS 'FILM NAME', COUNT(rental.rental_id) AS ' RENTAL COUNT'
FROM film 
INNER JOIN inventory ON 
film.film_id = inventory.film_id
INNER JOIN rental on 
rental.inventory_id = inventory.inventory_id
GROUP BY title
ORDER BY COUNT('RENTAL COUNT') DESC; 


-- 7f
SELECT*FROM store;
SELECT*FROM payment;
SELECT*FROM staff;

SELECT store.store_id , SUM(payment.amount) AS 'TOTAL REVENUE'
FROM store
INNER JOIN staff ON store.store_id = staff.store_id
INNER JOIN payment ON payment.staff_id = staff.staff_id
GROUP BY store_id; 

-- 7g
SELECT store.store_id, city.city, country.country
FROM store
LEFT JOIN address ON store.address_id = address.address_id
LEFT JOIN city ON address.city_id = city.city_id
LEFT JOIN country ON city.country_id = country.country_id; 

-- 7h
SELECT category.name, sum(payment.amount) as 'REVENUE' FROM category 
INNER JOIN film_category ON category.category_id = film_category.category_id
INNER JOIN inventory ON film_category.film_id = inventory.film_id
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
INNER JOIN payment ON payment.rental_id = rental.rental_id
GROUP BY name
ORDER BY SUM(payment.amount) DESC
LIMIT 5;

-- 8a

CREATE VIEW top_five_genre AS 
SELECT category.name, sum(payment.amount) as 'REVENUE' FROM category 
JOIN film_category 
ON category.category_id = film_category.category_id
JOIN inventory 
ON film_category.film_id = inventory.film_id
JOIN rental 
ON rental.inventory_id = inventory.inventory_id
JOIN payment 
ON payment.rental_id = rental.rental_id
GROUP BY name
ORDER BY SUM(payment.amount) DESC
LIMIT 5;


-- 8b
SELECT * FROM top_five_genre;

-- 8c
DROP VIEW top_five_genre;





 





 

