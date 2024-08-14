from flask import Flask, request, jsonify
from searchrecordssearcher import get_student_details
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/api/search', methods = ['POST'])
def search():
    """
    to retrive a details from the db
    """
    search_details = request.json
    searchelement = search_details.get('searchelement')
    searchvalue = search_details.get('searchvalue')

    student_details = get_student_details(searchelement,searchvalue)

    if student_details["status"] == 'success':
        response = {"student": student_details['student']}

    else:
        response = {"student":"Details not found"}
    
    return jsonify(response)




if __name__ == "__main__":
    app.run(debug=True)


