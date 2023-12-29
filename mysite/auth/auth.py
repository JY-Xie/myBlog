import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash

from ..model.tables import Admin

bp = Blueprint('auth', __name__, url_prefix='/auth')
engine = create_engine("sqlite:///mysite/model/database.db", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


# @bp.route('/register', methods=("GET", "POST"))
# def register():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         db = get_db()
#         error = None
#
#         if not username:
#             error = "Username is required."
#         elif not password:
#             error = "Password is required."
#
#         if error is None:
#             try:
#                 db.execute(
#                     "INSERT INTO user (username, password) VALUES (?, ?)",
#                     (username, generate_password_hash(password)),
#                 )
#                 db.commit()
#             except db.IntegrityError:
#                 error = f"User {username} is already registered."
#             else:
#                 return redirect(url_for("auth.login"))
#
#             flash(error)
#
#     return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = db_session.query(Admin).filter(Admin.name == username).first()
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'
        if error is None:
            db_session.close()
            session['user_id'] = user.name
            return redirect(url_for('index_page.index_page'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        sss = db_session.query(Admin).filter(Admin.name == user_id).first()
        g.user = sss


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index_page.index_page'))


def login_required(view):
    """
    这段代码定义了一个装饰器函数 login_required，用于保护需要登录才能访问的视图函数。

    装饰器函数是一种在不修改被装饰函数源代码的情况下，对其进行功能扩展或修改的方式。login_required 装饰器可以应用于需要登录才能访问的视图函数，以确保只有已登录用户才能执行该视图函数。

    下面是对代码的解释：

    login_required 是一个装饰器函数，它接受一个视图函数 view 作为参数。

    @functools.wraps(view) 是一个装饰器，它用于将内部函数 wrapped_view 的元数据（如函数名、文档字符串等）设置为与被装饰的视图函数 view 相同，以确保在调试和文档生成等情况下能够正确显示。

    wrapped_view 是一个内部函数，它接受任意数量的关键字参数 **kwargs。

    在 wrapped_view 函数内部，首先检查 g.user 是否为 None，g 是 Flask 中的一个全局对象，用于存储全局状态。在这里，g.user 可能是用于表示当前登录的用户。

    如果 g.user 为 None，即用户未登录，则使用 redirect 函数将用户重定向到名为 'auth.login' 的登录页面。url_for('auth.login') 用于生成登录页面的 URL。

    如果 g.user 不为 None，即用户已登录，则执行原始的视图函数 view，并将关键字参数 **kwargs 传递给它。

    最后，返回 wrapped_view 函数作为装饰器的结果。

    通过将 @login_required 放置在需要登录的视图函数上，可以实现对这些视图函数的保护。如果用户未登录，访问这些视图函数时会被重定向到登录页面；如果用户已登录，则可以正常访问这些视图函数。

    这种装饰器的使用方式可以提高代码的可重用性和安全性，因为它将登录验证逻辑从每个需要登录的视图函数中分离出来，并将其集中在一个装饰器函数中。
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
