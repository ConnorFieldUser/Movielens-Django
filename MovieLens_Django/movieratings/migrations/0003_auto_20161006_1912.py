# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 19:12
from __future__ import unicode_literals

from django.db import migrations


import csv


def add_my_files(apps, schema_editor):
    Item = apps.get_model("movieratings", "Item")
    Rater = apps.get_model("movieratings", "Rater")
    Data = apps.get_model("movieratings", "Data")
    with open('item.csv', encoding='latin1') as infile:
        reader = csv.DictReader(infile, delimiter='|', fieldnames=["id", "title", "release_date", "vid_releasr",
                                "IMDb_url", "unknown", "action", "adventure", "animation", "childrens",
                                                                   "comedy", "crime", "documentary", "drama",
                                                                   "fantasy", "film_noir", "horror", "musical",
                                                                   "mystery", "romance",
                                                                   "sci_fi", "thriller", "war", "western"])
        for row in reader:
            Item.objects.create(title=row["title"],
                                release_date=row["release_date"], vid_releasr=row["vid_releasr"],
                                IMDb_url=row["IMDb_url"], unknown=row["unknown"], action=row["action"],
                                adventure=row["adventure"], animation=row["animation"],
                                childrens=row["childrens"], comedy=row["comedy"], crime=row["crime"],
                                documentary=row["documentary"], drama=row["drama"], fantasy=row["fantasy"],
                                film_noir=row["film_noir"], horror=row["horror"], musical=row["musical"],
                                mystery=row["mystery"], romance=row["romance"], sci_fi=row["sci_fi"],
                                thriller=row["thriller"], war=row["war"], western=row["western"])

    with open('rater.csv') as infile:
        reader = csv.DictReader(infile, delimiter='|', fieldnames=["id", "age", "gender", "occupation",
                                "zip_code"])
        for row in reader:
            Rater.objects.create(age=row["age"], gender=row["gender"],
                                 occupation=row["occupation"], zip_code=["zip_code"])

    with open('data.csv', encoding='latin1') as infile:
        reader = csv.DictReader(infile, delimiter='\t', fieldnames=["rater_id", "item_id", "rating", "timestamp"])
        for row in reader:
            rater_id = Rater.objects.get(id=row["rater_id"])
            item_id = Item.objects.get(id=row["item_id"])
            Data.objects.create(rater_id=rater_id, item_id=item_id, rating=row["rating"],
                                timestamp=row["timestamp"])


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0002_auto_20161006_1909'),
    ]

    operations = [
        migrations.RunPython(add_my_files)
    ]