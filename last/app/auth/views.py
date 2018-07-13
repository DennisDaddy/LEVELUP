from . import auth_blueprint
from flask.views import MethodView
from flask import make_response, request, jsonify
from  app.models import User

class RegistrationView(MethodView):
    """Class for registering user"""

    def post(self):
        """handles post request"""
        user = User.query.filter_by(email=request.data['email']).first()

        if not user:
            try:
                post_data = request.data
                # Register user
                email = post_data['email']
                password = post_data['password']
                user = User(email=email, password=password)
                user.save()

                response = {
                    'message': 'you registered successfully please login'
                }

                return make_response(jsonify(response)), 201
            except Exception as e:
                response = {
                    'message': str(e)
                }

                return make_response(jsonify(response)), 401
        else:
            # tell user they already exists
            response = {
                'message': 'User already exists. please login'
            }

            return make_response(jsonify(response)), 202
registration_view = RegistrationView.as_view('register_view')
# add rule for  Blueprint
auth_blueprint.add_url_rule(
   '/auth/register',
    view_func=registration_view,
    methods=['POST']
    )