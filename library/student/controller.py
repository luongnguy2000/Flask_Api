from flask import Blueprint
from .services import *
students = Blueprint("students", __name__)

@students.route('/book-management/students',methods=['GET'])
def get_all_students():
    return get_all_students_service()

@students.route('/book-management/student/<int:id>',methods=['GET'])
def get_student_by_id(id):
    return get_student_by_id_service(id)

@students.route('/book-management/student',methods=['POST'])
def create_student():
    return add_student_service()

@students.route('/book-management/student/<int:id>',methods=['PUT'])
def update_student(id):
    return update_student_by_id_service(id)
@students.route('/book-management/student/<int:id>',methods=['DELETE'])
def delete_student(id):
    return delete_student_by_id(id)