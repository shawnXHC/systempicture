from django.urls import re_path
from myapp import views
from rest_framework import routers
# 可以结合routers使用，结合viewset


urlpatterns = [
    re_path('users/', views.UserList.as_view()),
    re_path('powers/',views.Test.as_view())
]

# router = routers.SimpleRouter()
# router.register()
#
# urlpatterns += router.urls
