from flask import request, make_response
from functools import wraps
from utils.htpasswd import HtpasswdFile


def auth_required(htpasswd_obj, enable=False):
    def inner_decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if enable:
                auth = request.authorization
                if auth and htpasswd_obj.user_is_valid(auth.username, auth.password):
                    return f(*args, **kwargs)
                return make_response('Could not verify your login!', 401,
                                     {'WWW-Authenticate': 'Basic realm="Login Required"'})
            else:
                return f(*args, **kwargs)

        return decorated

    return inner_decorator
