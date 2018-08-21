from datetime import datetime
from . import Van
from flask_mongoengine import MongoEngine
from app.config import SALT

db = MongoEngine()


class User(db.Document):
    __tablename__ = 'users'

    MEMBER = 100
    MODERATOR = 200
    ADMIN = 300

    username = db.StringField()
    nickname = db.StringField(default='')
    email = db.EmailField(default='void@void.com')
    selfie = db.StringField(default='default.png')
    role = db.IntField(default=MEMBER)
    password = db.StringField(default='')
    block = db.BooleanField(default=False)
    index = db.IntField(default=-1)
    ct = db.DateTimeField(default=datetime.now)
    ut = db.DateTimeField(default=datetime.now)

    @staticmethod
    def salted_password(password):
        import hashlib

        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()

        hash1 = sha256(password)
        hash2 = sha256(hash1 + SALT)
        return hash2

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.index = Van.next_id(self.__class__.__name__)
        self.nickname = self.username
        self.password = self.salted_password(self.password)

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @classmethod
    def register(cls, username, email, password):
        u = User(username=username, email=email, password=password)
        if u.verify_username():
            u.save()
            return u
        return None

    def verify_username(self) -> bool:
        """
        return True when database doesn't exist this username
        :return:
        """
        return User.objects(username=self.username).count() == 0

    def validation_login(self) -> bool:
        """
        return True when user exist and password same to the database field.
        :return:
        """
        db_u = User.objects(username=self.username).first()
        return db_u and db_u.password == self.password

    # def check_pwd(self, password):
    #     from werkzeug.security import check_password_hash
    #     return check_password_hash(self.password, password)