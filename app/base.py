from flask import Flask, request, render_template, session
from flask_bootstrap import Bootstrap
from flask_session import Session

from app.games import gensim_model, gaps_game, guesser_game
from app import settings

from time import time


def create_app():
    app = Flask(__name__, template_folder=settings.TEMPLATE_DIR)

    app.secret_key = 'super secret key'
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    Bootstrap(app)
    Session(app)
    
    return app


app = create_app()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/models")
def models():
    return render_template("models/index.html")

@app.route("/games")
def games():
    return render_template("games/index.html")

@app.route("/games/guesser", methods=['GET', 'POST'])
def guesser():
    state = session.get("guesser_state")
    if not state:
        guesser_game.new()
    else:
        guesser_game.state = state

    if request.method == 'GET':
        return render_template("games/guesser.html", context=guesser_game._state)
    elif request.method == 'POST':
        if request.form.get('Submit') == 'Submit':
            guesser_game.step(request.form.get('word'), gensim_model)
        elif request.form.get('New game') == 'New game':
            guesser_game.new()
    
        session["guesser_state"] = guesser_game.state
        return render_template("games/guesser.html", context=guesser_game._state)

@app.route("/games/gaps", methods=['GET', 'POST'])
def gaps():
    return render_template("games/gaps.html", context=gaps_game._state)

@app.route("/about")
def about():
    return render_template("about/index.html")

@app.route("/test")
def test():
    return render_template("test/index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('main/404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('main/500.html'), 500