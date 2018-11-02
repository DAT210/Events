SELECT 'INITIALIZING DATABASE...' AS '';

-- Create database if it does not exist:
CREATE DATABASE IF NOT EXISTS events_db /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

-- Use the database:
USE events_db;

-- Drop this table of it exists:
DROP TABLE IF EXISTS events;

-- Creates the events table for events:
CREATE TABLE events (
  event_id int(10) NOT NULL,
  user_id int (10) unsigned NOT NULL,
  event_date int(10) unsigned NOT NULL,
  meny_id int(10) unsigned NOT NULL,
  PRIMARY KEY (event_id),
  UNIQUE KEY event_id_UNIQUE (event_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

-- Locks and unlocks the meal user_id table:
LOCK TABLES events WRITE;
UNLOCK TABLES;

-- Insert an event of the resturant in the events table:
INSERT INTO events (event_id, user_id, event_date, meny_id) VALUES 
  (1, 1,2018-12-12, 5);

SELECT 'DATABASE INITIALIZED!' AS '';
