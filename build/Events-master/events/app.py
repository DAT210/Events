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

@app.route('/')
def hello():
	return app.send_static_file("index.html")


@app.route("/show-events")
def showEvents():
	events = event.getPublicEvents()
	return render_template("show-events.html", events=events)

@app.route("/edit-events")
def editEvents():
	publicEvents = event.getPublicEvents()
	privateEvents = event.getPrivateEvents()
	return render_template("edit-events.html", publicEvents=publicEvents, privateEvents=privateEvents)

@app.route("/updateEventInfo", methods=["POST"])
def updateEventInfo():
	event_id = request.form.get("event_id")
	publicEvent = request.form.get("publicEvent")
	event_name = request.form.get("event_name")
	event_date = request.form.get("event_date")
	event_description = request.form.get("event_description")
	event.set(event_id, publicEvent, event_date, event_name, event_description)
	return render_template("edit-events.html", publicEvents= event.getPublicEvents(), privateEvents=privateEvents)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)