import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .model.tables import Photo


def create_app(test_config=None):
    app = Flask(__name__, static_folder='./static', template_folder='./templates')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(r'/model/database.db'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    engine = create_engine("sqlite:///database.db", echo=True)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))

    from .photo import photos_show
    app.register_blueprint(photos_show.bp)

    from .index import index_page
    app.register_blueprint(index_page.bp)

    from .auth import auth
    app.register_blueprint(auth.bp)

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
