import re
from benefitsHub import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from benefitsHub.forms import RegistrationForm, LoginForm
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
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@benefitshub.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)