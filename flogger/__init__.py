from flask import (
    Flask,
    jsonify,
    request
)

from flask_restful import Api
from .db import init_db

app = Flask('flogger', instance_relative_config=True)
app.config.from_envvar('FLOGGER_SETTINGS')

db = init_db(app)
api = Api(app)


from .core import (
    WorkBench,
    Posts, Post,
    Tags, Categories
)

api.add_resource(WorkBench, '/api/workbench')
api.add_resource(Tags, '/api/tags')
api.add_resource(Categories, '/api/categories')
api.add_resource(Posts, '/api/posts')
api.add_resource(Post, '/api/post/<_id>')
