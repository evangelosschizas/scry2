from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/card_search")
def card_search():
    search = request.args.get("searchbox")
    return render_template("search.html", search=search)