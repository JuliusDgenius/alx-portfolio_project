from benefitsHub import create_app
from markupsafe import Markup

app = create_app()

@app.template_filter('nl2br')
def nl2br_filter(s):
    return Markup(s.replace('\n', '<br>\n'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
