USE dims;

CREATE TABLE primary_location (
	id INT NOT NULL AUTO_INCREMENT,
    primary_location VARCHAR(255),
    PRIMARY KEY (id)
);

-- THE TABLE WILL BE EMPTY, BUT SHOWS THE COLUMNS CREATED
SELECT * FROM primary_location;