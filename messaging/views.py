from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status,permissions
from rest_framework.views import APIView
from .serializers import MessageSerializer
from .models import Messages
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
User =get_user_model()
# Create your views here.
def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('homepage:index')
    if request.method == "GET":
        return render(request, 'chatting/chat.html',
                      {'users': User.objects.exclude(email=request.user.email)})

def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('homepage:index')
    if request.method == "GET":
        return render(request, "chatting/messages.html",
                      {'users': User.objects.exclude(email=request.user.email),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Messages.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Messages.objects.filter(sender_id=receiver, receiver_id=sender)})
class MessageList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def dispatch(self, request, *args, **kwargs):
        self.sender = kwargs['sender']
        self.receiver = kwargs['receiver']
        return super().dispatch(request,*args,**kwargs)
    def get(self,request,format=None,sender=None,receiver=None):
        messages = Messages.objects.filter(sender_id=sender,receiver_id=receiver)
        serializer = MessageSerializer(messages,many=True,context={'request':request})
        #mark the messages as read
        for message in messages:
            message.is_read=True
            message.save()
        return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
    def post(self,request):
        data =JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=True,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def message_list(request,sender=None,receiver=None):
    if request.method == 'GET':
        messages = Messages.objects.filter(sender_id=sender,receiver_id=receiver)
        serializer = MessageSerializer(messages,many=True,context={'request':request})
        return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
    elif request.method == "POST":
        data= JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)