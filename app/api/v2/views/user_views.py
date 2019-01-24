from flask import jsonify, request
from ...v2 import version_2 as v2
from ..schemas.user_schema import UserSchema
from ..models.user_model import User

db = User()

@v2.route('/', methods=['GET'])
@v2.route('/welcome', methods=['GET'])
def index():
    return jsonify({'status': 200, 'message': 'Welcome !! A meetup Application:'}), 200

@v2.route('/register', methods=['POST'])
def register():
    """ Function to register new user """
    json_data = request.get_json()

    # No data has been provided
    if not json_data:
        return jsonify({'status': 400, 'message': 'No Sign up data provided'}), 400

    # Check if request is valid
    data, errors = UserSchema().load(json_data)
    if errors:
        return jsonify({'status': 400, 'message' : 'Invalid data. Please fill all the required fields', 'errors': errors}), 400


    # Save new user and get result
    new_user = db.save(data)
    result = UserSchema(exclude=['password']).dump(new_user).data

    
    return jsonify({
        'status': 201, 
        'message' : 'User created successfully', 
        'data': result, 
       
        }), 201
