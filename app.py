from flask import Flask
from config.db import init_db
from routes.reminder_routes import reminder_bp
import pkgutil
import os
from pathlib import Path
import yaml

# Fallback: some Python installations or shadowed modules may lack
# `pkgutil.get_loader`. Flask's package-finding uses it; provide a
# safe no-op to avoid AttributeError seen in some environments.
if not hasattr(pkgutil, 'get_loader'):
    pkgutil.get_loader = lambda name: None


def load_yaml_config():
    config_path = Path('config/settings.yaml')
    if not config_path.exists():
        return {}
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def create_app():
    app = Flask(__name__)

    file_config = load_yaml_config()
    def configured(key, default=None):
        return os.getenv(key, file_config.get(key, default))

    app.config['SECRET_KEY'] = configured('SECRET_KEY', 'clave_secreta')
    app.config['TOKEN_EXPIRATION_SECONDS'] = int(configured('TOKEN_EXPIRATION_SECONDS', 60))
    app.config['MONGODB_URI'] = configured('MONGODB_URI', 'mongodb://admin:admin@localhost:27017/dbagenda')

    init_db(app)
    app.register_blueprint(reminder_bp, url_prefix='/recordatorios')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
