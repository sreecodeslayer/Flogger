from flask import (
    request,
    jsonify,
    make_response
)
from flask_restful import Resource
from flogger.db.models import (
    Posts as PostsColl,
    Categories as CategoriesCol,
    Tags as TagsCol
)
from mongoengine.errors import (
    ValidationError,
    DoesNotExist
)


class Tags(Resource):
    def post(self):
        try:
            data = request.get_json()

            name = data.get('name')

            assert name, 'Tag name is required'
        except AssertionError as e:
            return make_response(jsonify(message=str(e)), 400)

        try:
            tag = TagsCol(name=name)
            tag.save()
            return jsonify(tag=tag)
        except Exception as e:
            raise

    def get(self):
        try:
            params = request.args
            page = params.get('page', 1)

            per_page = params.get('per_page', 10)

            per_page = 20 if per_page > 20 else per_page

        except Exception as e:
            raise e

        try:
            _tags = TagsCol.objects.paginate(
                page=page, per_page=per_page)
            tags = _tags.__dict__

            tags.pop('iterable')
            return jsonify(tags=tags)
        except Exception as e:
            raise e


class Categories(Resource):
    def post(self):
        try:
            data = request.get_json()

            name = data.get('name')

            assert name, 'Category name is required'
        except AssertionError as e:
            return make_response(jsonify(message=str(e)), 400)

        try:
            cat = CategoriesCol(name=name)
            cat.save()
            return jsonify(category=cat)
        except Exception as e:
            raise

    def get(self):
        try:
            params = request.args
            page = params.get('page', 1)

            per_page = params.get('per_page', 10)

        except Exception as e:
            raise e

        try:
            _cats = CategoriesCol.objects.paginate(
                page=page, per_page=per_page)
            cats = _cats.__dict__

            cats.pop('iterable')
            return jsonify(categories=cats)
        except Exception as e:
            raise e


class Posts(Resource):

    def get(self):
        try:
            params = request.args
            page = int(params.get('page', 1))

            per_page = int(params.get('per_page', 10))

            q = params.get('q')

            # Filters

            tag = params.get('tag')
            category = params.get('category')

        except Exception as e:
            raise e

        try:
            if tag and not category:
                try:
                    tag = TagsCol.objects.get(id=tag)
                    _posts = PostsColl.objects(
                        tags__in=[tag]).order_by(
                        'created_on', '-created_on')
                except DoesNotExist:
                    _posts = PostsColl.objects().order_by(
                        'created_on', '-created_on')

            elif category and not tag:
                try:
                    cat = CategoriesCol.objects.get(id=category)
                    _posts = PostsColl.objects(
                        category=cat).order_by(
                        'created_on', '-created_on')
                except DoesNotExist:
                    _posts = PostsColl.objects().order_by(
                        'created_on', '-created_on')
            elif category and tag:
                try:
                    tag = TagsCol.objects.get(id=tag)
                    cat = CategoriesCol.objects.get(id=category)
                    _posts = PostsColl.objects(category=cat, tags__in=[
                                               tag]).order_by(
                        'created_on', '-created_on')
                except DoesNotExist:
                    _posts = PostsColl.objects().order_by(
                        'created_on', '-created_on')

            else:
                _posts = PostsColl.objects().order_by(
                    'created_on', '-created_on')

            _posts = _posts.paginate(page=page, per_page=per_page)
            posts = _posts.__dict__
            posts.pop('iterable')

            return jsonify(posts=posts)
        except Exception as e:
            raise e

    def post(self):
        try:
            data = request.get_json()

            title = data.get('title')
            assert title, 'Post should have a valid title'

            cover_img = data.get('cover_img')
            assert title, 'Post should have a valid cover_img url'

            caption = data.get('caption')
            assert caption, 'Post should have a valid caption'

            category = data.get('category')
            assert category, 'Post should have a valid category'

            tags = data.get('tags')
            content = data.get('content', '')

        except AssertionError as e:
            return make_response(jsonify(message=str(e)), 400)

        try:
            category = CategoriesCol.objects.get(id=category)
        except ValidationError as e:
            return make_response(
                jsonify(message=str(e)), 422)
        except DoesNotExist as e:
            return make_response(jsonify(message=str(e)), 404)

        try:
            # Database
            post = PostsColl(title=title, caption=caption, cover_img=cover_img)
            post.content = content
            post.category = category
            post.save()

            if tags:
                _tags = []
                for tag in tags:
                    try:
                        tag = TagsCol.objects.get(id=tag)
                        _tags.append(tag)
                    except DoesNotExist:
                        pass
                post.update(add_to_set__tags=_tags)
                post.reload()
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
            return make_response(jsonify(message=str(e)), 404)

    def delete(self, _id):
        try:
            post = PostsColl.objects.get(id=_id)
            post.delete()

            return make_response(jsonify(post=post), 204)
        except DoesNotExist as e:
            return make_response(jsonify(message=str(e)), 404)
