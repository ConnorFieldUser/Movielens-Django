from django.shortcuts import render

from movieratings.models import Item

# Create your views here.


def index_view(request):
    context = {
        Item.get_average_rating()
    }
    return render(request, 'index.html', context)
