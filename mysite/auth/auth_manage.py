import os

from werkzeug.utils import secure_filename
from .auth import login_required
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash
from ..model.tables import Photo, Article

bp = Blueprint('auth_manage', __name__, url_prefix='/auth_manage')
engine = create_engine("sqlite:///mysite/model/database.db", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


@bp.route('/photo_manage')
@login_required
def manage_photo():
    page = int(request.args.get('page', 1))
    per_page = 10

    db_list = db_session.query(Photo).all()
    total_length = len(db_list)
    total_pages = len(db_list) // per_page + 1
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    current_page_content = db_list[start_index:end_index]
    return render_template(
        './auth/auth_manage_photo.html',
        photos_list=current_page_content,
        page=page,
        total_pages=total_pages,
        total_length=total_length)


@login_required
@bp.route('/<int:id>/photo_delete', methods=('POST',))
def delete_photo(id):
    to_del = db_session.query(Photo).get(id)
    db_session.delete(to_del)
    db_session.commit()
    return redirect(url_for('auth_manage.manage_photo'))


@login_required
@bp.route('/photo_update/', methods=('POST', ))
def update_photo():
    image = request.files["image"]
    photo_location = request.form["photo_location"]
    photo_sentence = request.form["photo_sentence"]
    if image:
        filename = secure_filename(image.filename)
        photo_abs_path = os.path.join(os.getcwd(), "mysite/static/photos", filename)
        image.save(photo_abs_path)
        local_engine = create_engine("sqlite:///mysite/model/database.db", echo=True)
        db_session = scoped_session(sessionmaker(autocommit=False,
                                                 autoflush=False,
                                                 bind=local_engine))
        photo_relative_path = "photos/{}".format(filename)
        photo_to_add = Photo(
            photo_path=photo_relative_path,
            photo_location=photo_location,
            photo_sentence=photo_sentence
        )

        db_session.add(photo_to_add)
        db_session.commit()
        return redirect(url_for('auth_manage.manage_photo'))

    else:
        return redirect(url_for('auth_manage.manage_photo'))








@bp.route('/article_manage')
@login_required
def manage_article():
    page = int(request.args.get('page', 1))
    per_page = 10
    db_list = db_session.query(Article.id, Article.article_head, Article.article_abstract).all()
    total_length = len(db_list)
    total_pages = len(db_list) // per_page + 1
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    current_page_content = db_list[start_index:end_index]
    print(db_list)
    return render_template(
            './auth/auth_manage_article.html',
            abstract_list=current_page_content,
            page=page,
            total_pages=total_pages,
            total_length=total_length
        )


@login_required
@bp.route('/<int:id>/article_delete', methods=('POST',))
def delete_article(id):
    to_del = db_session.query(Article).get(id)
    db_session.delete(to_del)
    db_session.commit()
    return redirect(url_for('auth_manage.manage_article'))


@bp.route('/article_create', methods=('POST', ))
@login_required
def create_article():
    if request.method == 'POST':
        title = request.form['article_title']
        description = request.form['article_description']
        body = request.form['article_content']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            local_engine = create_engine("sqlite:///mysite/model/database.db", echo=True)
            db_session = scoped_session(sessionmaker(autocommit=False,
                                                     autoflush=False,
                                                     bind=local_engine))
            article_to_add = Article(
                article_head=title,
                article_abstract=description,
                article_body=body
            )
            db_session.add(article_to_add)
            db_session.commit()


    return redirect(url_for('auth_manage.manage_article'))
