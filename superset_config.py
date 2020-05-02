import os


user = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']
hostname = os.environ['DB_SERVER']
port = os.environ['DB_PORT']
database = os.environ['DB_DATABASE']

SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{user}:{password}@{hostname}:{port}/{database}?charset=utf8'

PUBLIC_ROLE_LIKE_GAMMA = True
SECRET_KEY = os.environ['SECRET_KEY']

MAPBOX_API_KEY = os.environ['MAPBOX_API_KEY']
