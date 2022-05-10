from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    books = db.relationship("Book", back_populates="author")

    def to_dictionary(self):
        return dict(
            id = self.id,
            name = self.name)
    
    @classmethod
    def from_dict(cls, data_dict):
        return Author(name=data_dict["name"])