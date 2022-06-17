from flask import Blueprint
from .services import *

borrow = Blueprint('borrow', __name__)

@borrow.route('/borrow-management/borrow/<string:student_name>',methods = ['GET'])
def get_borrow_author_cat(student_name):
    return get_borrow_author_cat_service(student_name)

@borrow.route('/borrow-management/borrows',methods = ['GET'])
def get_all_borrows():
    return get_borrows_service()
@borrow.route('/borrow-management/borrow', methods = ['POST'])
def create_borrow():
    return add_borrow_author_cat_service()