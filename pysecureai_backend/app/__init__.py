from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import auth, logs, incidents, vulnerabilities
    app.register_blueprint(auth.bp)
    app.register_blueprint(logs.bp)
    app.register_blueprint(incidents.bp)
    app.register_blueprint(vulnerabilities.bp)

    return app
