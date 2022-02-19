from flask import Flask, request, render_template, redirect

from .queues import get_queue

app = Flask(__name__)


@app.route("/")
def index():
    message = request.args.get("message", "")
    return render_template('index.html', message=message)


@app.route("/api/add/<queue_name>/<task>", methods=['POST', 'GET'])
def api_add(queue_name=None, task=None):
    count = request.args.get("count", "1")
    for _ in range(int(count)):
        get_queue(queue_name).enqueue(f'src.tasks.{task}')

    return redirect(f"/?message=Added!")
