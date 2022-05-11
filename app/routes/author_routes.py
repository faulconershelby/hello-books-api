from attr import validate
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.author import Author
from app.models.book import Book
from .routes_helper import error_message, get_record_by_id


authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

@authors_bp.route("", methods=["GET"])
def manage_authors():

    authors = Author.query.all()
    name_query = request.args.get("name")

    if name_query:
        authors = Author.query.filter_by(name=name_query)
    else:
        authors = Author.query.all()
    
    authors_response = [author.to_dictionary() for author in authors]

    return jsonify(authors_response)


@authors_bp.route("", methods = ["POST"])
def handle_authors():
    request_body = request.get_json()
    new_author = Author(
        name = request_body["name"])

    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f'Author {new_author.name} successfully added'), 201)


@authors_bp.route("/<author_id>/books", methods=["POST"])
def create_book_with_author(author_id):
    author = get_record_by_id(Author, author_id)

    request_body = request.get_json()
    new_book = Book.from_dict(request_body)
    new_book.author = author
    
    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book.to_dictionary()), 201

@authors_bp.route("/<author_id>/books", methods=["GET"])
def get_book_for_author(author_id):
    author = get_record_by_id(Author, author_id)
    books_info = [book.to_dictionary() for book in author.books]

    return jsonify(books_info)

@authors_bp.route("/<author_id>", methods=["DELETE"])
def delete_author_by_id(author_id):
    author = get_record_by_id(Author, author_id)

    db.session.delete(author)
    db.session.commit()

    return make_response(f"Author {author.name} successfully deleted.")
