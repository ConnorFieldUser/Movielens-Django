from django.contrib import admin
# Register your models here.
from movieratings.models import Item, Rater, Data


admin.site.register(Item)
admin.site.register(Rater)
admin.site.register(Data)
