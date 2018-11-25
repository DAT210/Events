from flask import (
	Flask, g, jsonify, make_response, request, abort, Blueprint
)
import event, db

bp = Blueprint('api',__name__,url_prefix='/api/1.0')

# Blueprints:
@bp.route('/test', methods=['GET'])
def test():
	reply = {
		'status': "Success",
		'data': {
			'id': 'test_id',
			'rating': 5,
			'description': "The id test_id has a rating of 5 stars."
		}
	}

	return make_response(jsonify(reply)), 200

#Update/Modify
@bp.route('/events/', methods=['PATCH'])
def set_event_id():
	if not request.json or not 'event_id' in request.json:
		abort(400)
		event.set(event_id, publicEvent, event_date, event_name, event_description, event_facebook_link, event_image)
	return jsonify({'ok': 'success'})

@bp.route('/events/<string:event_id>/', methods=['GET'])
@bp.route('/events/<string:event_id>', methods=['GET'])
def get(event_id):
	Event = event.pullById(event_id)
	if Event is None:
		abort(400)
	return jsonify(Event)


@bp.route('/events/date/<string:event_date>/', methods=['GET'])
@bp.route('/events/date/<string:event_date>', methods=['GET'])
def getByDate(event_date):
	Event = event.getByDate(event_date)
	return jsonify(Event)
	

@bp.route('/events', methods=['GET'])
def get_events():
	Event = event.pull()
	return jsonify(Event)



@bp.route('/events', methods=['POST'])
def add_event_id():
	event.add(event_id)
	return jsonify({'ok': 'success'})

@bp.route('/events/<string:event_id>', methods=['DELETE'])
def remove_event_id(event_id):
	event.remove(event_id)
	return jsonify({'ok': 'success'})

# Error handling:
@bp.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': {
		'code': 404,
		'message': "The event_id you were trying to reach on the website couldn't be found on the database",
		'type': "Event Not Found Error."
	}}), 404)

@bp.errorhandler(400)
def none_type(error):
	return make_response(jsonify({
		'error': {
			'code': 400,
			'message': "The specified id does not exist.",
			'type': "Bad Request Error"
		}
	}))