-- lists all records in secod_table table
-- only score and name will be displayed
-- rocords whose score is below 10 will not be displayed
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
