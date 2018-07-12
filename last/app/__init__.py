from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local imports
from instance.config import app_config

# create sqlalchemy object
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Comment
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/comments/', methods=['POST', 'GET'])
    def comments():
        if request.method == "POST":
            title = str(request.data.get('title', ''))
            if title:
                comment = Comment(title=title)
                comment.save()
                response = jsonify({
                    'id': comment.id,
                    'title': comment.title,
                    'date_created': comment.date_created,
                    'date_modified': comment.date_modified
                })

                response.status_code = 201
                return response
        else:
            # GET request
            comments = Comment.get_all()
            results = []

            for comment in comments:
                obj = {
                    'id': comment.id,
                    'title': comment.title,
                    'date_created': comment.date_created,
                    'date_modified': comment.date_modified
                }

                results.append(obj)
            response =jsonify(results)
            response.status_code = 200
            return response


    return app
