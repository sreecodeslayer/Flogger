from flask import (
    Flask,
    jsonify,
    request,
    abort,
    render_template,
    make_response,
    abort
)

from flask_restful import Api
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
    get_jwt_claims
)
from datetime import datetime, timedelta

app = Flask('flogger', instance_relative_config=True)
app.config.from_envvar('FLOGGER_SETTINGS')
app.config['JWT_SECRET_KEY'] = SECRET_KEY = 'thIs is a cr@zy s3cr3t k3y'


# Init Database
from .db import init_db
from mongoengine.errors import DoesNotExist

db = init_db(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.before_first_request
def check_profile():
    from .db.models import Profile
    try:
        profile = app.config['PROFILE']
        full_name = profile.get('full_name')
        email = profile.get('email')
        password = profile.get('password')
        dob = profile.get('dob')

        assert profile.get(
            'full_name'), 'Please update your flask'
        'config with PROFILE["full_name"]'
        assert profile.get(
            'email'), 'Please update your flask'
        'config with PROFILE["email"]'
        assert profile.get(
            'password'), 'Please update your flask'
        'config with PROFILE["password"]'
        assert profile.get(
            'dob'), 'Please update your flask'
        'config with PROFILE["dob"] > Format "DD-MM-YYY"'
        try:
            dob = datetime.strptime(dob, '%d-%m-%Y')
        except ValueError as e:
            raise RuntimeError(e)

        # Make an admin [User]
        try:
            profile = Profile.objects.get(email=email)
        except DoesNotExist:
            profile = Profile(
                full_name=full_name,
                email=email,
                dob=dob
            )
            profile.set_password(password)
            profile.save()
        except Exception as e:
            raise
    except AssertionError as e:
        raise RuntimeError(e)


# Flask JWT
def authenticate(email, pswd):
    try:
        user = Profile.objects.get(email=email)
        if user and user.verify_password(pswd):
            return {'id': str(user.id),
                    'email': user.email}
    except DoesNotExist:
        user = None
    return user


@app.route('/auth/login', methods=['POST'])
def get_token():
    data = request.get_json()
    try:
        email = data.get('email')
        passwd = data.get('password')

        usr = Profile.objects.get(email=email)

        if not usr.verify_password(passwd):
            return make_response(
                jsonify(message='Invalid credentials'), 403
            )

        token = ''

        access_token = create_access_token(identity=usr)
        return jsonify(message='Logged in successfully', token=access_token)

    except DoesNotExist as e:
        return make_response(
            jsonify(message='User not found'), 404
        )


jwt = JWTManager(app)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.email


# Init Rest API
api = Api(app)

workbench_api = Api(app, decorators=[jwt_required])
from .core import (
    WorkBench, Profile,
    Posts, Post,
    Tags, Categories
)


# PUBLIC routes for others to view blog


# APIs below are accessible to the Maintainer
workbench_api.add_resource(WorkBench, '/api/workbench')
workbench_api.add_resource(Profile, '/api/workbench/profile')
workbench_api.add_resource(Tags, '/api/tags')
workbench_api.add_resource(Categories, '/api/categories')
workbench_api.add_resource(Posts, '/api/posts')
workbench_api.add_resource(Post, '/api/posts/<_id>')
