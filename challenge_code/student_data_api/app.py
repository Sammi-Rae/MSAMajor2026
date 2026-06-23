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
    student_dictionaries = sg.get_student_dictionaries()
    list_of_results = []
    for student_dict in student_dictionaries:
        if search_value.lower() == student_dict[search_key]:
            list_of_results.append(student_dict)
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
# Create a route that returns students of a specific class (freshman, sophomore, junior, senior)
# Create a route that returns a specific student by ID

# Run the application
app.run(debug=True)