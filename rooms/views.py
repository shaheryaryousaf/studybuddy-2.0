from django.shortcuts import render

# Create Room View
def createRoom(request):
    return render(request, 'rooms/create-room.html')


# Single Room View
def singleRoom(request, id):
    return render(request, 'rooms/single-room.html')