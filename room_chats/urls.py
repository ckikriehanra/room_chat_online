from django.urls import path
from . import views

"""Define URL for app: room_chats"""

app_name = 'room_chats'

urlpatterns = [ 
    path('', views.home, name='home'),
    path('checkview', views.checkview, name='checkview'),
    path('<str:room>/', views.room, name='room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]