from django.urls import path
from .views import MakeAppointment

urlpatterns=[
    path('create/',MakeAppointment.as_view(),name="create-appointment"),
]