from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

from models import db
db.init_app(app)

import flask_inventory.routes