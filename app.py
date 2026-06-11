from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"ID": 1, "Name": "Arun", "Age": 20, "College": "ABC Engineering College", "Branch": "Computer Science"},
    {"ID": 2, "Name": "Neha", "Age": 21, "College": "XYZ Institute of Technology", "Branch": "Electronics"},
    {"ID": 3, "Name": "Rahul", "Age": 19, "College": "ABC Engineering College", "Branch": "Mechanical"}
]

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["ID"] == id:
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)