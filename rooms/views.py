from django.shortcuts import render, redirect
from .models import Room, Message
from .forms import RoomForm


# Create Room View
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'rooms/create-room.html', context)


# Single Room View
def singleRoom(request, id):
    room = Room.objects.get(id=id)
    room_messages = room.message_set.all().order_by('created_at')
    participants = room.participants.all()
    
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('single-room', id=room.id)
    
    context = {
        'room': room,
        'messages': room_messages,
        'participants': participants,
    }
    return render(request, 'rooms/single-room.html', context)
