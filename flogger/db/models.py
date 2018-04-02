from flogger.db import get_db
from datetime import datetime

db = get_db()


class Categories(db.Document):
    name = db.StringField(max_length=50, required=True)

    meta = {
        'strict': False
    }


class Tags(db.Document):
    name = db.StringField(max_length=30, required=True)

    meta = {
        'strict': False
    }


class Posts(db.Document):
    title = db.StringField(max_length=100, required=True)
    caption = db.StringField(max_length=150, required=True)
    content = db.StringField()
    category = db.ReferenceField(Categories)
    tags = db.ListField()
    created_on = db.DateTimeField(default=datetime.utcnow, required=True)

    meta = {
        'strict': False,
        'index': ['created_on', 'title']
    }
