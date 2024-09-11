from flask import current_app
import re
import os
import secrets
from PIL import Image


# helper functions
def linkify(text):
    """
    Helper function to find URLs in text and turn them into clickable links
    """
    url_pattern = re.compile(r'(https?://\S+)')

    return url_pattern.sub(r'<a href="\1" target="_blank">\1</a>', text)


def save_picture(form_picture):
    """Helper function to save profile pictures"""
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_extension
    picture_path = os.path.join(current_app.root_path,
                                'static/uploads', picture_filename)

    output_size = (150, 150)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)

    return picture_filename
