# Python REST API Tutorial for Beginners
# Dave Gray
# Tested using Thunderclient
# Create a REST API using flask


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)

# using sqlite database
# name of database: database.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

# database structure
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    # representation
    def __repr__(self):
        return f"User(name= {self.name}, email= {self.email})"

# validate input
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_args.add_argument('email', type=str, required=True, help="Email cannot be blank")


userFields = {
    'id':fields.Integer,
    'name': fields.String,
    'email':fields.String,
}

# define endpoint
class Users(Resource):
    # decorate with marshal_with
    @marshal_with(userFields)
    # retrieve all users
    def get(self):
        users= UserModel.query.all()  
        return users

    # post function. add a user
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201

class User(Resource):
    # retrieve a user
    @marshal_with(userFields)
    def get(self,id):
        # return the first user with id
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        return user
   
   # update a user
    @marshal_with(userFields)
    def patch(self,id):
        args = user_args.parse_args()
        # return the first user with id
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        # Update user
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user
    
   # remove a user
    @marshal_with(userFields)
    def delete(self,id):
        # return the first user with id
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        # remove user
        db.session.delete(user)
        db.session.commit()
        # return remaining users
        users = UserModel.query.all()
        return users


# assign to a URL
api.add_resource(Users,'/api/users/')
# request user by id
api.add_resource(User, '/api/users/<int:id>')


# define Home route
@app.route('/')
def home():
    return '<h1>Flask REST API</h1>'

# run program
if __name__ == '__main__':
    app.run(debug=True)

