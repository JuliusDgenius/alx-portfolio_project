import re
import secrets
import os
from flask_login import login_user, current_user, logout_user, login_required
from benefitsHub import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from benefitsHub.forms import RegistrationForm, LoginForm, UpdateAccountForm
from benefitsHub.models.base_model import User

# helper functions
def linkify(text):
    # Regular expression to find URLs
    url_pattern = re.compile(r'(https?://\S+)')

    # Replace URLs with clickable links
    return url_pattern.sub(r'<a href="\1" target="_blank">\1</a>', text)


benefits = [
    {'id': 1,
     'name': 'Npower',
     'date_posted': 'August 28, 2024',
     'end_date': 'August 28, 2024',
     'description': 'Npower description',
     'eligibility': 'Npower requirement',
     'image': '../static/assets/npower2.jpeg',
     'link': 'https://npower-fmhds-gov-ng.web.app/',
    },
    {'id': 2,
     'name': '3MTT',
     'date_posted': 'August 28, 2024',
      'end_date': 'August 28, 2024',
     'description': '3MTT description',
     'requirement': '3MTT requirement',
     'image': '../static/assets/3mtt.jpeg',
     'link': 'https://3mtt.nitda.gov.ng/',
    },
    {'id': 3,
     'name': 'Student Loan',
     'date_posted': 'August 28, 2024',
      'end_date': 'August 28, 2024',
     'description': 'Student Loan description',
     'requirement': 'Student Loan requirement',
     'image': '../static/assets/student_loan.jpeg',
     'link': 'https://portal.nelf.gov.ng/',
    },
    {'id': 4,
     'name': 'Presidential Conditional\
Grant Scheme (PCGS)',
     'date_posted': 'August 28, 2024',
     'end_date': 'August 28, 2024',
     'description': 'Micro grants description',
     'requirement': 'NIN is a major requirement for the Federal Government Grants and Loans Scheme. Loan applicants who have already filled the form should simply log in and update their loan application with their NIN. Grants Applicants, who already filled the form, should update their NIN by clicking this link: https://grant.fedgrantandloan.gov.ng/auth/nin/register',
     'image': '../static/assets/palliative_grant.jpeg',
     'link': 'https://www.fedgrantandloan.gov.ng/',
    },
    {'id': 4,
     'name': 'Presidential Conditional\
Grant Scheme (PCGS)',
     'date_posted': 'August 28, 2024',
     'end_date': 'August 28, 2024',
     'description': 'Micro grants description',
     'requirement': 'Micro grants requirement',
     'image': '../static/assets/palliative_grant.jpeg',
     'link': 'https://www.fedgrantandloan.gov.ng/',
    },
    {'id': 4,
     'name': 'Presidential Conditional\
Grant Scheme (PCGS)',
     'date_posted': 'August 28, 2024',
     'end_date': 'August 28, 2024',
     'description': 'Micro grants description',
     'requirement': 'Micro grants requirement',
     'image': '../static/assets/palliative_grant.jpeg',
     'link': 'https://www.fedgrantandloan.gov.ng/',
    },
    {'id': 4,
     'name': 'Presidential Conditional\
Grant Scheme (PCGS)',
     'date_posted': 'August 28, 2024',
     'end_date': 'August 28, 2024',
     'description': 'Micro grants description',
     'requirement': 'Micro grants requirement',
     'image': '../static/assets/palliative_grant.jpeg',
     'link': 'https://www.fedgrantandloan.gov.ng/',
    },
    {'id': 4,
     'name': 'Presidential Conditional\
Grant Scheme (PCGS)',
     'date_posted': 'August 28, 2024',
     'end_date': 'August 28, 2024',
     'description': 'Micro grants description',
     'requirement': 'Micro grants requirement',
     'image': '../static/assets/palliative_grant.jpeg',
     'link': 'https://www.fedgrantandloan.gov.ng/',
    },
]

for benefit in benefits:
    for key, value in benefit.items():
        if key == "requirement" or key == "description":
            value = linkify(value)
        benefit[key] = value

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', benefits=benefits)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/explore_benefits")
def explore_benefits():
    return render_template('explore_benefits.html', benefits=benefits, title='Explore Benefits')

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {user.username}! Your account has been created successfully! You can now login to see all your benefits.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    """Helper function to save profile pictures"""
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_extension
    picture_path = os.path.join(app.root_path, 'static/assets', picture_filename)
    form_picture.save(picture_path)

    return picture_filename

@app.route('/account', methods=["GET", "POST"])
@login_required # login is required to access this route.
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.update_picture.data:
            picture_file = save_picture(form.update_picture.data)
            current_user.profile_pic = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_pic = url_for('static', filename='assets/' + current_user.profile_pic)
    return render_template('account.html', title='Account', profile_pic=profile_pic, form=form)