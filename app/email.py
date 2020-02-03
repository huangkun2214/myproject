from flask_mail import Message
from flask import current_app,render_template
from threading import Thread
from app.extensions import mail

def ansy_send_mail(app,msg):
   with app.app_context():
       mail.send(msg)

def send_mail(to,object,templates,**kwargs):
    app=current_app._get_current_object()
    msg=Message(subject=object,sender=app.config['MAIL_USERNAME'],recipients=to)
    msg.html=render_template(templates+'.html',**kwargs)
    # msg.body=render_template(templates+'.txt',**kwargs)
    t=Thread(target=ansy_send_mail,args=[app,msg])
    t.start()