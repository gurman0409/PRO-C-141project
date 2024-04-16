from flask import Flask , jsonify , request
import csv

all_articles = []

with open ("shared_articles.csv") as f:
    reader = csv.reader()
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)
@app.route("/get-article")

def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/liked_article")

def liked_movie():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/not_liked_article")

def not_liked_movies():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()