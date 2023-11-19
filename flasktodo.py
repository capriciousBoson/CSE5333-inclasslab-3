from flask import Flask, request, jsonify
app = Flask(__name__)

Tasks =[
    {"id":1, "title":"Task: #1", "description":"Preapare Well for cloud computing exam" },
    {"id":2, "title":"Task: #2", "description":"Study well for DAA exam"},
    {"id":3, "title":"Task: #3", "description":"Solve 10 Leetcode problems"}
]

#API endpoint for retrieving all tasks:

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks":Tasks})

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((task for task in Tasks if task["id"]==id), None)
    if task is None:
        return jsonify({"message":"not found"}), 404
    return jsonify({"task":task})

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if "title" not in data or "description" not in data:
        return jsonify({"message": "Title and description are required"}), 400
    new_task = {
        "id": len(Tasks) + 1,
        "title": data["title"],
        "description": data["description"],
    }
    Tasks.append(new_task)
    return jsonify({"message": "Task created", "task": new_task}), 201

# Endpoint to update a task by ID (PUT)
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = next((task for task in Tasks if task["id"] == id), None)
    if task is None:
        return jsonify({"message": "Task not found"}), 404
    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    return jsonify({"message": "Task updated", "task": task})

# Endpoint to delete a task by ID (DELETE)
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = next((task for task in Tasks if task["id"] == id), None)
    if task is None:
        return jsonify({"message": "Task not found"}), 404
    Tasks.remove(task)
    return jsonify({"message": "Task deleted", "task": task})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True)