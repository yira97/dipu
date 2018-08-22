from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from app.forms import AddTopicForm
from app.models.reply import Reply
from app.models.topic import Topic
from app.routes.bbs import login_required, current_user

main = Blueprint('topic', __name__)


@login_required
@main.route("/add", methods=["GET", "POST"])
def add():
    u = current_user()
    form = AddTopicForm()
    if form.validate_on_submit():
        Topic.register(title=form.title.data, content=form.title.data, author=u.username)
        return redirect(url_for('index.index'))
    return render_template('add_topic.html', form=form)


@main.route("/detail/<int:index>", methods=["GET", "POST"])
def detail(index):
    u = current_user()
    t = Topic.objects(index=index).first()
    rs = Reply.objects()
    form = ReplyForm()
    if form.validate_on_submit:
        Reply.register()
    return render_template('detail.html', topic=t, user=u, replys=rs,form=form)
