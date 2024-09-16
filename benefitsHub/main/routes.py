from flask import render_template, request, Blueprint
from benefitsHub.models.base_model import Benefit


main = Blueprint('main', __name__)
cover_images = [
    "{{ url_for('static', filename='assets/cover-images/cover-image_1.jpeg') }}",
    "{{ url_for('static', filename='assets/cover-images/cover-image_2.jpeg') }}",
    "{{ url_for('static', filename='assets/cover-images/cover-image_3.jpeg') }}",
    "{{ url_for('static', filename='assets/cover-images/cover-image_4.jpeg') }}",
    "{{ url_for('static', filename='assets/cover-images/cover-image_5.jpeg') }}",
    "{{ url_for('static', filename='assets/cover-images/cover-image_6.jpeg') }}",
    "{{ url_for('static', filename='assets/cover-images/cover-image_7.jpeg') }}",
    "{{ url_for('static', filename='assets/cover-images/cover-image_8.jpeg') }}",
]


@main.route("/")
@main.route("/home")
def home():
    """Home route. will serve as the landing page"""
    page = request.args.get('page', 1, type=int)
    benefits = Benefit.query.\
        order_by(Benefit.benefit_created_on.desc()).\
        paginate(page=page, per_page=6)
    return render_template('home.html', benefits=benefits)


@main.route("/about")
def about():
    return render_template('about.html', title='About', cover_images=cover_images)
