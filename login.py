from flask import Flask, request, jsonify
from flask_cors import CORS
from loginsearcher import authenticate_user

app = Flask(__name__)
CORS(app)



@app.route('/api/login', methods=['POST'])
def login():    
    """
    user Creadentials to login
    """
    user_details = request.json
    userid = user_details.get('userid')
    password = user_details.get('password')

    user = authenticate_user(userid, password)

    if user:
        response = {"Login Succesfull": True}
    else:
        response = {"Login Failed": False}

    return jsonify(response)

print("Login Successfull")

if __name__ == "__main__":
    app.run(debug=True)
