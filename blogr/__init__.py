import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mydatabase

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    basedir = os.path.abspath(os.path.dirname(__name__))

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # from . import db
    # db.init_app(app)
    #
    # from . import auth
    # app.register_blueprint(auth.bp)
    #
    # from . import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')
    return app
