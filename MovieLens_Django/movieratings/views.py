from django.shortcuts import render

from movieratings.models import Item

# Create your views here.


def index_view(request):
    context = {
    }
    return render(request, 'index.html', context)


def top_20_view(request):
    context = {
        "all_movies": Item.objects.all()
    }
    return render(request, 'top_20.html', context)


def all_movies_view(request):
    context = {
        "all_movies": Item.objects.all()
    }
    return render(request, 'all_movies.html', context)


def raters_view(request):
    context = {
    }
    return render(request, 'raters.html', context)
