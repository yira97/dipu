from bson import ObjectId
from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from app.forms import AddTopicForm, ReplyForm
from app.models.topic import Topic
from app.routes.bbs import login_required, current_user

main = Blueprint('topic', __name__)


@main.route("/add", methods=["GET", "POST"])
@login_required
def add():
    u = current_user()
    form = AddTopicForm()
    if form.validate_on_submit():
        Topic.register(title=form.title.data, content=form.content.data, username=u.username)
        return redirect(url_for('index.index'))
    return render_template('add_topic.html', form=form, user=u)


@main.route("/detail/<string:index>", methods=["GET", "POST"])
@login_required
def detail(index):
    u = current_user()
    a = ObjectId(index)
    t = Topic.objects(id=a).first()
    form = ReplyForm()
    return render_template('detail.html', topic=t, user=u,form = form)
