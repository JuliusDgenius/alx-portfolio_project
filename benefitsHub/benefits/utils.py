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
    if not file_extension:
        print(f"Error: Not a valid file extension", flush=True)
        return None
    picture_filename = random_hex + file_extension
    picture_path = os.path.join(current_app.root_path,
                                'static/uploads', picture_filename)
    print(f"Saving picture to: {picture_path}", flush=True)

    output_size = (150, 150)
    try:
        image = Image.open(form_picture)
    except Exception as e:
        print(f"Error opening file {e}", flush=True)
    image.thumbnail(output_size)
    try:
        image.save(picture_path)
    except Exception as e:
        print(f"Error saving picture", flush=True)

    return picture_filename
