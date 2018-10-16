
import db

def set(event_id, user_id, event_date, meny_id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "UPDATE events SET event_id=%s, user_id=%s, event_date=%s , meny_id=%s WHERE event_id=%s"
		cursor.execute(sql, (event_id, user_id, event_date, meny_id, id,))
		database.commit()
	except db.mysql.connector.Error as err:
		print(f"Error_set: {err}")
	finally:
		cursor.close()
	return

def get(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "SELECT event_id FROM events WHERE event_date=%s"
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