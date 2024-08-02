from django.shortcuts import render
from rooms.models import Room


# Home Page View
def index(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'pages/index.html', context)
