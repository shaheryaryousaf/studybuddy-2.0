from django.shortcuts import render
from rooms.models import Room, Category, Message
from django.db.models import Q


# Home Page View
def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    ).order_by('-created_at')
    categories = Category.objects.all()
    recent_activity = Message.objects.filter(
        Q(room__category__name__icontains=q)).order_by('-created_at')[:3]
    context = {
        'rooms': rooms,
        'categories': categories,
        'activity': recent_activity
    }
    return render(request, 'pages/index.html', context)
