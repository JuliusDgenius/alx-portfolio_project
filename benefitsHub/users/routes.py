"""Routes for the users module"""
from flask import (render_template, url_for, flash, redirect, request,
                   Blueprint)
from benefitsHub import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from benefitsHub.models.base_model import User, Post
from benefitsHub.users.forms import (RegistrationForm, LoginForm,
                                     UpdateAccountForm, RequestResetForm,
                                     ResetPasswordForm)
from benefitsHub.users.utils import save_picture, send_reset_email


users = Blueprint('users', __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    """
    Route to register a new user.
    
    GET: Displays the registration form.
    POST: Processes the form submission, creates a new user, and redirects to login.
    """
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
            .decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {user.username}!\
              Your account has been created successfully!\
              You can now login to see all your benefits.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    """
    Route to log in a user.
    
    GET: Displays the login form.
    POST: Authenticates the user and redirects to home or next page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else\
                redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password',
                  'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    """Route to log out the current user."""
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=["GET", "POST"])
@login_required  # login is required to access this route.
def account():
    """
    Route to update the user's account information.
    
    GET: Displays the account update form.
    POST: Processes the form submission and updates the user's information.
    """
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.update_picture.data:
            picture_file = save_picture(form.update_picture.data)
            current_user.profile_pic = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_pic = url_for('static', filename='assets/'
                          + current_user.profile_pic)
    return render_template('account.html', title='Account',
                           profile_pic=profile_pic, form=form)


@users.route("/user/<string:username>")
def user_posts(username):
    """
    Route to view a specific user's posts.
    
    Displays paginated posts for the given username.
    """
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user.username)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


@users.route('/reset_password', methods=["GET", "POST"])
def reset_request():
    """
    Route to request a password reset.
    
    GET: Displays the password reset request form.
    POST: Processes the form and sends a reset email if valid.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("An email has been sent with your password reset token. "
              "Use within 30 minutes.", 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password',
                           form=form)


@users.route('/reset_password/<token>', methods=["GET", "POST"])
def reset_token(token):
    """
    Route to reset password using a token.
    
    GET: Displays the password reset form.
    POST: Processes the form and updates the user's password if valid.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if not user:
        flash("That is an invalid or expired token", 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)\
            .decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Welcome {user.username}!\
              Your password has been updated successfully!\
              You can now login to see all your benefits.', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password',
                           form=form)
