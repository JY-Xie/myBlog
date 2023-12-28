import datetime
from flask import Blueprint, flash, g, redirect, render_template, request, url_for, current_app
from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from ..model.tables import Photo

bp = Blueprint('photos_show', __name__, url_prefix='/photos_show')
engine = create_engine("sqlite:///mysite/model/database.db", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


@bp.route('/photos')
def show_photos():
    spongebob = Photo(
        photo_path="photos/1(1).jpg",
        photo_time=datetime.datetime.now(),
        photo_location="chengdu2",
        photo_sentence="testin1111111g"
    )
    db_session.add(spongebob)
    db_session.commit()

    db_list = db_session.query(Photo).all()
    photos_urls = [
       i.photo_path for i in db_list
    ]
    photos_times = [
        i.photo_time for i in db_list
    ]
    photos_locations = [
        i.photo_location for i in db_list
    ]
    photos_sentences = [
        i.photo_sentence for i in db_list
    ]

    return render_template(
        './photo/photos.html',
        photos_list=db_list
    )
