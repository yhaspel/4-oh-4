from django.core.urlresolvers import reverse
from django.db import models
from fourohfour.settings import MEDIA_URL


class EMessage(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000, null=True, blank=True)
    error_code = models.CharField(max_length=6, primary_key=True)
    photo = models.ImageField(upload_to="error_images", default="", null=True, blank=True)

    def __str__(self):
        return "EMessage.;{}".format(self.title)

    @property
    def get_absolute_image_url(self):
        return '%s%s' % (MEDIA_URL, self.photo)
