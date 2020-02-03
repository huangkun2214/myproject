from flask import  Blueprint,redirect,render_template,request,url_for,flash
from app.forms.reginest_user import Reginest,LoginForm,Reset_pwd1,Reset_pwd2,Reset_pwd3
from app.model import User
from sqlalchemy import or_
from flask_login import login_user,current_user,logout_user
from app.extensions import db
from app.utils import random_string
from app.email import send_mail
# user=Blueprint('user',url_prefix='/user')
users=Blueprint('users',__name__)

@users.route('/reginest/',methods=['POST','GET'])
def reginest():
    form=Reginest()

    if form.validate_on_submit():

        user=User(username=form.username.data,password=form.password.data,email=form.email.data)
        print(1)
        db.session.add(user)
        db.session.commit()
        send_mail([user.email],'激活账户','users/mail_active',username=user.username)
        flash('注册成功！')
        return redirect(url_for('users.login'))

    return render_template('users/reginest.html',form=form)

@users.route('/login/',methods=['POST','GET'])
def login():
    form = LoginForm()
    username = form.username.data
    # print(form.validate_on_submit())
    if form.validate_on_submit():
        username = form.username.data

        user = User.query.filter(or_(User.username == username, User.email == username)).first()
        print(username + '0')
        if not user:
            print(username+'1')
            flash('用户名或密码错误')
        elif not user.confirm:
            print(username + '2')
            flash('用户未被激活,请先激活在登录')

        elif not user.verify_password(form.password.data):
            print(username + '3')
            flash('用户名或密码错误 ')
        else:
            print(username + '4')
            login_user(user, remember=form.remember.data)
            flash('登录成功')

            return redirect(url_for('main1.index'))
    return render_template('users/login.html', form=form)


@users.route('/reset_password1/',methods=['POST','GET'])
def reset_password1():
    form=Reset_pwd1()
    if form.validate_on_submit():
        global authcode
        authcode=random_string(length=6)

        user=User.query.filter(or_(User.username==form.username.data,User.email==form.username.data)).first()
        if user:
            global uname
            uname=user.username
            send_mail([user.email],'验证码','users/mail_auth',username=user.username,authcode=authcode)
            flash('验证码已经发送')
            return redirect(url_for('users.reset_password2',))
        else:
            flash('没有此用户！')
    return render_template('users/reset_pwd1.html',form=form)

#验证码判断
@users.route('/reset_password2',methods=['POST','GET'])
def reset_password2():
    form=Reset_pwd2()
    if form.validate_on_submit():
        if form.auth_code.data==authcode:
            flash('验证成功！')
            return redirect(url_for('users.reset_password3'))
    # if form.validate_on_submit():

    return render_template('users/reset_pwd2.html',form=form)

@users.route('/reset_password3',methods=['POST','GET'])
def reset_password3():
    form=Reset_pwd3()
    if form.validate_on_submit():
        user=User.query.filter(or_(uname==User.email,uname==User.username)).first()
        user.password=form.new_pwd.data
        db.session.add(user)
        db.session.commit()
        logout_user()
        return redirect(url_for('users.reset_password4'))

    return render_template('users/reset_pwd3.html',form=form)

@users.route('/reset_password4',methods=['POST','GET'])
def reset_password4():
    return render_template('users/reset_pwd4.html')


#激活账户
@users.route('/mail_active/<username>',methods=['POST','GET'])
def mail_active(username):
    user=User.query.filter(User.username==username).first()
    print(user.confirm)
    if not user.confirm:
        user.confirm=True
        db.session.add(user)
        db.session.commit()
    return '激活成功！'

