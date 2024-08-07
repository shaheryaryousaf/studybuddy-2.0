from django.shortcuts import render
from rooms.models import Room, Category


# Home Page View
def index(request):
    rooms = Room.objects.all()
    categories = Category.objects.all()
    context = {
        'rooms': rooms,
        'categories': categories,
    }
    return render(request, 'pages/index.html', context)
