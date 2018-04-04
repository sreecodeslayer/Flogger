from flask import (
    request,
    make_response,
    jsonify
)

from flask_restful import Resource

from flask_jwt_extended import (
    current_user,
    get_jwt_identity
)

from mongoengine.errors import (
    DoesNotExist,
    ValidationError
)

from flogger.db.models import (
    Profile
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


            profile = Profile.objects.get(id=_id)

            if old_pswd and new_pswd:
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
        except Exception as e:
            raise e
