from ntpath import join
from library.extension import db
from library.library_ma import BookSchema, BorrowSchema
from library.model import *
from flask import request, jsonify
from sqlalchemy import func
import json 

borrows_schema = BorrowSchema(many=True)

def get_borrow_author_cat_service(student_name):
    borrows = db.session.query(Borrow.id, Book.name, Category.name, Author.name).join(Student, Borrow.student_id == Student.id).join(Book, Borrow.book_id == Book.id).join(
        Category, Book.category_id == Category.id).join(Author, Book.author_id == Author.id).filter(func.lower(Student.name) == student_name.lower()).all()
    if borrows:
        return jsonify({f'{student_name} borrowed': borrows}),200
    else:
        return jsonify({'message':'Not found borrow'}),400
    
def get_borrows_service():
    borrows = Borrow.query.all()
    if borrows:   
        return borrows_schema.jsonify(borrows)
    else:
        return jsonify({"message":"Not found books!"}),404
    
    
def add_borrow_author_cat_service():
    data = request.json
    if data:
        book_id = data['book_id']
        student_id = data['student_id']
        borrow_date = data['borrow_date']
        return_date = data['return_date']
        try:
            new_bor = Borrow(book_id,student_id,borrow_date,return_date)
            db.session.add(new_bor)
            db.session.commit()
            return jsonify({"message":"Borrow session added"}),200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message":"Borrow session not added"}),400
    else:
        return jsonify({'message': "Request error"}),400