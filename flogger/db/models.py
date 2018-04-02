from flogger.db import get_db
from datetime import datetime

db = get_db()


class Posts(db.Document):
    title = db.StringField(max_char=100, required=True)
    caption = db.StringField(max_char=150, required=True)
    content = db.StringField()
    created_on = db.DateTimeField(default=datetime.utcnow, required=True)
