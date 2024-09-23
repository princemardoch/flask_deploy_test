from datetime import timedelta

from flask import Flask, session

app = Flask(__name__)

app.url_map.strict_slashes = False

app.config['SECRET_KEY'] = 'ieA6Fbj3oidmG3BYqbPZwydfAgM'

app.permanent_session_lifetime = timedelta(100)

from .user.userr import user
from .auth.authr import auth

app.register_blueprint(user, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')