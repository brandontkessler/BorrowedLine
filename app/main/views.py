from flask import render_template
from flask_login import login_required
from . import main
from ..decorators import check_confirmed


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/secret')
@login_required
@check_confirmed
def secret():
    return "<h1>SECRET PAGE ACCESSED!</h1>"
