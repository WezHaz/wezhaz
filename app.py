from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from markupsafe import Markup
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hard to guess string'

# configure database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# db = SQLAlchemy(app)

# Initialize Flask-Bootstrap
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():  # put application's code here
    # return 'Hello World!'
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
