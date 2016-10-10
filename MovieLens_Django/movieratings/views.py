
from django.shortcuts import render

from movieratings.models import Item, Rater

# Create your views here.


def index_view(request):
    context = {
    }
    return render(request, 'index.html', context)


def top_20_view(request):
    context = {
        "all_movies": Item.objects.all()[:20]
    }
    return render(request, 'top_20.html', context)


def all_movies_view(request):
    context = {
        "all_movies": Item.objects.all()
    }
    return render(request, 'all_movies.html', context)


def movie_page_view(request, item_id):
    context = {  # possibly deceptive var names here
        "title_finder": Item.objects.all(),
        "movie": Item.objects.get(id=item_id),
        "all_of_raters": Rater.objects.all()
    }
    return render(request, 'movie_page.html', context)


def raters_view(request):
    context = {
        "all_raters": Rater.objects.all()
    }
    return render(request, 'all_raters.html', context)


def rater_page_view(request, rater_id):
    context = {
     "rater": Rater.objects.get(id=rater_id)
    }
    return render(request, 'rater_page.html', context)
