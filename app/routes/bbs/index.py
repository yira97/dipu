from time import sleep

from flask import render_template, Blueprint, flash, redirect, url_for, session

from app.forms import LoginForm, RegistrationForm
from app.models.topic import Topic
from app.models.user import User
from app.routes.bbs import current_user, login_required

main = Blueprint('index', __name__)


@main.route("/", methods=["GET"])
def index():
    u = current_user()
    ts = Topic.objects(floor=0)
    return render_template('index.html', user=u, topics=ts)


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User(username=form.data['username'], password=form.data['password'])
        if u.verify_username():
            flash("账号不存在")
            return redirect(url_for('index.login'))
        elif u.validation_password():
            flash("密码错误")
            return redirect(url_for('index.login'))
        session['username'] = u.username
        session.permanent = True
        return redirect(url_for('index.index'))
    return render_template('login.html', form=form)


@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        u = User.register(username=form.data['username'], password=form.data['password'], email=form.data['email'])
        if u is not None:
            session['username'] = u.username
            flash("注册成功", 'ok')
            return redirect(url_for('index.index'))
    return render_template('register.html', form=form)


@main.route("/logout", methods=["GET"])
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('index.index'))
