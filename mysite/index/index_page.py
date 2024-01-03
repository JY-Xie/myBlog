from flask import Blueprint, flash, g, redirect, render_template, request, url_for, current_app
from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from ..model.tables import Photo

bp = Blueprint('index_page', __name__, url_prefix='')


@bp.route('/')
def index_page():
    return render_template('./index/index.html')


@bp.route('/trends')
def trends():
    return render_template('./trend/trends.html')


@bp.route('/codes')
def codes():
    return render_template('./code/codes.html')


@bp.route('/CV')
def curriculum_vitae():
    return render_template('./index/curriculum_vitae.html')


