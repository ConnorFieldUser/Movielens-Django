
from django.shortcuts import render

from movieratings.models import Item, Rater

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


def movie_page_view(request, item_id):
    context = {
        "movie": Item.objects.get(id=item_id)
    }
    return render(request, 'movie_page.html', context)


def raters_view(request):
    context = {
        "all_raters": Rater.objects.all()
    }
    return render(request, 'all_raters.html', context)
