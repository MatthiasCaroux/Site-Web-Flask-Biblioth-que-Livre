from flask import Flask
from flask_bootstrap import Bootstrap
from flask import request, render_template, redirect, url_for



app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SECRET_KEY'] = "58e3a937-6c81-446b-8bca-71a4f6a844bc"
bootstrap = Bootstrap(app)


import os.path


def mkpath(p):
    print()
    return os.path.normpath(os.path.join(os.path.dirname(__file__), p))

from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)



from flask_login import LoginManager
login_manager = LoginManager(app)
login_manager.login_view = "login"