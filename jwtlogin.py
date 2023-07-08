import jwt
from flask import Flask, request, jsonify
#from validtoken import requires_auth_token

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qamarejaz'

@app.route('/login', methods=['POST'])

# @requires_auth_token()

def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Perform authentication logic here
    # You can validate the username and password against a database or any other authentication mechanism

    # Example authentication check
    if username == 'qe2' and password == 'Pichu@1234':
        # Generate JWT token
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid username Or password'})

if __name__ == '__main__':
    app.run(port=9997, debug=True)
