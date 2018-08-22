from flask import Blueprint, render_template
from app.routes.bbs import login_required, current_user

main = Blueprint('profile', __name__)


@login_required
@main.route("/", methods=["GET"])
def index():
    u = current_user()
    return render_template('profile.html', user = u)

