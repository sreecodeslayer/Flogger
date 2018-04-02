from flask import (
    request,
    jsonify,
    make_response
)
from flask_restful import Resource
from flogger.db.models import (
    Posts as PostsColl
)
from mongoengine.errors import (
    ValidationError,
    DoesNotExist
)


class Posts(Resource):
    def get(self):
        pass

    def post(self):
        try:
            data = request.get_json()

            title = data.get('title')
            assert title, 'Post should have a valid title'

            caption = data.get('caption')
            assert caption, 'Post should have a valid caption'

            category = data.get('category')
            assert category, 'Post should have a valid category'

            content = data.get('content', '')

        except AssertionError as e:
            return make_response(jsonify(message=str(e)), 400)

        try:
            # Database
            post = PostsColl(title=title, caption=caption)
            post.content = content
            post.save()
        except ValidationError as e:
            return make_response(
                jsonify(message=str(e)), 422)
        return make_response(
            jsonify(message='Post created', post=post), 200)


class Post(Resource):
    def get(self, _id):
        try:
            post = PostsColl.objects.get(id=_id)

            return jsonify(post=post)
        except DoesNotExist as e:
            return make_response(jsonify(message=e), 404)

    def delete(self, _id):
        try:
            post = PostsColl.objects.get(id=_id)
            post.delete()

            return make_response(jsonify(post=post), 204)
        except DoesNotExist as e:
            return make_response(jsonify(message=str(e)), 404)
