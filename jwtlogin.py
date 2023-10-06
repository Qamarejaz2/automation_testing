import jwt
from flask import Flask, request, jsonify


app = Flask(__name__)
app.config['SECRET_KEY'] = 'qamarejaz'

@app.route('/login', methods=['POST'])

# @requires_auth_token()

def login():
    username = request.json.get('username')
    password = request.json.get('password')

    
  


    if username == 'name' and password == 'pwd':
       
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid username Or password'})

if __name__ == '__main__':
    app.run(port=9997, debug=True)
