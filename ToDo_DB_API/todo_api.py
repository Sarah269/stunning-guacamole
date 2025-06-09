# ToDo List FLASK REST API
# Create a REST API for a ToDo List
# Store list in SQLite database
# Tested using Thunderclient



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)

# using sqlite database
# name of database: todo.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
api = Api(app)

# database structure
class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), unique=True, nullable=False)
    
    # representation
    def __repr__(self):
        return f"Todo(task= {self.task})"

# validate input
todo_args = reqparse.RequestParser()
todo_args.add_argument('task', type=str, required=True, help="Task cannot be blank")


todoFields = {
    'id':fields.Integer,
    'task': fields.String,
    
}

# define endpoint
class Todos(Resource):
    # decorate with marshal_with
    @marshal_with(todoFields)
    # retrieve all todos
    def get(self):
        todos= TodoModel.query.all()  
        return todos

    # post function. add a todo
    @marshal_with(todoFields)
    def post(self):
        args = todo_args.parse_args()
        todo = TodoModel(task=args["task"])
        db.session.add(todo)
        db.session.commit()
        todos = TodoModel.query.all()
        return todos, 201

class Todo(Resource):
    # retrieve a todo
    @marshal_with(todoFields)
    def get(self,id):
        # return the first todo with id
        todo = TodoModel.query.filter_by(id=id).first()
        if not todo:
            abort(404, message = "Todo not found")
        return todo
   
   # update a todo
    @marshal_with(todoFields)
    def patch(self,id):
        args = todo_args.parse_args()
        # return the first todo with id
        todo = TodoModel.query.filter_by(id=id).first()
        if not todo:
            abort(404, message = "Todo not found")
        # Update todo
        todo.task = args["task"]
        db.session.commit()
        return todo
    
   # remove a todo
    @marshal_with(todoFields)
    def delete(self,id):
        # return the first todo with id
        todo = TodoModel.query.filter_by(id=id).first()
        if not todo:
            abort(404, message = "Todo not found")
        # remove todo
        db.session.delete(todo)
        db.session.commit()
        # return remaining todos
        todos = TodoModel.query.all()
        return todos


# assign to a URL
api.add_resource(Todos,'/api/todolist/')
# request todo by id
api.add_resource(Todo, '/api/todolist/<int:id>')


# define Home route
@app.route('/')
def home():
    return '<h1>Simple Todo List REST API</h1>'

# run program
if __name__ == '__main__':
    app.run(debug=True)

