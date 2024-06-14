# run.py
from flask import Flask
from .database import init_db
from .models import db, QueryHistory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['result_backend'] = 'redis://redis:6379/0'
app.config['broker_url'] = 'redis://redis:6379/0'

init_db(app)

if __name__ == '__main__':
    app.run(debug=True)
