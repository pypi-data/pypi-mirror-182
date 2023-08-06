from functools import wraps

from ..exceptions.unauthorized_exception import UnauthorizedException


def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwa):
        if not args[0].ctx.current_user:
            raise UnauthorizedException()

        return f(*args, **kwa)
    return decorated_function
