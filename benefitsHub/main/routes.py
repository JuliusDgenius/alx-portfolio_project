from flask import render_template, request, Blueprint, url_for
from benefitsHub.models.base_model import Benefit


# Create a Blueprint for the main routes
main = Blueprint('main', __name__)

# List of cover image filenames
# cover_image_files = [
#     'assets/cover-images/cover-image_1.jpeg',
#     'assets/cover-images/cover-image_2.jpeg',
#     'assets/cover-images/cover-image_3.jpeg',
#     'assets/cover-images/cover-image_4.jpeg',
#     'assets/cover-images/cover-image_5.jpeg',
#     'assets/cover-images/cover-image_6.jpeg',
#     'assets/cover-images/cover-image_7.jpeg',
#     'assets/cover-images/cover-image_8.jpeg',
# ]

# Generate valid URLs for cover images
# cover_images = [url_for('static', filename=file) for file in cover_image_files]


@main.route("/")
@main.route("/home")
def home():
    """Home route. Will serve as the landing page."""
    # Get the page number from the request arguments
    page = request.args.get('page', 1, type=int)
    
    # Query benefits, order by creation date, and paginate
    benefits = Benefit.query.\
        order_by(Benefit.benefit_created_on.desc()).\
        paginate(page=page, per_page=6)
    
    return render_template('home.html', benefits=benefits)


@main.route("/about")
def about():
    """About route. Displays information about the application."""
    return render_template('about.html', title='About', cover_images=cover_images)
