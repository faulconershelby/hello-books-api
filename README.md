# Hello Books API

# code graveyard #

<!-- @books_bp.route("", methods = ["GET"])
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
    # try:
    book = validate_book(book_id)
    # except:
    #     return {"message": f"book {book_id} invalid"}, 400
    # for book in books:
    #     if book.id == book_id:
    return {
        "id" : book.id,
        "title" : book.title,
        "description" : book.description,
        }


    # return {"message": f"book {book_id} not found"}, 404 -->

##     end      ##