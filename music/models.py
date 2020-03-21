# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Grene(models.Model):
    title = models.CharField(max_length=50)


    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Artist (models.Model):
    title = models.CharField(max_length=50, unique=True)
    grene = models.ManyToManyField(Grene)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Album (models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    featured_artist = models.ManyToManyField( Artist, blank=True, related_name='featured_album_artist')
    primary_grene = models.ForeignKey(Grene,on_delete=models.CASCADE, blank=True, null=True, related_name='primary_album_set')

    grene = models.ManyToManyField(Grene)
 
    class Meta:
            ordering = ('title',)

    def __str__(self):
        return self.title

class Country(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Groupie(models.Model):
    obsession = models.ForeignKey(Artist, to_field='title', on_delete=models.CASCADE)