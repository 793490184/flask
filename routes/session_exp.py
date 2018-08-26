from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    session,
)


main = Blueprint('session', __name__)


@main.route('/')
def index():
    username = session.get("username", None)
    if username is None:
        return render_template('login.html')
    else:
        return render_template('session_index.html', username=username)

