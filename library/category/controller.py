from flask import Blueprint
from .services import *
categories = Blueprint("categories", __name__)

@categories.route('/book-management/categories', methods=['GET'])
def get_all_cats():
    return get_all_categories_service()

@categories.route('/book-management/category/<int:id>', methods=['GET'])
def get_category_by_id(id):
    return get_cat_by_id_service(id)

@categories.route('/book-management/category', methods=['POST'])
def add_category():
    return add_cat_service()

@categories.route('/book-management/category/<int:id>', methods=['PUT'])
def update_category(id):
    return update_cat_by_id_service(id)

@categories.route('/book-management/category/<int:id>',methods = ['DELETE'])
def delete_category(id):
    return delete_cat_by_id_service(id)