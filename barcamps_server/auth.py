from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import jwt
import os

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """ Custom auth using JWT
        """
        authorization_header = request.META.get("HTTP_AUTHORIZATION")

        if not authorization_header:
            return None # not authenticated

        # decode the jwt
        user_jwt = authorization_header.split()[1]
        payload = jwt.decode(user_jwt, os.environ.get('JWT_SECRET'), algorithms=['HS256'])

        try:
            user = User.objects.get(email=payload['email'])
        except Exception:
            return None # can't find user => not authenticated

        return (user, None)
