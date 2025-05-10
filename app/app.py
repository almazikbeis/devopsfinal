from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from ext import db
from models import Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
metrics = PrometheusMetrics(app)

with app.app_context():
    db.create_all()

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = Task(title=data["title"])
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title} for t in tasks])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
