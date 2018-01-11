"""
WeListen website index (home page) view.

URLs include:
/
"""
import flask
import welisten


@welisten.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template("index.html", **context)
