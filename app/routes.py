from attr import validate
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.book import Book


books_bp = Blueprint("books_bp", __name__, url_prefix="/books")


@books_bp.route("", methods = ["POST"])
def handle_books():
    request_body = request.get_json()
    new_book = Book(
        title = request_body["title"],
        description = request_body["description"]
        )

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f'Book {new_book.title} successfully added'), 201)


@books_bp.route("", methods=["GET"])
def manage_books():
    # return make_response("I'm a lil teapot", 418)
    books = Book.query.all()
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()
    
    books_response = [book.to_dictionary() for book in books]

    return jsonify(books_response)


@books_bp.route("/<book_id>", methods=["GET"])
def get_book_by_id(book_id):
    book = validate_book(book_id)

    return jsonify(book.to_dictionary())



@books_bp.route("/<book_id>", methods=["PUT"])
def replace_book_by_id(book_id):
    request_body = request.get_json()
    book = validate_book(book_id)

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return jsonify(book.to_dictionary())


@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book_by_id(book_id):
    book = validate_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f" Book {book.title} sucessfully deleted."))


@books_bp.route("/<book_id>", methods = ["PATCH"])
def update_book_with_id(book_id):
    book = validate_book(book_id)
    request_body = request.get_json()
    book_keys = request_body.keys()

    if "title" in book_keys:
        book.title = request_body["title"]

    if "description" in book_keys:
        book.description = request_body["description"]
    
    db.session.commit()

    return jsonify(book.to_dictionary())


def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message": f"book {book_id} invalid"}, 400))
    
    book = Book.query.get(book_id)

    if not book:
        abort(make_response({"message":f"book {book_id} not found"}, 404))

    return book
    