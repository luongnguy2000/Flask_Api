from flask import Blueprint
from .services import *
books = Blueprint("books", __name__)

@books.route('/book-management/books', methods=['GET'])
def get_all_books():
    return get_all_books_service()

@books.route('/book-management/book/<int:id>', methods=['GET'])
def get_book_by_id(id):
    return get_book_by_id_service(id)

@books.route('/book-management/book/<string:author>', methods=['GET'])
def get_book_by_author(author):
    return get_book_by_author_service(author)

@books.route('/book-management/book', methods=['POST'])
def add_book():
    return add_book_service()

@books.route('/book-management/book/<int:id>', methods=['PUT'])
def update_book(id):
    return update_book_by_id_service(id)

@books.route('/book-management/book/<int:id>', methods=['DELETE'])
def delete_book(id):
    return delete_book_by_id_service(id)