"""
Main module for the Yahtzee game.
"""

from flask import Flask, render_template
from src.hand import Hand

app = Flask(__name__)


@app.route("/")
def main():
    """
    Renders the main page of the Yahtzee game.
    """
    hand = Hand()
    return render_template("index.html", hand=hand)


@app.route("/about")
def about():
    """
    Renders the about page of the Yahtzee game.
    """
    return render_template("about.html")


@app.errorhandler(400)
def bad_request():
    """
    400 Bad Request error page.
    """
    return render_template("400.html"), 400


@app.errorhandler(500)
def internal_server_error():
    """
    500 Internal Server Error page.
    """
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
