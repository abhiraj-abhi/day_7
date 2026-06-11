from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.get_json()

    student = {
        "name": data["name"],
        "age": data["age"],
        "college": data["college"],
        "branch": data["branch"]
    }

    students.append(student)

    return jsonify({
        "message": "Student Added Successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)