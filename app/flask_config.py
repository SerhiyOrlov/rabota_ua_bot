class FlaskConfig:
    # Flask settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///example.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery settings
    result_backend = 'redis://redis:6379/0'
    broker_url = 'redis://redis:6379/0'
