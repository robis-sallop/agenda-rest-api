import os
from mongoengine import connect


def init_db(app=None):
    # MONGODB_URI can be provided via environment variable or defaults to local
    uri = os.environ.get('MONGODB_URI') or 'mongodb://admin:admin@localhost:27017/dbagenda'
    # connect() will use the alias 'default' for global access
    connect(host=uri, alias='default')
