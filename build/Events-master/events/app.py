import os, click

from flask import Flask, render_template, request
import event
import json


test_config = None

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(SECRET_KEY='dev')

if test_config is None:
	app.config.from_pyfile('config.py', silent=True)
else:
	app.config.from_mapping(test_config)
try:
	os.makedirs(app.instance_path)
except OSError:
	pass

import db
db.init_app(app)

import api
app.register_blueprint(api.bp)

@app.route('/booking')
def booking():
    return render_template("eventbooking.html")

@app.route('/demo')
def bookingtest():
    return render_template("eventbooking_demo.html")

@app.route("/show-events")
def showEvents():
	events = event.getPublicEvents()
	pEvents = event.getPrivateEvents()
	return render_template("show-events.html", events=events , pEvents=pEvents)

@app.route("/show-private-events")
def showPEvents():
	events = event.getPublicEvents()
	pEvents = event.getPrivateEvents()
	return render_template("show_p_events.html", events=events , pEvents=pEvents)

@app.route("/edit-events")
def editEvents():
	publicEvents = event.getPublicEvents()
	privateEvents = event.getPrivateEvents()
	return render_template("edit-events.html", publicEvents=publicEvents, privateEvents=privateEvents)


@app.route("/edit-private-events")
def editPEvents():
	publicEvents = event.getPublicEvents()
	privateEvents = event.getPrivateEvents()
	return render_template("edit_private_events.html", publicEvents=publicEvents, privateEvents=privateEvents)



@app.route("/create-public-event", methods=["POST"])
def createPublicEvent():
	publicEvent = request.form.get("publicEvent")
	event_date = request.form.get("event_date")
	event_name = request.form.get("event_name")
	event_description = request.form.get("event_description")
	event_facebook_link = request.form.get("event_facebook_link")
	event_image = request.form.get("event_image")
	event.add(publicEvent, event_date, event_name, event_description, event_facebook_link, event_image)
	return editEvents()

@app.route("/create-private-event", methods=["POST"])
def createPrivateEvent():
	publicEvent = "No"
	event_date = request.form.get("event_date")
	event_name = request.form.get("event_name")
	event_description = request.form.get("event_description")
	event_facebook_link = request.form.get("event_facebook_link")
	event_image = request.form.get("event_image")
	event.add(publicEvent, event_date, event_name, event_description, event_facebook_link, event_image)
	return editPEvents()

@app.route("/deleteEvent/<int:event_id>")
def deleteEvent(event_id):
	event.remove(event_id)
	return editEvents()

@app.route("/updateEventInfo", methods=["POST"])
def updateEventInfo():
	event_id = request.form.get("event_id")
	publicEvent = request.form.get("publicEvent")
	event_name = request.form.get("event_name")
	event_date = request.form.get("event_date")
	event_description = request.form.get("event_description")
	event_facebook_link = request.form.get("event_facebook_image")
	event_image = request.form.get("event_image")
	event.set(event_id, publicEvent, event_date, event_name, event_description, event_facebook_link, event_image)
	return editEvents()

@app.route("/updateEventInfo", methods=["POST"])
def updatePrivateEventInfo():
	event_id = request.form.get("event_id")
	publicEvent = "No"
	event_name = request.form.get("event_name")
	event_date = request.form.get("event_date")
	event_description = request.form.get("event_description")
	event_facebook_link = request.form.get("event_facebook_image")
	event_image = request.form.get("event_image")
	event.set(event_id, publicEvent, event_date, event_name, event_description, event_facebook_link, event_image)
	return editPEvents()




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)