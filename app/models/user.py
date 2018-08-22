from datetime import datetime
from flask_mongoengine import MongoEngine
from app.config import SALT

db = MongoEngine()


class User(db.Document):
    """
    # 程序保证数据正确，而不是数据库保证。所以在这里字符串类型都默认空串
    # MEMBER = 100， MODERATOR = 200， ADMIN = 300
    # 既然用了NOSQL数据库，仍然用自增ID做主键有点吃饱了撑的，所以拿username作为uniqueness字段
    """
    username = db.StringField(default='')
    nickname = db.StringField(default='')
    password = db.StringField(default='')
    role = db.IntField(default=100)
    email = db.StringField(default='')
    selfie = db.StringField(default='default.jpeg')
    intro = db.StringField(default='')
    block = db.BooleanField(default=False)
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

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    def _set_password(self):
        self.password = User.salted_password(self.password)

    @classmethod
    def register(cls, *args, **kwargs):
        u = cls(*args, **kwargs)
        if u.verify_username():
            u._set_password()
            u.save()
            return u
        return None

    @classmethod
    def login(cls, *args, **kwargs):
        u = cls(*args, **kwargs)
        return u.validation_password

    def validation_password(self) -> bool:
        """
        return True when user exist and password same to the database field.
        :return:
        """
        db_u = User.objects(username=self.username).first()
        return db_u and db_u.password == self.password

    def verify_username(self) -> bool:
        """
        return True when database doesn't exist this username
        :return:
        """
        return User.objects(username=self.username).count() == 0
