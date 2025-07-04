from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from users.models import User

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('jwt-auth') # jwt token

        if not token:
            return None
        
        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user_id = decoded.get('id')

            if not user_id:
                raise AuthenticationFailed('Invalid Token')

            user = User.objects.get(id=user_id)
            return (user, None)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('token has expired')
        except jwt.DecodeError:
            raise AuthenticationFailed('error decoding token')
        except User.DoesNotExist:
            raise AuthenticationFailed('user not found')