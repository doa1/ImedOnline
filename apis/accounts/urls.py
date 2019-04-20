from django.urls import path
from .views import *
app_name ='accounts'
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',LoginApi.as_view(),name='login'),
    path('logout/',LogoutApi.as_view(), name="logout")
]