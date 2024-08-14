from studentRegistermodel import Student
from fetchstudentdb import Session



def get_student_details(searchelement,searchvalue):
    """
    To fetch the details based on the searched element and searched value
    
    """
    session = Session()
    try:
        if searchelement and searchvalue:
            search_filter = {searchelement: searchvalue}
            student = session.query(Student).filter_by(**search_filter).first()

            if student:
                student_data = {
                    "register_number": student.register_number,
                    "firstname": student.firstname,
                    "middlename": student.middlename,
                    "lastname": student.lastname,
                    "emailid": student.emailid,
                    "phonenumber": student.phonenumber,
                    "dob": student.dob,
                    "branch": student.branch,
                    "admission_date": student.admission_date,
                    "bloodgroup": student.bloodgroup,
                    "city": student.city,
                    "state": student.state,
                    "addr1": student.addr1,
                    "addr2": student.addr2,
                    "zipcode": student.zipcode,
                    "gender": student.gender
                }
                response = {"status": "success", "student": student_data}
            else:
                response = {"status": "error", "message": "Student not found"}

        else:
            response = {"status": "error", "message": "Invalid search criteria"}

    except Exception as e:
        response = {"status": "error", "message": str(e)}
    finally:
        session.close()
    
        return response