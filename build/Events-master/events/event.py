import mysql.connector
import db
from flask import render_template

def set(event_id, publicEvent, event_date, event_name, event_description):
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "UPDATE events SET event_id=%s, publicEvent%s, event_date=%s , event_name=%s WHERE event_description=%s"
		cursor.execute(sql, (event_id, publicEvent, event_date, event_name, event_description,))
		database.commit()
	except db.mysql.connector.Error as err:
		print(f"Error_set: {err}")
	finally:
		cursor.close()
	return

def pull():
	database = db.get_db()
	cursor = database.cursor()
	try:
		events = []
		sql = "SELECT * FROM events"
		cursor.execute(sql)
		for(event_id, publicEvent, event_date, event_name, event_description) in cursor:
			events.append({
                "event_id" : event_id,
                "publicEvent": publicEvent,
                "event_date": event_date,
                "event_name": event_name,
                "event_description": event_description
            })
		return events
	except mysql.connector.Error as err:
		print(f"Error_get(): {err}")
	finally:
		cursor.close()
	return

def get(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "SELECT * FROM events WHERE event_id=%s"
		cursor.execute(sql, (id,))
		event_id = cursor.fetchone()
		if event_id is not None:
			(event_id,) = event_id
		return event_id
	except db.mysql.connector.Error as err:
		print(f"Error_get: {err}")
	finally:
		cursor.close()
	return

def remove(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "DELETE FROM events WHERE event_id=%s"
		cursor.execute(sql, (id,))
		database.commit()
	except db.mysql.connector.Error as err:
		print(f"Error_remove: {err}")
	finally:
		cursor.close()
	return

def add(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "INSERT INTO events (event_id, user_id, event_date, meny_id) VALUES (%s, 0, 0, 0)"
		cursor.execute(sql, (id,))
		database.commit()
	except db.mysql.connector.Error as err:
		print(f"Error_add: {err}")
	finally:
		cursor.close()
	return

def getPublicEvents():
	allEvents = pull()
	publicEvents = []
	for event2 in allEvents:
		if event2.get("publicEvent") ==  None:
			publicEvents.append(event2)
	return publicEvents

def getPrivateEvents():
	allEvents= pull()
	privateEvents = []
	for event2 in allEvents:
		if event2.get("publicEvent") != None:
			privateEvents.append(event2)
	return privateEvents

def get2(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		cursor.execute("LOCK TABLES events READ;")
		sql = "SELECT * FROM events WHERE event_id=%s;"
		cursor.execute(sql, (id,))
		result = cursor.fetchone()
		cursor.execute("UNLOCK TABLES;")
		if result is not None:
			(publicEvent, event_date, event_name, rating_2, event_description,) = result
			result = (publicEvent, event_date, event_name, rating_2, event_description)
		return result
	except mysql.connector.Error as err:
		return err
	finally:
		cursor.close()
	return


def pullById(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		events = []
		sql = "SELECT * FROM events WHERE event_id=%s;"
		cursor.execute(sql, (id,))
		for(event_id, publicEvent, event_date, event_name, event_description) in cursor:
			events.append({
				"event_id" : event_id,
				"publicEvent": publicEvent,
				"event_date": event_date,
				"event_name": event_name,
				"event_description": event_description
			})
		return events
	except mysql.connector.Error as err:
		print(f"Error_get(): {err}")
	finally:
		cursor.close()
	return

def getByDate(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		events = []
		sql = "SELECT * FROM events WHERE event_date=%s;"
		cursor.execute(sql, (id,))
		if not cursor.rowcount:
    			events.append({
					"date_busy": "False"
				})
		else:
			for(event_id, publicEvent, event_date, event_name, event_description) in cursor:
				events.append({
					"event_id" : event_id,
					"publicEvent": publicEvent,
					"event_date": event_date,
					"event_name": event_name,
					"date_busy": True,
					"event_description": event_description
				})
		return events
	except mysql.connector.Error as err:
		print(f"Error_get(): {err}")
	finally:
		cursor.close()
	return