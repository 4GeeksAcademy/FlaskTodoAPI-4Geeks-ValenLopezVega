from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    {'label': 'Wash the dishes', 'done': False},
    {'label': 'Arrange books', 'done': False},
    {'label': 'Discover new music', 'done': False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return get_todos()

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    return get_todos()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)