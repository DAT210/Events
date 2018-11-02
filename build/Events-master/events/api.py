from flask import (
	Flask, g, jsonify, make_response, request, abort, Blueprint
)
import event, db

bp = Blueprint('api',__name__,url_prefix='/api/1.0')

@bp.route('/test', methods=['GET'])
def test():
	dbb = db.get_db()
	print(f"TEST: {dbb}")
	return jsonify({'test': "Success!"})

#Update/Modify
@bp.route('/events/', methods=['PATCH'])
def set_event_id():
	if not request.json or not 'event_id' in request.json:
		abort(400)
	event.set(event_id, user_id, event_date, meny_id)
	return jsonify({'ok': 'success'})


@bp.route('/events/<string:event_id>', methods=['GET'])
def get_event_id(event_id):
	Event = event.get(event_id)
	if Event is None:
		abort(400)
	x = {
		'event id': event_id,
		'user id': Event,
		'description': f"ID: {event_id} has the event {Event}"
	}
	return jsonify(x)
	

@bp.route('/events', methods=['GET'])
def get_events():
   return jsonify({'events': 'N/A'})



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