CREATE DATABASE IF NOT EXISTS event_testdb /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE event_testdb;

CREATE TABLE IF NOT EXISTS events (
  event_id int(10) NOT NULL,
  user_id int (10) NOT NULL,
  event_date int(10) unsigned NOT NULL,
  meny_id int(10) unsigned NOT NULL,
  PRIMARY KEY (event_id),
  UNIQUE KEY event_id_UNIQUE (event_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

TRUNCATE events;

INSERT INTO events (event_id, user_id, event_date, meny_id) VALUES 
  (1, 1, 2018-10-23, 5),
  (2, 1, 2018-10-10, 3),
  (3, 2, 2018-12-12, 5),
  (4, 1, 2018-09-21, 6),
  (6, 1, 2018-12-11, 2),
  (7, 1, 2018-10-11, 6),
  (8, 1, 2018-11-21, 2);
