from flask import Blueprint
from .services import *
authors = Blueprint("authors", __name__)

@authors.route('/book-management/authors', methods=['GET'])
def get_all_authors():
    return get_all_authors_service()

@authors.route('/book-management/author/<int:id>', methods=['GET'])
def get_author_by_id(id):
    return get_author_by_id_service(id)

@authors.route('/book-management/author/', methods=['POST'])
def add_author():
    return add_author_service()

@authors.route('/book-management/author/<int:id>', methods=['PUT'])
def update_author_by_id(id):
    return update_author_by_id_service(id)

@authors.route('/book-management/author/<int:id>', methods=['DELETE'])
def delete_author_by_id(id):
    return  delete_author_by_id_service(id)