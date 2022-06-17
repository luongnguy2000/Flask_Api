from library.extension import db
from library.library_ma import AuthorSchema
from library.model import Book, Author,Category
from flask import request, jsonify
from sqlalchemy.sql import func
import json

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many = True)

def get_all_authors_service():
    authors = Author.query.all()
    if authors:
        return authors_schema.jsonify(authors)
    else:
        return jsonify({"message":"Not found author!"}),404
    
def get_author_by_id_service(id):
    author = Author.query.get(id)
    if author:
        return author_schema.jsonify(author)
    else:
        return jsonify({"message":"Not found author!"}),404

def add_author_service():
    data = request.json
    if data:
        name = data['name']
        try:
            new_author = Author(name)
            db.session.add(new_author)
            db.session.commit()
            return jsonify({'message': "Add success"}),200
        except IndentationError:
            db.session.rollback()
            return jsonify({'message': "Can not add author!"}),400
    else:
        return jsonify({'message': "Request error"}),400
    
def update_author_by_id_service(id):
    author = Author.query.get(id)
    data = request.json
    if author:
        if data and 'name' in data:
            try:
                author.name = data['name']
                db.session.commit()
                return "Author Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message":"Can not delete author!"}),400
    else:
        return "Author not found!"
    
def delete_author_by_id_service(id):
    author = Author.query.get(id)
    if author:
        try:
            db.session.delete(author)
            db.session.commit()
            return "Author deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message":"Can not delete author!"}),400
    else:
        return "Author not found!"
            