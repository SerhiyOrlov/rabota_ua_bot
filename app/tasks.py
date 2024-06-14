# tasks.py
from celery_app import make_celery
from celery.schedules import crontab
from app import app
from models import db, QueryHistory


from api_service import get_vacancies_amount

celery_app = make_celery(app)


@celery_app.task
def get_and_save_data(keywords):
    response = get_vacancies_amount(keywords)

    if "error" in response.keys():
        error_msg = response['error']
        return error_msg
    try:
        new_query = QueryHistory(vacancies_count=response['success'])
    except KeyError:
        return {"error": "Invalid response"}
    except Exception as e:
        return {"error": e}
    # TODO: Добавить последний результат vacancies_count в реддис чтобы определять разницу

    db.session.add(new_query)
    db.session.commit()


celery_app.conf.beat_schedule = {
    'fetch-and-store-data-every-hour': {
        'task': 'tasks.fetch_and_store_data',
        'schedule': crontab(minute=0, hour='*'),  # Каждые часы
    },
}
