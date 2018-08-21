from flask_mongoengine import MongoEngine

db = MongoEngine()


class Van(db.Document):
    __tablename__ = 'van'
    current_idx = db.IntField(default=1)
    db_name = db.StringField(default='')

    @classmethod
    def next_id(cls, db_name):
        o = cls.objects(db_name=db_name).first()
        if o is not None:
            o.current_idx += 1
            o.save()
            return o.current_idx - 1
        else:
            cls(db_name=db_name, current_idx=2).save()
            return 1
