from datetime import timedelta
import secrets

from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_urlsafe(30)
app.permanent_session_lifetime = timedelta(100)

from .user.userr import user
from .auth.authr import auth

app.register_blueprint(user, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')