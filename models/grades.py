from models import db

class Grade(db.Model):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    marks = db.Column(db.Integer, nullable=False)

    student = db.relationship('Student', backref='grades')

    def __repr__(self):
        return f"<Grade {self.subject}: {self.marks} for Student {self.student_id}>"
