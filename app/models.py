# models.py
from datetime import datetime as dt
from database import db


class QueryHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=dt.utcnow, nullable=False)
    vacancies_count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<QueryHistory {self.query}>'
