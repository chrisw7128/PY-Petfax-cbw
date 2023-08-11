from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "This is our index page"

    from . import pet
    from . import facts

    app.register_blueprint(pet.bp)
    app.register_blueprint(facts.bp_facts)

    return app
