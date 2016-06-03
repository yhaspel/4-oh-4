from django.forms import ModelForm
from . import models


class TipsForDayForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TipsForDayForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['tip_author'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['tip_category'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['tip_text'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['glyph_icon_class_name'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = models.TipOfDay
        fields = [
            'title',
            'tip_author',
            'tip_category',
            'tip_text',
            'glyph_icon_class_name',
        ]
