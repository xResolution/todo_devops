from flask import jsonify, request, abort, render_template

from .models import Task

tasks = []
task_id_counter = 1

def register_routes(app):
    global task_id_counter

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/tasks', methods=['POST'])
    def add_task():
        global task_id_counter
        if not request.json or 'description' not in request.json:
            abort(400)
        task = Task(
            id=task_id_counter,
            description=request.json['description'],
            completed=False
        )
        tasks.append(task)
        task_id_counter += 1
        return jsonify(task.to_dict()), 201

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        return jsonify([task.to_dict() for task in tasks])

    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        task = next((t for t in tasks if t.id == task_id), None)
        if task is None:
            abort(404)
        if not request.json:
            abort(400)
        if 'completed' in request.json:
            task.completed = request.json['completed']
        if 'description' in request.json:
            task.description = request.json['description']
        return jsonify(task.to_dict())

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        global tasks
        tasks = [t for t in tasks if t.id != task_id]
        return '', 204

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "ok"})
