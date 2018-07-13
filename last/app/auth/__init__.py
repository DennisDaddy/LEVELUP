from flask import Blueprint

# Instance of a Blueprint that presents the authentification blueprint
auth_blueprint = Blueprint('auth', __name__)

from . import views