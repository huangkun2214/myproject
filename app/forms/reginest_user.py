from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,FileField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
from app.model import User,Post
from flask import flash

#注册表单
# class Reginest(FlaskForm):
#     username=StringField('账号',validators=[DataRequired(message='账号不能为空'),Length(5,8,message='说话注意分寸！')])
#     password=PasswordField('密码',validators=[DataRequired(message='密码不能为空'),EqualTo('confire')])
#     confire=PasswordField('确认密码')
#     email=StringField('邮箱',validators=[Email(message='请填写正确的邮箱')])
#     submit=SubmitField('注册')
#     def validate_username(self,username):
#         name=User.query.filter_by(username=username.data).first()
#         if name:
#             raise ValidationError('用户名字被注册了')
#     def validate_email(self,email):
#         email=User.query.filter_by(email=email.data).first()
#         if email:
#             raise ValidationError('邮箱已经存在')
class Reginest(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired(message='请填写用户名'), Length(4, 20, message='长度在4到20个字符之间')])
    email = StringField(u'邮箱(务必填写正确,否则无法激活登录)', validators=[DataRequired(message='请填写邮箱'), Email(message='请填写正确的邮箱格式')])
    password = PasswordField(u'密码', validators=[DataRequired(message='请填写密码'), Length(8, 20, message='密码长度在8到20之间'),
                                               EqualTo('confirm', message='密码不一致')])
    confirm = PasswordField(u'密码确认',validators=[DataRequired()])
    submit = SubmitField(u'注册')

    # 检验username是否存在
    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('用户名已存在')
            
    # 校验邮箱是否已存在
    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('邮箱已存在')

#登陆表单
class LoginForm(FlaskForm):
    username = StringField('用户名或邮箱', validators=[DataRequired(message='用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
    remember = BooleanField('记住我', default=True)
    submit = SubmitField('登录')


#忘记密码验证表单
class Reset_pwd1(FlaskForm):
    username=StringField('输入账号或者邮箱',validators=[DataRequired()])
    submit=SubmitField('下一步')

class Reset_pwd2(FlaskForm):
    auth_code=StringField('输入验证码',validators=[DataRequired()])
    submit=SubmitField('下一步')

class Reset_pwd3(FlaskForm):

    new_pwd=PasswordField('输入新密码',validators=[DataRequired(),EqualTo('confirm')])
    confirm=PasswordField('确认密码',validators=[DataRequired()])
    submit=SubmitField('下一步')
