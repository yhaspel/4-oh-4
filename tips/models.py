from django.db import models
import sys


class TipOfDay(models.Model):
    title = models.CharField(max_length=40)
    tip_text = models.TextField(max_length=1000)
    tip_author = models.TextField(max_length=100)
    # http://www.w3schools.com/bootstrap/bootstrap_ref_comp_glyphs.asp
    glyph_icon_class_name = models.CharField(max_length=100, null=True, blank=True)
    tip_category = models.CharField(max_length=100, null=True, blank=True)  # mood:  glyph == category(opinion)
    # this text is big text (maybe bigger then the title? nullable.. not implemented)
    mega_text = models.CharField(max_length=10, null=True, blank=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "TipOfDay.: {}".format(self.title)


