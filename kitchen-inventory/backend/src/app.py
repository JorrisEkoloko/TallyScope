# src/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:Jorris123@localhost/kitchen_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


from routes.auth import auth
from routes.inventory import inventory
from routes.station import station
from routes.recipe import recipe

app.register_blueprint(auth)
app.register_blueprint(inventory)
app.register_blueprint(station)
app.register_blueprint(recipe)


if __name__ == '__main__':
    app.run(debug=True)
