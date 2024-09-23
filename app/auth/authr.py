from flask import Blueprint, render_template, redirect, url_for, request, session

auth = Blueprint('auth', __name__)

@auth.before_request
def verif_login():
    # Rediriger vers la page de login si l'utilisateur n'est pas connecté
    if not session.get('user_is_login') and request.endpoint != 'auth.login':
        return redirect(url_for('auth.login'))

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'test' and password == 'test':
            session['user_is_login'] = True
            return redirect(url_for('user.islogin'))
    return render_template('login.html')
