from marshmallow import (
    Schema,
    fields,
    validate,
    pre_load,
    post_dump,
    post_load
)
from bson import ObjectId


class ObjectID(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            ''
        return str(value)


Schema.TYPE_MAPPING[ObjectId] = ObjectID


class CategoriesSchema(Schema):
    id = ObjectID(dump_only=True)
    name = fields.String(required=True, validate=[
                         validate.Length(min=6, max=40)])


class TagsSchema(Schema):
    id = ObjectID(dump_only=True)
    name = fields.String(required=True, validate=[
                         validate.Length(min=6, max=30)])


from .models import Posts


class PostsSchema(Schema):
    id = ObjectID(dump_only=True)
    title = fields.String(required=True, validate=[
        validate.Length(min=40, max=100)])
    cover_img = fields.Url(required=True, validate=validate.URL)
    caption = fields.String(required=True, validate=[
        validate.Length(min=50, max=80)])
    content = fields.String(dump_only=True)
    category = fields.Nested(CategoriesSchema, dump_only=True)
    tags = fields.List(fields.Nested(TagsSchema), dump_only=True)
    created_on = fields.DateTime(dump_only=True)

    @post_load
    def make_object(self, data):
        if not data:
            return None
        return Posts(
            title=data['title'],
            cover_img=data['cover_img'],
            caption=data['caption']
        )


from .models import SocialLinks


class SocialLinksSchema(Schema):
    id = ObjectID(dump_only=True)
    fa_class = fields.String()
    name = fields.String(required=True, validate=[
        validate.Length(max=15)])
    url = fields.Url(required=True, validate=validate.URL)

    @post_load
    def make_object(self, data):
        if not data:
            return None
        return SocialLinks(
            name=data['name'],
            url=data['url'],
            fa_class=data.get('fa_class', '')
        )


from .models import Skills


class SkillsSchema(Schema):
    id = ObjectID(dump_only=True)
    name = fields.String(required=True, validate=[
        validate.Length(min=3, max=15)])
    proficiency = fields.Integer(required=True)

    @post_load
    def make_object(self, data):
        if not data:
            return None
        return Skills(
            name=data['name'],
            proficiency=data['proficiency']
        )