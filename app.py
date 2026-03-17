from flask import Flask
from config.db import init_db
from routes.reminder_routes import reminder_bp
import pkgutil

# Fallback: some Python installations or shadowed modules may lack
# `pkgutil.get_loader`. Flask's package-finding uses it; provide a
# safe no-op to avoid AttributeError seen in some environments.
if not hasattr(pkgutil, 'get_loader'):
    pkgutil.get_loader = lambda name: None


def create_app():
    app = Flask(__name__)
    # Optional: load settings from environment or .env if desired
    init_db(app)
    app.register_blueprint(reminder_bp, url_prefix='/recordatorios')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
