""" Third party imports """
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

"""Local imports"""
from config import app_config

# create db object
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Comment
    app = Flask(__name__, instance_relative_config=True)
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
                    'tittle': comment.tittle,
                    'content': comment.content,
                    'date_created': comment.date_created
                })

                response.status_code = 201
                return response

            else:
                comments = Comment.get_all()
                result = []

                for comment in comments:
                    obj = {

                        'id': comment.id,
                        'tittle': comment.tittle,
                        'content': comment.content,
                        'date_created': comment.date_created
                    }

                    results.append(obj)
                    response = jsonify(results)
                    response.status_code= 200
                    return response

    return app