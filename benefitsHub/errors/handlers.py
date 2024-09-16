# Import necessary modules from Flask
from flask import Blueprint, render_template

# Create a Blueprint for error handling
errors = Blueprint('errors', __name__)

# Error handler for 404 Not Found
@errors.app_errorhandler(404)
def error_404(error):
    """Custom 404 error handler"""
    # Render the 404 error template and return with 404 status code
    return render_template('errors/404.html'), 404

# Error handler for 403 Forbidden
@errors.app_errorhandler(403)
def error_403(error):
    """Custom 403 error handler"""
    # Render the 403 error template and return with 403 status code
    return render_template('errors/403.html'), 403

# Error handler for 500 Internal Server Error
@errors.app_errorhandler(500)
def error_500(error):
    """Custom 500 error handler"""
    # Render the 500 error template and return with 500 status code
    return render_template('errors/500.html'), 500
