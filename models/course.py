from models import db
class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Course {self.name} by {self.instructor}>"
