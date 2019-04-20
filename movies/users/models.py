from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models
import json



class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Movies(models.Model):
    name = CharField(null=True, blank=True, max_length=255)
    popularity = CharField(null=True, blank=True, max_length=255)
    director= CharField(null=True, blank=True, max_length=255)
    imdb_score = models.FloatField(null=True, blank=True, default=None)
    genre =CharField(null=True, blank=True, max_length=300)

    def set_genre(self, x):
        self.foo = json.dumps(x)

    def get_genre(self):
        return json.loads(self.foo)

    def __str__(self):
        return '%s %s' % (self.name, self.imdb_score)

