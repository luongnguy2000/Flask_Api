from library.extension import db
from library.library_ma import CatSchema
from library.model import Book, Author,Category
from flask import request, jsonify
from sqlalchemy.sql import func
import json

category_schema = CatSchema()
categories_schema = CatSchema(many=True)

def get_all_categories_service():
    cats = Category.query.all()
    if cats:
        return categories_schema.jsonify(cats)
    else:
        return jsonify({"message":"Not found cat!"}),404
    
def get_cat_by_id_service(id):
    cat = Category.query.get(id)
    if cat:
        return category_schema.jsonify(cat)
    else:
        return jsonify({"message":"Not found cat!"}),404

def add_cat_service():
    data = request.json
    if data:
        name = data['name']
        try:
            new_cat = Category(name)
            db.session.add(new_cat)
            db.session.commit()
            return jsonify({'message': "Add success"}),200
        except IndentationError:
            db.session.rollback()
            return jsonify({'message': "Can not add cat!"}),400
    else:
        return jsonify({'message': "Request error"}),400
    
def update_cat_by_id_service(id):
    cat = Category.query.get(id)
    data = request.json
    if cat:
        if data and 'name' in data:
            try:
                cat.name = data['name']
                db.session.commit()
                return "Category Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message":"Can not delete category!"}),400
    else:
        return "Author not found!"
    
def delete_cat_by_id_service(id):
    cat = Category.query.get(id)
    if cat:
        try:
            db.session.delete(cat)
            db.session.commit()
            return "Caterogy deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message":"Can not delete cat!"}),400
    else:
        return "Category not found!"
            