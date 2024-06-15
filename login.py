from flask import Flask, request, jsonify
from flask_cors import CORS
from fetchlogindb import Session
from loginsearcher import authenticate_user

app = Flask(__name__)
CORS(app)

@app.route('/api/login', methods=['POST'])
def login():
    """
    User credentials to login
    """
    user_details = request.json
    userid = user_details.get('userid')
    password = user_details.get('password')

    user = authenticate_user(userid, password)

    if user:
        response = {"Login Successful": True}
    else:
        response = {"Login Failed": False}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
