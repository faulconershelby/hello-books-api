from attr import validate
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.author import Author

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
