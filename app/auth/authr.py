from flask import Blueprint, render_template, redirect, url_for, request, session

auth = Blueprint('auth', __name__)

@auth.before_request
def verif_not_login():
    if session.get('user_is_login') and request.endpoint == 'auth.login':
        return redirect(url_for('user.islogin'))

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'test' and password == 'test':
            session['user_is_login'] = True
            return redirect(url_for('user.islogin'))
    return render_template('login.html')
