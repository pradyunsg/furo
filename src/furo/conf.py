from sphinx.application import Sphinx

def setup(app: Sphinx):
    app.add_js_file("rate-the-docs.min.js")
