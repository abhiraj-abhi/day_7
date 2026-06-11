from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"ID": 1, "name": "James", "age": 20, "college": "ABC College", "branch": "Computer Science"},
    {"ID": 2, "name": "Arun", "age": 21, "college": "XYZ College", "branch": "Mechanical"},
    {"ID": 3, "name": "Priya", "age": 22, "college": "LMN College", "branch": "Electronics"}
]

@app.route('/search-student/<name>', methods=['GET'])
def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)