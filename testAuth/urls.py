from django.urls import path
from apis.test_auth.views import *

urlpatterns =[
    path('', TestAuthView.as_view(), name='test_auth', ),
    path('logout/', LogoutViewEx.as_view(), name='rest_logout', ),
    path('login/', LoginView.as_view(), name='rest_login', ),
    path('home/', HomeTemplateView.as_view(), name='home', ),
]