from app import db
from sqlalchemy import UniqueConstraint, PrimaryKeyConstraint


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.String(128), nullable=False)
    login = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=True)
    salary = db.Column(db.Float, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id'),
        UniqueConstraint('id'),
        UniqueConstraint('login')
    )

    def __repr__(self):
        return f'<Employee: {self.id}>'



