from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Band(models.Model):

    class Genre(models.TextChoices):
        ALTERNATIVE_ROCK = 'AR'
        HEAVY_METAL = 'HM'
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    """
    To display the band's name directly in the Django Admin object list
    (not required if it has been added in a ModelAdmin).

    Or when selecting it as a foreign key in the Django Admin
    (required if we don't want to see something like
    "Band object (id_number)").
    """
    def __str__(self):
        return f"{self.name}"


class Listing(models.Model):

    class Type(models.TextChoices):
        RECORDS = "R"
        CLOTHING = "C"
        POSTERS = "P"
        MISCELLANEOUS = "M"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)])
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    """
    To display the listing's title directly in the Django Admin object list
    (not required if it has been added in a ModelAdmin).

    Or when selecting it as a foreign key in the Django Admin
    (required if we don't want to see something like
    "Listing object (id_number)").
    """
    def __str__(self):
        return f"{self.title}"