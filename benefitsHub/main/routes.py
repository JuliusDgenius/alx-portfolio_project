from flask import render_template, url_for, flash, redirect, request, Blueprint, current_app
from flask_login import login_user, current_user, logout_user, login_required
from benefitsHub.models.base_model import Benefit



main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """Home route. will serve as the landing page"""
    page = request.args.get('page', 1, type=int)
    benefits = Benefit.query.order_by(Benefit.benefit_created_on.desc()).paginate(page=page, per_page=6)
    return render_template('home.html', benefits=benefits)


@main.route("/about")
def about():
    return render_template('about.html', title='About')