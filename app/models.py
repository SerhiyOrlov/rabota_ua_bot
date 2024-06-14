# models.py
from datetime import datetime
from database import db

class QueryHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(255), nullable=False)
    parsed_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    vacancies_count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<QueryHistory {self.query}>'
