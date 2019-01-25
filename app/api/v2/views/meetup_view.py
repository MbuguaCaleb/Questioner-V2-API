from flask import jsonify, request
from ...v2 import version_2 as v2
from ..schemas.meetup_schema import MeetupSchema
from ..models.meetup_model import Meetup

db = Meetup()


@v2.route('/meetups', methods=['POST'])
def create_meetup():
    """ Function to create a meetup """
    json_data = request.get_json()

    # No data has been provided
    if not json_data:
        return jsonify({'status': 400, 'error': 'No data provided'}), 400

    # Check if request is valid
    data, errors = MeetupSchema().load(json_data)
    if errors:
        return jsonify({'status': 400, 'error' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400

    if db.exists('topic', data['topic']):
       return jsonify({'status': 409, 'message' : 'Meetup already does exists'}), 409
 
    # Save new meetup and return response
    new_meetup = db.save(data)
    result = MeetupSchema().dump(new_meetup).data
    return jsonify({'status': 201, 'message': 'Meetup created successfully', 'data': [result]}), 201



