import mysql.connector
import db
from flask import render_template
# Save event to db:
def set(event_id, publicEvent, event_date, event_name, event_description, event_facebook_link, event_image):
	database = db.get_db()
	cursor = database.cursor()
	try:
		cursor.execute("""
			UPDATE events 
			SET publicEvent=%s, event_date=%s, event_name=%s, event_description=%s, event_facebook_link=%s, event_image=%s
			WHERE event_id=%s
		""",(publicEvent, event_date, event_name, event_description, event_facebook_link, event_image, event_id))
		database.commit()
	except db.mysql.connector.Error as err:
		print(f"Error_set: {err}")
	finally:
		cursor.close()
	return
# Get event from db:
def pull():
	database = db.get_db()
	cursor = database.cursor()
	try:
		events = []
		sql = "SELECT * FROM events"
		cursor.execute(sql)
		for(event_id, publicEvent, event_date, event_name, event_description, event_facebook_link, event_image) in cursor:
			events.append({
                "event_id" : event_id,
                "publicEvent": publicEvent,
                "event_date": event_date,
                "event_name": event_name,
                "event_description": event_description,
				"event_facebook_link": event_facebook_link,
				"event_image": event_image
            })
		return events
	except mysql.connector.Error as err:
		print(f"Error_get(): {err}")
	finally:
		cursor.close()
	return

# Get event by ID from db:
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

# Remove event from db by ID:
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


# Add event to db :
def add(publicEvent, event_date, event_name, event_description, event_facebook_link, event_image):
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "INSERT INTO events (publicEvent, event_date, event_name, event_description, event_facebook_link, event_image) VALUES (%s, %s, %s, %s, %s, %s)"
		cursor.execute(sql, (publicEvent, event_date, event_name, event_description, event_facebook_link, event_image))
		database.commit()
	except db.mysql.connector.Error as err:
		print(f"Error_add: {err}")
	finally:
		cursor.close()
	return

# Get public event from db:
def getPublicEvents():
	allEvents = pull()
	publicEvents = []
	for event2 in allEvents:
		if event2.get("publicEvent") ==  None:
			publicEvents.append(event2)
	return publicEvents


# Get private event from db:
def getPrivateEvents():
	allEvents= pull()
	privateEvents = []
	for event2 in allEvents:
		if event2.get("publicEvent") != None:
			privateEvents.append(event2)
	return privateEvents

# Get private event from database using ID :
def pullById(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		events = []
		sql = "SELECT * FROM events WHERE event_id=%s;"
		cursor.execute(sql, (id,))
		for(event_id, publicEvent, event_date, event_name, event_description, event_facebook_link, event_image) in cursor:
			events.append({
                "event_id" : event_id,
                "publicEvent": publicEvent,
                "event_date": event_date,
                "event_name": event_name,
                "event_description": event_description,
				"event_facebook_link": event_facebook_link,
				"event_image": event_image
            })
		return events
	except mysql.connector.Error as err:
		print(f"Error_get(): {err}")
	finally:
		cursor.close()
	return


# Get private event from database using a DATE. If not found, show json with statue date_busy:fasle :
def getByDate(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		events = []
		sql = "SELECT * FROM events WHERE event_date=%s;"
		cursor.execute(sql, (id,))
		if  cursor is None:
			events.append({
				"date_busy": "False"
						})

			events = ["false"]
		else:
			for(event_id, publicEvent, event_date, event_name, event_description, event_facebook_link, event_image) in cursor:
				events.append({
					"event_id" : event_id,
					"publicEvent": publicEvent,
					"event_date": event_date,
					"event_name": event_name,
					"event_description": event_description,
					"event_facebook_link": event_facebook_link,
					"event_image": event_image
				})
	
		if not events:
			events.append({
		"date_busy": "False",
		"event_description": "This date is not busy"
			})	
		return events
	except mysql.connector.Error as err:
		print(f"Error_get(): {err}")
	finally:
		cursor.close()
	return