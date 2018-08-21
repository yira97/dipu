from functools import wraps

from flask import session, redirect, url_for

from app.models.user import User


def current_user():
    username = session.get('username', '-1')
    u = User.objects(username=username).first()
    return u


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get('username'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return decorated_function
