from django.db import models

from django.db.models import Avg


class Item(models.Model):

    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=11)
    vid_releasr = models.CharField(max_length=100)
    IMDb_url = models.CharField(max_length=150)
    unknown = models.BooleanField()
    action = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    childrens = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    film_noir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    sci_fi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()

    def __str__(self):
        return self.title

    @property
    def get_average_rating(self):
        return "Average Rating: {}".format(round(Data.objects.filter(item_id=self).aggregate(Avg(
                                                'rating')).get('rating__avg'), 2))


class Rater(models.Model):

    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6)

    def __str__(self):
        return str(self.id)


class Data(models.Model):

    rater_id = models.ForeignKey(Rater)
    item_id = models.ForeignKey(Item)
    rating = models.IntegerField()
    timestamp = models.CharField(max_length=9)
