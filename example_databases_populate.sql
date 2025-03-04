-- Insert data into city table
INSERT INTO city (city_name) VALUES
('New York'),
('Los Angeles'),
('Chicago'),
('Houston'),
('San Francisco'),
('Seattle'),
('Boston'),
('Denver'),
('Miami'),
('Atlanta');

-- Insert data into house_type table
INSERT INTO house_type (house_type_id, label) VALUES
(1, 'Apartment'),
(2, 'Condo'),
(3, 'Townhouse'),
(4, 'Single-Family Home'),
(5, 'Villa'),
(6, 'Cottage'),
(7, 'Penthouse'),
(8, 'Bungalow'),
(9, 'Studio'),
(10, 'Duplex');

-- Insert data into addresses table
INSERT INTO addresses (address_id, street_name, house_type) VALUES
(1, '5th Avenue', 1),
(2, 'Sunset Boulevard', 2),
(3, 'Michigan Avenue', 3),
(4, 'Main Street', 4),
(5, 'Ocean Drive', 5),
(6, 'Broadway', 6),
(7, 'Beacon Hill', 7),
(8, 'Larimer Street', 8),
(9, 'Collins Avenue', 9),
(10, 'Peachtree Street', 10);

-- Insert data into persons table
INSERT INTO persons (person_id, LastName, FirstName, Address, City) VALUES
(1, 'Smith', 'Alice', 1, 1),
(2, 'Johnson', 'Bob', 2, 2),
(3, 'Williams', 'Charlie', 3, 3),
(4, 'Brown', 'David', 4, 4),
(5, 'Davis', 'Eve', 5, 5),
(6, 'Miller', 'Frank', 6, 6),
(7, 'Wilson', 'Grace', 7, 7),
(8, 'Moore', 'Hank', 8, 8),
(9, 'Taylor', 'Ivy', 9, 9),
(10, 'Anderson', 'Jack', 10, 10);
