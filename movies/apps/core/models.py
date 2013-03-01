# -*- coding: utf-8 -*-
"""
Core models.
"""
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from annoying.fields import AutoOneToOneField
from modelhelpers.mixins import DummyUrlMixin, TitleSlugifyMixin


class Movie(models.Model, DummyUrlMixin, TitleSlugifyMixin):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(_("Name to be used in urls"), max_length=100, unique=True, blank=True)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    played_times = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ("movies.apps.core.views.movie_details", (), {"slug": self.slug})


class ImagedModel(models.Model):
    image = models.ImageField(upload_to='movie-shots', height_field='image_height', width_field='image_width')
    image_width = models.SmallIntegerField(default=0)
    image_height = models.SmallIntegerField(default=0)

    class Meta:
        abstract = True


class MovieShot(ImagedModel, DummyUrlMixin):
    pass


class Trailer(ImagedModel, DummyUrlMixin):
    pass


class NewsItem(models.Model, DummyUrlMixin, TitleSlugifyMixin):
    SHORT_TEXT_LENGTH = 150
    WORD_DELIMITERS = (u" ", u"," u".")
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(_("Name to be used in urls"), max_length=100, unique=True, blank=True)
    short_text = models.CharField(max_length=100, blank=True)
    full_text = models.TextField()
    chosen_image = models.ForeignKey(MovieShot)
    chosen_trailer = models.ForeignKey(Trailer)

    def __unicode__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super(NewsItem, self).__init__(*args, **kwargs)
        self._prev_full_text = self.full_text

    def save(self, *args, **kwargs):
        if self._prev_full_text != self.full_text or not self.short_text:
            self.short_text = NewsItem.get_short_text(self.full_text)
        super(NewsItem, self).save(*args, **kwargs)

    @classmethod
    def get_short_text(cls, text):
        shorter = text[:cls.SHORT_TEXT_LENGTH]
        sane_limit = int(cls.SHORT_TEXT_LENGTH / 3)
        for char in cls.WORD_DELIMITERS:
            new_limit = shorter.rfind(char)
            if new_limit >= sane_limit:
                sane_limit = new_limit
        return u"%s…" % shorter[:sane_limit]