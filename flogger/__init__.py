from flask import (
    Flask,
    jsonify,
    request,
    render_template
)

from flask_restful import Api
from .db import init_db

app = Flask('flogger', instance_relative_config=True)
app.config.from_envvar('FLOGGER_SETTINGS')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

db = init_db(app)
api = Api(app)


from .core import (
    WorkBench,
    Posts, Post,
    Tags, Categories
)

# PUBLIC routes for others to view blog


# APIs below are accessible to the Maintainer
api.add_resource(WorkBench, '/api/workbench')
api.add_resource(Tags, '/api/tags')
api.add_resource(Categories, '/api/categories')
api.add_resource(Posts, '/api/posts')
api.add_resource(Post, '/api/posts/<_id>')
