
import os
import jwt
from ..exceptions.unauthorized_exception import UnauthorizedException
from decouple import config


def current_user(request):
    if request.headers.get('authorization'):
        bearer_token = request.headers.get('authorization')
        token = bearer_token.split()[1]

        try:
            payload = jwt.decode(token, os.environ.get(
                "JWT_SECRET_KEY", config('JWT_SECRET_KEY')), 'HS256')
            request.ctx.current_user = payload['sub']
        except:
            raise UnauthorizedException()
