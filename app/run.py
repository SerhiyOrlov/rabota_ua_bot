# run.py
from flask import Flask
from .database import init_db
from .models import db, QueryHistory
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['result_backend'] = 'redis://redis:6379/0'
app.config['broker_url'] = 'redis://redis:6379/0'

init_db(app)


@app.route('/heartbeat')
def heartbeat():
    return {'success': 'OK'}


@app.route('/get_today_statistic')
def get_today_statistic():
    pass


if __name__ == '__main__':
    app.run(debug=True)
