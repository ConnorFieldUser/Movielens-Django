"""MovieLens_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from movieratings.views import index_view, top_20_view, all_movies_view, raters_view
from movieratings.views import movie_page_view, rater_page_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view),
    url(r'^top_20/', top_20_view),
    url(r'^all_movies/', all_movies_view),
    url(r'^movie_page/(?P<item_id>\d+)/$', movie_page_view, name="movie_view"),
    url(r'^all_raters/', raters_view),
    url(r'^rater_page/(?P<rater_id>\d+)/$', rater_page_view, name="rater_view")
]
