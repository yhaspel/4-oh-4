import os

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from fourohfour import settings
from fourohfour.settings import MEDIA_URL


class EMessage(models.Model):
    user = models.ForeignKey(User, related_name="emessages", blank=True, null=True)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000, null=True, blank=True)
    error_code = models.CharField(max_length=6)
    photo = models.ImageField(upload_to="error_images",
                              default=os.path.join('', 'misc', 'no-image.png'),
                              null=True,
                              blank=True)

    class Meta:
        unique_together = (('user', 'error_code'),)

    def __str__(self):
        return "EMessage.;{}".format(self.title)

    @property
    def get_absolute_image_url(self):
        return '%s%s' % (MEDIA_URL, self.photo)


def create_em_for_new_user(user):
    qs = EMessage.objects.filter(user=None)
    for item in qs:
        item.id = None
        item.user = user
        item.save()
