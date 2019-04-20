from django.urls import path
from .views import AddPatientView,StaffRegister,activate_account,ActivateAccount
app_name="profiles"
urlpatterns= [
    path('patient/add/',AddPatientView.as_view(),name="patient-register"),
    path('staff/add/',StaffRegister.as_view(),name="staff-register"),
    path('activate/<str:uidb64>/<str:token>',activate_account,name="activate")
]