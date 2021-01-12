from rest_framework.authentication import BaseAuthentication
from reglog.models import product
from rest_framework.exceptions import AuthenticationFailed
class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        name=request.GET.get("name")
        print(name)
        if name is None:
            return None

        try:
            query=product.objects.get(name=name)
        except product.DoesNotExist:
            raise AuthenticationFailed("invalid authetication")
        return (query,None)

from django.contrib.auth.models import User
class CustomAuthenticationByKey(BaseAuthentication):
    def authenticate(self, request):
        name=request.GET.get("name")
        if name is None:
            return None
        try:
            query=product.objects.get(name=name)
        except product.DoesNotExist:
            raise AuthenticationFailed("kuch to galat")
        return(query,None)



