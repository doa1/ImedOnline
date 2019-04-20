from rest_framework import serializers
from .models import Messages
from django.contrib.auth import get_user_model
Users = get_user_model()
class MessageSerializer(serializers.ModelSerializer):
    '''for serializing the messages'''
    sender =serializers.SlugRelatedField(many=False,slug_field='identity',queryset=Users.objects.all())
    receiver = serializers.SlugRelatedField(many=False,slug_field='identity',queryset=Users.objects.all())
    '''The sender and receiver of Message is serialized as SlugRelatedField to represent the target of the relationship 
    using a field on the target. The field is specified as slug_field. It also takes a 'many' argument which identifies 
    the relation is many-to-many or not. We gave it false, since a message can only contain a single sender and receiver.
    The 'queryset' argument takes the list of objects from which the related object is to be chosen.'''
    class Meta:
        model = Messages
        fields = ['sender','receiver','message','created']
