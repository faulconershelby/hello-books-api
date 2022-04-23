from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id 
        self.title = title
        self.description = description

books = [
    Book(1, "Braiding Sweetgrass", "non-fiction; Kimmerer uses botany and ancestreal knowledge "
    "of the Citizen Potawatomi Nation to expand our relationship of Earth and Human."),
    Book(2, "An Eternal Golden Braid", "philosophy; An exploration of cognitive science "
    "through the relationships parallel through different disciplines."),
    Book(3, "The Illustrated Man", "scifi; A collection of short, mystical stories "
    "told through enchanted tattoos.")
    ]


books_bp = Blueprint("books", __name__, url_prefix="/books")


@books_bp.route("", methods = ["GET"])
def manage_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description" : book.description
        })
    return jsonify(books_response), 200

@books_bp.route("/<book_id>", methods =["GET"])
def manage_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            return {
                "id" : book.id,
                "title" : book.title,
                "description" : book.description,
            }
