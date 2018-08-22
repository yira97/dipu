from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from mongoengine import IntField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, TextAreaField, FileField
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
    confirm = PasswordField(label=u'确认密码', render_kw={
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
                       }, )

    accept_tos = BooleanField(label=u'我接受以上条款', validators=[DataRequired()])

    def validate_username(self, filed):
        username = filed.data
        if User.objects(username=username).first() is not None:
            raise ValidationError("用户名已经存在")


class LoginForm(BaseUserForm):
    remember = BooleanField(label=u'记住登录', validators=[DataRequired()])


class AddTopicForm(FlaskForm):
    title = StringField(label=u'标题', validators=[DataRequired('请输入标题'), Length(min=4, max=25)], description="标题",
                        render_kw={
                            "class": "form-control",
                            "placeholder": "title",
                            "required": 'required',
                            "aria - label": "Sizing example input",
                            "aria - describedby": "inputGroup-sizing-default"
                        }, )
    content = TextAreaField(label=u'内容', validators=[DataRequired('请输入内容'), Length(min=4, max=2500)], description="内容",
                            render_kw={
                                "class": "form-control",
                                "placeholder": "content",
                                "required": 'required',
                                "aria - label": "With textarea",
                                "rows": "20"
                            }, )
    submit = SubmitField(label=u"提交", render_kw={"class": "btn btn-secondary btn-block btn-flat", })


class AddSelfieForm(FlaskForm):
    image = FileField(label=u'文件', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'gif'],
                                                                           message=u'jpg/png/jpeg/gif allowed!')])
    submit = SubmitField(label=u"提交", render_kw={"class": "btn btn-secondary btn-block  btn-flat","style":"margin-top:1em"})




    # floor = db.IntField(default=0)  # 回复的楼层，0代表楼主
    # replyed_user = db.StringField(default='')  # 被回复的人
    # content = db.StringField(default='')  # 回复的内容
    # block = db.BooleanField(default=False)  # 状态
class ReplyForm(FlaskForm):
    floor = IntField(FileRequired())
    content = StringField(FileRequired())
