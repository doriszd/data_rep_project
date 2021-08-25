/*  
Data representation Big project
Doris Zdravkovic
Creating database and tables with its data in MySql
*/
 
 -- crating database hotel_guests
 create database hotel_guests;

-- using hotel_guests database
 use hotel_guests;
 
 
 -- creating table visits in database hotel_guests
 create table visits(
    visitID int PRIMARY KEY,
    guestID int,
    number_guests int
    );


-- describing the table
desc visits;

-- inserting data into the table visits
insert into visits(visitID, guestID, number_guests) VALUES
    (1001, 2, 4),
    (1002, 6, 5),
    (1003, 9, 1);

-- selecting all data from the table visits
select * from visits;

-- creating table guest
CREATE TABLE guest(
    guestID int,
    guest_name VARCHAR (250),
    guest_surname VARCHAR (250),
    country VARCHAR (250),
    FOREIGN KEY (guestID) REFERENCES visits(guestID)
    );

-- describing guest table
desc guest;

-- inserting data into guest table
insert into guest(guestID, guest_name, guest_surname, country) VALUES
    (2, "Maria", "Smith", "UK"),
    (6, "John", "Donne", "Ireland"),
    (9, "Joe", "O'Brien", "Ireland");

-- selecting everything from guest table to see if data was properly inserted
select * from guest;