mysql > create database whiteboard;  
mysql > use whiteboard;  
mysql > create table room(id int unique, name text, password varchar(60));  
mysql > create table user(id int unique, name text, username text, password varchar(60)); 
mysql > create table drawn_info(id int unique, user_id int unique, room_id int unique, date datetime);  
mysql> create table point(id int unique, x int, y int, col varchar(6));  

