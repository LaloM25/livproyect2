from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def flower_view(request):
    return render(request, 'flower_index.html')