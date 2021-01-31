"""
Config for Apache Superset.
"""

import os

from celery.schedules import crontab


user = os.environ["DB_USERNAME"]
password = os.environ["DB_PASSWORD"]
hostname = os.environ["DB_SERVER"]
port = os.environ["DB_PORT"]
database = os.environ["DB_DATABASE"]

SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{user}:{password}@{hostname}:{port}/{database}?charset=utf8"

SECRET_KEY = os.environ["SECRET_KEY"]

# Expose certain dashboards without signing in
PUBLIC_ROLE_LIKE = "Gamma"

MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY", "")

# Caching setup
CACHE_CONFIG = {
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 60 * 60 * 24, # 1 day default (in secs)
}

DATA_CACHE_CONFIG = {
    **CACHE_CONFIG,
}

CELERYBEAT_SCHEDULE = {
    "cache-warmup-hourly": {
        "task": "cache-warmup",
        "schedule": crontab(minute=0, hour="*"),  # hourly
        "kwargs": {
            "strategy_name": "top_n_dashboards",
            "top_n": 5,
            "since": "7 days ago",
        },
    },
}
