from django.shortcuts import render


# Home Page View
def index(request):
    return render(request, 'pages/index.html')
