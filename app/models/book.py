from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author", back_populates="books")
    __tablename__ = "books"

    def to_string(self):
        return f"{self.id}: {self.title} Description: {self.description}"


    def to_dictionary(self):
        return dict(
                id = self.id,
                title = self.title,
                description = self.description)
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title=data_dict["title"],
            description=data_dict["description"]
        )
    
    def replace_details(self, data_dict):
        self.title = data_dict["title"]
        self.description = data_dict["description"]