from flask import Flask
from flask_mongoengine import MongoEngine


def BluePrintRegister(app):
    from app.routes.bbs.index import main as bbs_index
    app.register_blueprint(bbs_index, url_prefix='/')


app = Flask(__name__)
app.config.from_pyfile('config.py')

BluePrintRegister(app)
db = MongoEngine(app)
