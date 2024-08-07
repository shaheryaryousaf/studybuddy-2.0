from django.shortcuts import render, redirect
from .models import Room
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
    context = {
        'room': room,
    }
    return render(request, 'rooms/single-room.html', context)
