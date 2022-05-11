from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    books = db.relationship("Book", back_populates="author")
    # __tablename__ = "authors"

    def to_dictionary(self):
        books_info = [book.to_dictionary() for book in self.books]

        return dict(
            id = self.id,
            name = self.name,
            books = books_info)
    
    @classmethod
    def from_dict(cls, data_dict):
        return Author(name=data_dict["name"])
    
    # def replace_details(self, data_dict):
    #     self.name = data_dict["name"]