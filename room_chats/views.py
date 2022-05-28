from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Message, Room

# Create your views here.
def home(request):
    """Home page"""
    return render(request, 'room_chats/home.html')

def room(request, room):
    """Room page"""
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    context = {
        'username': username,
        'room': room,
        'room_details': room_details
    }
    return render(request, 'room_chats/room.html', context)

def checkview(request):
    """Find right room."""
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect(reverse('room_chats:room', kwargs={'room':room}) 
        +'?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect(reverse('room_chats:room', kwargs={'room':room}) 
        +'?username='+username)
    
def send(request):
    """Send messages."""
    if request.method == 'POST':
        message = request.POST['message']
        username = request.POST['username']
        room_id = request.POST['room_id']

        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()
        return HttpResponse('Message sent successfully')
    else:
        return redirect(reverse('room_chats:room', kwargs={'room':room}) 
        +'?username='+username)
    
def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})



