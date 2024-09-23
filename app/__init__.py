from datetime import timedelta
import secrets

from flask import Flask, session

app = Flask(__name__)

app.url_map.strict_slashes = False

app.config['SECRET_KEY'] = secrets.token_urlsafe(30)
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

@app.before_request
def make_session_permanent():
    session.permanent = True

from .user.userr import user
from .auth.authr import auth

app.register_blueprint(user, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')