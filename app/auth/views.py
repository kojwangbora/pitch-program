from flask import render_template, redirect, url_for, flash
from .forms import Register,LoginForm
from . import auth
from ..models import User
from .. import db
from flask_login import login_user,logout_user, current_user, login_required
from ..email import mail_message

@auth.route('/register', methods = ['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        user = User(username= form.username.data,email = form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login')

       # mail_message('Welcome to talky pitch Application','email/welcome', user.email, user=user)

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form = form)


@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            # next = request.args.get('next')
            # if next is None or not next.startswith('/'):
            #     next = url_for('main.pitches')
            return redirect(url_for('main.pitches'))
        flash('Invalid username or password')
    return render_template('auth/login.html',form = form)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))