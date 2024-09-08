from flask import current_app
from benefitsHub import db, email
from PIL import Image
import os
from flask_mail import Message
import secrets


def save_picture(form_picture):
    """Helper function to save profile pictures"""
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_extension
    picture_path = os.path.join(current_app.root_path, 'static/assets', picture_filename)

    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)

    return picture_filename

def send_reset_email(user):
    """Sends an email containing the reset token"""
    token = user.get_reset_token()
    message = Message('Password Request Reset', sender='ibejulius1@gmail.com',
                      recipients=[user.email])
    message.body = f'''Click the link below to reset your password
    {url_for('users.reset_token', token=token, _external=True)}

    If you did not make this request, simply ignore this message and no changes will be made.
    '''
    email.send(message)