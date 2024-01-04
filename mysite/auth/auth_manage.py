import functools
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


# @bp.route('/create', methods=('GET', 'POST'))
# @login_required
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None
#
#         if not title:
#             error = 'Title is required.'
#
#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 'INSERT INTO post (title, body, author_id)'
#                 ' VALUES (?, ?, ?)',
#                 (title, body, g.user['id'])
#             )
#             db.commit()
#             return redirect(url_for('blog.index'))
#
#     return render_template('blog/create.html')

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
