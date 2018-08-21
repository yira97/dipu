from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError, Length, EqualTo

from app.models.user import User


class BaseUserForm(FlaskForm):
    username = StringField(label=u'用户名',
                           validators=[DataRequired(u'请输入用户名'), Length(min=4, max=25)],
                           render_kw={
                               "class": "form-control",
                               "placeholder": "username",
                               "required": 'required'
                           })
    password = PasswordField(label=u'密码',
                             validators=[DataRequired(u'请输入密码'), Length(min=4, max=25)],
                             render_kw={
                                 "class": "form-control",
                                 "placeholder": "password",
                                 "required": 'required'
                             })
    submit = SubmitField(
        label=u"提交",
        render_kw={
            "class": "btn btn-secondary btn-block btn-flat",
        }
    )


class RegistrationForm(BaseUserForm):
    confirm = PasswordField(label=u'确认密码',render_kw={
                                 "class": "form-control",
                                 "placeholder": "confirm",
                                 "required": 'required'
                             }, validators=[
        DataRequired(),
        EqualTo('password', message=u'密码必须一致')
    ])
    email = EmailField(label="邮箱", validators=[DataRequired('请输入邮箱'), Email('邮箱格式不正确')],
                       description="邮箱",
                       render_kw={
                           "class": "form-control",
                           "placeholder": "email",
                           "required": 'required',
                       },)

    accept_tos = BooleanField(label=u'我接受以上条款', validators=[DataRequired()])


    def validate_username(self,filed):
        username = filed.data
        if User.objects(username=username).first() is not None:
            raise ValidationError("用户名已经存在")


class LoginForm(BaseUserForm):
    remember = BooleanField(label=u'记住登录', validators=[DataRequired()])


class AddTopic(FlaskForm):
    title = StringField(label=u'标题', validators=[DataRequired(), Length(min=4, max=25)])
    content = StringField(label=u'内容', validators=[DataRequired(), Length(min=4, max=2500)])
    submit = SubmitField(
        label=u"提交",
        render_kw={
            "class": "btn btn-secondary btn-block btn-flat",
        }
    )
