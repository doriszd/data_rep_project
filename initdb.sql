/*  
Data representation Big project
Doris Zdravkovic
Creating database and tables with its data in MySql
*/
 
 -- crating database hotel_guests
 create database hotel_guests;

-- using hotel_guests database
 use hotel_guests;
 


-- creating table guest
CREATE TABLE guest(
    id INT AUTO_INCREMENT PRIMARY KEY,
    guestID int,
    guest_name VARCHAR (250),
    guest_surname VARCHAR (250),
    country VARCHAR (250)

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