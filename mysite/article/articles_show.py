from flask import Blueprint, flash, g, redirect, render_template, request, url_for, current_app
from sqlalchemy import select, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from ..model.tables import Article

bp = Blueprint('articles_show', __name__, url_prefix='/articles_show')
engine = create_engine("sqlite:///mysite/model/database.db", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


@bp.route('/abstract')
def show_abstract():
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
            './article/show_abstract.html',
            abstract_list=current_page_content,
            page=page,
            total_pages=total_pages,
            total_length=total_length
        )





@bp.route('/articles/<int:article_id>')
def show_articles(article_id):
    article = db_session.query(Article.article_head, Article.article_body).filter(Article.id == article_id).first()
    return render_template('./article/articles.html', article=article)
