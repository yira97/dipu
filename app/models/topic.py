from datetime import datetime
from app.models.user import User
from flask_mongoengine import MongoEngine

db = MongoEngine()


class Topic(db.Document):
    username = db.StringField(default='')
    content = db.StringField(default='')
    title = db.StringField()  # 标题（楼主专属）
    is_host = db.BooleanField(default=True)
    floor = db.IntField(default=0)
    block = db.BooleanField(default=False)
    ct = db.DateTimeField(default=datetime.now)
    ut = db.DateTimeField(default=datetime.now)

    def __init__(self, *args, **kwargs):
        super(Topic, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Topic_author:{}>'.format(self.username)

    @property
    def selfie(self):
        return User.objects(username=self.username).first().selfie

    @classmethod
    def register(cls, *args, **kwargs):
        t = cls(*args, **kwargs)
        t.save()
        return t

    @classmethod
    def make_reply(cls, receiver_id, *args, **kwargs):
        """
        # 如果被回者是楼主：回复者楼层=层主数
        # 如果被回者是层主：回复者的楼层 = 被回者楼层，回复者host改为false
        :param receiver_id:
        :param args:
        :param kwargs:
        :return:
        """
        receiver_topic = Topic.objects(id=receiver_id).first()
        submitter_topic = cls(*args, **kwargs)

        if receiver_topic.is_host:
            submitter_topic.floor = len(Topic.objects(is_host=True))
        else:
            submitter_topic.floor = receiver_topic.floor
            submitter_topic.is_host = False
        submitter_topic.save()

    def get_index(self):
        return str(self.id)

    @classmethod
    def find_topic(cls, index):
        return Topic.objects(id=index).first()
