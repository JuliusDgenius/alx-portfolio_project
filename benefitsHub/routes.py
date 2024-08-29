from benefitsHub import app
from flask import render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = 'fdf898181ba60d610301084df980e442'

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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
