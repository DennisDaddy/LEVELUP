from flask import Blueprint

#represents authentication blueprint

auth_blueprint = Blueprint('auth', __name__)

from . import views