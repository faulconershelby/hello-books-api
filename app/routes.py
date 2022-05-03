from attr import validate
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.book import Book


# class Book:
#     def __init__(self, id, title, description):
#         self.id = id 
#         self.title = title
#         self.description = description

#     def to_dictionary(self):
#         return dict(
#                 id = self.id,
#                 title = self.title,
#                 description = self.description
#         )

# books = [
#     Book(1, "Braiding Sweetgrass", "non-fiction; Kimmerer uses botany and ancestreal knowledge "
#     "of the Citizen Potawatomi Nation to expand our relationship of Earth and Human."),
#     Book(2, "An Eternal Golden Braid", "philosophy; An exploration of cognitive science "
#     "through the relationships parallel through different disciplines."),
#     Book(3, "The Illustrated Man", "scifi; A collection of short, mystical stories "
#     "told through enchanted tattoos.")
#     ]

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

    return make_response(f"Book {new_book.title} successfully added!", 201)

@books_bp.route("", methods=["GET"])
def manage_books():
    books = Book.query.all()
    books_response = [book.to_dictionary() for book in books]
    # for book in books:
    #     books_response.append({
    #         "id" : book.id,
    #         "title" : book.title,
    #         "description" : book.description
    #     })
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

# @books_bp.route("/<book_id>", methods =["GET"])
# def get_book_by_id(book_id):
#     book = get_book_record_by_id(book_id)
#     return jsonify(book.to_dictionary())

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book_by_id(book_id):
    book = validate_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f" Book {book.title} sucessfully deleted.")

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


# def get_book_record_by_id(id):
#     try:
#         id = int(id)
#     except ValueError:
#         abort(make_response(jsonify(dict(details=f"Invalid ID {id}")), 400))
#         book = Book.query.get(id)
#     if book:
#         return book

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message": f"book {book_id} invalid"}, 400))
    
    book = Book.query.get(book_id)

    # for book in books:
    #     if book.id == book_id:
    if not book:
        abort(make_response({"message":f"book {book_id} not found"}, 404))

    return book
    