from flask import Flask, request, Blueprint
from .books.controller import books
from .borrow.controller import borrow
from .author.controller import authors
from .category.controller import categories
from .student.controller import students
from .extension import db, ma
from .model import Student, Book, Author, Category, Borrow
import os


def create_db(app):
    if not os.path.exists("library/library.db"):
        db.create_all(app=app)
        print("Created DB!")


def create_app(config_file="config.py"):
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    app.config.from_pyfile(config_file)
    create_db(app)
    app.register_blueprint(books)
    app.register_blueprint(borrow)
    app.register_blueprint(authors)
    app.register_blueprint(categories)
    app.register_blueprint(students)
    return app