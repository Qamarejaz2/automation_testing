import jwt
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qamarejaz'

import jwt

def requires_auth_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Get the Authorization header from the request
        auth_header = request.headers.get('Authorization')

        # Check if the Authorization header is present
        if not auth_header:
            return jsonify({'message': 'Authorization token is missing'}), 401

        # Extract the token from the Authorization header
        auth_token = auth_header.split(' ')[1] if len(auth_header.split(' ')) > 1 else None

        # Check if the token is valid
        try:
            # Verify and decode the token
            decoded_token = jwt.decode(auth_token, app.config['SECRET_KEY'], algorithms=['HS256'])
            request.jwt_data = decoded_token  # Store the decoded token data for later use
        except jwt.exceptions.InvalidTokenError:
            return jsonify({'message': 'Invalid authorization token'}), 401

        # Call the decorated function if the token is valid
        return f(*args, **kwargs)

    return decorated


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Perform authentication logic here
    # You can validate the username and password against a database or any other authentication mechanism

    # Example authentication check
    if username == 'qe2' and password == 'Hassan@4321':
        # Generate JWT token
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid username Or password'})

@app.route('/protected')
@requires_auth_token
def protected_route():
    username = request.jwt_data.get('username')
    return jsonify({'message': 'Protected route for user: {}'.format(username)})


if __name__ == '__main__':
    app.run(port=9996, debug=True)
