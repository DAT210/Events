SELECT 'INITIALIZING DATABASE...' AS '';


-- Create database if it does not exist:
CREATE DATABASE IF NOT EXISTS events_db /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;

-- Use the database:
USE events_db;

CREATE USER 'root'@'%' IDENTIFIED BY 'root';
grant all privileges on *.* to 'root'@'%' with grant option;


-- Drop this table of it exists:
DROP TABLE IF EXISTS events;

-- Creates the events table for events:

CREATE TABLE events (
  event_id MEDIUMINT NOT NULL AUTO_INCREMENT,
  publicEvent CHAR(10) DEFAULT NULL,
  event_date date NOT NULL,
  event_name VARCHAR(35) NOT NULL,
  event_description TEXT,
  event_facebook_link CHAR(254),
  event_image CHAR(50),
  PRIMARY KEY (event_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- Locks and unlocks the meal user_id table:
LOCK TABLES events WRITE;
UNLOCK TABLES;

-- Insert an event of the resturant in the events table:
INSERT into events(publicEvent, event_date, event_name, event_description, event_facebook_link, event_image)
VALUES(NULL,"2018-11-15","Taco-Night", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales neque quis nisi facilisis lobortis. Namefficitur eget nisi sit amet bibendum. Vestibulum elementum faucibus quam ut posuere. Vivamus pellentesque
        luctus nunc at bibendum. Mauris viverra ultrices nisi, sit amet imperdiet lectus accumsan eu. Morbi ornare diam
        nulla, nec aliquet nisl accumsan dictum. Mauris sit amet tellus in ipsum commodo hendrerit. Nunc at mollis
        magna. Proin felis nibh, venenatis non lobortis quis, ullamcorper nec dolor. Vivamus tempus volutpat fringilla.
        Praesent volutpat sit amet massa nec ultricies. Curabitur sollicitudin pharetra tortor in dictum. In mattis orci
        vel augue vehicula rutrum. Nullam vitae sollicitudin orci.", "https://www.facebook.com/events/239880163310493/", "mexican.png");

INSERT into events(publicEvent, event_date, event_name, event_description, event_facebook_link, event_image)
VALUES(NULL,"2018-12-18", "X-mas Feast", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales neque quis nisi facilisis lobortis. Namefficitur eget nisi sit amet bibendum. Vestibulum elementum faucibus quam ut posuere. Vivamus pellentesque
        luctus nunc at bibendum. Mauris viverra ultrices nisi, sit amet imperdiet lectus accumsan eu. Morbi ornare diam
        nulla, nec aliquet nisl accumsan dictum. Mauris sit amet tellus in ipsum commodo hendrerit. Nunc at mollis
        magna. Proin felis nibh, venenatis non lobortis quis, ullamcorper nec dolor. Vivamus tempus volutpat fringilla.
        Praesent volutpat sit amet massa nec ultricies. Curabitur sollicitudin pharetra tortor in dictum. In mattis orci
        vel augue vehicula rutrum. Nullam vitae sollicitudin orci.", "https://www.facebook.com/events/239880163310493/", "x_mas.jpg");

INSERT into events(publicEvent, event_date, event_name, event_description, event_facebook_link, event_image)
VALUES(NULL, "2019-3-18", "Easter Disaster", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales neque quis nisi facilisis lobortis. Namefficitur eget nisi sit amet bibendum. Vestibulum elementum faucibus quam ut posuere. Vivamus pellentesque
        luctus nunc at bibendum. Mauris viverra ultrices nisi, sit amet imperdiet lectus accumsan eu. Morbi ornare diam
        nulla, nec aliquet nisl accumsan dictum. Mauris sit amet tellus in ipsum commodo hendrerit. Nunc at mollis
        magna. Proin felis nibh, venenatis non lobortis quis, ullamcorper nec dolor. Vivamus tempus volutpat fringilla.
        Praesent volutpat sit amet massa nec ultricies. Curabitur sollicitudin pharetra tortor in dictum. In mattis orci
        vel augue vehicula rutrum. Nullam vitae sollicitudin orci.", "https://www.facebook.com/events/239880163310493/", "easter.jpg");

INSERT into events(publicEvent, event_date, event_name,event_image)
VALUES("","2019-2-18", "Gjerts Bursdag","birthday.png");


INSERT into events(publicEvent, event_date, event_name,event_image)
VALUES("","2019-3-18", "Evry Team building","Business_meeting.png");

INSERT into events(publicEvent, event_date, event_name,event_image)
VALUES("","2019-1-8", "Frida og Fredds frieri","wedding.jpg");
        
INSERT into events(publicEvent, event_date, event_name, event_description, event_facebook_link, event_image)
VALUES(NULL, "2019-2-28", "Extra day Party", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales neque quis nisi facilisis lobortis. Namefficitur eget nisi sit amet bibendum. Vestibulum elementum faucibus quam ut posuere. Vivamus pellentesque
        luctus nunc at bibendum. Mauris viverra ultrices nisi, sit amet imperdiet lectus accumsan eu. Morbi ornare diam
        nulla, nec aliquet nisl accumsan dictum. Mauris sit amet tellus in ipsum commodo hendrerit. Nunc at mollis
        magna. Proin felis nibh, venenatis non lobortis quis, ullamcorper nec dolor. Vivamus tempus volutpat fringilla.
        Praesent volutpat sit amet massa nec ultricies. Curabitur sollicitudin pharetra tortor in dictum. In mattis orci
        vel augue vehicula rutrum. Nullam vitae sollicitudin orci.", "https://www.facebook.com/events/239880163310493/", "29_February.jpg");

SELECT 'DATABASE INITIALIZED!' AS '';