from flask import Flask
from flask_mongoengine import MongoEngine


def BluePrintRegister(app):
    from app.routes.bbs.index import main as bbs_index
    from app.routes.bbs.topic import main as topic_index
    from app.routes.bbs.profile import main as profile_index
    app.register_blueprint(bbs_index)
    app.register_blueprint(topic_index, url_prefix='/topic')
    app.register_blueprint(profile_index, url_prefix='/profile')

app = Flask(__name__)
app.config.from_pyfile('config.py')

BluePrintRegister(app)
db = MongoEngine(app)
