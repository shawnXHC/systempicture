from rest_framework import authentication


class MyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        return True
