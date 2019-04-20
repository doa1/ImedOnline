from rest_framework import serializers
from departments.models import Consultation
from appointments.models import Appointment

class TreatementSerializer(serializers.ModelSerializer):
    sickness_category =serializers.CharField(source="get_sickness_category_display")
    sickness_period = serializers.CharField(source="get_sickness_period_display")
    class Meta:
        model = Consultation
        fields = ['doctor','appointment','hospital','new_patient','sickness_category', 'sickness_period', 'symptoms', 'other_info', 'previous_medication', 'image',
                  'audio_clip', 'video_clip','disease','results','drugs','prescription','diatery_advice','medical_advice']
        #there are foreign keys pointing to other models,tell serializer to fetch these too
        depth=1