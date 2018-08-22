from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from app.forms import AddTopicForm
from app.models.topic import Topic
from app.routes.bbs import login_required, current_user

main = Blueprint('topic', __name__)


@login_required
@main.route("/add", methods=["GET", "POST"])
def add():
    form = AddTopicForm()
    if form.validate_on_submit():
        u = current_user()
        t = Topic(title=form.title.data, content=form.title.data, author=u.username)
        t.set_index()
        t.save()
        return redirect(url_for('index.index'))
    return render_template('add_topic.html', form=form)


@main.route("/detail/<int:index>", methods=["GET"])
def detail(index):
    u =current_user()
    t = Topic.objects(index=index).first()
    return render_template('detail.html', topic=t,user = u)
