USE master

CREATE DATABASE testDB1;

CREATE DATABASE testDB2;
use testDB1;
CREATE TABLE persons (  
     person_id int,  
     LastName varchar(255),  
     FirstName varchar(255),  
     Address int,  
     City int
);

CREATE TABLE addresses (  
     address_id int,  
     street_name varchar(255),  
     house_type int
);

CREATE TABLE city (  
     city_id int IDENTITY(1,1),  
     city_name varchar(255)
);

CREATE TABLE house_type (  
     house_type_id int,  
     label varchar(255)
);