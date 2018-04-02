from flask import (
    Flask,
    jsonify,
    request
)

from flask_restful import Api

app = Flask('flogger')

api = Api(app)


from .core import (
    WorkBench
)

api.add_resource(WorkBench, '/workbench')
