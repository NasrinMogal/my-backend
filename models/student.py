from extensions import db
from models.course import Course  # assuming it's in models/course.py

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    photo = db.Column(db.String(200), nullable=True)

    Course = db.relationship('Course', back_populates='student', cascade="all, delete_orphan")

    def __repr__(self):
        return f"<Student {self.name}, Email: {self.email}>"
