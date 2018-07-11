from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local import
from instance.config import app_config

# initialize sql-alchemy
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
        return 'Welcome to homepage'

    @app.route('/level/api/v1/comments/', methods=['POST', 'GET'])
    def comments():
        if request.method == "POST":
            #create comment using POST request
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
            # Get all comments using GET request
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
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/level/api/v1/comments/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def comment_manipulation(id, **kwargs):
     # retrieve a buckelist using it's ID
        comment = Comment.query.filter_by(id=id).first()
        if not comment:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            comment.delete()
            return {
            "message": "comment {} deleted successfully".format(comment.id) 
         }, 200
         
        elif request.method == 'PUT':
            title = str(request.data.get('title', ''))
            comment.title = title
            comment.save()
            response = jsonify({
                'id': comment.id,
                'title': comment.title,
                'date_created': comment.date_created,
                'date_modified': comment.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': comment.id,
                'title': comment.title,
                'date_created': comment.date_created,
                'date_modified': comment.date_modified
            })
            response.status_code = 200
            return response
    


    return app