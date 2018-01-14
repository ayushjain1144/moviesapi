from __future__ import unicode_literals

from django.db import models


class movie(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    release = models.CharField(max_length=20, default="N/A")
    poster = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "".join([self.name," ",self.release])

    class Meta:
        ordering = ("name",)


class actor(models.Model):
    name = models.CharField(max_length=30)
    movie_name = models.ManyToManyField(movie)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class director(models.Model):
    name = models.CharField(max_length=30)
    movie_name = models.ManyToManyField(movie)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)

class genre(models.Model):
    name = models.CharField(max_length=20)
    movie_name = models.ManyToManyField(movie)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)

