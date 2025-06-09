# ToDo List FLASK REST API with Database

## Project
Create a REST API using FLASK.  This API will handle todo list items. The API will create, retrieve, update, and delete todo list items data. The todo list items will be stored in a SQLite database.  Each todo item is assigned a numerical id.

## Tools
- Python, flask, flask_restful, flask_sqlalchemy, Thunderclient, VScode

# Message Format
- JSON: {"task": "Todo List Item"}
  
## File
- todo_api.py: rest api
- create_db_todo.py:  create SQLite database

## Setup
Instructions for Windows
- Create a virtual environment: python -m venv myenv
- Activate virtual enviroment: myenv\Scripts\activate
- Install requirements: pip install -r requirements.txt


## Testing
- manually tested api using Thunderclient
