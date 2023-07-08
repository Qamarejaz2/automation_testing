import flask 
from flask import Flask, request
from flask import Flask, jsonify, request
app = Flask(__name__)

users = [
    {"id": 1, "name": "qamar"},
    {"id": 2, "name": "umaq"}
]
@app.route('/users', methods=['GET'])
def get_users():
   return jsonify(users)

app.run(port=9998, debug=True)



