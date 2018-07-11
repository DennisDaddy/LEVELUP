from . import auth_blueprint
from flask.views import MethodView
from flask import make_response, request, jsonify
from app.models import User

class RegistrationView(MethodView):
    """ class for registering a new user """
    def post(self):
        """ handle post request for register url """
        # checks if user exists
        user = User.querry.filter_by(email=request.data['email']).first()

        if not user:
            #register user if they dont exist
            try:
                post_data = request.data
                #Register user
                email = post_data['email']
                password = post_data['password']
                user = User(email=email, password=password)
                user.save()

                response = {
                    'message': 'You are registered successfully. please login'
                }

                return make_response(jsonify(response)), 201
            except Exception as e:
                response = {
                    'message': str(e)
                }

                return make_response(jsonify(response), 401)