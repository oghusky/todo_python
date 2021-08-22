from flask import Flask, render_template, jsonify, request, redirect
from flask_cors import CORS
from pymongo import MongoClient
import os
import datetime

app = Flask(__name__)
app.config['MONGO_CONNECT'] = False
CORS(app)
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client.pytodo


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/api", methods=["GET", "POST"])
def get_all_todos():
    if request.method == "GET":
        todos = []
        for todo in list(db.todos.find()):
            todos.append({
                "id": todo["id"],
                "text": todo["text"],
                "name": todo["name"],
            })
        return jsonify(data={"status": 200, "msg": "Found Todos", "todos": todos})
    if request.method == "POST":
        text = request.form["text"]
        name = request.form["name"]
        db.todos.insert_one({
            "id": str(datetime.datetime.now().timestamp()),
            "text": text,
            "name": name
        })
        return jsonify(data={"status": 201, "msg": "You made a todo"})


# @app.route("/api/create_todo", methods=["POST"])
# def post_create_todo():

#     redirect("/", 301)


if __name__ == "__main__":
    app.run(debug=True)
