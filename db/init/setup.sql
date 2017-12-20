create database whiteboard;
use whiteboard;
create table room(id int unique, name text);
create table user(id int unique, name text);
create table password(id int unique, password varchar(50));
create table drawn_info(id int unique, user_id int unique, room_id int unique, date datetime);
create table point(id int unique, x int, y int, col varchar(6));
