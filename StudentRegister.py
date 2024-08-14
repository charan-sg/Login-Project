from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine                #one of the module in sqlalchemy that helps to create a connections between databases
from sqlalchemy.orm import sessionmaker
from studentRegistermodel import Base, Student
from datetime import datetime
import random


# create a instance of class object
app = Flask(__name__)
CORS(app)

# create a SQLAlchemy engine
engine = create_engine('sqlite:///students.db')

# create the students table if it doesn't exist
Base.metadata.create_all(engine)

# create a sessionmaker
Session = sessionmaker(bind=engine)

@app.route('/api/submitForm', methods=['POST'])
def submitForm():
    """
    Storing the Details in the database

    """
    register_number = random.randint(10000, 99999)
    form_data = request.json
    firstname = form_data.get('firstname')
    middlename = form_data.get('middlename')
    lastname = form_data.get('lastname')
    emailid = form_data.get('emailid')
    phonenumber = form_data.get('phonenumber')
    dob = form_data.get('dob')
    branch = form_data.get('branch')
    admission_date = form_data.get('admision_date')    
    bloodgroup = form_data.get('bloodgroup')
    city = form_data.get('city')
    state = form_data.get('state')
    addr1 = form_data.get('addr1')
    addr2 = form_data.get('addr2')
    zipcode = form_data.get('zipcode')
    gender = form_data.get('gender')

    # converting string date to date format
    if admission_date:
        adm_datetime = datetime.strptime(admission_date, '%Y-%m-%dT%H:%M:%S.%fZ')
        admdate_formatted = adm_datetime.date()

    if dob:
        dob_datetime = datetime.strptime(dob, '%Y-%m-%dT%H:%M:%S.%fZ')
        dob_formatted = dob_datetime.date()

    # create a session
    session = Session()

    # create a new Student instance with the form data
    try:
        student = Student(
        register_number=register_number,
        firstname=firstname,
        middlename=middlename,
        lastname=lastname,
        emailid=emailid,
        phonenumber=phonenumber,
        dob=dob_formatted,
        branch=branch,
        admission_date=admdate_formatted,
        bloodgroup=bloodgroup,
        city=city,
        state=state,
        addr1=addr1,
        addr2=addr2,
        zipcode=zipcode,
        gender=gender
    )

    # Add the student to the session
        session.add(student)

    # commit the transaction to save the data to the database
        session.commit()
        response = {"message": "Registration Successful", "Register Number is": register_number}

    except Exception as e:
        session.rollback()
        response = {"message": f"Registration Failed: {str(e)}"}
    finally:
        session.close()

    return jsonify({"status": "success", "response": response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
