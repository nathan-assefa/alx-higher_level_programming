-- a script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- USE command makes the specific database to be the default database
USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS cities
(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);
