from flask import request, make_response
from functools import wraps 

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args, **kwargs)

        return make_response('Could not verify your login!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated