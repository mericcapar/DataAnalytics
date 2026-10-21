/*
a) actor_id, first_name, last_name and last_update
b) film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features and last_update. It stores details about each film.
c) The film_actor table contains both actor_id and film_id. It connects actors to the films they appeared in.
d) The rental table includes rental_id, rental_date, inventory_id, customer_id, return_date, staff_id and last_update. It is hard to read because most of the columns are ID numbers, so you can't see film or customer names without looking at other tables.
e) The inventory table includes inventory_id, film_id, store_id and last_update. It shows which film copies are in which store. It is also hard to read.
f) I need the rental, inventory and film tables. The rental table has the rental_date and inventory_id. The inventory table connects inventory_id to film_id. The film table connects film_id to the film title. So rental links to inventory through inventory_id, and inventory links to film through film_id.
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;