from flask import (
    Flask,
    jsonify,
    request
)

from flask_restful import Api

app = Flask('flogger')

api = Api(app)


from .core import (
    WorkBench,
    Posts
)

api.add_resource(WorkBench, '/api/workbench')
api.add_resource(Posts, '/api/posts')
