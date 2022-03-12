from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject, template, to, **kwags):
  sender_email = 'flasky.pitch@gmail.com'
  msg = Message(subject, sender=sender_email, recipients=[to])
  msg.body = render_template(template + '.txt', **kwags)
  msg.html = render_template(template + '.html', **kwags)
  mail.send(msg)