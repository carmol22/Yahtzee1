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

if __name__ == "__main__":
    app.run(debug=True)
