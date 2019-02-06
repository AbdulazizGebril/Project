USE SAKILA;

DESCRIBE actor;

SELECT* FROM actor;

-- list of all the actors who have Display the first and last names of all actors from the table `actor`
SELECT first_name, last_name FROM actor;

-- Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`
SELECT concat_ws('  ',first_name, last_name)
 AS 'Actor Name'
 FROM actor;
 
 -- find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe."
 SELECT actor_id, first_name, last_name
 FROM actor
 WHERE first_name = 'JOE';
 
 -- Find all actors whose last name contain the letters `GEN`:
 SELECT* FROM actor
 WHERE last_name 
 LIKE '%GEN%';
 
 -- Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first name, in that order:
SELECT* FROM actor 
WHERE last_name 
LIKE '%LI%'
ORDER BY last_name;

-- Display the `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT* FROM country;

SELECT country_id, country 
FROM country
WHERE country IN('Afghanistan', 'Bangladesh','China');

-- Add a `middle_name` column to the table `actor`. Position it between `first_name` and `last_name`.
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(20)
AFTER first_name;

-- SELECT*FROM actor;  To See the updated table

-- Change the data type of the `middle_name` column to `blobs`.
ALTER TABLE actor
MODIFY COLUMN middle_name BLOB;

-- Delete the `middle_name` column.
ALTER TABLE actor
DROP COLUMN middle_name;

-- SELECT*FROM actor;  To See the updated table

-- List the last names of actors, as well as how many actors have that last name
SELECT last_name, COUNT(*)
FROM actor
GROUP BY last_name;

-- List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
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

-- locate the schema of the `address` table.
SHOW COLUMNS FROM sakila.address; 
SHOW CREATE TABLE sakila.address;

-- Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:
select*FROM address;
SELECT*FROM staff;

SELECT staff.first_name, staff.last_name, address,address
FROM staff
Inner JOIN address ON staff.address_id = address.address_id;

-- Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`.
SELECT*FROM payment;
SELECT staff.staff_id, first_name, last_name, SUM(amount) AS 'TOTAL AMOUNT'
FROM staff
Inner JOIN payment 
ON staff.staff_id = payment.staff_id
GROUP BY staff.staff_id;

-- List each film and the number of actors who are listed for that film. 
SELECT*FROM film;
SELECT*FROM film_actor;
SELECT title AS 'Film Name', COUNT(actor_id) AS 'Number Of Actors'
FROM film_actor
INNER JOIN film ON film.film_id = film_actor.film_id
GROUP BY title;

-- How many copies of the film `Hunchback Impossible` exist in the inventory system?
SELECT title AS 'Film Name', COUNT(inventory_id) AS 'Number Of Copies' 
FROM inventory
INNER JOIN film ON film.film_id = inventory.film_id
GROUP BY title
HAVING title = 'Hunchback Impossible'; 

-- list the total paid by each customer. List the customers alphabetically by last name:
SELECT payment.customer_id, first_name, last_name, sum(amount) AS 'Total Payment'
FROM customer
INNER JOIN payment ON customer.customer_id = payment.customer_id
GROUP BY payment.customer_id
ORDER BY last_name;  

-- display the titles of movies starting with the letters `K` and `Q` whose language is English. 
SELECT*FROM film;
SELECT*FROM language;


SELECT title FROM film
WHERE language_id IN 
(SELECT language_id 
FROM language
WHERE name = 'English')
AND (title LIKE '%K%') OR (title LIKE '%Q%'); 

-- display all actors who appear in the film `Alone Trip`.
   
SELECT*FROM film_actor;

SELECT*FROM actor;

SELECT first_name, last_name 
FROM actor 
WHERE actor_id IN
(SELECT actor_id 
FROM film_actor
WHERE film_id IN
( SELECT film_id FROM film WHERE title = 'ALONE TRIP'));

-- the names and email addresses of all Canadian customers.
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

-- Identify all movies categorized as family films.
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

-- Display the most frequently rented movies in descending order.
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


-- display how much business, in dollars, each store brought in.
SELECT*FROM store;
SELECT*FROM payment;
SELECT*FROM staff;

SELECT store.store_id , SUM(payment.amount) AS 'TOTAL REVENUE'
FROM store
INNER JOIN staff ON store.store_id = staff.store_id
INNER JOIN payment ON payment.staff_id = staff.staff_id
GROUP BY store_id; 

-- display for each store its store ID, city, and country.
SELECT store.store_id, city.city, country.country
FROM store
LEFT JOIN address ON store.address_id = address.address_id
LEFT JOIN city ON address.city_id = city.city_id
LEFT JOIN country ON city.country_id = country.country_id; 

-- List the top five genres in gross revenue in descending order.
SELECT category.name, sum(payment.amount) as 'REVENUE' FROM category 
INNER JOIN film_category ON category.category_id = film_category.category_id
INNER JOIN inventory ON film_category.film_id = inventory.film_id
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
INNER JOIN payment ON payment.rental_id = rental.rental_id
GROUP BY name
ORDER BY SUM(payment.amount) DESC
LIMIT 5;

-- easy way of viewing the Top five genres by gross revenue.

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





 





 

