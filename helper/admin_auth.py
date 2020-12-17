from werkzeug.exceptions import HTTPException
from flask import Response, redirect
from flask_admin.contrib.sqla import ModelView

from app import auth


class AuthException(HTTPException):
    """
    class raise error when admin authentication is failed
    """

    def __init__(self, message):
        super().__init__(
            message,
            Response(
                "You could not be authenticated. Please Go Back",
                401,
                {"WWW-Authenticate": 'Basic realm="Login Required"'},
            ),
        )


class Authenticate(ModelView):
    """
    class override the class Modelview for authentication
    """

    def is_accessible(self):
        if not auth.authenticate():
            raise AuthException("Not authenticated.")
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(auth.challenge())
