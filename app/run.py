import os
from datetime import datetime
from flask import Flask, send_file
from models import QueryHistory
from database import init_db


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
    today = datetime.utcnow().strftime('%d-%m-%Y')
    path = f"{today}.xlsx"
    print(os.getcwd())
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
