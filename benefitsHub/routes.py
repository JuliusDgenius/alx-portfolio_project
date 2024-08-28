from benefitsHub import app
from flask import render_template, url_for

benefits = [
    {'id': 1,
     'name': 'Npower',
     'description': 'Npower description',
     'requirement': 'Npower requirement',
     'image': '../static/images/npower.jpeg',
     'link': 'https://npower-fmhds-gov-ng.web.app/',
    },
    {'id': 2,
     'name': 'Npower',
     'description': 'Npower description',
     'requirement': 'Npower requirement',
     'image': '../static/images/npower.jpeg',
     'link': 'https://npower-fmhds-gov-ng.web.app/',
    },
    {'id': 3,
     'name': 'Npower',
     'description': 'Npower description',
     'requirement': 'Npower requirement',
     'image': '../static/images/npower.jpeg',
     'link': 'https://npower-fmhds-gov-ng.web.app/',
    },
    {'id': 4,
     'name': 'Npower',
     'description': 'Npower description',
     'requirement': 'Npower requirement',
     'image': '../static/images/npower.jpeg',
     'link': 'https://npower-fmhds-gov-ng.web.app/',
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/explore_benefits")
def explore_benefits():
    return render_template('explore_benefits.html')

@app.route("/register")
def register():
    return render_template('register.html')
