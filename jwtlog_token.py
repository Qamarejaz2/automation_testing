import jwt
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qamarejaz'

import jwt

def requires_auth_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
       
        auth_header = request.headers.get('Authorization')

       
        if not auth_header:
            return jsonify({'message': 'Authorization token is missing'}), 401

    
        auth_token = auth_header.split(' ')[1] if len(auth_header.split(' ')) > 1 else None

        
        try:
            
            decoded_token = jwt.decode(auth_token, app.config['SECRET_KEY'], algorithms=['HS256'])
            request.jwt_data = decoded_token  # Store the decoded token data for later use
        except jwt.exceptions.InvalidTokenError:
            return jsonify({'message': 'Invalid authorization token'}), 401

     
        return f(*args, **kwargs)

    return decorated


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

   
    if username == 'name' and password == 'pwd':
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
