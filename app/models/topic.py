from datetime import datetime
from . import Van
from flask_mongoengine import MongoEngine

db = MongoEngine()


class Topic(db.Document):
    __tablename__ = 'topics'

    author = db.StringField(default='')
    reply = db.IntField(default=0)
    title = db.StringField(default='')
    content = db.StringField(default='')
    index = db.IntField(default=-1)
    ct = db.DateTimeField(default=datetime.now)
    ut = db.DateTimeField(default=datetime.now)
    block = db.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(Topic, self).__init__(*args, **kwargs)


    def __repr__(self):
        return '<Tipic:{}>'.format(self.title)

    def set_index(self):
        self.index = Van.next_id(self.__class__.__name__)
