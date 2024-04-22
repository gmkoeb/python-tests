from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/postgres'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    students_instances = Student.query.all()
    students = []
    for student in students_instances:
        students.append({'firstName': student.firstname,
                        'lastName': student.lastname,
                        'email': student.email,
                        'age': student.age,
                        'bio': student.bio})
    return jsonify(students), 200