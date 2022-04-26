from flask import Blueprint, jsonify, abort, make_response

class Book:
    def __init__(self, id, title, description):
        self.id = id 
        self.title = title
        self.description = description

    def to_dictionary(self):
        return dict(
                id = self.id,
                title = self.title,
                description = self.description
        )

books = [
    Book(1, "Braiding Sweetgrass", "non-fiction; Kimmerer uses botany and ancestreal knowledge "
    "of the Citizen Potawatomi Nation to expand our relationship of Earth and Human."),
    Book(2, "An Eternal Golden Braid", "philosophy; An exploration of cognitive science "
    "through the relationships parallel through different disciplines."),
    Book(3, "The Illustrated Man", "scifi; A collection of short, mystical stories "
    "told through enchanted tattoos.")
    ]


books_bp = Blueprint("books", __name__, url_prefix="/books")


@books_bp.route("", methods = ("GET",))
def manage_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description" : book.description
        })
    return jsonify(books_response), 200


@books_bp.route("/<book_id>", methods =("GET",))
def manage_book(book_id):
    book = validate_book(book_id)
    return book.to_dictionary()


def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message": f"book {book_id} invalid"}, 400))

    for book in books:
        if book.id == book_id:
            return book
    abort(make_response({"message":f"book {book_id} not found"}, 404))
    