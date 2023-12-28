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
    page = int(request.args.get('page', 1))
    per_page = 10


    # spongebob = Photo(
    #     photo_path="photos/1(1).jpg",
    #     photo_time=datetime.datetime.now(),
    #     photo_location="chengdu2",
    #     photo_sentence="testin1111111g"
    # )
    # db_session.add(spongebob)
    # db_session.commit()

    db_list = db_session.query(Photo).all()
    total_length = len(db_list)
    total_pages = len(db_list) // per_page + 1
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    current_page_content = db_list[start_index:end_index]

    return render_template(
        './photo/photos.html',
        photos_list=current_page_content,
        page=page,
        total_pages=total_pages,
        total_length=total_length
    )
