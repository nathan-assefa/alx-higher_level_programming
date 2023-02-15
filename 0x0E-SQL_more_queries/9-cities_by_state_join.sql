-- Write a script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities c INNER JOIN states s ON c.state_id = s.id ORDER BY cities.id;
