# Data representation: Project


The aim of this project is to make a web application called hotel_guests that will
have hotel guest database which will be easy to navigate. It has a flask server that has REST API
to perform CRUD operations on an accompanying web interface. 


My project is based on retrieving data from MySql database called hotel_guests. Within this database there is a table called 
guest with some data about guest that visited hotel. 


### Contents of this repository

The repository contains: 

- gitignore: to ignore files like config files and venv to perform on virtual machine.

- readme: information about the project

- dbconfig: configuration file with my credentials to MySql database

- hotel_guestsDAO: Python DAO file to connect to the MySql database and retrieve data.

- initdb.sql: the commands used to create the database and the table in MySql

- requirements.txt: contains list of packages that should be installed in a virtual machine to run the server

- server.py: Python app server which should be run in a virtual environment

