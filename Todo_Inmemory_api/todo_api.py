# Python API
# Simple Todo.  List is stored in memory
# Gemini 2.5
# Tested using Thunderclient

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database" for todo items
todos ={}
current_id = 1

# Define route
@app.route('/')
def home():
    return "Welcome to the Simple To-Do API!"


# Define to-do endpoints

# Get All To-Do Items

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Get a single To-DO Item

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = todos.get(todo_id)
    if todo:
        return jsonify(todo)
    return jsonify({"message": "To-Do item not found"}), 404

# Create a To-Do Item
@app.route('/todos', methods=['POST'])
def create_todo():
    global current_id
    data = request.json # Expecting JSON data in request body
    if not data or 'task' not in data:
        return jsonify ({"message": "Task is required"}), 400

    new_todo = {
        "id": current_id,
        "task": data['task'],
        "completed": False
    }
    todos[current_id] = new_todo
    current_id +=1
    return jsonify(new_todo), 201 #201  Created

# Update a To-Do Item
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        return jsonify({"message": "To-Do item not found"}), 404
    
    data = request.json
    # data is {}
    if not data:
        return jsonify({"message": "No data provided for update"}), 400

    # if message is blank, returns 415 Unsupported media type

    if 'task' in data:
        todo['task'] = data['task']
    if 'completed' in data:
        todo['completed'] = data['completed']

    return jsonify(todo)

# Delete a To-Do item
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id in todos:
        del todos[todo_id]
        return jsonify({"message": "To-Do item deleted successfully"}), 204 # 204 No Content status code
    return jsonify({"message": "To-Do item not found"}), 404




if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for automatic reloading and helpful error messages