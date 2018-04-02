from flask import (
    request,
    jsonify,
    make_response
)
from flask_restful import Resource


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

            content = data.get('content', '')

        except AssertionError as e:
            return make_response(jsonify(message=str(e)), 400)

        try:
            # Database
            post = {}
        except Exception as e:
            raise e
        return make_response(jsonify(message='Post created', post=post), 200)
