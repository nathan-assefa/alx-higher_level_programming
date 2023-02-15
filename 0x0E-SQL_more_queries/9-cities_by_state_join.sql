-- Write a script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, state.name, states.name FROM cities LEFT JOIN states ON cities.state.id = states.id ORDER BY cities.id;
