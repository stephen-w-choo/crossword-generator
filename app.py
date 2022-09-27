from flask import Flask, render_template, request
from static.crossword.generate import generate_crossword

app = Flask(__name__)

@app.route("/")
def index():
    return generate_crossword()

