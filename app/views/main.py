from flask import Blueprint,request
from flask import render_template,current_app
from flask_login import current_user
from app.forms.post import PostsForm
from app.forms.reginest_user import Reginest
from app.model.users import User,Post
from app.extensions import db,IMAGES,photos
import os
from PIL import Image
from app.utils import random_string

main1=Blueprint('main1',__name__)
@main1.route('/main1',methods=['POST','GET'])
def index():
    # form=Reginest()
    form=PostsForm()
    print(form.contend.data)
    print(form.category.data)
    print((form.pic.data))

    if form.validate_on_submit():
       if current_user.is_authenticated:
           print(current_user.get_id())
           return 'dsadas11112233344'
       else:
           return 'ssss'

    return render_template('users/main/main.html',form=form)
    # return render_template('users/reginest.html', form=form)

