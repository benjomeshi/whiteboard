create database whiteboard;
use whiteboard;
create table room(id int AUTO_INCREMENT NOT NULL PRIMARY KEY unique, name text NOT NULL);
create table user(id int AUTO_INCREMENT NOT NULL PRIMARY KEY unique, name text);
create table password(id int AUTO_INCREMENT NOT NULL PRIMARY KEY unique, password varchar(50));
create table drawn_info(id int AUTO_INCREMENT NOT NULL PRIMARY KEY unique, user_id int, room_id int, date datetime);
create table point(id int unique AUTO_INCREMENT NOT NULL PRIMARY KEY, x int, y int, col varchar(6));
