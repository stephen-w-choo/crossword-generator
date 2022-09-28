from flask import Flask, render_template, request
from static.crossword.generate import generate_crossword
import os

app = Flask(__name__)

@app.route("/")
def index():




@app.route("/generate")
    return generate_crossword(
        os.path.join("static", "crossword", "data", "structure0.txt"),
        os.path.join("static", "crossword", "data", "words0.txt") 
        )

