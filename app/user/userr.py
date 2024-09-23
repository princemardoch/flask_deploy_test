from flask import Blueprint, render_template, redirect, url_for, request, session

user = Blueprint('user', __name__)

@user.before_request
def verif_login():
    if session.get('user_is_login') is None and request.endpoint != 'auth.login':
        return redirect(url_for('auth.login'))

@user.route('/')
def home():
    return redirect(url_for('user.islogin'))

@user.route('/success')
def islogin():
    return render_template('index.html')


@user.route('/clear_session', methods=['GET', 'POST'])
def clear_session():
    if request.method == 'POST':
        session.clear()
    return redirect(url_for('user.islogin'))