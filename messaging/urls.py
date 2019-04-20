from .views import message_list,MessageList,message_view,chat_view
from django.urls import path
app_name='messaging'
urlpatterns = [
    path('', chat_view, name='chats'),

    path('messages/<int:sender>/<int:receiver>/', message_view, name='chat'),
# URL form : "/api/messages/1/2"
    path('api/messages/<int:sender>/<int:receiver>/',message_list,name='message_detail'),
    # URL form : "/api/messages/"
    path('api/messages/',message_list,name='message_list'),
]
