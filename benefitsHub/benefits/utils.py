# helper functions
def linkify(text):
    """Helper function to find URLs in text and turn them into clickable links"""
    # Regular expression to find URLs
    url_pattern = re.compile(r'(https?://\S+)')

    # Replace URLs with clickable links
    return url_pattern.sub(r'<a href="\1" target="_blank">\1</a>', text)