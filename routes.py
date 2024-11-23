from flask import Blueprint, request, jsonify
from models import Task
from database import db

api = Blueprint('api', __name__)

@api.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data.get('description'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id}), 201

@api.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed} for task in tasks])

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    task.title = data['title']
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)
    db.session.commit()
    return jsonify({'id': task.id})

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})

@api.route('/tasks', methods=['DELETE'])
def delete_all_tasks():
    db.session.query(Task).delete()
    db.session.commit()
    return jsonify({'result': True})