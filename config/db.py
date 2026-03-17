import os
from mongoengine import connect


def init_db(app=None):
    # MONGODB_URI can venir de app.config, de variable de entorno o por defecto local
    uri = None
    if app is not None:
        uri = app.config.get('MONGODB_URI')
    if not uri:
        uri = os.environ.get('MONGODB_URI') or 'mongodb://admin:admin@localhost:27017/dbagenda'
    # connect() will use the alias 'default' for global access
    connect(host=uri, alias='default')
