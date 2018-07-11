""" Third party imports """
import json
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort, make_response


"""Local imports"""

from instance.config import app_config

# create db object
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Comment
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        return "welcome to homepage"

    @app.route('/comments/new', methods=['POST', 'GET'])

    def comments():
        if request.method == "POST":
            title = str(request.data.get('title', ''))
            if title:
                comment = Comment(title=title)
                comment.save()
                response = jsonify({
                    'id': comment.id,
                    'title': comment.title,
                    'date_created': comment.comment.date_created
                })
                response.status_code = 201
                return response
    



    return app