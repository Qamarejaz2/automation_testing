from functools import wraps
from flask import request, jsonify
from flask import Flask, request, jsonify
#from jwtlogin import login

app = Flask(__name__)
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
        if not auth_token or auth_token != 'YOUR_AUTH_TOKEN':
            return jsonify({'message': 'Invalid authorization token'}), 401

        # Call the decorated function if the token is valid
        return f(*args, **kwargs)

    return decorated

@app.route('/protected')
@requires_auth_token
def protected_route():
    # Code for the protected route
    return jsonify({'message': 'Protected route'})

if __name__ == '__main__':
    app.run(port=9997, debug=True)

