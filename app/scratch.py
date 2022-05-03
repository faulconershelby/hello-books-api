#### CODE GRAVEYARD ####
########################
########################
########################
########book.py#########
# useful for later:
########################
# books = [
#     Book(1, "Braiding Sweetgrass", "Nonfiction; Kimmerer uses botany and ancestreal knowledge of the Citizen Potawatomi Nation to expand our relationship of Earth and Human."),
#     Book(2, "An Eternal Golden Braid", "Philosophy; An exploration of cognitive science through the relationships parallel through different disciplines."),
#     Book(3, "The Illustrated Man", "Sci-fi; A collection of short, mystical stories told through enchanted tattoos.")
#     ]
########################
#######routes.py########

# <!-- @books_bp.route("", methods = ["GET"])
# def manage_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description" : book.description
#         })
#     return jsonify(books_response), 200

# @books_bp.route("/<book_id>", methods =["GET"])
# def manage_book(book_id):
#     # try:
#     book = validate_book(book_id)
#     # except:
#     #     return {"message": f"book {book_id} invalid"}, 400
#     # for book in books:
#     #     if book.id == book_id:
#     return {
#         "id" : book.id,
#         "title" : book.title,
#         "description" : book.description,
#         }


#     # return {"message": f"book {book_id} not found"}, 404 -->

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


# @books_bp.route("/<book_id>", methods =["GET"])
# def get_book_by_id(book_id):
#     book = get_book_record_by_id(book_id)
#     return jsonify(book.to_dictionary())




## manage book GET endpoint:
# for book in books:
#     books_response.append({
#         "id" : book.id,
#         "title" : book.title,
#         "description" : book.description
#     })

# when using list indexing:
# def get_book_record_by_id(id):
#     try:
#         id = int(id)
#     except ValueError:
#         abort(make_response(jsonify(dict(details=f"Invalid ID {id}")), 400))
#         book = Book.query.get(id)
#     if book:
#         return book

## list indexing with validate book function

# for book in books:
#     if book.id == book_id:

########################
########################
#######__init__#########

########################

#########################
##### END GRAVEYARD #####