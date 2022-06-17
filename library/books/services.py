from library.extension import db
from library.library_ma import BookSchema
from library.model import Book, Author,Category
from flask import request, jsonify
from sqlalchemy.sql import func
import json
book_schema = BookSchema()
books_schema = BookSchema(many=True)


def get_all_books_service():
    books = Book.query.all()
    if books:
        return books_schema.jsonify(books)
    else:
        return jsonify({"message":"Not found books!"}),404
    
def get_book_by_id_service(id):
    book = Book.query.get(id)
    if book:
        return book_schema.jsonify(book)
    else:
        return jsonify({"message":"Not found book!"}),404

def get_book_by_author_service(author):
    books = Author.query.join(Author).filter(func.lower(Author.name)== author.lower()).all()
    if books:
        return books_schema.jsonify(books)
    else:
        return jsonify({"message": f"Not found book {author}"}),404
    
def add_book_service():
    data = request.json
    if (data and ('name'in data) and ('page_count' in data) and ('author_id' in data) and ('category_id' in data)):
        name = data['name']
        page_count = data['page_count']
        author_id = data['author_id']
        category_id = data['category_id']
        try:
            new_book = Book(name, page_count, author_id, category_id)
            db.session.add(new_book)
            db.session.commit()
            return jsonify({'message': "Add success"}),200
        except IndentationError:
            db.session.rollback()
            return jsonify({'message': "Can not add book!"}),400
    else:
        return jsonify({'message': "Request error"}),400
    
def update_book_by_id_service(id):
    book = Book.objects.get(id)
    data = request.json
    if book:
        if data and 'page_count' in data:
            try:
                book.page_count = data['page_count']
                db.session.commit()
                return "Book Update"
            except IndentationError:
                db.session.rollback()
                return jsonify({'message': "Can not delete book!"}),400
    else:
        return "Book not found!"

def delete_book_by_id_service(id):
    book = Book.objects.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return "Book deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message":"Can not delete book!"}),400
    else:
        return "Book not found!"
    
    