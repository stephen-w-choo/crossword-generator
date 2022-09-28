from flask import Flask, render_template, request
from static.crossword.generate import generate_crossword
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/generate", methods=["GET", "POST"])
def crossword():
    if request.method == "POST":
        data = request.json
        # Get the data from the form
        difficulty = data["difficulty"]
        # Generate the crossword
        # Return the crossword
        # return render_template("test.html", response = {
        #     "difficulty": difficulty,
        #     "request": request,
        #     "path": os.path.join("static", "crossword", "data", f"{difficulty}.txt"),
        #     "function": generate_crossword(
        #     os.path.join("static", "crossword", "data", f"{difficulty}.txt"),
        #     os.path.join("static", "crossword", "data", "words2.txt") 
        #     )
        # })
        return generate_crossword(
           os.path.join("static", "crossword", "data", f"{difficulty}.txt"),
           os.path.join("static", "crossword", "data", "words2.txt") 
           )

