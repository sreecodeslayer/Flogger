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
    cover_img = db.URLField(required=True)
    caption = db.StringField(max_length=150, required=True)
    content = db.StringField()
    category = db.ReferenceField(Categories)
    tags = db.ListField()
    created_on = db.DateTimeField(default=datetime.utcnow, required=True)

    meta = {
        'strict': False,
        'index': ['created_on', 'title']
    }


class SocialLinks(db.Document):
    name = db.StringField(required=True)
    url = db.URLField(required=True)
    fa_class = db.StringField()

    meta = {
        'strict': False,
        'index': ['name']
    }


class Skills(db.Document):
    name = db.StringField(required=True)
    proficiency = db.IntField(required=True)

    meta = {
        'strict': False,
        'index': ['name', 'proficiency']
    }


class Profile(db.Document):
    full_name = db.StringField(required=True)
    email = db.EmailField(required=True)
    dob = db.DateTimeField(required=True)
    avatar = db.URLField()
    permanent_residence = db.StringField()
    current_residence = db.StringField()
    mobile = db.StringField()
    tel = db.StringField()
    social_links = db.ListField(db.ReferenceField(SocialLinks))
    skills = db.ListField(db.ReferenceField(Skills))

    meta = {
        'strict': False
    }
