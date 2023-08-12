from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:2023!@localhost:5434/petfax"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from . import models

    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route("/")
    def index():
        return "This is our index page"

    from . import pet
    from . import facts

    app.register_blueprint(pet.bp)
    app.register_blueprint(facts.bp_facts)

    return app
