import os

from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import secure_filename, redirect

from app.routes.bbs import login_required, current_user
from app.forms import AddSelfieForm
from app.utils import log

main = Blueprint('profile', __name__)


@main.route("/", methods=["GET"])
@login_required
def index():
    form = AddSelfieForm()
    u = current_user()
    return render_template('profile.html', user=u, form=form)


@main.route("/add_selfie", methods=["POST"])
@login_required
def add_selfie():
    u = current_user()
    form = AddSelfieForm()
    if form.validate_on_submit() and request.content_length < 1000000:
        image = form.image.data
        filename = secure_filename(image.filename)
        file_path = os.path.join(os.path.dirname(os.path.abspath(__name__)), 'app/static/selfie', filename)
        image.save(file_path)
        u.selfie = filename
        u.save()
    return redirect(url_for('profile.index'))
