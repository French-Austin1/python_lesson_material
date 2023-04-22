from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

# A dictionary to store our data, 5 users : This would be a database in a real world application
DICTIONARY_OF_DATA = {
    1: {
        "name": "John",
        "age": 25,
        "occupation": "Software Engineer"
    },
    2: {
        "name": "Jane",
        "age": 30,
        "occupation": "Data Scientist"
    },
    3: {
        "name": "Bob",
        "age": 20,
        "occupation": "Student"
    },
    4: {
        "name": "Mary",
        "age": 35,
        "occupation": "Teacher"
    },
    5: {
        "name": "Steve",
        "age": 40,
        "occupation": "Manager"
    }
}

@app.route('/get-data')
def get_data():
    '''Returns all the data in the dictionary as JSON'''
    return jsonify(DICTIONARY_OF_DATA)

@app.route('/get-data/<int:user_id>')
def get_data_by_id(user_id):
    '''Returns the data of a specific user as JSON'''
    if user_id in DICTIONARY_OF_DATA:
        return jsonify(DICTIONARY_OF_DATA[user_id])
    else:
        return make_response(jsonify({"error": "User not found"}), 404)
    
@app.route('/add-data', methods=['POST'])
def add_data():
    '''Adds data to the dictionary'''
    if not request.json:
        return make_response(jsonify({"error": "No data provided"}), 400)
    else:
        user_id = request.json['id']
        name = request.json['name']
        age = request.json['age']
        occupation = request.json['occupation']
        
        if user_id in DICTIONARY_OF_DATA:
            return make_response(jsonify({"error": "User already exists"}), 400)
        else:
            DICTIONARY_OF_DATA[user_id] = {
                "name": name,
                "age": age,
                "occupation": occupation
            }
            return make_response(jsonify({"message": "User added successfully"}), 201)
        

if __name__ == '__main__':
    app.run(debug=True)
