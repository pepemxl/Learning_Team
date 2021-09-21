from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .auth import token_required
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    #return 'Index'
    return render_template('index.html')

@main.route('/profile')
#@login_required
@token_required
def profile():
    #return 'Profile'
    return render_template('profile.html', name=current_user.name)
