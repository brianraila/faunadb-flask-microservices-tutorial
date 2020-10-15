from flask import (
    Blueprint, render_template, jsonify
)

bp = Blueprint('index', __name__, url_prefix='')
from app.functions import login_required


@bp.route('/')
def index_root():


    return render_template("index.html")

@bp.route('/secured')
@login_required
def index_unsecured():

    return render_template("index.html")
