from flask import (
    request,
    make_response,
    jsonify
)

from flask_restful import Resource
from datetime import datetime, timedelta

from flask_jwt_extended import (
    current_user,
    get_jwt_identity
)

from mongoengine.errors import (
    DoesNotExist,
    ValidationError
)

from flogger.db.models import (
    Profile,
    Skills,
    SocialLinks
)


class WorkBenchResource(Resource):
    def get(self):
        pass


class ProfileResource(Resource):
    def get(self):
        try:
            email = get_jwt_identity()
            profile = Profile.objects.exclude('password').get(email=email)
            return jsonify(profile=profile)
        except Exception as e:
            raise

    def patch(self):
        try:
            data = request.get_json()
            _id = data.get('id')
            assert _id, 'Profile id is required'
        except AssertionError as e:
            return make_response(
                jsonify(message=str(e)),
                400
            )
        try:
            old_pswd = data.get('old_password')
            new_pswd = data.get('new_password')
            full_name = data.get('full_name')
            dob = data.get('dob')
            skills = data.get('skills')
            social_links = data.get('social_links')

            if old_pswd and new_pswd:
                profile = Profile.objects.get(id=_id)
                # Reset / Change password

                # Verify current password
                if profile.verify_password(old_pswd):
                    profile.set_password(new_pswd)
                    profile.save()
                    return jsonify(message='Password updated')
                else:
                    return make_response(
                        jsonify(message='Invalid current password'),
                        403
                    )

            else:
                profile = Profile.objects.exclude('password').get(id=_id)
                if full_name:
                    profile.update(full_name=full_name)
                if dob:
                    try:
                        dob = datetime.strptime(dob, '%d-%m-%Y')
                        profile.update(dob=dob)
                    except ValueError as e:
                        raise
                if skills:
                    for _id in skills:
                        try:
                            skill = Skills.objecs.get(id=_id)
                            profile.update(add_to_set__skills=[skill])
                        except DoesNotExist:
                            pass
                if social_links:
                    for _id in social_links:
                        try:
                            social = SocialLinks.objecs.get(id=_id)
                            profile.update(add_to_set__social_links=[social])
                        except DoesNotExist:
                            pass
                return jsonify(message='Changes made to profile',
                               profile=profile.reload(
                                   'full_name', 'dob', 'skills', 'social_links'
                               )
                               )
        except Exception as e:
            raise e
