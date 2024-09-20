"""
This module defines the utils for the application.
"""
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
    if not form_picture:
        return None

    # Generate a random filename
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.splitext(form_picture.filename)
    
    # Check if the file has a valid extension
    if not file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        print(f"Invalid file extension: {file_extension}", flush=True)
        return None

    picture_filename = random_hex + file_extension
    picture_path = os.path.join(current_app.root_path,
                                'static', 'post_uploads', picture_filename)

    output_size = (512, 512)
    try:
        with Image.open(form_picture) as image:
            image.thumbnail(output_size)
            image.save(picture_path)
    except Exception as e:
        print(f"Error processing image: {e}", flush=True)
        return None

    return picture_filename
