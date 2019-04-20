from rest_framework import permissions,authentication,status
from rest_framework.generics import RetrieveAPIView
from .serializers import TreatementSerializer
from departments.models import Consultation
from appointments.models import Appointment

class TreatementDetailApi(RetrieveAPIView):
    serializer_class = TreatementSerializer
    queryset = Consultation.objects.all()
    permission_classes = (permissions.IsAuthenticated,)