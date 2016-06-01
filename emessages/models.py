from django.db import models


class EMessage(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    img_url = models.CharField(max_length=500, name='image URL')
    error_code = models.CharField(max_length=6)
    # photo = models.ImageField(upload_to="", null=True, blank=True)

    def __str__(self):
        return "{}".format(self.title)
