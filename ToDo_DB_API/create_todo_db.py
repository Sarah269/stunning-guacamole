# Create a database
# The database will be used by the API to store data

from todo_api import app, db

# create the database
with app.app_context():
    db.create_all()