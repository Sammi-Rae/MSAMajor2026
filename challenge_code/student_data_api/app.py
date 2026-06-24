import flask
from flask import request, jsonify
import student_generator_v2 as sg

# Create a flask app object
app = flask.Flask(__name__)

# Tell the server to reload each time the code changes
app.config["DEBUG"] = True
"""
Function to query the list of student dictionaries based on a search key
Input: search_key - the key in the dictionary we want to check the value of
    search_value - the value of the key we need to match
output: list of student dicstionaries that match the search criteria
"""

def search_dictionary_list(search_key, search_value):
    # Get the list of student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    list_of_results = []

    # Loop through the dictionaries
    for student_dict in student_dictionaries:
        # Determine if the search value matches the key value we are looking for
        if search_value.lower() == student_dict[search_key].lower():

            # Add the student dictionary to the results list
            list_of_results.append(student_dict)
    # Return the results list
    return list_of_results
        

# Create a route/view for the home page of the application
@app.route('/', methods = ['GET'])
def index():
    return "<h1>Student Data API</h1>"
# Create endpoints for the funcitons we will create
# Create a route to return all the student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    # Get student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)



# Create a route that returns students in a certain major
# api/majors/{major we are looking for}
@app.route('/api/majors/<string:major>', methods=['GET'])
def api_students_by_major(major:str):
    # Call the search function to get students with this major
    major_students = search_dictionary_list("major", major)
    return jsonify(major_students)
# Create a route that returns students of a specific class (freshman, sophomore, junior, senior)
# api/class/{the class we are looking for}
@app.route('/api/class/<string:student_class>', methods=['GET'])
def api_students_by_class(student_class:str):
    # Call the search function to get students from that class
    class_students = search_dictionary_list("class", student_class)
    return jsonify(class_students)
# Create a route that returns a specific student by ID
@app.route('/api/student/id/<string:id>', methods=['GET'])
def api_student_by_id(id:str):
    student = search_dictionary_list("id", id)
    print(id)
    return jsonify(student)

# Run the application
app.run(debug=True)