from flogger.db import get_db
from datetime import datetime
from passlib.hash import pbkdf2_sha512

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
    def __init__(self, **kwargs):
        super(Profile, self).__init__(**kwargs)

    full_name = db.StringField(required=True)
    password = db.StringField()
    email = db.EmailField(required=True)
    dob = db.DateTimeField(required=True)
    avatar = db.URLField()
    permanent_residence = db.StringField()
    current_residence = db.StringField()
    mobile = db.StringField()
    tel = db.StringField()
    social_links = db.ListField(db.ReferenceField(SocialLinks))
    skills = db.ListField(db.ReferenceField(Skills))

    def __str__(self):
        return "Users(id='%s')" % str(self.id)

    def set_password(self, pswd):
        self.password = pbkdf2_sha512.hash(pswd)

    def verify_password(self, pswd):
        return pbkdf2_sha512.verify(pswd, self.password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id, 'email': self.email})

    meta = {
        'strict': False,
        'index': ['email']
    }
