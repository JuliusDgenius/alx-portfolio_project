"""Utility functions for the users module"""
from flask import current_app, url_for
from benefitsHub import db, email
from PIL import Image
import os
from flask_mail import Message
import secrets


def save_picture(form_picture):
    """
    Helper function to save profile pictures
    
    Args:
        form_picture: The uploaded picture file from the form

    Returns:
        str: The filename of the saved picture
    """
    # Generate a random hex string for the filename
    random_hex = secrets.token_hex(8)
    # Split the filename and extension
    _, file_extension = os.path.splitext(form_picture.filename)
    # Create the new filename
    picture_filename = random_hex + file_extension
    # Generate the full path to save the picture
    picture_path = os.path.join(current_app.root_path, 'static/assets',
                                picture_filename)

    # Set the output size for the image thumbnail
    output_size = (125, 125)
    # Open the image using PIL
    image = Image.open(form_picture)
    # Create a thumbnail of the image
    image.thumbnail(output_size)
    # Save the thumbnail
    image.save(picture_path)

    return picture_filename

def send_reset_email(user):
    """
    Sends an email containing the reset token
    
    Args:
        user: The user object for whom the reset email is being sent
    """
    # Generate a reset token for the user
    token = user.get_reset_token()
    # Create a Message object for the email
    message = Message('Password Request Reset', sender='ibejulius1@gmail.com',
                      recipients=[user.email])
    # Set the body of the email message
    message.body = f'''Click the link below to reset your password
    {url_for('users.reset_token', token=token, _external=True)}

    If you did not make this request,
    simply ignore this message and no changes will be made.
    '''
    # Send the email
    email.send(message)
