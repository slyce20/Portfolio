from flask import Blueprint, render_template

home_bp = Blueprint('home_page', __name__, template_folder='templates')


@home_bp.route('/')
def home_page():
    return render_template('index.html')
