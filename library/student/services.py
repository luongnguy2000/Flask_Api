from library.extension import db
from library.library_ma import StudentSchema
from library.model import Book, Author,Category, Student
from flask import request, jsonify
from sqlalchemy.sql import func
import json

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

def get_all_students_service():
    stu = Student.query.all()
    if stu:
        return students_schema.jsonify(stu)
    else:
        return jsonify({"message":"Student not found"}),400
    
def get_student_by_id_service(id):
    stu = Student.query.get(id)
    if stu:
        return student_schema.jsonify(stu)
    else:
        return jsonify({"message":"Student not found"}),400
    
def add_student_service():
    data = request.json
    if data:
        name = data['name']
        birth_date = data['birth_date']
        gender = data['gender']
        class_name = data['class_name']
        try:
            new_stu = Student(name,birth_date,gender,class_name)
            db.session.add(new_stu)
            db.session.commit()
            return jsonify({"message":"Student added"}),200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message":"Student not added"}),400
    else:
        return jsonify({'message': "Request error"}),400

def update_student_by_id_service(id):
    stu = Student.query.get(id)
    data = request.json
    if stu:
        if data and 'name' in data and 'birth_date' in data and 'gender' in data and 'class_name' in data:
            try:
                stu.name = data['name']
                stu.birth_date = data['birth_date']
                stu.gender = data['gender']
                stu.class_name = data['class_name']
                db.session.commit()
                return "Student Update"
            except IndentationError:
                db.session.rollback()
                return jsonify({'message': "Can not delete student!"}),400
    else:
        return "Student not found!"
    
def delete_student_by_id(id):
    stu = Student.query.get(id)
    if stu:
        try:
            db.session.delete(stu)
            db.session.commit()
            return "Student deleted"
        except IndentationError:
            return jsonify({"message":"Can not delete student!"}),400
    else:
        return "Student not found!"